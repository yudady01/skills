# dtg-pay 项目工作流说明文档

本文档介绍 dtg-pay 项目中可用的 Claude Code 工作流。

## 可用工作流

### `/workflow` - 环境信息概览

**功能**: 显示当前项目的基本信息，包括问候语、工作目录和 Git 分支。

**使用方法**:
```
/workflow
```

**输出内容**:
- 问候语
- 当前工作目录
- 当前 Git 分支

**示例**:
```
用户: /workflow
Claude:
你好

**当前目录：** `/Users/tommy/Documents/work.nosync/dtg/dtg-pay`

**当前分支：** `EZPAY-730`
```

---

## 工作流开发规范

### 工作流文件结构

每个工作流都是一个独立的 Markdown 文件，位于 `.claude/workflows/` 目录下：

```markdown
---
description: 工作流的简短描述
---

工作流的具体内容，可以包含模板变量
```

### 可用的模板变量

在工作流中可以使用以下变量：

| 变量 | 说明 | 示例 |
|------|------|------|
| `{{workdir}}` | 当前工作目录 | `/Users/tommy/Documents/work.nosync/dtg/dtg-pay` |
| `{{git_current_branch}}` | 当前 Git 分支 | `EZPAY-730` |
| `{{git_status}}` | Git 状态 | 简化的状态信息 |

### 添加新工作流

1. 在 `.claude/workflows/` 目录下创建新的 `.md` 文件
2. 文件名即为工作流名（如 `review.md` 对应 `/review` 工作流）
3. 添加 YAML frontmatter（至少包含 `description`）
4. 在下方编写工作流内容，可使用模板变量

### 工作流示例

```markdown
---
description: 显示项目统计信息
---

**项目统计**

- 工作目录：`{{workdir}}`
- 当前分支：`{{git_current_branch}}`
- 语言：Java
- 框架：Spring Boot + Dubbo
```

## 工作流 vs 命令

| 特性 | Commands | Workflows |
|------|----------|-----------|
| 用途 | 执行特定任务 | 显示信息或执行多步骤流程 |
| 模板变量 | 不支持 | 支持 `{{workdir}}` 等变量 |
| 典型场景 | 代码审查、生成代码 | 项目信息、环境检查 |

## 注意事项

- 工作流文件名建议使用小写字母和连字符
- description 应简洁明了，说明工作流的用途
- 模板变量使用 `{{变量名}}` 格式
- 工作流适合需要动态获取项目信息的场景
