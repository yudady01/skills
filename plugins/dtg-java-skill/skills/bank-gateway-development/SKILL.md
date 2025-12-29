---
name: bank-gateway-development
description: RBGI 银行网关开发技能。提供银行 API 集成、存款/取款处理和证书管理的完整指导。
version: 1.0.0
tags: ["bank-gateway", "rbgi", "cash-in", "cash-out", "bank-integration"]
---

# RBGI 银行网关开发技能

RBGI 是基于 Spring Boot 的支付网关服务，与 RBGI 银行系统集成，提供存款（Cash In）和取款（Cash Out）功能。

## 模块信息

| 属性 | 值 |
|------|-----|
| 模块名称 | rbgi |
| 模块类型 | 银行支付网关 |
| HTTP 端口 | 8195 |
| 主要职责 | 与 RBGI 银行系统对接、存款/取款处理 |

## 核心技术栈

| 技术 | 版本 |
|------|------|
| Spring Boot | 2.x |
| Spring Security + JWT | 最新 |
| MyBatis Plus | 3.5.7 |
| MySQL + Flyway | 最新 |
| Redis | 最新 |
| ActiveMQ | 最新 |
| OkHttp | 4.12.0 |
| SpringDoc OpenAPI | 3.0 |

## 构建与测试

```bash
# 构建（跳过测试）
mvn clean install -DskipTests

# 构建（包含测试）
mvn clean install

# 运行所有测试
mvn test

# 运行单个测试类
mvn test -Dtest=AppTest

# 使用 Maven 运行
./mvnw spring-boot:run

# 或直接运行 JAR
java -jar target/rbgi-1.0.0.jar
```

## 应用配置

### 基本配置
- 默认端口: 8195
- 应用入口: `org.xxpay.RbgiApplication`
- 主配置文件: `src/main/resources/application.yml`

### 环境配置
通过 `spring.profiles.active` 切换环境：
- `local` - 本地开发环境（Swagger 启用）
- `dtg-stg` - 测试环境（Swagger 启用）
- `dtg-prod` - 生产环境（Swagger 禁用）

### 环境变量
```bash
# 数据库配置
DATASOURCE_URL=jdbc:mysql://localhost:3306/rbgi
DATASOURCE_USERNAME=root
DATASOURCE_PASSWORD=password

# Redis 配置
REDIS_HOST=localhost
REDIS_PASSWORD=your_redis_password

# ActiveMQ 配置
ACTIVEMQ_BROKER=tcp://localhost:61616
ACTIVEMQ_USER=admin
ACTIVEMQ_PASSWORD=admin
```

## 代码架构

### 分层结构
```
controller/    # 控制器层（按功能分组：generate/pay/rbgi）
service/       # 业务逻辑层
dao/          # 数据访问层（MyBatis Mapper 接口）
entity/       # 数据库实体类
```

### 支付通道架构
支付通道采用策略模式设计，位于 `channel/` 目录：
- `channel/auth/` - 认证通道（IAuth 接口，RbgiIAuth 实现）
- `channel/in/` - 入账通道（CashIn 接口，In1001/In1002 实现）
- `channel/out/` - 出账通道（CashOut 接口，Out1003 实现）

### 通道实现模式
每个通道实现类都定义了四个核心方法：
1. `generateXxxRequest()` - 组装请求参数
2. `doXxxApi()` - 执行 API 调用
3. `handleXxxResponse()` - 处理 API 响应
4. `handleXxxNotify()` - 处理回调通知

详细代码见 `references/code-examples.md`

## API 文档

### Swagger 配置
- Swagger UI: http://localhost:8195/docs/index.html
- OpenAPI JSON: http://localhost:8195/docs/api
- 分组: generate（/api/generate/**）、pay（/api/pay/**）、rbgi（/ips-payments/**）

## 数据库迁移

### Flyway 配置
- 使用 Flyway 管理
- 迁移脚本: `src/main/resources/db/migration/`
- 配置了 `baseline-on-migrate: true` 支持已有数据库

### 迁移脚本命名
```
V{版本号}__{描述}.sql

示例:
V0.3.161__add_performance_indexes.sql
V0.0.40__add_currency_In_config.sql
```

### 最佳实践
```sql
-- 检查索引是否存在后再创建
SET @idx_name := 'idx_name';
SET @tbl_name := 'table_name';
SELECT COUNT(1) INTO @exists
FROM information_schema.STATISTICS
WHERE table_schema = DATABASE()
  AND table_name = @tbl_name
  AND index_name = @idx_name;
SET @sql := IF(@exists = 0,
  'CREATE INDEX idx_name ON table_name (...);',
  'SELECT ''Index already exists'';');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;
```

## 关键配置说明

### MyBatis Plus 配置
```yaml
mybatis-plus:
  configuration:
    # 关闭一级缓存以适应微服务架构
    localCacheScope: STATEMENT
    map-underscore-to-camel-case: true
    cache-enabled: false
    log-impl: org.apache.ibatis.logging.slf4j.Slf4jImpl
```

### HikariCP 配置
```yaml
spring:
  datasource:
    hikari:
      maximum-pool-size: 80
      minimum-idle: 20
      connection-timeout: 30000
      idle-timeout: 600000
      max-lifetime: 1800000
```

### 性能参数

| 参数 | 值 | 说明 |
|------|---|------|
| 最大空闲连接 | 80 | 连接池大小 |
| 最小空闲连接 | 20 | 保持活跃的连接数 |
| 单个 API 最大并发 | 50 | 银行限流考虑 |
| 连接保持时间 | 5 分钟 | 复用连接 |

## Actuator 配置

所有端点暴露在 `/actuator` 路径下：
- `/actuator/health` - 健康检查
- `/actuator/info` - 应用信息
- `/actuator/metrics` - 性能指标

## 开发指南

### 添加新的支付通道
1. 在 `channel/` 下创建新目录
2. 实现对应接口（IAuth、CashIn、CashOut）
3. 实现 4 个核心方法
4. 在 `application.yml` 添加通道配置

### 添加数据库迁移
1. 在 `src/main/resources/db/migration/` 创建 SQL 文件
2. 遵循 Flyway 命名规范
3. 使用幂等的 SQL 语句

### 添加 API 接口
1. 创建 Controller 类
2. 添加 `@Tag` 注解用于 Swagger 分组
3. 实现 API 方法
4. 在 `application.yml` 配置分组

## 常见问题

### 本地开发配置
- 本地开发需设置 `spring.profiles.active=local` 启用 SQL 日志和 Swagger

### JWT Token 配置
- JWT token 相关配置在 `springboot/security/` 目录

### ActiveMQ 消息监听器
- ActiveMQ 消息监听器在 `mq/` 目录

### 定时任务
- 定时任务在 `task/` 目录

## 依赖关系

rbgi 是 dtg-pay 多模块项目的一部分，父项目为 `org.dtg:dtg-pay:1.0.0`。
