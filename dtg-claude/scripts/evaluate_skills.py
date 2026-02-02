#!/usr/bin/env python3
"""Skill evaluation hook for Claude Code.

UserPromptSubmit hook that evaluates skills against user prompts.
Cross-platform compatible (Windows, macOS, Linux).
"""
import sys
import os
import json

# Add lib directory to path
lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")
sys.path.insert(0, lib_dir)

from skill_evaluator import evaluate_skills, format_eval_result, format_compact_result


def main() -> int:
    """Main entry point."""
    # Read JSON from stdin
    input_data = sys.stdin.read()
    if not input_data:
        return 0

    try:
        data = json.loads(input_data)
    except json.JSONDecodeError:
        return 0

    # Extract prompt from JSON - handle different possible field names
    prompt = data.get("prompt") or data.get("message") or data.get("text")
    if not prompt:
        return 0

    # Skip very short prompts (likely continuations)
    if len(prompt.strip()) < 5:
        return 0

    # Skip skill invocations (don't suggest skills when already using one)
    if prompt.strip().startswith("/"):
        return 0

    # Evaluate skills
    result = evaluate_skills(
        prompt=prompt,
        threshold=0.15,  # Low threshold for broad matching
        max_results=3
    )

    # Only output if we have good matches
    if result.has_suggestion:
        # Use compact format to minimize noise
        output = format_compact_result(result)

        # If no high-confidence match, use verbose format for lower scores
        if not output and result.top_matches:
            output = format_eval_result(result, verbose=False)

        if output:
            print(output)

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        # Never block on errors - just log and exit 0
        print(f"Warning: evaluate_skills.py error: {e}", file=sys.stderr)
        sys.exit(0)
