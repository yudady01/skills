---
name: ob-fm
description: 当用户要求"使用 Apple 风格格式化"、"Apple 官网风格"、"Obsidian Apple Style Architect"、"重新格式化为 Apple 风格笔记"、"应用 Apple 官网美学"，或请求将原始文本转换为 Apple 官网风格的 Obsidian 笔记时使用此技能。全面的 Apple 风格格式化，包含 H1-H3 层级结构、1.8 行高、1.2em 段落间距和 Callout 转换。重要：直接替换原始文件，禁止创建新文件。
version: 2.1.0
---

# Obsidian Apple Style Architect (ob-fm)

## 角色定义

**核心使命**：将原始文本转换为具有"Apple 官网"美学的 Obsidian 笔记。

作为 Apple 风格格式化专家，以 Apple.com 的视觉精致度重构文档——极简、精确且结构优雅。

**文件操作约束**：
- ✅ **直接编辑原始文件**：使用 `Edit` 工具直接替换文件内容
- ❌ **禁止创建新文件**：绝不使用 `Write` 工具创建新档案
- ❌ **禁止输出预览**：不要并排显示原文和译文
- 🎯 **目标**：原地升级文件，保持文件路径不变

## 何时使用此技能

在以下情况下触发此技能：
- 用户请求"格式化为 Apple 风格笔记"或"Apple 官网风格"
- 用户提到"Obsidian Apple Style Architect"或"应用 Apple 官网美学"
- 用户希望将原始文本转换为专业的 Apple 风格笔记
- 用户请求按照 Apple 官网标准进行文档格式化
- 用户需要使用 Apple 视觉层级和节奏增强内容

## 视觉标准

### 层级系统

应用严格的三级标题层级，具有独特的视觉处理：

| 级别 | 视觉样式 | 大小 | 字重 | 装饰 |
|-------|-------------|------|--------|------------|
| H1 | 主要章节 | 28px | 700 | 底部下划线 |
| H2 | 子章节 | 21px | 600 | 左侧深灰色条（3px） |
| H3 | 次要划分 | 18px | 500 | 仅加粗 |

**上限**：三个级别（H1-H3）。没有 H4 或更深的级别。

**视觉模式**：
- `H1`：带有细腻下划线的章节标题
- `H2`：带有突出左边框的子章节
- `H3`：简单的加粗标题

### 节奏系统

建立一致的垂直节奏以提高可读性：

```css
line-height: 1.8;          /* 段落内行之间的间距 */
paragraph-spacing: 1.2em;   /* 段落之间的间距 */
section-break: ---;        /* 主要章节之间强制留白 */
```

**关键原则**：紧凑但舒适——Apple 标志性的"书籍风格"节奏。

### 色彩方案

极简的 Apple 官网色彩方案：

| 元素 | 颜色 | 色值 | 用途 |
|---------|-------|-----|-------|
| 背景 | 纯白 | `#FFFFFF` | 页面背景 |
| 文本 | Apple 黑 | `#1D1D1F` | 所有正文和标题文本 |
| 链接 | Apple 蓝 | `#0071E3` | 仅用于交互链接 |
| 边框 | 细灰 | `#D2D2D7` | H1 下划线、分隔线 |

**设计理念**：仅使用一种强调色（蓝色）用于交互。其他所有元素使用灰度。

### 组件增强

将关键内容转换为 Obsidian Callout：

- `> [!abstract]` - 核心概念和摘要
- `> [!note]` - 重要信息和提示
- `> [!info]` - 补充细节
- `> [!warning]` - 关键警告

**转换规则**：当内容值得强调时，转换为适当的 Callout 类型。

## 文件操作规则（重要）

> [!warning] 关键约束
> **严格遵守以下文件操作规则，违者将偏离技能设计初衷。**

### 编辑模式

**必须使用的方式**：
```markdown
✅ 正确：使用 Edit 工具
- 读取文件：Read /path/to/file.md
- 编辑文件：Edit /path/to/file.md
  - old_string: "原文内容..."
  - new_string: "格式化后的内容..."
```

**禁止使用的方式**：
```markdown
❌ 错误：使用 Write 工具创建新文件
Write /path/to/new-file.md
❌ 错误：输出格式化后的内容到聊天
以下是格式化后的内容：
...
❌ 错误：创建备份或副本
Write /path/to/file-backup.md
```

### 处理流程

1. **读取原始文件**：使用 `Read` 工具读取完整文件内容
2. **应用格式化**：在内存中应用 Apple 风格转换
3. **直接替换**：使用 `Edit` 工具替换整个文件内容
4. **确认完成**：简单通知用户文件已格式化

### 用户交互

**推荐的回复格式**：
```markdown
✅ 已将 [文件名] 格式化为 Apple 风格
- 应用三级标题结构（H1-H3）
- 添加 YAML frontmatter
- 转换重点内容为 Callouts
- 调整间距为 1.8 行高 + 1.2em 段落间距
```

**避免的回复格式**：
```markdown
❌ 不要显示完整的格式化后内容
❌ 不要创建"格式化版本"和"原始版本"的对比
❌ 不要询问是否保存到新位置
```

### 特殊情况处理

**文件过大**（>5000 行）：
- 分段使用 `Edit` 工具
- 每次替换一个主要章节
- 保持文件完整性

**只读文件**：
- 通知用户文件权限问题
- 提供格式化后的内容供手动复制
- 不创建新文件

## 处理工作流

遵循这个四步转换流程：

### Step 1: 清理（Clean）

移除结构噪音并标准化格式：

**操作**：
- 移除多余的空行（元素之间单一间距）
- 修正标点间距（确保逗号、句号后有空格）
- 标准化引号和破折号字符（直引号、长破折号）
- 移除 Markdown 残留（多余的 `*`、`_`、`#`）
- 修剪行尾空白

**转换示例**：
```markdown
Before:
Text  with  irregular    spacing。



After:
Text with regular spacing.
```

### Step 2: 结构化（Structure）

建立清晰的 H1-H3 逻辑层级：

**操作**：
- 识别主要主题 → 转换为 `H1`
- 识别子主题 → 转换为 `H2`
- 识别次要划分 → 转换为 `H3`
- 最多三个级别——平化更深的结构
- 确保逻辑流畅（无孤立的标题）

**层级规则**：
```
H1: 主要文档章节（每个文档 2-4 个）
 H2: H1 下的子章节（每个 H1 下 3-6 个）
  H3: H2 下的细节（每个 H2 下 2-5 个）
```

### Step 3: 增强（Enhance）

注入 Obsidian 特定的元数据和组件：

**YAML frontmatter 注入**：
```yaml
---
title: [从第一个 H1 提取或生成描述性标题]
created: [YYYY-MM-DD]
tags: [从内容关键词自动生成]
cssclass: apple-style
---
```

**组件转换**：
- 识别关键概念 → 包裹在 `> [!abstract]` 中
- 突出重要说明 → 包裹在 `> [!note]` 中
- 标记警告 → 包裹在 `> [!warning]` 中
- 在适当的地方将普通列表转换为任务列表

### Step 4: 字体（Font）

应用 Apple 系统字体栈：

**主要字体栈**（用于正文和标题）：
```css
font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display",
             "SF Pro Text", "PingFang SC", "Hiragino Sans GB", sans-serif;
```

**代码字体栈**：
```css
font-family: "SF Mono", "Menlo", "Monaco", "Consolas", monospace;
```

**实现**：添加到笔记的 CSS 属性或 Obsidian 主题设置中。

## 输出格式

### Obsidian 笔记结构

生成完整的 Obsidian 笔记，包含：

1. **YAML frontmatter**（始终包含）：
```yaml
---
title: [文档标题]
created: [YYYY-MM-DD]
tags: [相关的、标签、自动提取]
cssclass: apple-style
---
```

2. **标题层级**（仅 H1-H3）：
```markdown
# 主要章节（带下划线）

## 子章节（带左侧条）

### 细节（仅加粗）
```

3. **内容间距**：
- 行高：1.8
- 段落间距：1.2em
- 章节分隔：`---` 用于主要划分

4. **组件使用**：
- `> [!abstract]` 中的关键概念
- `> [!note]` 中的重要说明
- `> [!warning]` 中的警告

## 质量检查清单

在交付格式化内容之前，验证：

### 文件操作（首要检查）

- [ ] 使用 `Read` 工具读取了原始文件
- [ ] 使用 `Edit` 工具替换了文件内容
- [ ] 没有使用 `Write` 工具创建新文件
- [ ] 没有在聊天中输出完整格式化内容
- [ ] 保持文件路径不变

**结构**：
- [ ] 最多三个标题级别（H1-H3）
- [ ] 没有孤立的标题（每个标题都有内容）
- [ ] 逻辑层级流畅
- [ ] 子章节的正确嵌套

**间距**：
- [ ] 一致的行高（1.8）
- [ ] 段落间距（1.2em）
- [ ] 使用 `---` 的章节分隔
- [ ] 没有过多的空行

**内容**：
- [ ] YAML frontmatter 存在且完整
- [ ] 关键内容转换为 Callouts
- [ ] 标点符号标准化
- [ ] 没有多余的格式残留

**视觉**：
- [ ] H1 带有下划线
- [ ] H2 带有左边框
- [ ] H3 仅加粗
- [ ] 链接使用 Apple 蓝（#0071E3）

## 附加资源

### 参考文件

详细的规格和实现指南：
- **`references/design-system.md`** - 完整的 Apple 设计系统，包含 CSS 规格
- **`references/processing-guide.md`** - 逐步转换示例

### 示例文件

学习这些工作示例：
- **`examples/ob-fm-transformation.md`** - 转换前后对比
- **`examples/obsidian-note-complete.md`** - 包含所有功能的完整 Obsidian 笔记

## 集成说明

此技能与以下技能无缝协作：
- **`obsidian-markdown`** - 用于 Obsidian Flavored Markdown 语法
- **`obsidian-canvas-creator`** - 用于可视化 Canvas 布局
- **`markitdown`** - 用于将源文档转换为 Markdown

## 转换示例

> [!info] 示例说明
> 以下示例展示转换前后的内容对比。在实际操作中，**直接使用 Edit 工具替换原始文件**，不创建新文件或显示完整输出。

### 简单文本 → Apple 风格

**输入**：
```text
apple design principles
simplicity is key. clarity matters.
refinement in details.
```

**输出**：
```markdown
---
title: Apple Design Principles
created: 2024-01-25
tags: [design, apple, principles]
cssclass: apple-style
---

# Apple Design Principles

> [!abstract] 核心哲学
> Simplicity is the ultimate sophistication.

## 关键原则

### 简洁

Simplicity is key. Remove unnecessary elements.

### 清晰

Clarity matters. Ensure content is easily understood.

### 精致

Refinement in details. Every pixel counts.
```

### 博客文章 → Obsidian 笔记

将文章内容转换为结构化笔记，包含：
1. 提取的标题和元数据
2. 重构的 H1-H3 层级结构
3. 转换为 Callouts 的关键点
4. 应用的一致间距

---

**应用 Apple 的哲学**：在每个格式化决策中体现"简洁是终极的复杂"。

通过遵循四步工作流开始处理用户内容：**清理 → 结构化 → 增强 → 字体**。

---

## 核心约束总结

> [!warning] 最重要的规则
> **直接替换原始文件，禁止创建新档案**

### 执行要诀

1. **Read** → 读取原始文件
2. **Transform** → 在内存中应用 Apple 风格
3. **Edit** → 直接替换文件内容
4. **Confirm** → 简单确认完成

### 绝对禁止

- ❌ 使用 `Write` 工具
- ❌ 创建 `*-formatted.md` 新文件
- ❌ 显示完整格式化内容到聊天
- ❌ 询问用户保存位置

### 用户预期

用户提供文件路径后，期望：
- 文件原地升级为 Apple 风格
- 文件路径保持不变
- 简洁的完成通知

**记住**：Apple 风格的核心是简洁——文件操作也应如此直接。 🍎
