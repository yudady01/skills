# AI Coding Boilerplate Plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin-purple)](https://claude.ai/code)

为 Claude Code 优化的 TypeScript 项目模板插件，通过专业化 AI 代理和自动化工作流程实现高质量、高效率的开发体验。

## 🚀 功能特性

### 🤖 专业化 AI 代理系统
- **需求分析代理** - 智能评估工作规模和确定所需文档
- **任务执行代理** - 执行具体的实现任务
- **代码审查代理** - 自动化代码合规性检查

### ⚡ 完整的斜杠命令
- `/implement` - 端到端功能开发
- `/task` - 单一任务精确执行
- `/design` - 创建设计文档
- `/review` - 代码合规性检查
- `/project-inject` - 项目上下文配置
- `/code-quality` - 代码质量检查

### 📚 文档模板系统
- PRD（产品需求文档）模板
- ADR（架构决策记录）模板
- 设计文档模板
- 工作计划模板

### 🔧 开发工具集成
- Vitest 测试框架
- Biome 代码质量工具
- TypeScript 严格模式
- 自动化质量检查

## 📦 安装

```bash
# 方式1: 从 Marketplace 安装（推荐）
claude --install ai-coding-boilerplate

# 方式2: 本地安装
claude --plugin-dir /path/to/ai-coding-boilerplate
```

## 🎯 快速开始

### 1. 项目初始化
```bash
# 启动 Claude Code
claude

# 注入项目上下文
/project-inject

# 开始开发功能
/implement "你的功能需求"
```

### 2. 日常开发工作流
```bash
# 小任务
/task "修复登录 bug"

# 功能开发
/implement "添加用户认证功能"

# 代码审查
/review

# 质量检查
/code-quality
```

## 📖 详细文档

### 使用指南
- [快速开始指南](docs/guides/quickstart.md)
- [命令参考](docs/guides/commands.md)
- [代理系统说明](docs/guides/agents.md)
- [最佳实践](docs/guides/best-practices.md)

### 模板参考
- [PRD 模板](docs/templates/prd.md)
- [ADR 模板](docs/templates/adr.md)
- [设计文档模板](docs/templates/design.md)

### 开发规则
- [项目上下文](docs/rules/project-context.md)
- [编码标准](docs/rules/coding-standards.md)
- [文档规范](docs/rules/documentation-criteria.md)

## 🔧 配置

插件支持个性化配置，创建 `.claude/ai-coding-boilerplate.local.md` 文件：

```markdown
---
projectName: "我的项目"
projectType: "web"
techStack: ["TypeScript", "React", "Node.js"]
teamSize: 1
---

项目特定的配置信息
```

## 🌍 语言支持

- 🇨🇳 中文
- 🇺🇸 English

## 🤝 贡献

欢迎贡献！请查看 [贡献指南](CONTRIBUTING.md)。

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件。

---

基于原始 [AI Coding Project Boilerplate](https://github.com/shinpr/ai-coding-project-boilerplate) 项目开发。