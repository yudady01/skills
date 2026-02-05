---
name: planning-with-files
version: "2.10.0"
description: 实现 Manus 风格的基于文件的复杂任务规划。创建 task_plan.md、findings.md 和 progress.md。在开始复杂的多步骤任务、研究项目或任何需要 >5 次工具调用的任务时使用。现在支持 /clear 后的自动会话恢复。
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - WebFetch
  - WebSearch
hooks:
  PreToolUse:
    - matcher: "Write|Edit|Bash|Read|Glob|Grep"
      hooks:
        - type: command
          command: "cat task_plan.md 2>/dev/null | head -30 || true"
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: "echo '[planning-with-files] 文件已更新。如果完成了一个阶段，请更新 task_plan.md 状态。'"
  Stop:
    - hooks:
        - type: command
          command: |
            SCRIPT_DIR="${CLAUDE_PLUGIN_ROOT:-$HOME/.claude/plugins/planning-with-files}/scripts"

            IS_WINDOWS=0
            if [ "${OS-}" = "Windows_NT" ]; then
              IS_WINDOWS=1
            else
              UNAME_S="$(uname -s 2>/dev/null || echo '')"
              case "$UNAME_S" in
                CYGWIN*|MINGW*|MSYS*) IS_WINDOWS=1 ;;
              esac
            fi

            if [ "$IS_WINDOWS" -eq 1 ]; then
              if command -v pwsh >/dev/null 2>&1; then
                pwsh -ExecutionPolicy Bypass -File "$SCRIPT_DIR/check-complete.ps1" 2>/dev/null ||
                powershell -ExecutionPolicy Bypass -File "$SCRIPT_DIR/check-complete.ps1" 2>/dev/null ||
                sh "$SCRIPT_DIR/check-complete.sh"
              else
                powershell -ExecutionPolicy Bypass -File "$SCRIPT_DIR/check-complete.ps1" 2>/dev/null ||
                sh "$SCRIPT_DIR/check-complete.sh"
              fi
            else
              sh "$SCRIPT_DIR/check-complete.sh"
            fi
---

# 使用文件进行规划

像 Manus 一样工作：使用持久的 markdown 文件作为您的"磁盘上的工作记忆"。

## 首先：检查以前的会话（v2.2.0）

**在开始工作之前**，检查来自以前会话的未同步上下文：

```bash
# Linux/macOS
$(command -v python3 || command -v python) ${CLAUDE_PLUGIN_ROOT}/scripts/session-catchup.py "$(pwd)"
```

```powershell
# Windows PowerShell
& (Get-Command python -ErrorAction SilentlyContinue).Source "$env:USERPROFILE\.claude\skills\planning-with-files\scripts\session-catchup.py" (Get-Location)
```

如果追赶报告显示未同步的上下文：
1. 运行 `git diff --stat` 查看实际的代码更改
2. 阅读当前的规划文件
3. 根据追赶 + git diff 更新规划文件
4. 然后继续执行任务

## 重要：文件放在哪里

- **模板**位于 `${CLAUDE_PLUGIN_ROOT}/templates/`
- **您的规划文件**放在**您的项目目录**中

| 位置 | 内容 |
|----------|-----------------|
| 技能目录（`${CLAUDE_PLUGIN_ROOT}/`） | 模板、脚本、参考文档 |
| 您的项目目录 | `task_plan.md`、`findings.md`、`progress.md` |

## 快速开始

在任何复杂任务之前：

1. **创建 `task_plan.md`** — 使用 [templates/task_plan.md](templates/task_plan.md) 作为参考
2. **创建 `findings.md`** — 使用 [templates/findings.md](templates/findings.md) 作为参考
3. **创建 `progress.md`** — 使用 [templates/progress.md](templates/progress.md) 作为参考
4. **在决策前重新阅读计划** — 刷新注意力窗口中的目标
5. **在每个阶段后更新** — 标记完成，记录错误

> **注意：**规划文件放在您的项目根目录中，而不是技能安装文件夹中。

## 核心模式

```
上下文窗口 = RAM（易失，有限）
文件系统 = 磁盘（持久，无限）

→ 任何重要内容都会写入磁盘。
```

## 文件用途

| 文件 | 用途 | 更新时机 |
|------|---------|----------------|
| `task_plan.md` | 阶段、进度、决策 | 每个阶段后 |
| `findings.md` | 研究、发现 | 任何发现后 |
| `progress.md` | 会话日志、测试结果 | 整个会话期间 |

## 关键规则

### 1. 首先创建计划
永远不要在没有 `task_plan.md` 的情况下开始复杂任务。不可协商。

### 2. 两操作规则
> "在每 2 次查看/浏览器/搜索操作后，立即将关键发现保存到文本文件。"

这可以防止视觉/多模态信息丢失。

### 3. 决策前阅读
在做出重大决定之前，阅读计划文件。这可以保持目标在您的注意力窗口中。

### 4. 操作后更新
完成任何阶段后：
- 标记阶段状态：`in_progress` → `complete`
- 记录遇到的任何错误
- 注明创建/修改的文件

### 5. 记录所有错误
每个错误都进入计划文件。这可以建立知识并防止重复。

```markdown
## 遇到的错误
| 错误 | 尝试 | 解决方案 |
|-------|---------|------------|
| FileNotFoundError | 1 | 创建默认配置 |
| API timeout | 2 | 添加重试逻辑 |
```

### 6. 永远不要重复失败
```
if action_failed:
    next_action != same_action
```
跟踪您尝试过的内容。改变方法。

## 三次错误协议

```
尝试 1：诊断并修复
  → 仔细阅读错误
  → 识别根本原因
  → 应用有针对性的修复

尝试 2：替代方法
  → 仍然出错？尝试不同的方法
  → 不同的工具？不同的库？
  → 永远不要重复完全相同的失败操作

尝试 3：更广泛的重新思考
  → 质疑假设
  → 搜索解决方案
  → 考虑更新计划

3 次失败后：升级到用户
  → 解释您尝试了什么
  → 分享具体错误
  → 请求指导
```

## 读写决策矩阵

| 情况 | 操作 | 原因 |
|-----------|--------|--------|
| 刚刚写入文件 | 不要读取 | 内容仍在上下文中 |
| 查看图像/PDF | 立即写入发现 | 多模态 → 在丢失之前转为文本 |
| 浏览器返回数据 | 写入文件 | 屏幕截图不会持久化 |
| 开始新阶段 | 阅读计划/发现 | 如果上下文过时，重新定位 |
| 发生错误 | 阅读相关文件 | 需要当前状态来修复 |
| 间隔后恢复 | 阅读所有规划文件 | 恢复状态 |

## 五问题重启测试

如果您能回答这些问题，您的上下文管理就很扎实：

| 问题 | 答案来源 |
|----------|---------------|
| 我在哪里？ | task_plan.md 中的当前阶段 |
| 我要去哪里？ | 剩余阶段 |
| 目标是什么？ | 计划中的目标声明 |
| 我学到了什么？ | findings.md |
| 我做了什么？ | progress.md |

## 何时使用此模式

**用于：**
- 多步骤任务（3+ 步骤）
- 研究任务
- 构建/创建项目
- 跨越许多工具调用的任务
- 任何需要组织的任务

**跳过：**
- 简单问题
- 单文件编辑
- 快速查找

## 模板

复制这些模板以开始：

- [templates/task_plan.md](templates/task_plan.md) — 阶段跟踪
- [templates/findings.md](templates/findings.md) — 研究存储
- [templates/progress.md](templates/progress.md) — 会话日志

## 脚本

用于自动化的辅助脚本：

- `scripts/init-session.sh` — 初始化所有规划文件
- `scripts/check-complete.sh` — 验证所有阶段完成
- `scripts/session-catchup.py` — 从以前的会话恢复上下文（v2.2.0）

## 高级主题

- **Manus 原则：** 参阅 [reference.md](reference.md)
- **真实示例：** 参阅 [examples.md](examples.md)

## 反模式

| 不要做 | 改为这样做 |
|-------|------------|
| 使用 TodoWrite 进行持久化 | 创建 task_plan.md 文件 |
| 陈述一次目标然后忘记 | 在决策前重新阅读计划 |
| 隐藏错误并静默重试 | 将错误记录到计划文件 |
| 把所有东西都塞进上下文 | 将大内容存储在文件中 |
| 立即开始执行 | 首先创建计划文件 |
| 重复失败的操作 | 跟踪尝试，改变方法 |
| 在技能目录中创建文件 | 在您的项目中创建文件 |
