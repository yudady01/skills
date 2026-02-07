# Ralph 调用技能

**允许 Claude 直接启动 Ralph-Wiggum 自主循环，无需用户命令。**

## 前置条件

`ralph-wiggum` 插件必须已安装并启用：
```
/plugin install ralph-wiggum@claude-code-plugins
/plugin enable ralph-wiggum@claude-code-plugins
```

## 触发条件

在以下情况下使用此技能：
- 用户要求"启动 ralph 循环"或"运行 ralph"
- 用户希望对任务进行自主迭代
- 用户说"持续工作直到完成"或"迭代直到完成"
- 复杂任务将受益于多次迭代
- 用户明确请求 Claude 调用 ralph

## 如何启动 Ralph 循环

运行此 bash 命令：

```bash
"$HOME/.claude/plugins/cache/claude-code-plugins/ralph-wiggum/1.0.0/scripts/setup-ralph-loop.sh" \
  "<TASK_DESCRIPTION>" \
  --max-iterations <N> \
  --completion-promise "<PROMISE_TEXT>"
```

### 参数

| 参数 | 必需 | 默认值 | 描述 |
|-----------|----------|---------|-------------|
| TASK_DESCRIPTION | 是 | - | 要处理的任务 |
| --max-iterations | 推荐 | 无限制 | 安全限制（建议使用 20-100） |
| --completion-promise | 推荐 | null | 真正完成时输出的文本 |

### 示例调用

**简单任务：**
```bash
"$HOME/.claude/plugins/cache/claude-code-plugins/ralph-wiggum/1.0.0/scripts/setup-ralph-loop.sh" \
  "修复所有 TypeScript 类型错误" \
  --max-iterations 50 \
  --completion-promise "ALL_ERRORS_FIXED"
```

**复杂重构：**
```bash
"$HOME/.claude/plugins/cache/claude-code-plugins/ralph-wiggum/1.0.0/scripts/setup-ralph-loop.sh" \
  "将所有 API 处理程序迁移到新的 v2 模式" \
  --max-iterations 100 \
  --completion-promise "MIGRATION_COMPLETE"
```

## 循环如何工作

1. **Claude 运行设置脚本** → 在 `.claude/ralph-loop.local.md` 创建状态文件
2. **Claude 处理任务** → 正常操作
3. **Claude 尝试退出** → Stop hook 拦截
4. **Hook 重新注入提示** → Claude 继续处理相同任务
5. **重复**直到：
    - 达到最大迭代次数，或
    - Claude 输出 `<promise>PROMISE_TEXT</promise>`

## 完成循环

当任务真正完成时，在 XML 标签中输出完成承诺：

```
<promise>ALL_ERRORS_FIXED</promise>
```

**关键规则：**
- 仅在陈述为 TRUE 时输出承诺
- 不要撒谎以退出循环
- 即使卡住也不要输出虚假承诺
- 信任过程 - 如果卡住，请以不同方式迭代尝试

## 取消循环

如需要，使用以下命令取消：
```bash
rm .claude/ralph-loop.local.md
```

或使用：`/ralph-wiggum:cancel-ralph`

## 最佳实践

1. **始终设置 --max-iterations** - 防止成本失控（50-100 是合理的）
2. **使用具体的完成承诺** - 使用 "ALL_TESTS_PASS" 而不是 "DONE"
3. **在任务中包含成功标准** - 明确说明"完成"的含义
4. **监控进度** - 使用 `head -10 .claude/ralph-loop.local.md`
5. **从小开始** - 首先用 3-5 次迭代进行测试

## 成本警告

自主循环会快速消耗代币。50 次迭代的循环可能花费 $50-100+ 的 API 使用费用。始终使用 --max-iterations 作为安全网。

## 为什么存在此技能

官方 ralph-wiggum 插件要求用户运行 `/ralph-loop` 命令。此技能使 Claude 能够直接调用循环，实现：
- Claude 对复杂任务发起的迭代
- 来自其他技能/代理的编程式循环触发
- 无需手动命令的自动化工作流程
