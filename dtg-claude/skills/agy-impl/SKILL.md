---
name: agy-impl
description: This skill should be used when the user asks to "implement Antigravity plan", "execute implementation plan", "实作 Antigravity 计划", "执行实作计划", "执行 antigravity 计划", "执行计划实作", "运行实作计划", or mentions "implementation_plan.md.resolved" files. Provides specialized guidance for executing Antigravity plan implementations including plan retrieval, code modification (MODIFY/DELETE/ADD), test validation, and completion reporting.
version: 1.0.0
---

# Antigravity 计划实作指南

此 skill 提供执行 Antigravity 计划实作的完整工作流程和指导，包括计划检索、代码修改、测试验证和完成报告。

## 概述

Antigravity 计划实作涉及读取存储在 `~/.gemini/antigravity/brain` 目录下的 `implementation_plan.md.resolved` 文件，解析其中的修改方案，并精确执行代码变更。

## 计划检索

### 判断用户输入

**首先检查用户是否提供了计划名称：**

1. **用户提供计划名称**：执行「搜索计划文件」流程
2. **用户未提供计划名称**：执行「列出所有可用计划」流程

### 搜索计划文件

当用户提供计划名称时：

1. 在 `~/.gemini/antigravity/brain` 目录下递归搜索所有 `implementation_plan.md.resolved` 文件
2. 使用 Glob 工具：`~/.gemini/antigravity/brain/**/implementation_plan.md.resolved`
3. 读取每个文件内容，检查是否包含计划名称
4. 计划名称通常出现在文件标题（如 `# EZPAY-730-3 分润计算问题修复计划`）

### 验证计划文件

- 确认找到的计划文件是唯一的
- 如果找到多个匹配文件，向用户确认应该使用哪一个
- 如果找不到匹配文件，向用户报告并列出可用的计划

### 列出所有可用计划

**当用户未提供计划名称时，或者找不到匹配的计划时：**

1. 使用 Glob 工具搜索所有计划文件
2. 读取每个计划文件的标题（第一行 `#` 标题）
3. 以列表形式展示所有可用计划

**输出格式**：
```
📋 可用的 Antigravity 计划：

1. [计划名称1] - [简短描述]
   📁 ~/.gemini/antigravity/brain/[uuid-1]/implementation_plan.md.resolved

2. [计划名称2] - [简短描述]
   📁 ~/.gemini/antigravity/brain/[uuid-2]/implementation_plan.md.resolved

...

💡 使用 /agy-impl [计划名称] 执行指定计划
```

**如果没有任何计划文件**：
```
❌ 未找到任何 Antigravity 计划文件

可能的原因：
1. 计划目录 ~/.gemini/antigravity/brain/ 不存在或为空
2. 没有任何已解析的计划文件（implementation_plan.md.resolved）
```

## 计划解析

### 读取计划内容

完整读取 `implementation_plan.md.resolved` 文件并解析以下部分：

- **问题概要**: 理解要解决的问题和风险等级
- **问题分析**: 深入理解问题的根本原因
- **修改方案**: 所有需要执行的代码变更（MODIFY/DELETE/ADD）
- **验证计划**: 自动化测试和验证步骤
- **修改文件清单**: 汇总所有需要修改的文件

### 创建任务清单

根据计划的修改文件清单，使用 TodoWrite 工具创建详细的实作任务列表。

## 用户确认

### 展示计划摘要

在解析计划后、开始实作前，向用户展示计划摘要并请求确认：

```
📋 找到 Antigravity 计划：[计划名称]

📄 计划文件：[完整路径]

🎯 实作概要：
- 问题概要：[简短描述]
- 修改文件：[N] 个文件
  - [文件1路径]
  - [文件2路径]
  - ...
- 操作类型统计：
  - MODIFY: [N] 处
  - DELETE: [N] 处
  - ADD: [N] 处
- 风险等级：[高/中/低]

⚠️ 即将执行代码修改，请确认是否继续？
```

### 确认逻辑

**必须使用 AskUserQuestion 工具向用户请求确认：**

- 问题：是否执行此 Antigravity 计划？
- 选项：
  - **是** → 开始执行代码实作
  - **否** → 放弃执行，退出 skill

### 用户选择处理

**选择"是"**：
- 继续执行【代码实作】阶段

**选择"否"**：
- 输出：`❌ 用户取消执行`
- 停止实作流程

## 代码实作

### MODIFY 操作

修改现有代码时：

1. 使用 Read 工具读取完整的文件内容
2. 找到计划中指定的代码段
3. 使用 Edit 工具精确替换代码
4. 重新读取文件确认修改正确

**示例**：
```diff
-BigDecimal floatingAmount = XXPayUtil.calOrderMultiplyRate(orderAmount, layer.getFloatingRate());
+BigDecimal floatingAmount = XXPayUtil.calOrderMultiplyRateforFee(orderAmount, layer.getFloatingRate());
```

### DELETE 操作

删除代码时：

1. 使用 Edit 工具删除指定的代码段或方法
2. 确保删除后代码仍然完整（如配对的括号）
3. 检查是否有其他代码引用被删除的部分

### ADD 操作

添加新代码时：

1. 确定添加位置（文件开头、指定方法内、指定行号等）
2. 使用 Edit 工具在指定位置插入新代码
3. 验证新代码与现有代码的集成

## 验证与测试

### 编译验证

运行编译命令确保代码没有编译错误：

```bash
# Maven 项目
mvn compile

# Gradle 项目
gradle build
```

### 自动化测试

执行计划中列出的所有测试命令：

```bash
mvn test -Dtest="org.xxpay.service.service.profitsharing.*Test"
```

### 质量检查

验证修改后的代码：
- 符合项目编码规范
- 没有引入新的性能或安全问题
- 导入语句正确且无冗余

## 完成报告

实作完成后提供详细的完成报告：

```
✨ 实作完成！

📊 实作总结：
- 修改文件：[列表]
- 修改行数：约 [N] 行

🧪 验证结果：
- 编译状态：✅
- 测试通过率：[N]%

📌 后续步骤：
1. [建议的后续步骤]
```

## 输出格式规范

### 用户确认阶段（在开始实作前）

参见【用户确认】章节的计划摘要格式。

### 每个文件修改

```
📝 修改文件：[文件路径]
操作类型：[MODIFY/DELETE/ADD]
✅ 已完成
```

### 验证阶段

```
🧪 开始验证...

1️⃣ 编译验证...
✅ 编译成功

2️⃣ 运行测试...
✅ 所有测试通过
```

## 错误处理

### 找不到计划

```
❌ 未找到匹配的计划文件：[计划名称]

💡 可用的计划：
- [计划1名称]
- [计划2名称]

请确认计划名称是否正确。
```

### 修改失败

```
⚠️ 修改文件时遇到问题：[文件路径]

问题：[具体问题描述]

建议解决方案：
1. [方案1]
2. [方案2]

等待用户指示...
```

### 测试失败

```
❌ 验证失败：[测试名称]

失败原因：[具体原因]

建议：[如何修复]

实作暂停，等待问题解决...
```

## 工作原则

1. **严格遵循计划**: 不要偏离计划中定义的修改方案
2. **保持透明**: 在执行每个主要步骤前向用户说明
3. **质量优先**: 不跳过验证步骤，不容忍编译错误
4. **安全意识**: 在修改前确认当前工作分支，不提交代码（除非用户明确要求）
5. **智能处理**: 理解计划的意图，而不只是机械地执行 diff

## 可用工具

- **Bash**: 执行命令和测试
- **Glob**: 搜索计划文件
- **Grep**: 搜索代码内容
- **Read**: 读取文件内容
- **Edit**: 修改代码
- **Write**: 创建新文件
- **NotebookEdit**: 编辑 Jupyter notebook
- **TodoWrite**: 追踪任务进度

## 计划文件位置

```
~/.gemini/antigravity/brain/
├── [uuid-1]/
│   └── implementation_plan.md.resolved
├── [uuid-2]/
│   └── implementation_plan.md.resolved
└── ...
```

## 技术能力

此 skill 涵盖以下技术领域：
- Java、Spring Boot、MyBatis
- Maven/Gradle 构建工具
- 财务计算、分润系统业务逻辑
- 单元测试、集成测试最佳实践
- Git 版本控制和工作流程

## 注意事项

1. **工作目录**: 始终在用户项目的根目录下工作
2. **代码风格**: 遵循项目现有的代码风格和命名规范
3. **注释保留**: 保留有意义的注释，删除过时的注释
4. **导入管理**: 及时清理不再使用的导入语句

## 附加资源

### Reference Files

- **`references/workflow.md`** - 详细工作流程指南
- **`references/plan-format.md`** - 计划文件格式规范

### Example Files

- **`examples/plan-example.md`** - 完整计划文件示例
