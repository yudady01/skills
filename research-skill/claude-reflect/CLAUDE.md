# CLAUDE.md

此文件为 Claude Code (claude.ai/code) 在处理此存储库中的代码时提供指导。

## 项目概述

claude-reflect 是一个 Claude Code 插件，实现了两阶段自主学习系统：
1. **捕获阶段**（自动）：Hooks 检测用户提示中的修正模式并将它们排队
2. **处理阶段**（手动）：`/reflect` 命令通过人工审查处理排队的 learnings 并写入 CLAUDE.md 文件

## 架构

```
.claude-plugin/plugin.json  → 插件清单，指向 hooks
hooks/hooks.json            → Hook 定义（PreCompact、PostToolUse）
scripts/                    → 用于 hooks 和提取的 Python 脚本
scripts/lib/                → 共享工具（reflect_utils.py）
scripts/legacy/             → 已弃用的 bash 脚本（供参考）
commands/*.md               → /reflect、/reflect-skills、/skip-reflect、/view-queue 的技能定义
SKILL.md                    → 调用插件时提供的上下文
tests/                      → 测试套件（pytest）
```

### 数据流

1. 用户提示 → `capture_learning.py`（UserPromptSubmit hook）→ `~/.claude/learnings-queue.json`
2. `/reflect` 命令 → 读取队列 + 扫描会话 → 过滤/去重 → 写入 CLAUDE.md/AGENTS.md
3. 会话文件位于 `~/.claude/projects/[PROJECT_FOLDER]/*.jsonl`

### 关键文件

- `scripts/lib/reflect_utils.py`：共享工具（路径、队列操作、正则表达式模式检测）
- `scripts/lib/semantic_detector.py`：通过 `claude -p` 进行 AI 驱动的语义分析
- `scripts/capture_learning.py`：模式检测（修正、积极、显式标记）及置信度评分
- `scripts/check_learnings.py`：在上下文压缩前备份队列的 PreCompact hook
- `scripts/extract_session_learnings.py`：从会话 JSONL 文件中提取用户消息
- `scripts/extract_tool_rejections.py`：从工具拒绝中提取用户修正
- `scripts/compare_detection.py`：比较正则表达式 vs 语义检测
- `commands/reflect.md`：主技能 - 定义 /reflect 工作流程的 850+ 行文档
- `commands/reflect-skills.md`：技能发现 - 从会话中进行 AI 驱动的模式检测

## 开发命令

```bash
# 使用模拟输入测试捕获 hook
echo '{"prompt":"no, use gpt-5.1 not gpt-5"}' | python3 scripts/capture_learning.py

# 查看当前 learnings 队列
cat ~/.claude/learnings-queue.json

# 测试会话提取
python3 scripts/extract_session_learnings.py ~/.claude/projects/[PROJECT]/*.jsonl --corrections-only

# 运行测试
python -m pytest tests/ -v

# 清空队列进行测试
echo "[]" > ~/.claude/learnings-queue.json
```

## 插件结构

插件通过 `.claude-plugin/plugin.json` 注册：
- Hooks 在 `hooks/hooks.json` 中定义
- 命令（技能）是 `commands/` 中的 markdown 文件
- 当插件处于活动状态时，`SKILL.md` 提供上下文

### Hook 事件

| Hook | 脚本 | 目的 |
|------|--------|---------|
| SessionStart | `session_start_reminder.py` | 显示待处理的 learnings 提醒 |
| UserPromptSubmit | `capture_learning.py` | 检测修正并将它们排队 |
| PreCompact | `check_learnings.py` | 在压缩前备份队列 |
| PostToolUse (Bash) | `post_commit_reminder.py` | 在提交后提醒运行 /reflect |

## 检测方法

### 正则表达式模式（实时）

`scripts/lib/reflect_utils.py` 定义模式检测：
- **修正**："no, use X"、"don't use"、"stop using"、"that's wrong"、"actually"、"use X not Y"
- **积极**："perfect!"、"exactly right"、"great approach"、"nailed it"
- **显式**："remember:" 前缀（最高置信度）

置信度分数范围为 0.60-0.90，基于模式强度和数量。

### 语义 AI 验证（在 /reflect 期间）

`scripts/lib/semantic_detector.py` 提供 AI 驱动的验证：
- 使用 `claude -p --output-format json` 进行语义分析
- **多语言支持** — 适用于任何语言，不仅仅是英语
- **更高的准确性** — 过滤掉正则表达式的误报
- **更清晰的 learnings** — 提取简洁、可操作的陈述

关键函数：
- `semantic_analyze(text)` — 分析单个消息
- `validate_queue_items(items)` — 批量验证队列项

回退：如果 Claude CLI 不可用，则使用正则表达式检测作为回退。

### 比较测试

`scripts/compare_detection.py` 比较正则表达式 vs 语义检测：
```bash
python scripts/compare_detection.py --project .
```

## 会话文件格式

会话文件是 `~/.claude/projects/[PROJECT_FOLDER]/` 中的 JSONL：
- 用户消息：`{"type": "user", "message": {"content": [{"type": "text", "text": "..."}]}, "isMeta": false}`
- 工具拒绝：`{"type": "user", "message": {"content": [{"type": "tool_result", "is_error": true, "content": "...the user said:\n[feedback]"}]}}`
- 过滤 `isMeta: true` 以排除命令扩展

## 队列项结构

```json
{
  "type": "auto|explicit|positive|guardrail",
  "message": "user's original text",
  "timestamp": "ISO8601",
  "project": "/path/to/project",
  "patterns": "matched pattern names",
  "confidence": 0.75,
  "sentiment": "correction|positive",
  "decay_days": 90
}
```

## 技能发现（/reflect-skills）

分析会话历史以发现可能成为技能的重复模式。

**设计原则：**
- **AI 驱动** — Claude 使用推理来识别模式，而不是正则表达式
- **语义相似性** — 在不同措辞中检测相同意图
- **人工参与** — 用户在技能生成前批准

**用法：**
```bash
/reflect-skills              # 分析最近 14 天
/reflect-skills --days 30    # 分析最近 30 天
/reflect-skills --dry-run    # 预览而不生成文件
```

**它检测什么：**
- 工作流模式（重复的多步骤序列）
- 误解模式（可能成为 guardrails 的修正）
- 意图相似性（相同目标，不同措辞）

## 技能改进路由

运行 `/reflect` 时，在技能执行期间所做的修正可以路由回技能文件本身。

**工作原理：**
1. `/reflect` 检测到修正是否跟在技能调用之后（例如 `/deploy`）
2. Claude 推理修正是否与技能的工作流相关
3. 向用户提供路由选项：技能文件 | CLAUDE.md | 两者
4. 在适当的部分（步骤、guardrails 等）更新技能文件

**示例：**
```
User: /deploy
Claude: [deploys without running tests]
User: "no, always run tests before deploying"

 /reflect detects this relates to /deploy
 Offers to add "Run tests before deploying" to commands/deploy.md
→ Skill file updated with new step in workflow
```

## 平台支持

- **macOS**：完全支持
- **Linux**：完全支持
- **Windows**：完全支持（原生 Python，无需 WSL）

需要 Python 3.6+。

## 发布

有关版本更新清单和发布流程，请参阅 [RELEASING.md](RELEASING.md)。
