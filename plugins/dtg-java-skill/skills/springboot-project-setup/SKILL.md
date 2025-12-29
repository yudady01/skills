---
name: springboot-project-setup
description: 企业级 Spring Boot 2.7 + Apache Dubbo 3.2.14 微服务项目配置。包含完整的项目模板、代码示例和最佳实践。
version: 2.7.0
tags: ["spring-boot", "dubbo", "microservice", "enterprise", "java"]
---

# Spring Boot 2.7 + Dubbo 微服务配置技能

企业级 Spring Boot 2.7 + Apache Dubbo 3.2.14 微服务项目配置指导。

## 核心配置文件

### 项目配置模板
- **Maven 配置**: `references/pom.xml`
- **应用配置**: `references/application.yml`
- **开发环境**: `references/application-dev.yml`
- **Lombok 配置**: `references/lombok.config`

### 代码示例
- **实体和DTO**: `references/code-examples.md`
- **Dubbo 服务**: `references/code-examples.md`
- **测试配置**: `references/test-examples.md`

### 系统配置
- **项目结构**: `references/project-structure.md`
- **安全配置**: `references/security-config.java`
- **OpenAPI 配置**: `references/openapi-config.java`
- **Docker 部署**: `references/docker-deployment.md`
- **日志配置**: `references/logging-config.xml`

## 技术栈

| 技术 | 版本 |
|------|------|
| Java | 11 |
| Spring Boot | 2.7.18 |
| Apache Dubbo | 3.2.14 |
| MyBatis-Plus | 3.5.7 |
| MySQL | 8.0.33 |
| Redis | 最新 |

## 快速开始

### 1. 创建项目
```bash
# 使用 Spring Initializr 创建 Spring Boot 2.7.18 项目
# 添加依赖: Web, Security, Validation, Redis, MongoDB, ActiveMQ
```

### 2. 添加 Dubbo 依赖
参考 `references/pom.xml`

### 3. 配置应用
复制 `references/application.yml` 到项目

### 4. 配置 Lombok
复制 `references/lombok.config` 到项目根目录

### 5. 创建实体和服务
参考 `references/code-examples.md`

## 核心概念

### Dubbo 微服务架构
- **服务接口**: 使用 `@DubboService` 注解
- **服务实现**: 实现 Dubbo 服务接口
- **注册中心**: 支持 Zookeeper/Nacos
- **协议**: 默认 dubbo 协议

### 分层架构
- **Controller**: HTTP 请求处理
- **Service**: 业务逻辑
- **Repository**: 数据访问
- **DTO**: 数据传输对象

### 测试策略
- **单元测试**: Mockito + JUnit 5
- **集成测试**: Testcontainers
- 参考 `references/test-examples.md`

## 性能优化

### 数据层
- 连接池配置
- MyBatis-Plus 二级缓存
- 索引优化

### 缓存策略
- Redis 多级缓存
- Spring Cache 注解
- 缓存一致性

## 安全配置

- JWT 认证
- RBAC 权限控制
- 数据加密
- 参考 `references/security-config.java`

## 部署

- Docker 容器化
- Docker Compose 编排
- 参考 `references/docker-deployment.md`

## 最佳实践

1. **领域驱动设计 (DDD)**: 业务与技术分离
2. **微服务架构**: 单一职责，松耦合
3. **API 版本管理**: 路径或 Header 版本控制
4. **异常处理**: 统一异常处理机制
5. **日志聚合**: ELK Stack 集中管理

## 故障排除

| 问题 | 解决方案 |
|------|----------|
| Bean 循环依赖 | 使用 @Lazy 注解或重构 |
| 事务不生效 | 检查传播行为和异常类型 |
| 缓存穿透 | 使用布隆过滤器或缓存空值 |
| 连接池耗尽 | 优化连接池配置 |

## 参考资源

- [Spring Boot 2.7 文档](https://docs.spring.io/spring-boot/docs/2.7.18/reference/html/)
- [Apache Dubbo 3.2 文档](https://dubbo.apache.org/zh/docsv3.2/)
- [MyBatis-Plus 文档](https://baomidou.com/)
