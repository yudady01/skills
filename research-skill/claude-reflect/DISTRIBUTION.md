# claude-reflect 分发策略

本文档概述了在 Claude Code 插件市场和 awesome-lists 中最大化插件分发的提交材料。

## 优先目标（按影响力排名）

### 第一层：高影响力

| 平台 | 类型 | 预估覆盖范围 | 状态 |
|----------|------|-----------------|--------|
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | 官方市场 | 最高 | [PR #111](https://github.com/anthropics/claude-plugins-official/pull/111) |
| [ccplugins/awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins) | 精选列表 | ~1k+ stars | [PR #8](https://github.com/ccplugins/awesome-claude-code-plugins/pull/8) |
| [jeremylongshore/claude-code-plugins-plus](https://github.com/jeremylongshore/claude-code-plugins-plus) | 市场（243+ 插件） | 高 | [PR #241](https://github.com/jeremylongshore/claude-code-plugins-plus-skills/pull/241) |

### 第二层：中等影响力

| 平台 | 类型 | 状态 |
|----------|------|--------|
| [GiladShoham/awesome-claude-plugins](https://github.com/GiladShoham/awesome-claude-plugins) | 市场 | 就绪 |
| [hekmon8/awesome-claude-code-plugins](https://github.com/hekmon8/awesome-claude-code-plugins) | 精选列表 | 就绪 |
| [jmanhype/awesome-claude-code](https://github.com/jmanhype/awesome-claude-code) | 精选列表 | 就绪 |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 工作流/Hooks 专注 | 就绪 |

### 第三层：额外覆盖

| 平台 | 类型 | 状态 |
|----------|------|--------|
| [claudecodecommands.directory](https://claudecodecommands.directory/submit) | Web 目录 | 就绪 |
| [claude-plugins.dev](https://claude-plugins.dev) | 社区注册表 | 就绪 |
| [ananddtyagi/cc-marketplace](https://github.com/ananddtyagi/claude-code-marketplace) | 市场 | 就绪 |

---

## 提交 1：anthropics/claude-plugins-official

**目标**：`external_plugins/claude-reflect/`

**要求**：
- 必须符合质量和安全标准
- 带有 `.claude-plugin/plugin.json` 的标准插件结构
- README 文档
- 无硬编码的秘密

### PR 标题
```
feat: Add claude-reflect - self-learning system for CLAUDE.md
```

### PR 描述
```markdown
## Summary

Adds **claude-reflect** to external_plugins - a self-learning system that captures user corrections during Claude Code sessions and syncs them to CLAUDE.md.

## What it does

- **Automatic capture**: Hooks detect correction patterns ("no, use X", "actually...", "remember:") and queue them
- **Human review**: `/reflect` command processes queue with user approval before writing
- **Multi-target sync**: Updates ~/.claude/CLAUDE.md, ./CLAUDE.md, and AGENTS.md (industry standard)
- **Historical scan**: `/reflect --scan-history` finds corrections from past sessions

## Plugin Features

| Feature | Description |
|---------|-------------|
| Hooks | PreCompact (backup queue), PostToolUse (post-commit reminder) |
| Commands | `/reflect`, `/skip-reflect`, `/view-queue` |
| Pattern Detection | Corrections, positive feedback, explicit "remember:" markers |
| Confidence Scoring | 0.60-0.90 based on pattern strength |

## Quality Checklist

- [x] Standard plugin structure with `.claude-plugin/plugin.json`
- [x] Comprehensive README with usage examples
- [x] MIT License
- [x] No hardcoded secrets or credentials
- [x] Tested locally
- [x] Scripts have proper permissions

## Installation

```bash
/plugin install claude-reflect@claude-plugins-official
```

## Links

- Repository: https://github.com/bayramannakov/claude-reflect
- License: MIT
```

---

## 提交 2：ccplugins/awesome-claude-code-plugins

**类别**：工作流编排（或开发工程）

### PR 标题
```
Add claude-reflect to Workflow Orchestration
```

### 要添加的条目（在 README.md 中的"Workflow Orchestration"下）
```markdown
- [claude-reflect](https://github.com/bayramannakov/claude-reflect) - Self-learning system that captures corrections during sessions and syncs to CLAUDE.md. Features hook-based detection, confidence scoring, and multi-target export to AGENTS.md.
```

---

## 提交 3：GiladShoham/awesome-claude-plugins

**结构**：`plugins/claude-reflect/` 下的完整插件目录

### 所需文件

```
plugins/claude-reflect/
├── .claude-plugin/
│   └── plugin.json       # 从仓库复制
├── hooks/
│   └── hooks.json        # 从仓库复制
├── commands/
│   ├── reflect.md
│   ├── skip-reflect.md
│   └── view-queue.md
└── README.md             # 摘要版本
```

### plugin.json
```json
{
  "name": "claude-reflect",
  "version": "1.4.1",
  "description": "Self-learning system for Claude Code that captures corrections and updates CLAUDE.md automatically",
  "author": {
    "name": "Bayram Annakov",
    "url": "https://github.com/bayramannakov"
  },
  "repository": "https://github.com/bayramannakov/claude-reflect",
  "license": "MIT",
  "keywords": [
    "claude-code",
    "self-learning",
    "corrections",
    "CLAUDE.md",
    "memory",
    "learnings"
  ],
  "hooks": "./hooks/hooks.json"
}
```

### PR 描述
```markdown
## Add claude-reflect plugin

A self-learning system for Claude Code that:
- Captures corrections during sessions via hooks
- Queues learnings with confidence scoring
- Processes with human review via `/reflect`
- Syncs to CLAUDE.md and AGENTS.md

### Validation
- [x] Ran `./validate-plugins.sh` successfully
- [x] JSON schema valid
- [x] No duplicate names
- [x] All references accurate
```

---

## 提交 4：jeremylongshore/claude-code-plugins-plus

**选项 A：外部同步请求**（推荐 - 维护者每天从你的仓库镜像）

电子邮件至：jeremy@intentsolutions.io
```
Subject: External Plugin Sync Request: claude-reflect

Hi Jeremy,

I'd like to request external plugin synchronization for claude-reflect:

Repository: https://github.com/bayramannakov/claude-reflect
Category: Workflow Orchestration / Development Tools

Description: Self-learning system that captures corrections during Claude Code sessions and syncs them to CLAUDE.md. Features:
- Hook-based pattern detection (corrections, positive feedback, explicit markers)
- Confidence scoring (0.60-0.90)
- Human review via /reflect command
- Multi-target export (CLAUDE.md + AGENTS.md)

The plugin is production-ready with MIT license. Happy to provide any additional information needed.

Best,
Bayram Annakov
```

**选项 B：直接 PR**

添加到 `plugins/community/claude-reflect/`，使用标准结构。

---

## 提交 5：hekmon8/awesome-claude-code-plugins

### PR 标题
```
Add claude-reflect - self-learning CLAUDE.md manager
```

### 要添加的条目
```markdown
### Workflow Orchestration
- [claude-reflect](https://github.com/bayramannakov/claude-reflect) - Captures corrections during sessions and syncs to CLAUDE.md with human review. Includes hooks for automatic detection and confidence scoring.
```

---

## 提交 6：jmanhype/awesome-claude-code

### 类别：插件和扩展

### 要添加的条目
```markdown
- **[claude-reflect](https://github.com/bayramannakov/claude-reflect)** - Self-learning system that captures corrections and updates CLAUDE.md automatically
  ```bash
  /plugin marketplace add bayramannakov/claude-reflect
  /plugin install claude-reflect@claude-reflect-marketplace
  ```
```

---

## 提交 7：hesreallyhim/awesome-claude-code

### 类别：Hooks（主要）+ Agent Skills

### 要添加的条目
```markdown
### Hooks
- [claude-reflect](https://github.com/bayramannakov/claude-reflect) - Self-learning hooks that capture corrections (PreCompact backup, PostToolUse reminders) and sync to CLAUDE.md via `/reflect` command.
```

---

## 提交 8：claudecodecommands.directory

**URL**：https://claudecodecommands.directory/submit

### 表单字段

| 字段 | 值 |
|-------|-------|
| 名称 | claude-reflect |
| 描述 | Self-learning system that captures corrections during Claude Code sessions and syncs them to CLAUDE.md with human review |
| 仓库 URL | https://github.com/bayramannakov/claude-reflect |
| 类别 | Workflow / Development Tools |
| 命令 | /reflect, /skip-reflect, /view-queue |
| 作者 | Bayram Annakov |

---

## 提交 9：claude-plugins.dev

**GitHub**：https://github.com/Kamalnrf/claude-code-plugins

### PR 添加到注册表

查看他们的 CONTRIBUTING.md 或打开 issue 请求添加。

---

## 营销文案

### 一句话
> Self-learning system for Claude Code that captures corrections and syncs to CLAUDE.md

### 简短描述（125 字符）
> Captures user corrections during sessions, queues with confidence scoring, processes with human review via /reflect command

### 完整描述
> claude-reflect is a two-stage self-learning system for Claude Code. Stage 1 automatically captures corrections via hooks - detecting patterns like "no, use X", "actually...", and explicit "remember:" markers. Stage 2 is the `/reflect` command where you review queued learnings before they're written to CLAUDE.md. Supports confidence scoring, historical session scanning, semantic deduplication, and multi-target export to AGENTS.md (Codex, Cursor, Aider, Jules, Zed, Factory).

### 主要功能（要点）
- Automatic correction detection via hooks
- Confidence scoring (0.60-0.90)
- Human review before writing
- Historical session scanning
- Multi-target sync (CLAUDE.md + AGENTS.md)
- Semantic deduplication

---

## 执行清单

1. [ ] Fork anthropics/claude-plugins-official → PR 到 external_plugins/
2. [ ] Fork ccplugins/awesome-claude-code-plugins → PR 带条目
3. [ ] Fork GiladShoham/awesome-claude-plugins → PR 带完整插件结构
4. [ ] 发送电子邮件给 jeremylongshore 进行外部同步 OR fork claude-code-plugins-plus
5. [ ] Fork hekmon8/awesome-claude-code-plugins → PR 带条目
6. [ ] Fork jmanhype/awesome-claude-code → PR 带条目
7. [ ] Fork hesreallyhim/awesome-claude-code → PR 带条目
8. [ ] 在 claudecodecommands.directory/submit 提交表单
9. [ ] 在 Kamalnrf/claude-code-plugins 打开 issue/PR

---

## 注意事项

- 在平台上保持一致的描述
- 链接回主仓库：https://github.com/bayramannakov/claude-reflect
- 使用 MIT 许可证（已就位）
- 提交时的版本：1.4.1
