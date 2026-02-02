# claude-reflect

[![GitHub stars](https://img.shields.io/github/stars/BayramAnnakov/claude-reflect?style=flat-square)](https://github.com/BayramAnnakov/claude-reflect/stargazers)
[![Version](https://img.shields.io/badge/version-2.5.0-blue?style=flat-square)](https://github.com/BayramAnnakov/claude-reflect/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-141%20passing-brightgreen?style=flat-square)](https://github.com/BayramAnnakov/claude-reflect/actions)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey?style=flat-square)](https://github.com/BayramAnnakov/claude-reflect#platform-support)

Claude Code 的自主学习系统，捕获修正并发现工作流模式 — 将它们转化为永久记忆和可重用技能。

## 功能介绍

### 1. 从修正中学习

当你修正 Claude（"不，使用 gpt-5.1 而不是 gpt-5"）时，它会永久记住。

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   你修正了      │ ──► │  Hook 捕获并    │ ──► │  /reflect 添加  │
│   Claude Code   │     │  加入队列       │     │  到 CLAUDE.md   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
      (自动)                (自动)                   (人工审查)
```

### 2. 发现工作流模式（v2 新功能）

分析你的会话历史以查找可成为可重用命令的重复任务。

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   你的过去      │ ──► │ /reflect-skills │ ──► │    生成        │
│   会话记录      │     │  查找模式       │     │   /commands     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
    (68 个会话)           (AI 驱动)              (你批准)
```

示例：你已要求"review my productivity"（审查我的生产力）12 次 → 建议创建 `/daily-review`

## 核心功能

| 功能 | 作用 |
|---------|--------------|
| **永久记忆** | 修正同步到 CLAUDE.md — Claude 跨会话记住 |
| **技能发现** | 在历史记录中查找重复模式 → 生成命令 |
| **多语言** | AI 理解任何语言的修正 |
| **技能改进** | `/deploy` 期间的修正改进部署技能本身 |

## 安装

```bash
# 添加市场
claude plugin marketplace add bayramannakov/claude-reflect

# 安装插件
claude plugin install claude-reflect@claude-reflect-marketplace

# 重要：重启 Claude Code 以激活插件
```

安装后，**重启 Claude Code**（退出并重新打开）。然后 hooks 自动配置，命令就绪。

> **首次运行？** 当你第一次运行 `/reflect` 时，系统会提示你扫描过去的会话以获取学习内容。

### 前提条件

- 已安装 [Claude Code](https://claude.ai/code) CLI
- Python 3.6+（大多数系统已包含）

### 平台支持

- **macOS**：完全支持
- **Linux**：完全支持
- **Windows**：完全支持（原生 Python，无需 WSL）

## 命令

| 命令 | 描述 |
|---------|-------------|
| `/reflect` | 通过人工审查处理排队的 learnings |
| `/reflect --scan-history` | 扫描所有过去的会话以查找遗漏的 learnings |
| `/reflect --dry-run` | 预览更改而不应用 |
| `/reflect --targets` | 显示检测到的配置文件（CLAUDE.md、AGENTS.md） |
| `/reflect --review` | 显示队列的置信度分数和衰减状态 |
| `/reflect --dedupe` | 查找并合并 CLAUDE.md 中的相似条目 |
| `/reflect --include-tool-errors` | 在扫描中包含工具执行错误 |
| `/reflect-skills` | 从重复模式中发现技能候选 |
| `/reflect-skills --days N` | 分析最近 N 天（默认：14） |
| `/reflect-skills --project <path>` | 分析特定项目 |
| `/reflect-skills --all-projects` | 扫描所有项目以查找跨项目模式 |
| `/reflect-skills --dry-run` | 预览模式而不生成技能文件 |
| `/skip-reflect` | 丢弃所有排队的 learnings |
| `/view-queue` | 查看待处理的 learnings 而不处理 |

## 工作原理

![claude-reflect in action](assets/reflect-demo.jpg)

### 两阶段过程

**阶段 1：捕获（自动）**

Hooks 自动运行以检测和排队修正：

| Hook | 触发器 | 目的 |
|------|---------|---------|
| `session_start_reminder.py` | 会话开始 | 显示待处理的 learnings 提醒 |
| `capture_learning.py` | 每个提示 | 检测修正模式并将它们排队 |
| `check_learnings.py` | 压缩之前 | 备份队列并通知用户 |
| `post_commit_reminder.py` | git commit 之后 | 提醒在工作完成后运行 /reflect |

**阶段 2：处理（手动）**

运行 `/reflect` 审查并将排队的 learnings 应用到 CLAUDE.md。

### 检测方法

Claude-reflect 使用**混合检测方法**：

**1. 正则表达式模式（实时捕获）**

会话期间的快速模式匹配检测：

- **修正**：`"no, use X"` / `"don't use Y"` / `"actually..."` / `"that's wrong"`
- **积极反馈**：`"Perfect!"` / `"Exactly right"` / `"Great approach"`
- **显式标记**：`"remember:"` — 最高置信度

**2. 语义 AI 验证（在 /reflect 期间）**

当你运行 `/reflect` 时，AI 驱动的语义过滤器：
- **多语言支持** — 理解任何语言的修正
- **更高的准确性** — 过滤掉正则表达式的误报
- **更清晰的 learnings** — 提取简洁、可操作的陈述

示例：像 `"no, usa Python"` 这样的西班牙语修正即使不匹配英语模式也能被正确检测。

每个捕获的 learning 都有一个**置信度分数**（0.60-0.95）。最终分数是正则表达式和语义置信度中的较高者。

### 人工审查

当你运行 `/reflect` 时，Claude 会显示一个摘要表格和选项：
- **应用** - 接受 learning 并添加到 CLAUDE.md
- **应用前编辑** - 先修改 learning 文本
- **跳过** - 不应用此 learning

### 多目标同步

批准的 learnings 同步到：
- `~/.claude/CLAUDE.md`（全局 - 适用于所有项目）
- `./CLAUDE.md`（项目特定）
- `./**/CLAUDE.md`（子目录 - 自动发现）
- `./.claude/commands/*.md`（技能文件 - 当修正与技能相关时）
- `AGENTS.md`（如果存在 - 适用于 Codex、Cursor、Aider、Jules、Zed、Factory）

运行 `/reflect --targets` 查看哪些文件将被更新。

### 技能发现

运行 `/reflect-skills` 发现会话中的重复模式，这些模式可能成为可重用技能：

```
/reflect-skills                 # 分析当前项目（最近 14 天）
/reflect-skills --days 30       # 分析最近 30 天
/reflect-skills --all-projects  # 分析所有项目（较慢）
/reflect-skills --dry-run       # 预览模式而不生成文件
```

**功能：**
- **AI 驱动的检测** — 使用推理而不是正则表达式来查找模式
- **语义相似性** — 在不同措辞中检测相同意图
- **项目感知** — 按项目分组模式，建议正确位置
- **智能分配** — 询问每个技能应该去哪里（项目 vs 全局）
- **生成技能文件** — 在 `.claude/commands/` 中创建草稿技能

**工作原理：**

该技能通过语义分析你的会话历史来发现模式。可以识别相同意图的不同措辞：

```
Session 1: "review my productivity for today"
Session 2: "how was my focus this afternoon?"
Session 3: "check my ActivityWatch data"
Session 4: "evaluate my work hours"
```

Claude 推理：*"这 4 个请求具有相同的意图 - 审查生产力数据。工作流程是：获取时间跟踪数据 → 分类活动 → 计算专注度分数。这是 /daily-review 的有力候选。"*

**示例输出：**
```
════════════════════════════════════════════════════════════
SKILL CANDIDATES DISCOVERED
════════════════════════════════════════════════════════════

Found 2 potential skills from analyzing 68 sessions:

1. /daily-review (High) — from my-productivity-tools
   → Review productivity using time tracking data
   Evidence: 15 similar requests
   Corrections learned: "use local timezone", "chat apps can be work"

2. /deploy-app (High) — from my-webapp
   → Deploy application with pre-flight checks
   Evidence: 10 similar requests
   Corrections learned: "always run tests first"

════════════════════════════════════════════════════════════

Which skills should I generate?
> [1] /daily-review, [2] /deploy-app

Where should each skill be created?
┌──────────────────────┬─────────────────────────┐
│ /daily-review        │ my-productivity-tools   │
│ /deploy-app          │ my-webapp               │
└──────────────────────┴─────────────────────────┘

Skills created:
  ~/projects/my-productivity-tools/.claude/commands/daily-review.md
  ~/projects/my-webapp/.claude/commands/deploy-app.md
```

**生成的技能文件示例：**

```markdown
---
description: Deploy application with pre-flight checks
allowed-tools: Bash, Read, Write
---

## Context
Deployment scripts in ./scripts/deploy/

## Your Task
Deploy the application to the specified environment.

### Steps
1. Run test suite
2. Build production assets
3. Deploy to target environment
4. Verify deployment health

### Guardrails
- Always run tests before deploying
- Never deploy to production on Fridays
- Check for pending migrations

---
*Generated by /reflect-skills from 10 session patterns*
```

### 技能改进路由

当你使用技能时修正 Claude（例如 `/deploy`），修正可以路由回技能文件本身：

```
User: /deploy
Claude: [deploys without running tests]
User: "no, always run tests before deploying"

→ /reflect detects this relates to /deploy
→ Offers to add learning to .claude/commands/deploy.md
→ Skill file updated with new step
```

这使得技能随着时间的推移变得更智能，而不仅仅是 CLAUDE.md。

## 升级

### 从 v2.0.x 或更早版本

如果在更新后看到"Duplicate hooks file detected"或"No such file or directory"等错误，你需要清除插件缓存。这是由于已知的 Claude Code 缓存问题：
- [#14061](https://github.com/anthropics/claude-code/issues/14061) - `/plugin update` 不会使缓存失效
- [#15369](https://github.com/anthropics/claude-code/issues/15369) - 卸载不会清除缓存文件

```bash
# 1. 卸载插件
claude plugin uninstall claude-reflect@claude-reflect-marketplace

# 2. 清除两个缓存（必需！）
rm -rf ~/.claude/plugins/marketplaces/claude-reflect-marketplace
rm -rf ~/.claude/plugins/cache/claude-reflect-marketplace

# 3. 完全退出 Claude Code（重启终端或关闭应用）

# 4. 重新安装
claude plugin install claude-reflect@claude-reflect-marketplace
```

### 标准更新

对于正常更新（当没有缓存问题时）：

```bash
# 在 Claude Code 中使用 /plugin 菜单
/plugin
# 为 claude-reflect 选择"立即更新"
```

## 卸载

```bash
claude plugin uninstall claude-reflect@claude-reflect-marketplace
```

## 文件结构

```
claude-reflect/
├── .claude-plugin/
│   └── plugin.json         # 插件清单（自动注册 hooks）
├── commands/
│   ├── reflect.md          # 主命令
│   ├── reflect-skills.md   # 技能发现
│   ├── skip-reflect.md     # 丢弃队列
│   └── view-queue.md       # 查看队列
├── hooks/
│   └── hooks.json          # 安装插件时自动配置
├── scripts/
│   ├── lib/
│   │   ├── reflect_utils.py      # 共享工具
│   │   └── semantic_detector.py  # AI 驱动的语义分析
│   ├── capture_learning.py       # Hook: 检测修正
│   ├── check_learnings.py        # Hook: 预压缩检查
│   ├── post_commit_reminder.py   # Hook: 提交后提醒
│   ├── compare_detection.py      # 比较正则表达式 vs 语义检测
│   ├── extract_session_learnings.py
│   ├── extract_tool_errors.py
│   ├── extract_tool_rejections.py
│   └── legacy/                   # Bash 脚本（已弃用）
├── tests/                  # 测试套件
└── SKILL.md                # Claude 的技能上下文
```

## 功能

### 历史扫描

第一次使用 claude-reflect？运行：

```bash
/reflect --scan-history
```

这会扫描你所有过去的会话以查找你所做的修正，这样你就不会丢失安装前的 learnings。

### 智能过滤

Claude 过滤掉：
- 问题（不是修正）
- 一次性任务指令
- 特定于上下文的请求
- 模糊/不可操作的反馈

只保留可重用的 learnings。

### 重复检测

在添加 learning 之前，会检查现有的 CLAUDE.md 内容。如果存在相似内容，你可以：
- 与现有条目合并
- 替换旧条目
- 跳过重复

### 语义去重

随着时间的推移，CLAUDE.md 可能会积累相似的条目。运行 `/reflect --dedupe` 以：
- 查找语义相似的条目（即使措辞不同）
- 提议合并版本
- 清理冗余的 learnings

示例：
```
Before:
  - Use gpt-5.1 for complex tasks
  - Prefer gpt-5.1 for reasoning
  - gpt-5.1 is better for hard problems

After:
  - Use gpt-5.1 for complex reasoning tasks
```

## 提示

1. **对重要的 learnings 使用显式标记**：
   ```
   remember: always use venv for Python projects
   ```

2. **在 git 提交后运行 /reflect** - hook 会提醒你，但要养成习惯

3. **在新机器上进行历史扫描** - 设置新的开发环境时：
   ```
   /reflect --scan-history --days 90
   ```

4. **项目 vs 全局** - 模型名称和一般模式放在全局；项目特定的约定保留在项目 CLAUDE.md 中

5. **每月发现技能** - 每月运行 `/reflect-skills --days 30` 以查找你可能错过的自动化机会

6. **技能变得更智能** - 当你在技能期间修正 Claude 时，该修正可以通过 `/reflect` 路由回技能文件本身

## 贡献

欢迎拉取请求！请先阅读贡献指南。

## 许可证

MIT
