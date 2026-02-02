# 变更日志

claude-reflect 的所有重要更改都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)，
并且本项目遵循 [语义版本控制](https://semver.org/spec/v2.0.0.html)。

## [2.5.0] - 2026-01-25

### 新增
- **会话开始提醒** - 新的 SessionStart hook 在会话开始时显示待处理的 learnings (#13)
  - 显示最多 5 个 learnings 及其置信度分数
  - 提醒在适当的时间运行 `/reflect`
  - 可以通过 `CLAUDE_REFLECT_REMINDER=false` 环境变量禁用
  - 感谢 @xqliu 的贡献！

## [2.4.0] - 2026-01-23

### 新增
- **捕获反馈** - Hooks 现在在捕获 learnings 时输出确认 (#10)
  - 示例：`📝 Learning captured: 'no, use gpt-5.1 not gpt-5' (confidence: 85%)`
  - Claude 实时确认捕获
- **/view-queue 中的置信度** - 队列显示现在显示置信度分数、模式和相对时间戳
  - 格式：`[0.85] "message preview..." (pattern-name) - 2 days ago`
- **Guardrail 模式检测** - "don't do X" 约束的新模式类型
  - 检测："don't add X unless"、"only change what I asked"、"stop refactoring unrelated" 等
  - 约束型修正的更高置信度（0.85-0.90）
  - 路由到 CLAUDE.md 中的新 `## Guardrails` 部分
- **矛盾检测** - 查找冲突 CLAUDE.md 条目的语义分析
  - semantic_detector.py 中的新 `detect_contradictions()` 函数
  - 集成到 `/reflect --dedupe` 工作流程中
  - 解决选项：保留第一个、保留第二个、合并或保留两者

### 更改
- `/reflect --dedupe` 现在在相似性分组之前检查矛盾
- 将 `## Guardrails` 添加到标准部分标题

## [2.1.1] - 2026-01-06

### 修复
- **插件安装错误** - 从 plugin.json 中删除了重复的 hooks 声明 (#9)
  - `hooks/hooks.json` 文件由 Claude Code 自动加载；在清单中显式声明会导致"Duplicate hooks file detected"错误

## [2.1.0] - 2026-01-05

### 新增
- **工具错误提取** - 扫描会话文件以获取重复的工具执行错误并转换为 CLAUDE.md 指南 (#7)
  - 提取连接错误、环境问题、模块未找到错误
  - 过滤掉 Claude Code guardrails 和一次性错误
  - 用法：`/reflect --scan-history --include-tool-errors`
- **强制 TodoWrite 跟踪** - `/reflect` 工作流程现在使用 TodoWrite 跟踪所有阶段

### 更改
- 通过实时进度跟踪改进了工作流程可见性

## [2.0.0] - 2026-01-04

### 新增
- **Windows 支持** - 原生 Python 脚本替换 bash，无需 WSL (#1)
- **语义 AI 检测** - 通过 `claude -p` 支持多语言 (#2, #3)
- **UserPromptSubmit Hook** - 自动捕获现已正确注册
- **GitHub Actions CI** - 在 Windows、macOS、Linux（Python 3.8 和 3.11）上自动测试
- **比较工具** - `scripts/compare_detection.py` 用于测试检测准确性
- **90 个单元测试** - 具有模拟 Claude CLI 调用的全面测试覆盖

### 更改
- Hooks 现在使用 Python 脚本而不是 bash 以实现跨平台兼容性
- `/reflect` 命令在呈现之前使用语义 AI 验证队列项
- 检测使用混合方法：正则表达式模式（快速、实时）+ 语义 AI（准确、在 /reflect 期间）
- 使用新架构更新了文档（README.md、CLAUDE.md）

### 已弃用
- Bash 脚本移至 `scripts/legacy/`（仍可供参考）

### 修复
- 由于 bash 依赖导致 Hooks 在 Windows 上失败 (#1)
- 仅英语正则表达式模式的误报 (#2)
- 多语言修正未被检测 (#3)
- UserPromptSubmit hook 未在 hooks.json 中注册

## [1.4.1] - 2025-12-xx

### 修复
- 分发文件中的关键 jq 过滤器错误
- 历史扫描现在确保始终向用户显示匹配项
- 队列项在历史扫描期间被忽略

## [1.4.0] - 2025-12-xx

### 新增
- learnings 的置信度评分（0.60-0.90）
- 积极反馈模式检测
- AGENTS.md 同步支持
- 语义去重（`/reflect --dedupe`）

## [1.3.5] - 2025-12-xx

### 更改
- PreCompact hook 现在通知并备份而不是阻止

## [1.3.4] - 2025-12-xx

### 修复
- 恢复了 UserPromptSubmit hook 以进行自动捕获
