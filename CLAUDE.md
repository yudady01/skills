# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个 **Claude Code 技能仓库**，包含多个针对不同项目和场景的自定义技能、命令和代理配置。所有技能都遵循 Claude Code 的插件/技能市场架构。

## 目录结构

```
skills/
├── dtg-claude/          # DTG 支付系统专用技能集
├── dtg-agy/             # DTG Antigravity 代理配置
├── global-claude/       # 全局通用技能（en2zh, repeatable-sql）
├── mr9-agy-plt/         # MR9 PLT Antigravity 代理配置
├── mr9-agy-cs/          # MR9 CS Antigravity 代理配置
├── mr9-claude-plt/      # MR9 PLT 后端技能集
├── mr9-claude-cs/       # MR9 CS 客户端技能集
├── research-skill/      # 研究性技能和插件
├── template/            # 技能模板
└── docs/                # 项目文档
```

## 核心概念

### 技能 (Skill)

每个技能目录包含：
- `SKILL.md` - 技能定义文件（YAML frontmatter + 指令）
- `skills/` - 资源文件（模板、参考文档、脚本）
- 可选的 Python 脚本用于自动化验证

### 命令 (Command)

位于 `commands/` 目录，Markdown 文件格式：
- YAML frontmatter 定义元数据
- 文件名对应命令名（如 `hi.md` → `/hi`）
- 示例：`/agy-impl` - 执行 Antigravity 计划

### 代理配置 (Agent)

位于各 `*-agy/` 目录：
- `AGENT.md` - 项目特定上下文和架构指南
- `rules/` - 代码风格和开发规范
- `install.md` - 安装说明

### Hook (钩子)

用于在特定事件触发自定义行为：
- `hooks/hooks.json` - Hook 配置
- 支持 SessionStart, PreToolUse, PostToolUse, UserPromptSubmit 等事件
- 技能评估 Hook 自动推荐相关技能

## 常用命令

### 技能开发

```bash
# 列出所有技能
find . -name "SKILL.md"

# 验证技能 YAML frontmatter
python3 dtg-claude/scripts/evaluate_skills.py
```

### 技能模板结构

```markdown
---
name: skill-name
description: 技能描述，说明何时使用
tags: [tag1, tag2]
version: 1.0.0
---

# 技能指令内容
...
```

## 各项目特定技能

### DTG 支付系统 (dtg-claude/)

**技术栈**: Spring Boot 2.7 + Dubbo 3.2 + MySQL + Redis + ActiveMQ

**可用技能**:
- `dtg-create-plan` - Spring Boot 技术方案与执行计划
- `dtg-i18n` - 国际化翻译
- `dtg-mysql-sync` - MySQL 同步
- `flyway-idempotent` - 幂等数据库迁移脚本
- `dev-dtg` - DTG 项目开发助手
- `s-level-testing` - S 级测试

**代码规范**: `dtg-agy/rules/xxpay_java_style.md`
- 行宽 150 字符
- 禁止通配符导入
- 严格的类成员排列顺序

### MR9 PLT 后端 (mr9-claude-plt/)

**技术栈**: Spring Boot 3.x + PostgreSQL + MyBatis Plus + Redis + RabbitMQ

**可用技能**:
- `dev-git2doc` - 抽取 Git branch 变更，自动生成开发文档
- `report-creator` - 报表创建工具

**当前任务**: 提现系统重构（移除分配步骤，实现直通车模式）

### MR9 CS 客户端 (mr9-claude-cs/)

详细的客户端开发指南见 `mr9-claude-cs/README.md`

### 全局技能 (global-claude/)

- `en2zh` - 英中技术翻译（保留代码格式）
- `repeatable-sql` - 可重复执行 SQL 技能

## Antigravity 集成

各 `*-agy/` 目录包含与 Antigravity 计划执行系统的集成：

**命令**: `/agy-impl [plan-name]`

**功能**:
1. 搜索 `~/.gemini/antigravity/brain/` 下的 `implementation_plan.md.resolved`
2. 解析计划（问题分析、修改方案、验证步骤）
3. 执行代码修改（MODIFY/DELETE/ADD）
4. 运行测试和验证
5. 生成完成报告

## Hook 配置

### 技能评估 Hook

自动分析用户输入并推荐相关技能：

**配置文件**: `dtg-claude/hooks/hooks.json`

**白名单**: `dtg-claude/scripts/lib/whitelist.json`

**置信度等级**:
- 🔥 高 (≥50%)
- ⚡ 中 (30-50%)
- 💡 低 (15-30%)

### 工具使用 Hook

在工具调用前后注入提示：
- PreToolUse: 执行前说明
- PostToolUse: 执行后确认

## 安装与使用

### 为项目配置技能

创建符号链接到项目的 `.claude` 目录：

```bash
# DTG 项目
ln -s /Users/tommy/Documents/skills/dtg-claude /path/to/dtg-pay/.claude

# MR9 项目
ln -s /Users/tommy/Documents/skills/mr9-claude-plt /path/to/mr9-plt/.claude
```

### 配置 Antigravity brain

```bash
ln -s /Users/tommy/.gemini/antigravity/brain /path/to/project/.brain
```

## 开发新技能

1. 在对应项目目录下创建 `skills/your-skill/`
2. 创建 `SKILL.md` 文件
3. 添加必要的资源文件（templates/, references/, scripts/）
4. 更新 `hooks/whitelist.json`（如需自动推荐）

## Mermaid 图表规则

创建 Mermaid 图表时遵循 `obsidian-mermaid` 技能规范（见 `mr9-agy-plt/skills/obsidian-mermaid/SKILL.md`）

## 相关资源

- [Claude Code 文档](https://docs.anthropic.com/claude/docs/claude-code)
- [插件开发指南](https://docs.anthropic.com/claude/docs/plugins)
- DTG 项目: `dtg-agy/AGENT.md`
- MR9 PLT 项目: `mr9-agy-plt/AGENT.md`
