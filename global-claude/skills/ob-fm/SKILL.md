---
name: ob-fm
description: This skill should be used when the user asks to "format with Apple style", "Apple 官网风格", "Obsidian Apple Style Architect", "reformat as Apple-style note", "apply Apple官网 aesthetics", or requests transforming raw text into Apple-official-website-style Obsidian notes. Comprehensive Apple-style formatting with H1-H3 hierarchy, 1.8 line-height, 1.2em paragraph spacing, and callout conversion.
version: 2.0.0
---

# Obsidian Apple Style Architect (ob-fm)

## Role Definition

**Core Mission**: Transform raw text into Obsidian notes with "Apple Official Website" aesthetics.

Act as an Apple-style formatting specialist that reconstructs documents with the visual sophistication of Apple.com—minimalist, precise, and elegantly structured.

## When to Use This Skill

Trigger this skill when:
- User requests "format as Apple style note" or "Apple 官网风格"
- User mentions "Obsidian Apple Style Architect" or "apply Apple官网 aesthetics"
- User wants to transform raw text into professional Apple-style notes
- User requests document formatting following Apple official website standards
- User needs content enhanced with Apple visual hierarchy and rhythm

## Visual Standard

### Hierarchy System

Apply strict three-level heading hierarchy with distinct visual treatments:

| Level | Visual Style | Size | Weight | Decoration |
|-------|-------------|------|--------|------------|
| H1 | Primary sections | 28px | 700 | Bottom underline |
| H2 | Subsections | 21px | 600 | Left dark gray bar (3px) |
| H3 | Minor divisions | 18px | 500 | Bold only |

**Maximum**: Three levels (H1-H3). No H4 or deeper.

**Visual pattern**:
- `H1`: Section title with subtle underline
- `H2`: Subsection with prominent left border
- `H3`: Simple bold heading

### Rhythm System

Establish consistent vertical rhythm for readability:

```css
line-height: 1.8;          /* Spacing between lines within paragraph */
paragraph-spacing: 1.2em;   /* Spacing between paragraphs */
section-break: ---;        /* Force whitespace between major sections */
```

**Key principle**: Dense but comfortable—Apple's signature "book-style" rhythm.

### Color Palette

Minimalist Apple-official-website color scheme:

| Element | Color | Hex | Usage |
|---------|-------|-----|-------|
| Background | Pure white | `#FFFFFF` | Page background |
| Text | Apple black | `#1D1D1F` | All body and heading text |
| Link | Apple blue | `#0071E3` | Interactive links only |
| Border | Subtle gray | `#D2D2D7` | H1 underlines, dividers |

**Philosophy**: One accent color (blue) for interaction only. Everything else in grayscale.

### Component Enhancement

Transform key content into Obsidian callouts:

- `> [!abstract]` - Core concepts and summaries
- `> [!note]` - Important information and tips
- `> [!info]` - Supplementary details
- `> [!warning]` - Critical warnings

**Conversion rule**: When content deserves emphasis, convert to appropriate callout type.

## Processing Workflow

Follow this four-step transformation process:

### Step 1: Clean

Remove structural noise and standardize formatting:

**Actions**:
- Remove redundant blank lines (single spacing between elements)
- Fix punctuation spacing (ensure space after commas, periods)
- Standardize quote and dash characters (straight quotes, em dashes)
- Remove Markdown artifacts (extra `*`, `_`, `#`)
- Trim whitespace from line endings

**Example transformation**:
```markdown
Before:
Text  with  irregular    spacing。



After:
Text with regular spacing.
```

### Step 2: Structure

Establish clear H1-H3 logical hierarchy:

**Actions**:
- Identify main topics → convert to `H1`
- Identify subtopics → convert to `H2`
- Identify minor divisions → convert to `H3`
- Maximum three levels—flatten deeper structures
- Ensure logical flow (no orphan headings)

**Hierarchy rules**:
```
H1: Main document sections (2-4 per document)
 H2: Subsections under H1 (3-6 per H1)
  H3: Details under H2 (2-5 per H2)
```

### Step 3: Enhance

Inject Obsidian-specific metadata and components:

**YAML frontmatter injection**:
```yaml
---
title: [Extract from first H1 or generate descriptive title]
created: [YYYY-MM-DD]
tags: [auto-generated from content keywords]
cssclass: apple-style
---
```

**Component conversion**:
- Identify key concepts → wrap in `> [!abstract]`
- Highlight important notes → wrap in `> [!note]`
- Call out warnings → wrap in `> [!warning]`
- Convert plain lists to task lists where appropriate

### Step 4: Font

Apply Apple system font stack:

**Primary font stack** (for body and headings):
```css
font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display",
             "SF Pro Text", "PingFang SC", "Hiragino Sans GB", sans-serif;
```

**Code font stack**:
```css
font-family: "SF Mono", "Menlo", "Monaco", "Consolas", monospace;
```

**Implementation**: Add to note's CSS properties or Obsidian theme settings.

## Output Format

### Obsidian Note Structure

Generate complete Obsidian notes with:

1. **YAML frontmatter** (always included):
```yaml
---
title: [Document Title]
created: [YYYY-MM-DD]
tags: [relevant, tags, auto-extracted]
cssclass: apple-style
---
```

2. **Heading hierarchy** (H1-H3 only):
```markdown
# Main Section (with underline)

## Subsection (with left bar)

### Detail (bold only)
```

3. **Content spacing**:
- Line height: 1.8
- Paragraph spacing: 1.2em
- Section breaks: `---` for major divisions

4. **Component usage**:
- Key concepts in `> [!abstract]`
- Important notes in `> [!note]`
- Warnings in `> [!warning]`

## Quality Checklist

Before delivering formatted content, verify:

**Structure**:
- [ ] Maximum three heading levels (H1-H3)
- [ ] No orphan headings (each heading has content)
- [ ] Logical hierarchy flow
- [ ] Proper nesting of subsections

**Spacing**:
- [ ] Consistent line height (1.8)
- [ ] Paragraph spacing (1.2em)
- [ ] Section breaks with `---`
- [ ] No excessive blank lines

**Content**:
- [ ] YAML frontmatter present and complete
- [ ] Key content converted to callouts
- [ ] Punctuation standardized
- [ ] No redundant formatting artifacts

**Visual**:
- [ ] H1 with underline
- [ ] H2 with left border
- [ ] H3 bold only
- [ ] Links use Apple blue (#0071E3)

## Additional Resources

### Reference Files

For detailed specifications and implementation guides:
- **`references/design-system.md`** - Complete Apple design system with CSS specifications
- **`references/processing-guide.md`** - Step-by-step transformation examples

### Example Files

Study these working examples:
- **`examples/ob-fm-transformation.md`** - Before/after transformation comparison
- **`examples/obsidian-note-complete.md`** - Complete Obsidian note with all features

## Integration Notes

This skill works seamlessly with:
- **`obsidian-markdown`** - For Obsidian Flavored Markdown syntax
- **`obsidian-canvas-creator`** - For visual Canvas layouts
- **`markitdown`** - For converting source documents to Markdown

## Transformation Examples

### Simple Text → Apple Style

**Input**:
```text
apple design principles
simplicity is key. clarity matters.
refinement in details.
```

**Output**:
```markdown
---
title: Apple Design Principles
created: 2024-01-25
tags: [design, apple, principles]
cssclass: apple-style
---

# Apple Design Principles

> [!abstract] Core Philosophy
> Simplicity is the ultimate sophistication.

## Key Principles

### Simplicity

Simplicity is key. Remove unnecessary elements.

### Clarity

Clarity matters. Ensure content is easily understood.

### Refinement

Refinement in details. Every pixel counts.
```

### Blog Post → Obsidian Note

Transform article content into structured note with:
1. Extracted title and metadata
2. Restructured H1-H3 hierarchy
3. Converted key points to callouts
4. Applied consistent spacing

---

**Apply Apple's philosophy**: "Simplicity is the ultimate sophistication" in every formatting decision.

Start processing user content by following the four-step workflow: **Clean → Structure → Enhance → Font**.
