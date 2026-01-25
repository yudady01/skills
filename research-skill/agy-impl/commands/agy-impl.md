---
description: 执行 Antigravity 计划实作
argument-hint: [plan-name]
allowed-tools: Bash, Glob, Grep, Read, Edit, Write, NotebookEdit, TodoWrite
---

执行 Antigravity 计划实作：$ARGUMENTS

使用 agy-impl skill 来：
1. 搜索 ~/.gemini/antigravity/brain 目录下的 implementation_plan.md.resolved 文件
2. 解析计划内容（问题分析、修改方案、验证步骤）
3. 执行代码修改（MODIFY/DELETE/ADD）
4. 运行测试和验证
5. 生成完成报告

**使用示例**:
- `/agy-impl EZPAY-730-3` - 执行指定的 Antigravity 计划
- `/agy-impl` - 列出所有可用的计划
