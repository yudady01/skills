#!/usr/bin/env python3
"""Skill evaluation engine for Claude Code plugin.

Cross-platform compatible (Windows, macOS, Linux).
This module provides skill matching and evaluation capabilities.
"""
import json
import re
import os
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from difflib import SequenceMatcher


# =============================================================================
# Configuration
# =============================================================================

def _load_whitelist_config() -> tuple:
    """Load whitelist configuration from JSON file.

    Returns:
        Tuple of (whitelist_set, confidence_threshold, max_results)
    """
    import json
    config_path = Path(__file__).parent / "whitelist.json"

    if config_path.exists():
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            whitelist = set(data.get("whitelist", []))
            settings = data.get("settings", {})
            threshold = settings.get("confidence_threshold", 0.15)
            max_results = settings.get("max_results", 3)
            return whitelist, threshold, max_results
        except (json.JSONDecodeError, IOError):
            pass

    # Fallback defaults
    return set(), 0.15, 3


# Load configuration at module import time
SKILL_WHITELIST, CONFIDENCE_THRESHOLD, MAX_RESULTS = _load_whitelist_config()


# =============================================================================
# Data Models
# =============================================================================

@dataclass
class SkillMatch:
    """Represents a skill match result."""
    name: str
    description: str
    score: float
    matched_keywords: List[str]
    source: str  # 'global', 'project', etc.


@dataclass
class EvalResult:
    """Represents the evaluation result."""
    has_suggestion: bool
    top_matches: List[SkillMatch]
    total_skills_evaluated: int
    evaluation_time_ms: float


# =============================================================================
# Path Utilities
# =============================================================================

def get_plugin_root() -> Path:
    """Get the plugin root directory from environment variable."""
    plugin_root = os.environ.get("CLAUDE_PLUGIN_ROOT")
    if plugin_root:
        return Path(plugin_root)

    # Fallback: assume script is in scripts/lib/ subdirectory
    # __file__ = scripts/lib/skill_evaluator.py
    # parent.parent.parent = plugin root
    return Path(__file__).parent.parent.parent


def get_marketplace_path() -> Path:
    """Get path to marketplace.json."""
    return get_plugin_root() / ".claude-plugin" / "marketplace.json"


def get_skills_dir() -> Path:
    """Get path to skills directory."""
    return get_plugin_root() / "skills"


# =============================================================================
# Skill Loading
# =============================================================================

def load_marketplace_skills() -> List[Dict[str, Any]]:
    """Load skills from marketplace.json.

    Expands plugin groups to load individual skill details from SKILL.md files.

    Returns:
        List of skill dictionaries with name, description, etc.
    """
    marketplace_path = get_marketplace_path()
    if not marketplace_path.exists():
        return []

    try:
        data = json.loads(marketplace_path.read_text(encoding="utf-8"))
        plugins = data.get("plugins", [])
        skills_dir = get_skills_dir()

        result = []
        for plugin in plugins:
            skills_list = plugin.get("skills", [])

            if len(skills_list) == 0:
                continue

            if len(skills_list) == 1:
                # Single skill plugin - use plugin name and description directly
                result.append({
                    "name": plugin.get("name", ""),
                    "description": plugin.get("description", "")
                })
            else:
                # Multiple skills in one plugin - expand them
                for skill_path in skills_list:
                    if skill_path.startswith("./"):
                        # Extract skill name from path (e.g., "./skills/en2zh" -> "en2zh")
                        skill_name = skill_path.replace("./skills/", "").strip("/")
                        skill_details = load_skill_details(skill_name)
                        if skill_details:
                            result.append({
                                "name": skill_details.get("name", skill_name),
                                "description": skill_details.get("description", "")
                            })

        return result
    except (json.JSONDecodeError, IOError):
        return []


def load_skill_details(skill_name: str) -> Optional[Dict[str, Any]]:
    """Load detailed skill information from SKILL.md file.

    Args:
        skill_name: Name of the skill to load

    Returns:
        Dictionary with skill details or None if not found
    """
    skills_dir = get_skills_dir()
    skill_path = skills_dir / skill_name / "SKILL.md"

    if not skill_path.exists():
        return None

    try:
        content = skill_path.read_text(encoding="utf-8")

        # Parse YAML frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        frontmatter = {}
        if frontmatter_match:
            for line in frontmatter_match.group(1).split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip()

        return {
            "name": frontmatter.get("name", skill_name),
            "description": frontmatter.get("description", ""),
            "content": content
        }
    except IOError:
        return None


# =============================================================================
# Text Processing & Matching
# =============================================================================

def normalize_text(text: str) -> str:
    """Normalize text for matching.

    - Convert to lowercase
    - Remove extra whitespace
    - Remove punctuation (keep Chinese characters)
    """
    # Keep Chinese characters, alphanumeric, and basic punctuation
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    # Remove punctuation but keep Chinese characters
    text = re.sub(r'[^\w\s\u4e00-\u9fff]', ' ', text)
    return text.strip()


def extract_keywords(description: str, max_keywords: int = 10) -> List[str]:
    """Extract keywords from a skill description.

    Args:
        description: Skill description text
        max_keywords: Maximum number of keywords to extract

    Returns:
        List of extracted keywords
    """
    normalized = normalize_text(description)

    # Extract English words (2+ characters)
    english_words = [w for w in re.findall(r'\b[a-z]{2,}\b', normalized)]

    # Extract Chinese by splitting on spaces (normalized text has spaces instead of punctuation)
    # Then further split into 2-char sequences for better matching
    chinese_words = []
    for word in normalized.split():
        # Extract 2-char sequences from Chinese words
        if any('\u4e00' <= c <= '\u9fff' for c in word):
            # For Chinese text, extract overlapping 2-char sequences
            for i in range(len(word) - 1):
                seq = word[i:i+2]
                if all('\u4e00' <= c <= '\u9fff' for c in seq):
                    chinese_words.append(seq)
            # Also keep the full word if it's all Chinese
            if all('\u4e00' <= c <= '\u9fff' or c.isspace() for c in word):
                chinese_words.append(word)

    # Combine all keywords
    all_keywords = list(set(english_words + chinese_words))

    # Build frequency map
    from collections import Counter
    word_freq = Counter(all_keywords)

    # Boost score for meaningful phrases
    boosted = {}
    for word, count in word_freq.items():
        boost = 1.0
        # Boost Chinese 2-char phrases (most common word length in Chinese)
        if len(word) == 2 and all('\u4e00' <= c <= '\u9fff' for c in word):
            boost = 3.0  # High boost for 2-char Chinese words
        # Boost longer Chinese phrases
        elif len(word) > 2 and any('\u4e00' <= c <= '\u9fff' for c in word):
            boost = 2.0
        # Boost long English words
        elif len(word) >= 4:
            boost = 1.5
        boosted[word] = count * boost

    # Return top keywords
    sorted_keywords = sorted(boosted.items(), key=lambda x: x[1], reverse=True)
    return [w for w, _ in sorted_keywords[:max_keywords]]


def keyword_match_score(prompt: str, skill: Dict[str, Any]) -> Tuple[float, List[str]]:
    """Calculate keyword matching score between prompt and skill.

    Args:
        prompt: User's prompt text
        skill: Skill dictionary with 'description' field

    Returns:
        Tuple of (score, matched_keywords)
    """
    prompt_normalized = normalize_text(prompt)
    prompt_lower = prompt.lower()
    description = skill.get("description", "")
    skill_name = skill.get("name", "")

    # Build keywords from both name and description
    # Name gets higher weight
    name_keywords = extract_keywords(skill_name, max_keywords=5)
    desc_keywords = extract_keywords(description, max_keywords=10)

    # Mark which are name keywords (for scoring)
    keywords = [(k, 2.0) for k in name_keywords] + [(k, 1.0) for k in desc_keywords]

    if not keywords:
        return (0.0, [])

    # Count matching keywords with weights
    matched = []
    total_weight = 0.0
    matched_weight = 0.0

    for keyword, weight in keywords:
        total_weight += weight
        # Check substring match
        if keyword in prompt_normalized:
            matched.append(keyword)
            matched_weight += weight
            # Extra boost for exact word matches
            if keyword in prompt_lower.split():
                matched_weight += weight * 0.5

    if not matched:
        return (0.0, [])

    # Base score from weighted match ratio
    match_ratio = matched_weight / total_weight if total_weight > 0 else 0

    # Boost score for longer keyword matches (more specific)
    avg_keyword_length = sum(len(k) for k in matched) / len(matched)
    length_boost = min(avg_keyword_length / 4, 1.5)  # Max 1.5x boost

    # Check if keywords appear early in prompt
    prompt_words = prompt_normalized.split()[:20]  # First 20 words
    early_matches = sum(1 for k in matched if any(k in w for w in prompt_words))
    early_boost = (early_matches / len(matched)) * 0.3 if matched else 0

    # Final score
    score = match_ratio * length_boost + early_boost
    score = min(score, 1.0)  # Cap at 1.0

    return (score, matched)


def semantic_similarity_score(prompt: str, skill: Dict[str, Any]) -> float:
    """Calculate semantic similarity using SequenceMatcher.

    This is a lightweight alternative to full semantic vector matching.

    Args:
        prompt: User's prompt text
        skill: Skill dictionary with 'description' field

    Returns:
        Similarity score between 0 and 1
    """
    description = skill.get("description", "")
    skill_name = skill.get("name", "")
    prompt_normalized = normalize_text(prompt)

    # Combine name and description for similarity check
    # Name gets more weight (duplicate it)
    combined_text = normalize_text(f"{skill_name} {skill_name} {description}")

    # Use SequenceMatcher for basic similarity
    return SequenceMatcher(None, prompt_normalized, combined_text).ratio()


# =============================================================================
# Evaluation Engine
# =============================================================================

def evaluate_skills(
    prompt: str,
    threshold: Optional[float] = None,
    max_results: Optional[int] = None
) -> EvalResult:
    """Evaluate skills against a user prompt.

    Args:
        prompt: User's prompt text
        threshold: Minimum score threshold for matches (uses CONFIDENCE_THRESHOLD from config if None)
        max_results: Maximum number of results to return (uses MAX_RESULTS from config if None)

    Returns:
        EvalResult with top matching skills
    """
    # Use config defaults if not specified
    if threshold is None:
        threshold = CONFIDENCE_THRESHOLD
    if max_results is None:
        max_results = MAX_RESULTS
    import time
    start_time = time.time()

    # Load all skills from marketplace
    skills = load_marketplace_skills()

    if not skills:
        return EvalResult(
            has_suggestion=False,
            top_matches=[],
            total_skills_evaluated=0,
            evaluation_time_ms=0
        )

    # Evaluate each skill
    matches = []
    for skill in skills:
        skill_name = skill.get("name", "")

        # Skip if whitelist is enabled and skill is not in whitelist
        # Empty whitelist {} means evaluate all skills
        if SKILL_WHITELIST and skill_name not in SKILL_WHITELIST:
            continue

        # Get both keyword and semantic scores
        keyword_score, matched_keywords = keyword_match_score(prompt, skill)
        semantic_score = semantic_similarity_score(prompt, skill)

        # Combined score (weighted)
        combined_score = (keyword_score * 0.7) + (semantic_score * 0.3)

        if combined_score >= threshold:
            matches.append(SkillMatch(
                name=skill.get("name", "unknown"),
                description=skill.get("description", ""),
                score=combined_score,
                matched_keywords=matched_keywords,
                source="global"
            ))

    # Sort by score descending
    matches.sort(key=lambda m: m.score, reverse=True)

    # Return top results
    top_matches = matches[:max_results]

    elapsed_ms = (time.time() - start_time) * 1000

    return EvalResult(
        has_suggestion=len(top_matches) > 0,
        top_matches=top_matches,
        total_skills_evaluated=len(skills),
        evaluation_time_ms=elapsed_ms
    )


# =============================================================================
# Output Formatting
# =============================================================================

def format_eval_result(result: EvalResult, verbose: bool = False) -> str:
    """Format evaluation result for output.

    Args:
        result: EvalResult to format
        verbose: Whether to include verbose details

    Returns:
        Formatted string output
    """
    if not result.has_suggestion:
        return ""

    lines = [
        "",
        "🔍 检测到可能相关的技能:",
    ]

    for i, match in enumerate(result.top_matches, 1):
        # Score emoji based on confidence
        if match.score >= 0.6:
            emoji = "🔥"
        elif match.score >= 0.4:
            emoji = "⚡"
        else:
            emoji = "💡"

        lines.append(f"  {i}. {emoji} **{match.name}** (置信度: {match.score:.0%})")
        lines.append(f"     {match.description[:80]}{'...' if len(match.description) > 80 else ''}")

        if verbose and match.matched_keywords:
            lines.append(f"     匹配关键词: {', '.join(match.matched_keywords[:5])}")

    if verbose:
        lines.append(f"")
        lines.append(f"   评估了 {result.total_skills_evaluated} 个技能，耗时 {result.evaluation_time_ms:.1f}ms")

    return "\n".join(lines)


def format_compact_result(result: EvalResult) -> str:
    """Format a compact one-line result.

    Args:
        result: EvalResult to format

    Returns:
        Compact string or empty if no matches
    """
    if not result.has_suggestion:
        return ""

    top = result.top_matches[0]
    if top.score >= 0.5:
        return f"💡 技能建议: {top.name} (置信度 {top.score:.0%})"
    return ""
