# Apple Design System - Complete Specifications

## 核心设计理念 Core Design Philosophy

### 书籍风格排版 Book-Style Typography

- **紧凑舒适的段落间距** - Compact, comfortable paragraph spacing
- **接近纸质书阅读体验** -接近纸质书阅读体验
- **1.8 行高** - 1.8 line height for body text
- **0.02em 字间距** - 0.02em letter spacing for readability

### 克制的配色 Restrained Color Palette

- **灰色管结构** - Grayscale for structural elements
- **蓝色管交互** - Blue reserved for interactive elements (links only)
- **黑色管内容** - Black for content (highest priority)

### 渐进式层级 Progressive Hierarchy

- **通过字号、字重、装饰区分标题层次** - Differentiate heading levels through size, weight, and decoration
- **三级标题系统** - Three-level heading system
- **清晰视觉层级** - Clear visual hierarchy

### 上下文感知 Context-Aware Spacing

- **自动调整不同元素后的间距** - Automatically adjust spacing after different elements
- **标题后第一段零间距** - Zero spacing after headings (use heading's bottom margin)
- **列表/引用/代码后增加间距** - Add spacing after lists, quotes, code blocks

---

## 标题系统 Heading System (三级)

### H1 主要章节标题 Primary Section Heading

```css
font-size: 28px;
font-weight: 700;
line-height: 1.4;
letter-spacing: -0.3px;
margin-top: 48px;
margin-bottom: 24px;
border-bottom: 1px solid #d2d2d7;
```

**视觉效果**: 标题下方有细细的浅灰色横线 (Thin light gray underline below heading)

### H2 次级章节标题 Secondary Section Heading

```css
font-size: 21px;
font-weight: 600;
line-height: 1.5;
letter-spacing: -0.2px;
margin-top: 32px;
margin-bottom: 16px;
border-left: 3px solid #6e6e73;
padding-left: 16px;
```

**视觉效果**: 标题左侧有粗粗的深灰色竖线 (Thick dark gray vertical bar on left side)

### H3 小节标题 Subsection Heading

```css
font-size: 18px;
font-weight: 500;
line-height: 1.6;
margin-top: 24px;
margin-bottom: 12px;
```

**视觉效果**: 无任何装饰，靠字号和字重区分 (No decoration, differentiated by size and weight)

### 标题使用规则 Heading Usage Rules

1. **最多三级** - Maximum three levels
2. **不跳级** - No skipping levels (H1 → H2 → H3)
3. **H1 用于主要章节** - H1 for major sections
4. **H2 用于次级内容** - H2 for subsections
5. **H3 用于小节** - H3 for minor divisions

---

## 配色系统 Color System

### 主色调 Primary Colors

| 名称 Name | 色值 Hex | 用途 Usage |
|---------|----------|-----------|
| 主文本 Primary Text | `#1d1d1f` | Body text, headings |
| 次要文本 Secondary Text | `#6e6e73` | Auxiliary text, H2 borders |
| 三级文本 Tertiary Text | `#86868b` | Less prominent text |
| 分隔线 Separator | `#d2d2d7` | H1 underlines, quote borders |

### 背景色 Background Colors

| 名称 Name | 色值 Hex | 用途 Usage |
|---------|----------|-----------|
| 背景 Background | `#ffffff` | Page background |
| 表面 Surface | `#f5f5f7` | Quote blocks, subtle backgrounds |
| 代码背景 Code Background | `#fafafa` | Code block backgrounds |
| 行内代码背景 Inline Code BG | `#f5f5f7` | Inline code backgrounds |

### 强调色 Accent Colors

| 名称 Name | 色值 Hex | 用途 Usage |
|---------|----------|-----------|
| 链接蓝 Link Blue | `#0071e3` | Links only |
| 代码粉 Code Pink | `#c7254e` | Inline code text |

### 配色原则 Color Principles

✅ **灰色系 = 结构性元素** (Grayscale = Structural elements)
- Headings, separators, quotes, borders

✅ **蓝色 = 交互元素** (Blue = Interactive elements)
- Links and only links

✅ **黑色 = 内容文字** (Black = Content)
- Body text, highest priority content

❌ **避免使用** (Avoid):
- Bright colors except blue for links
- Multiple accent colors
- Decorative colors

---

## 间距系统 Spacing System

### 基础间距 Base Spacing (8px unit)

| 名称 Name | 值 Value | 用途 Usage |
|---------|---------|-----------|
| XS | 4px | Minimal padding |
| SM | 8px | Small elements, buttons |
| MD | 16px | Cards, content blocks |
| LG | 24px | Sections, major spacing |
| XL | 32px | Major headings |
| XXL | 48px | Top-level titles |

### 段落间距 Paragraph Spacing

| 场景 Scenario | 间距 Spacing | 说明 Description |
|--------------|-------------|------------------|
| 标题后第一段 After heading | 0px | 利用标题的下边距 (Use heading's bottom margin) |
| 普通段落间 Normal paragraphs | 12px | 紧凑舒适 (Compact, comfortable) |
| 列表后段落 After list | 20px | 12px + 8px 额外呼吸感 |
| 引用后段落 After quote | 20px | 12px + 8px 额外呼吸感 |
| 代码块后段落 After code block | 20px | 12px + 8px 额外呼吸感 |
| `---` 分段后 After separator | 24px | 大分段 (Major section break) |

### 标题间距 Heading Spacing

| 标题 Level | 上边距 Top | 下边距 Bottom |
|-----------|-----------|---------------|
| H1 | 48px | 24px |
| H2 | 32px | 16px |
| H3 | 24px | 12px |

### 元素间距 Element Spacing

```css
/* 正文段落 */
body {
  line-height: 1.8;
  letter-spacing: 0.02em;
  margin-bottom: 12px;
}

/* 大分段标记 */
hr {
  border: none;
  margin: 24px 0;
}
```

---

## 字体系统 Typography System

### 正文/标题字体 Body/Heading Font Stack

```css
font-family:
  -apple-system,
  BlinkMacSystemFont,
  "SF Pro Display",
  "SF Pro Text",
  "Helvetica Neue",
  "PingFang SC",
  "Hiragino Sans GB",
  Arial,
  sans-serif;
```

**字体优先级** (Priority):
1. SF Pro Display/Text (Apple system font)
2. Helvetica Neue (Classic Apple font)
3. PingFang SC (苹方 - Chinese)
4. Hiragino Sans GB (冬青黑 - Japanese)
5. Arial (Fallback)

### 代码字体 Code Font Stack

```css
font-family:
  "SF Mono",
  "Menlo",
  "Monaco",
  "Consolas",
  "Liberation Mono",
  monospace;
```

### 字号预设 Font Size Presets (三档)

| 档位 Tier | 正文 Body | H1 | H2 | H3 | 代码 Code | 适用场景 Scenario |
|----------|----------|----|----|----|----------|------------------|
| 小号 Small | 14px | 22px | 18px | 16px | 12px | 手机阅读 Mobile |
| 中号 Medium | 16px | 28px | 21px | 18px | 14px | 推荐 Recommended |
| 大号 Large | 18px | 32px | 24px | 20px | 16px | 大屏幕 Large screen |

### 字重系统 Font Weight System

| 名称 Name | 值 Value | 用途 Usage |
|---------|---------|-----------|
| Regular | 400 | Body text |
| Medium | 500 | H3 headings |
| SemiBold | 600 | H2 headings |
| Bold | 700 | H1 headings |

---

## 圆角系统 Border Radius

| 名称 Name | 值 Value | 应用 Application |
|---------|---------|-----------------|
| SM | 4px | Buttons, tags, inline code |
| MD | 8px | Cards, code blocks, images |
| LG | 12px | Panels, large containers |
| XL | 16px | Extra large elements |

---

## 代码样式 Code Styling

### 行内代码 Inline Code

```css
inline-code {
  font-size: 14px;
  font-family: "SF Mono", monospace;
  background-color: #f5f5f7;
  color: #c7254e;
  padding: 2px 6px;
  border-radius: 4px;
}
```

### 代码块 Code Block

```css
code-block {
  font-size: 14px;
  font-family: "SF Mono", monospace;
  line-height: 1.6;
  background-color: #fafafa;
  border: 1px solid #d2d2d7;
  padding: 16px 24px;
  margin: 16px 0;
  border-radius: 8px;
}
```

---

## 引用块样式 Quote Block Styling

```css
blockquote {
  font-size: 16px;
  line-height: 1.8;
  color: #6e6e73;
  background-color: #f5f5f7;
  padding: 16px 24px;
  margin: 16px 0;
  border-left: 3px solid #d2d2d7;
  border-radius: 0 4px 4px 0;
}
```

---

## 列表样式 List Styling

```css
/* 无序列表 */
ul {
  margin: 12px 0;
  padding-left: 24px;
}

li {
  margin-bottom: 8px;
  line-height: 1.8;
}

/* 嵌套列表 */
ul ul {
  margin-top: 8px;
}
```

---

## 响应式设计 Responsive Design

### 断点 Breakpoints

| 名称 Name | 宽度 Width | 适用设备 Device |
|---------|-----------|-----------------|
| Mobile | < 768px | 手机 Phones |
| Tablet | 768px - 1024px | 平板 Tablets |
| Desktop | > 1024px | 桌面 Desktop |

### 移动端调整 Mobile Adjustments

- 减小字号 (使用小号预设)
- 减少边距
- 保持可读性 (line-height 1.8)

---

## 完整样式规格表 Complete Style Specification

### 正文段落 Body Paragraph

```css
body {
  font-size: 16px;
  line-height: 1.8;
  letter-spacing: 0.02em;
  color: #1d1d1f;
  margin-bottom: 12px;
}
```

### 链接 Links

```css
a {
  color: #0071e3;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
```

### 分隔线 Horizontal Rule

```css
hr {
  border: none;
  margin: 24px 0;
}
```

---

## 设计模式示例 Design Pattern Examples

### 标准章节结构 Standard Section Structure

```markdown
# H1 主要章节

第一段内容，利用 H1 的 24px 下边距。

第二段内容，使用标准的 12px 段落间距。

## H2 次级章节

次级内容，左侧带有 3px 深灰色边框。

### H3 小节

小节内容，靠字号和字重区分。

---

下一个大节开始，使用 `---` 创建 24px 间距。
```

### 代码和引用混合 Code and Quote Mix

```markdown
## 示例代码

以下代码展示了 Apple 风格：

```python
def hello():
    print("Hello, Apple Style!")
```

### 代码说明

> 这是一个代码说明引用块，
> 使用浅灰色背景和左侧边框。

代码块和引用块之间使用 16px 间距。
```

---

此设计系统遵循 Apple 官方设计语言，确保文档具有一致、优雅的视觉效果。
