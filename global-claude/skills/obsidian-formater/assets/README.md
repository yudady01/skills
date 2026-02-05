# Apple Style CSS 使用指南

## 快速开始

### 方法 1：Obsidian Snippets（推荐）

1. **复制 CSS 文件**
   ```bash
   # 复制 CSS 文件到 Obsidian snippets 目录
   cp apple-style.css ~/.obsidian/snippets/
   ```

2. **在 Obsidian 中启用**
   - 打开 Obsidian 设置（Settings）
   - 进入 **Appearance** → **CSS snippets**
   - 点击 **Refresh** 按钮
   - 找到 `apple-style` 并点击开关启用

3. **在笔记中使用**
   ```markdown
   ---
   title: 我的笔记
   cssclass: apple-style
   ---

   # 这是标题

   这段文字会应用 Apple 风格。
   ```

### 方法 2：主题 CSS

如果使用自定义主题，可以将 CSS 添加到主题的 `obsidian.css` 文件中。

## CSS 类名

### 根类名

所有样式都通过 `.apple-style` 类名应用，确保不影响其他内容。

### 辅助类

```markdown
<div class="apple-style text-center">居中文本</div>
<div class="apple-style mt-lg">增加上边距</div>
<div class="apple-style mb-md">增加下边距</div>
```

## 设计系统

### 色彩系统

```css
--color-background: #FFFFFF;    /* 页面背景 */
--color-text: #1D1D1F;          /* 文字颜色 */
--color-text-secondary: #6E6E73; /* 次要文字 */
--color-link: #0071E3;          /* 链接颜色 */
--color-border: #D2D2D7;        /* 边框颜色 */
--color-surface: #F5F5F7;       /* 表面颜色 */
```

### 字体系统

```css
/* 正文字体 */
-apple-system, BlinkMacSystemFont, "SF Pro Display",
"SF Pro Text", "PingFang SC", "Hiragino Sans GB"

/* 代码字体 */
"SF Mono", "Menlo", "Monaco", "Consolas"
```

### 间距系统

```css
--spacing-xs: 4px;
--spacing-sm: 8px;
--spacing-md: 16px;
--spacing-lg: 24px;
--spacing-xl: 32px;
--spacing-xxl: 48px;
```

## 支持的元素

### 标题

- **H1**：28px，底部下划线
- **H2**：21px，左侧深灰条
- **H3**：18px，仅加粗

### Callout

支持所有 Obsidian Callout 类型：

```markdown
> [!abstract] 核心概念
> [!note] 重要说明
> [!info] 补充信息
> [!warning] 警告
```

### 代码块

```markdown
行内代码：`code`

代码块：
```
code block
```
```

### 表格

```markdown
| 列 1 | 列 2 |
|------|------|
| 数据 1 | 数据 2 |
```

## 响应式设计

CSS 包含移动设备优化：

- 小于 768px：减小字号和间距
- 打印模式：优化打印输出

## 自定义

### 覆盖颜色

在你的 vault 中创建自定义 CSS：

```css
.apple-style {
    --color-link: #0066CC; /* 自定义链接颜色 */
}
```

### 调整间距

```css
.apple-style {
    --spacing-lg: 32px; /* 增加大间距 */
}
```

## 故障排除

### 样式未生效

1. 确认 `cssclass: apple-style` 已添加到 frontmatter
2. 刷新 Obsidian（Ctrl/Cmd + R）
3. 检查 CSS snippets 是否启用

### 字体显示不正确

- macOS/iOS：自动使用 SF Pro
- Windows：需要安装 SF Pro 或使用回退字体
- Linux：使用 PingFang SC 或系统默认字体

## 示例笔记

```markdown
---
title: Apple 风格示例
cssclass: apple-style
tags: [示例, apple-style]
---

# Apple 设计原则

> [!abstract] 核心哲学
> 简洁是终极的复杂。

## 设计原则

### 简洁

去除不必要的元素。

### 清晰

确保信息传达清晰。

```python
def hello():
    print("Hello, Apple Style!")
```

| 原则 | 说明 |
|------|------|
| 简洁 | 去除冗余 |
| 清晰 | 信息明确 |

---

*应用 Apple 风格的核心是简洁。*
```

## 更新日志

### v2.1.0 (2024-01-25)

- 完整的 Apple 官网配色系统
- 三级标题层次（H1-H3）
- 1.8 行高 + 1.2em 段落间距
- Callout 样式优化
- 响应式设计支持
- Dataview 集成

## 相关资源

- [ob-fm 技能文档](../SKILL.md)
- [设计系统规范](../references/design-system.md)
- [转换示例](../examples/ob-fm-transformation.md)

## 许可

此 CSS 由 ob-fm (Obsidian Apple Style Architect) 提供，遵循 Apple 设计语言。

---

**记住**：Apple 风格的核心是简洁——保持设计干净、优雅、专注。 🍎
