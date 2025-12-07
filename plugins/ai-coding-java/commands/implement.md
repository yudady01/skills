---
description: 协调从需求到部署的完整 Spring Boot 2.7 企业级应用实现生命周期，智能化管理微服务开发流程
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, TodoWrite, Task]
---

# Spring Boot 2.7 企业级实现命令

这个命令协调完整的 Spring Boot 2.7 企业级应用开发流程，从需求分析到最终部署，确保每个阶段都遵循企业级微服务最佳实践。

## 执行决策流程

### 1. 当前情况评估

**分析用户请求**：`$ARGUMENTS`

根据当前情况选择执行路径：

| 情况模式 | 判断标准 | 执行策略 |
|---------|---------|----------|
| 新微服务需求 | 没有现有服务，新微服务开发 | 启动需求分析代理，确定微服务边界 |
| 继续开发 | 存在 PRD/设计文档，继续工作 | 识别当前阶段并执行下一步 |
| 质量问题 | 检测到错误、测试失败、构建问题 | 执行质量修复流程 |
| 模糊请求 | 意图不明确，需要澄清 | 向用户询问具体需求 |

### 2. 流程管理

**规模确定和任务注册**：
当确定工作规模后，将所有必要步骤注册到 TodoWrite：

```java
// 小规模任务示例
List<String> smallScaleTasks = Arrays.asList(
    "分析当前微服务架构",
    "实现业务逻辑代码",
    "编写单元测试和集成测试",
    "运行质量检查",
    "更新 API 文档"
);

// 中等规模任务示例
List<String> mediumScaleTasks = Arrays.asList(
    "创建技术设计文档",
    "数据库设计变更",
    "API 接口设计",
    smallScaleTasks
);

// 大规模任务示例
List<String> largeScaleTasks = Arrays.asList(
    "创建 PRD 和技术方案",
    "微服务架构设计（需要 ADR）",
    "数据流和服务边界设计",
    mediumScaleTasks
);
```

### 3. 代理协调

**调用专用代理**：
根据任务类型和规模，调用相应的专业化代理：

#### 需求分析阶段
```java
// 启动需求分析代理
Task requirementAnalysis = Task.builder()
    .subagentType("general-purpose")
    .prompt(String.format("""
        分析以下 Spring Boot 2.7 微服务需求并确定开发规模：%s

        请评估：
        - 微服务边界和职责划分
        - 技术复杂度和影响范围
        - 需要的文档类型（PRD/ADR/技术设计）
        - 预估开发时间和资源
        - 数据库设计和API设计需求

        参考文档：@docs/rules/documentation-criteria.md
        """, userRequest))
    .build();
```

#### 架构设计阶段（如果需要）
```java
// 对于中等等规模的功能
if (scale.equals("medium") || scale.equals("large")) {
    Task designPhase = Task.builder()
        .subagentType("general-purpose")
        .prompt(String.format("""
            基于需求分析结果创建 Spring Boot 2.7 微服务技术设计文档

            需求：%s

            请包含：
            - 微服务架构设计
            - 数据库设计和MyBatis-Plus实体
            - RESTful API 设计
            - Spring Security 安全设计
            - 缓存策略设计
            - 服务间通信设计
            - 技术选型说明
            """, requirementAnalysis))
        .build();
}
```

#### 实现阶段
```java
// 任务执行代理
Task implementation = Task.builder()
    .subagentType("general-purpose")
    .prompt(String.format("""
        基于设计文档实现 Spring Boot 2.7 微服务功能：

        设计文档：%s
        工作计划：%s

        请：
        1. 遵循 Spring Boot 2.7 最佳实践 @docs/rules/coding-standards.md
        2. 实现核心业务逻辑
        3. 配置 Spring Security 和JWT认证
        4. 编写相应的单元测试和集成测试
        5. 确保代码质量和安全性
        6. 添加适当的日志记录和监控
        """, designDoc, workPlan))
    .build();
```

### 4. 质量保证流程

**自动化质量检查**：
```java
// Spring Boot 2.7 质量检查清单
List<String> qualityChecks = Arrays.asList(
    "Java 编译和语法检查",
    "单元测试执行",
    "集成测试验证",
    "数据库迁移验证",
    "API 文档更新"
);

// 执行质量检查
for (String check : qualityChecks) {
    QualityCheckResult result = executeQualityCheck(check);
    if (!result.isPassed()) {
        // 启动质量修复代理
        fixQualityIssues(result.getIssues());
    }
}
```

### 5. 微服务特定检查

**Spring Boot 2.7 微服务验证**：
```java
// 微服务特定检查
List<String> microserviceChecks = Arrays.asList(
    "Spring Boot 2.7 应用启动验证",
    "数据库连接池配置",
    "Redis 缓存配置",
    "Spring Security 配置验证",
    "API 跨域配置",
    "日志配置",
    "应用配置文件验证",
    "Docker 镜像构建"
);
```

### 6. 文档更新

**维护企业级项目文档**：
- 更新 README.md
- 更新 OpenAPI/Swagger 文档
- 记录架构决策（ADR）
- 更新数据库变更日志
- 更新部署文档

## 使用指南

### 基础用法

```bash
# 小功能实现
/implement "添加用户管理 REST API，包含 CRUD 操作"

# 复杂功能实现
/implement "实现完整的订单管理微服务，包含支付集成"

# 继续之前的工作
/implement "继续实现用户认证和授权功能"
```

### 高级用法

```bash
# 带有具体需求的微服务功能
/implement "实现用户认证微服务，支持 JWT、OAuth2，集成 Redis 缓存"

# 修复和优化
/implement "重构用户服务，提高数据库查询性能，添加二级缓存"

# 集成新功能
/implement "集成消息队列 RabbitMQ，实现异步订单处理"
```

### 企业级功能示例

```bash
# 微服务拆分
/implement "从单体应用拆分出用户管理微服务，设计数据库分离策略"

# 性能优化
/implement "优化商品查询 API，实现多级缓存，目标响应时间 < 100ms"

# 安全加固
/implement "实现 API 安全网关，集成 Spring Security 和 OAuth2"
```

## 最佳实践

### 1. 微服务设计原则
- 单一职责原则
- 自治性设计
- 无状态服务
- 数据库分离
- 容错设计

### 2. Spring Boot 2.7 最佳实践
- 使用 Spring Boot 2.7 2.7.x
- 遵循 Spring 配置约定
- 合理使用 Spring 注解
- 配置外部化
- 健康检查和监控

### 3. 数据设计标准
- MyBatis-Plus 实体设计
- 数据库索引优化
- 事务边界管理
- 数据库连接池配置
- 飞行式迁移（Flyway）

### 4. 安全标准
- JWT 认证
- RBAC 授权
- API 安全
- 数据加密
- 安全审计日志

### 5. 质量标准
- 80%+ 测试覆盖率
- 完整的 API 文档

### 6. 部署标准
- Docker 容器化
- Kubernetes 配置
- 监控和日志
- 健康检查
- 自动化部署

## 常见场景

### 场景1：新微服务开发
```bash
/implement "创建产品管理微服务，支持产品分类、搜索和库存管理"
```

预期流程：
1. 需求分析（大规模）
2. 微服务边界设计
3. 数据库设计
4. RESTful API 设计
5. Spring Boot 2.7 项目实现
6. 安全配置
7. 缓存配置
8. 测试编写
9. Docker 配置
10. 文档更新

### 场景2：性能优化
```bash
/implement "优化订单查询性能，实现多级缓存，目标 TPS 提升 300%"
```

预期流程：
1. 性能基准测试
2. 瓶颈分析
3. 缓存策略设计
4. 数据库优化
5. 代码重构
6. 性能验证
7. 监控配置
8. 文档更新

### 场景3：安全加固
```bash
/implement "实现企业级安全认证，集成 LDAP，支持 SSO"
```

预期流程：
1. 安全需求分析
2. 安全架构设计
3. Spring Security 配置
4. LDAP 集成
5. JWT 配置
6. 安全测试
7. 审计日志
8. 文档更新

## 企业级开发模式

### 1. 微服务架构模式
- 服务发现（Zookeeper/Nacos）
- 配置中心（Nacos）
- API 网关（Spring Cloud Gateway + Dubbo）
- 熔断器（Dubbo Filter）
- 链路追踪（Dubbo 分布式追踪）

### 2. 数据管理模式
- 数据库分离
- 读写分离
- 分库分表
- 缓存策略
- 消息队列

### 3. 开发协作模式
- 代码审查
- 结对编程
- 技术分享
- 最佳实践制定

## 故障排除

### 常见问题

**问题**：微服务间通信失败
**解决**：检查服务注册、网络配置和负载均衡

**问题**：数据库连接池耗尽
**解决**：优化连接池配置，检查慢查询

**问题**：Spring Security 配置错误
**解决**：检查认证链和权限配置

**问题**：缓存穿透或雪崩
**解决**：实施缓存预热和限流策略

## 相关资源

### 参考文档
- **`@docs/rules/project-context.md`** - 项目上下文和约束
- **`@docs/rules/documentation-criteria.md`** - 文档标准
- **`@docs/rules/coding-standards.md`** - Java 编码规范

### 相关技能
- **`ai-coding-best-practices`** - Spring Boot 2.7 开发最佳实践
- **`springboot-project-setup`** - Spring Boot 2.7 项目配置
- **`quality-assurance`** - 企业级质量保证策略

### 相关命令
- **`/task`** - 单一任务执行
- **`/design`** - 技术设计文档创建
- **`/review`** - 代码审查
- **`/code-quality`** - 质量检查
- **`/microservice`** - 微服务架构设计

## 示例工作流

### 完整微服务开发示例

```bash
# 用户请求
/implement "创建电商订单管理微服务，支持订单创建、支付、状态跟踪"

# 系统自动执行的流程
# 1. 需求分析 → 确定为大规模微服务功能
# 2. 微服务设计 → 服务边界、数据库设计
# 3. 技术设计 → Spring Boot 2.7 架构、API 设计
# 4. 工作计划 → 任务分解和时间估算
# 5. 项目初始化 → Spring Boot 2.7 项目脚手架
# 6. 数据库实现 → MyBatis-Plus 实体、Mapper
# 7. 服务层实现 → 业务逻辑、事务管理
# 8. 控制器实现 → RESTful API
# 9. 安全配置 → Spring Security、JWT
# 10. 缓存配置 → Redis 集成
# 11. 测试实现 → 单元测试、集成测试
# 12. 质量保证 → 代码检查、性能测试
# 13. 部署配置 → Docker、Kubernetes
# 14. 文档完善 → API 文档、部署文档
# 15. 最终提交 → 符合企业级标准的代码提交
```

通过这个命令，您可以享受到从概念到部署的完整 Spring Boot 2.7 企业级微服务开发流程管理，确保每个环节都符合企业级最佳实践标准。