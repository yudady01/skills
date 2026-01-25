# AGY-Impl Plugin

Antigravity 计划实作插件 - 根据 `implementation_plan.md.resolved` 文件自动执行代码修改和验证。

## 简介

这是一个专门用于执行 Antigravity 计划实作的 Claude Code 插件。该插件会根据存储在 `~/.gemini/antigravity/brain` 目录下的 `implementation_plan.md.resolved` 文件，自动执行代码修改和验证工作。

## 安装

```bash
# 将插件复制到 Claude 插件目录
cp -r agy-impl ~/.claude/plugins/
```

## 使用方法

### 方式 1：使用 Command（推荐）

直接使用 `/agy-impl` 命令：

```bash
# 执行指定的 Antigravity 计划
/agy-impl EZPAY-730-3

# 列出所有可用的计划
/agy-impl
```

### 方式 2：自然语言触发

在对话中使用自然语言描述：

**英文触发:**
```
implement antigravity plan EZPAY-730-3
execute Antigravity implementation plan
```

**中文触发:**
```
实作 EZPAY-730-3 计划
执行 Antigravity 计划
帮我实作 EZPAY-730-3
```

## 工作流程

```
用户输入计划名称
       ↓
搜索 ~/.gemini/antigravity/brain/**/implementation_plan.md.resolved
       ↓
匹配包含计划名称的文件
       ↓
解析计划内容（问题分析、修改方案、验证步骤）
       ↓
展示计划摘要并请求用户确认
       ↓
    [用户确认]
    ↙         ↘
  是(执行)   否(放弃)
    ↓           ↓
按计划执行   退出流程
代码修改
    ↓
运行测试和验证
    ↓
生成完成报告
```

### 用户确认机制

在找到并解析计划后，插件会展示以下信息并请求确认：

```
📋 找到 Antigravity 计划：[计划名称]

📄 计划文件：[完整路径]

🎯 实作概要：
- 问题概要：[简短描述]
- 修改文件：[N] 个文件
- 操作类型统计：
  - MODIFY: [N] 处
  - DELETE: [N] 处
  - ADD: [N] 处
- 风险等级：[高/中/低]

⚠️ 即将执行代码修改，请确认是否继续？
```

**确认选项：**
- **是** → 开始执行代码实作
- **否** → 放弃执行，退出流程

## 支持的操作

- **MODIFY**: 修改现有代码
- **DELETE**: 删除代码或方法
- **ADD**: 添加新代码

## 计划文件格式

代理期望找到符合以下格式的 `implementation_plan.md.resolved` 文件：

```markdown
# [计划名称] [标题]

## 问题概要
| 问题 | 风险等级 | 影响 |
|------|---------|------|
| ... | ... | ... |

## 问题分析
[详细的问题分析]

## 修改方案
### [MODIFY] [文件路径]
[diff 格式的修改内容]

## 验证计划
### 自动化测试
```bash
[测试命令]
```

## 修改文件清单
| 文件 | 操作 | 问题 |
|------|------|------|
```

## 版本

- 版本: 1.0.0
- 创建日期: 2026-01-25
