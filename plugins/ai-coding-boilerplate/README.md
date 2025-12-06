# Spring Boot 2.7 + Dubbo AI Coding Boilerplate Plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin-purple)](https://claude.ai/code)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-2.7-brightgreen.svg)](https://spring.io/projects/spring-boot)
[![Apache Dubbo](https://img.shields.io/badge/Apache%20Dubbo-3.2.14-blue.svg)](https://dubbo.apache.org/)

为 Claude Code 优化的 Spring Boot 2.7 + Dubbo 企业级微服务项目模板插件，专为企业级分布式系统开发设计，提供完整的 AI 驱动微服务架构开发流程。

**核心特性**:
- 🏗️ 微服务架构 (Spring Boot + Dubbo)
- 📊 完整的运营管理后台
- 🔧 分布式部署支持

## 🛠️ 技术栈

### 后端技术栈
| 技术 | 版本 | 用途 |
|------|------|------|
| Java | JDK 11 | 编程语言 |
| Spring Boot | 2.7.18 | 应用框架 |
| Apache Dubbo | 3.2.14 | 微服务框架 |
| MySQL | 8.0.33 | 主数据库 |
| MongoDB | - | 文档数据库 |
| Redis | - | 缓存 |
| ActiveMQ | - | 消息队列 |
| MyBatis-Plus | 3.5.7 | ORM框架 |
| HikariCP | - | 连接池 |
| Zookeeper | - | 注册中心 |
| Spring Actuator | + Prometheus | 监控 |

### 前端技术栈
| 技术 | 版本 | 说明 |
|------|------|------|
| Layui | v2.3.0 | UI框架 |
| jQuery | 1.11.1 | JavaScript库 |
| ECharts | - | 图表库 |

### 🚀 功能特性

### 🤖 专业化 AI 代理系统
- **需求分析代理** - 智能评估分布式系统规模和确定微服务边界
- **任务执行代理** - 执行 Spring Boot + Dubbo 微服务实现任务
- **代码审查代理** - 自动化 Java 代码合规性和 Dubbo 最佳实践检查
- **架构优化代理** - 提供微服务架构设计建议和分布式系统优化方案

### ⚡ 完整的斜杠命令
- `/implement` - 端到端 Spring Boot + Dubbo 微服务开发
- `/task` - 单一任务精确执行，支持分布式业务逻辑
- `/design` - 创建微服务架构设计文档和服务边界图
- `/review` - Java 代码合规性检查和 Dubbo 最佳实践审查
- `/project-inject` - Spring Boot + Dubbo 项目上下文配置
- `/code-quality` - 微服务代码质量和分布式系统性能检查
- `/microservice` - Dubbo 微服务架构设计和实现
- `/database` - 分布式数据库设计和 MyBatis-Plus 实体生成

### 📚 文档模板系统
- 微服务产品需求文档模板
- 分布式系统架构决策记录（ADR）模板
- Dubbo 服务 API 设计文档模板
- 分布式数据库设计文档模板
- 微服务部署运维文档模板

### 🔧 开发工具集成
- Spring Boot 2.7 + Apache Dubbo 3.2.14 框架集成
- Maven 构建工具和依赖管理
- JUnit 5 + Mockito 微服务测试框架
- Checkstyle 代码质量工具和 Dubbo 规范检查
- SonarQube 集成和代码质量监控
- Docker 容器化和 Kubernetes 部署支持
- Spring Security + JWT 分布式安全框架
- MyBatis-Plus 数据访问层和多数据源支持
- Zookeeper 服务发现和配置中心
- Redis 缓存和 ActiveMQ 消息队列
- Prometheus + Grafana 监控体系

## 📦 安装

```bash
# 方式1: 从 Marketplace 安装（推荐）
claude --install ai-coding-boilerplate

# 方式2: 本地安装
claude --plugin-dir /path/to/ai-coding-boilerplate
```

## 🚀 快速开发

### 环境要求
- **JDK**: 11+
- **Maven**: 3.6+
- **MySQL**: 8.0+
- **Redis**: 5.0+
- **Zookeeper**: 3.6+

## 🎯 快速开始

### 1. Spring Boot + Dubbo 微服务项目初始化
```bash
# 启动 Claude Code
claude

# 注入 Spring Boot + Dubbo 项目上下文
/project-inject

# 开始开发分布式微服务功能
/implement "实现用户认证和授权微服务，支持 Dubbo 服务调用"

# 创建分布式数据库设计
/database "设计用户管理分布式数据库表结构，支持分库分表"
```

### 2. 日常分布式微服务开发工作流
```bash
# 小任务
/task "修复 Dubbo 服务调用超时配置问题"

# 微服务开发
/implement "实现订单管理微服务，包括库存扣减和支付集成，使用 ActiveMQ 异步处理"

# 微服务架构设计
/design "设计高并发的秒杀系统微服务架构，包含缓存和消息队列"

# 代码审查和 Dubbo 最佳实践检查
/review

# 微服务代码质量和分布式系统检查
/code-quality

# Dubbo 微服务架构评估
/microservice "评估现有单体应用的 Dubbo 微服务拆分方案"
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
projectName: "企业级微服务项目"
projectType: "enterprise-microservice"
springBootVersion: "2.7.x"
javaVersion: "11"
techStack: ["Spring Boot", "Spring Cloud", "Spring Security", "Spring Data JPA", "MySQL", "Redis", "Docker"]
buildTool: "maven"
teamSize: 5
architecture: "microservices"
database: "mysql"
cache: "redis"
messageQueue: "rabbitmq"
containerPlatform: "docker"
---

企业级 Spring Boot 项目特定配置信息
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