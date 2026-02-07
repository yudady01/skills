---
name: documentation
description: Enforces documentation standards and structure for this project. This skill should be used when creating, updating, or organizing documentation to ensure compliance with project rules, prevent redundancy, and maintain screen-based organization. Activates when user asks to create/update docs or when documentation needs to be generated.
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash]
---

# Documentation Skill

确保所有文档遵循项目标准并防止冗余文件。

## 目的

此技能提供高效文档管理的工具和工作流：
- 章节级交互脚本（搜索、获取、更新无需读取完整文件）
- 保持一致结构的文档模板
- 常见文档任务的工作流
- 防止冗余的规则和标准

## 何时使用此技能

在以下情况使用此技能：
- 为功能、屏幕或架构创建新文档
- 代码更改后更新现有文档
- 查找和合并重复文档
- 拆分大型文档文件（>500 行）
- 在文档中搜索特定信息
- 检查文档质量和合规性

## 核心原则

### 1. DRY（Don't Repeat Yourself）
- 创建新文件前检查现有文档
- 更新现有文档而不是创建副本
- 将相关信息合并到单个文件中

### 2. 基于屏幕的组织
```
docs/
├── README.md              # 主索引（请勿修改）
├── guides/                # 用户和开发者指南
├── architecture/          # 架构文档
└── screens/               # 屏幕特定文档
    └── {screen-name}/
        ├── README.md      # 概述（必需）
        ├── features.md    # 功能（可选）
        ├── technical.md   # 技术细节（必需）
        └── flows.md       # 流程（可选）
```

### 3. 大小限制
- 每个文件最多 500 行
- 拆分接近限制的文件（>450 行）
- 保持文档聚焦和易于浏览

## 如何使用此技能

### 步骤 1：检查现有文档

**使用脚本进行高效搜索**（减少 80-98% 的上下文）：

```bash
# 无需读取完整文件进行搜索
./scripts/doc-search.sh "topic-keyword"

# 获取文件元数据（读取 0 行）
./scripts/doc-metadata.sh docs/path/to/file.md

# 列出章节以便导航（仅结构）
./scripts/doc-list-sections.sh docs/file.md
```

**完整脚本文档：** 见 `scripts/README.md`

### 步骤 2：确定操作

**如果存在类似文档：**
- 加载工作流：`references/workflows/update-existing.md`
- 使用 `doc-get-section.sh` 仅读取相关章节
- 使用 `doc-update-section.sh` 更新章节

**如果创建新文档：**
- 加载工作流：`references/workflows/create-screen.md`
- 加载模板：`assets/templates/screen-readme.md` 或 `assets/templates/screen-technical.md`
- 遵循模板结构

**如果文件过大（>450 行）：**
- 加载工作流：`references/workflows/split-large-file.md`

**如果发现重复：**
- 加载工作流：`references/workflows/consolidate-duplicates.md`

### 步骤 3：根据规则进行验证

加载参考文件：`references/rules.md`

检查：
- ✅ 不存在重复内容
- ✅ 文件少于 500 行
- ✅ 代码引用包含 file:line 格式
- ✅ 所有代码块都指定了语言
- ✅ 示例已测试并可用

**完整规则：** 见 `references/rules.md`

## 捆绑资源

### 脚本（`scripts/`）

高效的章节级交互工具：

- **doc-search.sh** - 无需读取完整文件即可搜索内容
- **doc-list-sections.sh** - 列出所有标题及行号
- **doc-get-section.sh** - 仅提取特定章节（减少 90% 上下文）
- **doc-update-section.sh** - 无需读取完整文件即可更新章节
- **doc-delete-section.sh** - 删除章节
- **doc-insert-after.sh** - 在章节后插入内容
- **doc-metadata.sh** - 获取文件统计信息（减少 100% 上下文）
- **doc-find-duplicates.sh** - 查找冗余内容

**优势：** 与读取整个文件相比，上下文使用量减少 80-98%

**完整文档：** `scripts/README.md`

### 参考资料（`references/`）

根据需要加载以获取详细信息：

- **rules.md** - 完整的文档规则和反模式
- **structure.md** - 目录组织细节和导航
- **examples.md** - 来自此项目的真实示例（好模式 vs 坏模式）
- **workflows/** - 常见任务的分步工作流：
  - `create-screen.md` - 创建新的屏幕文档
  - `update-existing.md` - 更新现有文档
  - `consolidate-duplicates.md` - 合并重复文档
  - `split-large-file.md` - 拆分超过 500 行的文件
  - `add-examples.md` - 向文档添加示例
  - `review-quarterly.md` - 季度文档审查

### 资源（`assets/`）

文档输出中使用的模板：

- **templates/** - 文档模板：
  - `screen-readme.md` - 用于 docs/screens/{name}/README.md
  - `screen-technical.md` - 用于 docs/screens/{name}/technical.md
  - `screen-features.md` - 用于 docs/screens/{name}/features.md
  - `screen-flows.md` - 用于 docs/screens/{name}/flows.md
  - `architecture.md` - 用于 docs/architecture/*.md
  - `guide.md` - 用于 docs/guides/*.md

## 渐进式披露

此技能使用基于文件系统的渐进式披露：

**级别 1：元数据（始终在上下文中）**
- 技能名称和描述（约 100 词）

**级别 2：SKILL.md（当技能触发时）**
- 核心指令和工作流指南（约 2k 词）

**级别 3：捆绑资源（根据需要加载）**
- 脚本：执行时无需读入上下文
- 参考资料：需要详细信息时加载特定文件
- 资源：将模板复制到输出中

**示例：** 创建屏幕文档
- 之前：读取全部 3,620 行
- 之后：SKILL.md（300 行）+ 工作流（150 行）+ 模板（200 行）= 650 行（减少 82%）

## 典型工作流

### 创建新的屏幕文档

1. **检查：** `./scripts/doc-search.sh "ScreenName"`
2. **如果不存在：** 加载 `references/workflows/create-screen.md`
3. **遵循工作流：**
   - 创建目录：`docs/screens/{screen-name}`
   - 使用模板：`assets/templates/screen-readme.md`
   - 使用模板：`assets/templates/screen-technical.md`
   - 根据 `references/rules.md` 进行验证

### 更新现有文档

1. **获取元数据：** `./scripts/doc-metadata.sh docs/file.md`
2. **列出章节：** `./scripts/doc-list-sections.sh docs/file.md`
3. **获取章节：** `./scripts/doc-get-section.sh docs/file.md "Section"`
4. **更新章节：** `./scripts/doc-update-section.sh docs/file.md "Section" new-content.md`

### 查找和删除重复项

1. **查找重复：** `./scripts/doc-find-duplicates.sh docs/`
2. **加载工作流：** `references/workflows/consolidate-duplicates.md`
3. **遵循合并步骤**
4. **删除冗余文件**

## 向用户提问的问题

创建文档之前：
- "在 {path} 发现类似文档。是否更新现有文档而不是创建新文档？"
- "此功能是否已完成并准备好记录？"
- "这应该放在 screens/{screen}/、guides/ 还是 architecture/ 中？"
- "文件有 450+ 行。是否应该拆分为多个文件？"

## 成功标准

好的文档应该是：
- ✅ 易于查找（遵循 `references/structure.md` 中的结构）
- ✅ 易于阅读（少于 500 行）
- ✅ 无重复（DRY 原则）
- ✅ 最新（与当前代码匹配）
- ✅ 可操作（包含已测试的示例）
- ✅ 可追溯（包含 file:line 格式的代码引用）
