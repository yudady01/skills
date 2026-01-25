---
name: ob-fm
description: This skill should be used when the user asks to "format Markdown", "apply Apple style", "reformat document", "Apple style formatter", "obsidian 格式化", "苹果风格排版", or requests document reformatting with Apple design aesthetics. Provides comprehensive Apple-style Markdown formatting guidance.
version: 1.0.0
---

# Apple Style Formatter (ob-fm)

## Purpose

Transform Markdown documents into elegant Apple-style formatted content. Apply Apple's design language—minimalist aesthetics, precise typography, and refined spacing—to create professional, readable documents for Obsidian and general Markdown usage.

## When to Use This Skill

Trigger this skill when:
- User requests "format this document with Apple style"
- User mentions "Apple style formatting" or "苹果风格排版"
- User asks to "reformat" or "beautify" Markdown content
- User wants Obsidian notes with Apple aesthetics
- User requests document styling following Apple design guidelines

## Core Design Principles

### Typography System

Apply three-level heading hierarchy with distinct visual treatments:

| Level | Size | Weight | Decoration | Top Margin | Bottom Margin |
|-------|------|--------|------------|------------|---------------|
| H1 | 28px | 700 | Light gray underline (1px) | 48px | 24px |
| H2 | 21px | 600 | Dark gray left border (3px) | 32px | 16px |
| H3 | 18px | 500 | No decoration | 24px | 12px |

**H1**: Use `---` underlines for major sections
**H2**: Use blockquote-style left borders for subsections
**H3**: Clean headings relying on size/weight differentiation

### Color System

Use restrained grayscale palette with blue accent only for links:

| Element | Color | Hex | Usage |
|---------|-------|-----|-------|
| Primary text | Near black | `#1d1d1f` | Body, headings |
| Secondary text | Medium gray | `#6e6e73` |辅助说明, H2 borders |
| Tertiary text | Light gray | `#86868b` | Minor text |
| Separator | Very light gray | `#d2d2d7` | H1 underlines, quote borders |
| Background | Pure white | `#ffffff` | Page background |
| Surface | Very light gray | `#f5f5f7` | Quote blocks |
| Accent | Apple blue | `#0071e3` | Links only |

**Key Principle**: Grays for structure, blue for interaction, black for content.

### Spacing System

Book-style compact spacing with 8px base unit:

| Name | Value | Usage |
|------|-------|-------|
| XS | 4px | Minimal padding |
| SM | 8px | Small elements |
| MD | 16px | Cards, content blocks |
| LG | 24px | Sections, separators |
| XL | 32px | Major headings |
| XXL | 48px | Top-level titles |

### Paragraph Standards

- **Line height**: 1.8 for body text (book-like readability)
- **Letter spacing**: 0.02em for enhanced readability
- **Paragraph spacing**: 12px between consecutive paragraphs
- **Section separators**: Use `---` for 24px spacing between topic groups

### Font Stack

Prioritize Apple system fonts:

**Body/Headings**:
```
-apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text",
"Helvetica Neue", "PingFang SC", "Hiragino Sans GB", Arial, sans-serif
```

**Code**:
```
"SF Mono", "Menlo", "Monaco", "Consolas", "Liberation Mono", monospace
```

## Formatting Workflow

### 1. Analyze Input Document

Read the source document and identify:
- Document structure (headings, sections, lists)
- Content types (paragraphs, quotes, code blocks)
- Existing formatting issues
- Target output format (Markdown/Obsidian note)

### 2. Apply Apple Style Transformations

#### Headings

Convert headings to Apple style:

```markdown
# H1 主要章节标题
<!-- Add visual separator below -->

## H2 次级章节标题
<!-- Add left border decoration -->

### H3 小节标题
<!-- Clean, size-based differentiation -->
```

#### Paragraphs

Ensure proper spacing and readability:

```markdown
<!-- Standard paragraph with 1.8 line height -->
普通段落：采用 1.8 行高和 0.02em 字间距，提供舒适的书籍阅读体验。

<!-- Section separator (invisible, creates 24px spacing）-->
---

<!-- New section starts with 24px spacing -->
下一个段落组的内容...
```

#### Quotes

Style blockquotes with Apple aesthetics:

```markdown
<!-- Light gray background, left border, rounded corners -->
> 引用块：带有浅灰色的左侧边框和柔和的灰色背景
> 支持多行引用内容
```

#### Code

Apply inline code and code block styling:

```markdown
行内代码使用粉红色文字和浅灰背景。

```
代码块使用等宽字体、浅灰背景、带边框和圆角。
```
```

#### Lists

Maintain consistent list spacing with 8px increments:

```markdown
- 列表项 1
- 列表项 2
  - 嵌套项 2.1
  - 嵌套项 2.2
- 列表项 3
```

### 3. Validate and Refine

Check formatting against Apple standards:
- Heading hierarchy consistency
- Proper spacing between elements
- Color application (grays for structure, blue for links)
- Font stack implementation
- Responsive considerations

## Output Format

### Standard Markdown

Generate clean Markdown with Apple-style structure:
- Semantic heading hierarchy
- Proper paragraph spacing
- Styled code blocks
- Formatted quotes and lists

### Obsidian Note Format

Include Obsidian-specific enhancements:
- YAML frontmatter for metadata
- Wikilink support for internal references
- Callout blocks for highlighted content
- Tags for organization

Example Obsidian frontmatter:

```yaml
---
title: Document Title
created: 2024-01-25
tags: [apple-style, formatted]
cssclass: apple-style
---
```

## Common Formatting Tasks

### Convert Plain Text to Apple Style

1. Add proper heading hierarchy (H1 → H2 → H3)
2. Insert paragraph spacing (12px standard, 24px for sections)
3. Apply book-style line height (1.8)
4. Add section separators with `---` where appropriate

### Enhance Existing Documents

1. Review current heading structure
2. Apply Apple spacing system
3. Update colors to grayscale palette
4. Ensure proper font stack implementation
5. Add visual decorations (H1 underlines, H2 borders)

### Create Obsidian Notes

1. Start with YAML frontmatter
2. Apply Apple heading hierarchy
3. Use Obsidian-specific features (callouts, wikilinks)
4. Include proper spacing and typography
5. Add metadata tags

## Additional Resources

### Reference Files

For detailed design specifications and patterns:
- **`references/design-system.md`** - Complete Apple design system specifications
- **`references/typography.md`** - Typography and font stack details
- **`references/color-palette.md`** - Full color system and usage guidelines
- **`references/spacing-system.md`** - Comprehensive spacing rules and examples

### Example Files

Working examples demonstrating Apple style:
- **`examples/apple-style-example.md`** - Fully formatted example document
- **`examples/obsidian-note-example.md`** - Obsidian-specific formatting
- **`examples/before-after.md`** - Before/after comparison

## Best Practices

✅ **DO:**
- Maintain three-level heading hierarchy maximum
- Use 1.8 line height for body text
- Apply 8px-based spacing system
- Reserve blue (`#0071e3`) for links only
- Use grayscale for structural elements
- Include section separators for major topic changes

❌ **DON'T:**
- Use more than three heading levels
- Apply bright colors except for links
- Use inconsistent spacing
- Override system font stacks unnecessarily
- Add decorative elements beyond Apple guidelines
- Mix multiple design systems

## Integration with Other Skills

This skill can be combined with:
- **`obsidian-markdown`** - For Obsidian Flavored Markdown features
- **`obsidian-canvas-creator`** - For visual layout in Canvas format
- **`mermaid-visualizer`** - For diagrams in formatted documents

---

Apply Apple's minimalist design philosophy: **simplicity, clarity, and refinement** in every formatting decision.
