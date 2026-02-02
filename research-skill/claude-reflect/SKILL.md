---
name: claude-reflect
description: Self-learning system that captures corrections during sessions and reminds users to run /reflect to update CLAUDE.md. Use when discussing learnings, corrections, or when the user mentions remembering something for future sessions.
---

# Claude Reflect - 自学习系统

帮助 Claude Code 从用户修正中学习的两阶段系统。

## 工作原理

**阶段 1：捕获（自动）**
Hooks 检测修正模式（"no, use X"、"actually..."、"use X not Y"）并将它们排队到 `~/.claude/learnings-queue.json`。

**阶段 2：处理（手动）**
用户运行 `/reflect` 审查排队的 learnings 并将其应用到 CLAUDE.md 文件。

## 可用命令

| 命令 | 目的 |
|---------|---------|
| `/reflect` | 通过人工审查处理排队的 learnings |
| `/reflect --scan-history` | 扫描过去的会话以查找遗漏的 learnings |
| `/reflect --dry-run` | 预览更改而不应用 |
| `/reflect-skills` | 从重复模式中发现技能候选 |
| `/skip-reflect` | 丢弃所有排队的 learnings |
| `/view-queue` | 查看待处理的 learnings 而不处理 |

## 何时提醒用户

在以下情况下提醒用户关于 `/reflect`：
- 他们完成了一个功能或有意义的工作单元
- 他们做出了你应该为未来会话记住的修正
- 他们明确说"记住这个"或类似的话
- 上下文即将压缩并且队列中有项目

## 修正检测模式

高置信度修正：
- 工具拒绝（用户使用指导停止操作）
- "no, use X" / "don't use Y"
- "actually..." / "I meant..."
- "use X not Y" / "X instead of Y"
- "remember:"（显式标记）

## Learning 目标

- `~/.claude/CLAUDE.md` - 全局 learnings（模型名称、一般模式）
- `./CLAUDE.md` - 项目特定 learnings（约定、工具、结构）
- `commands/*.md` - 技能改进（技能执行期间的修正）

## 交互示例

```
User: no, use gpt-5.1 not gpt-5 for reasoning tasks
Claude: Got it, I'll use gpt-5.1 for reasoning tasks.

[Hook captures this correction to queue]

User: /reflect
Claude: Found 1 learning queued. "Use gpt-5.1 for reasoning tasks"
        Scope: global
        Apply to ~/.claude/CLAUDE.md? [y/n]
```
