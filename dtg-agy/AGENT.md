# AGENT.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

`dtg-pay`（内部称为 `xxpay4dubbo`）是一个基于 **Spring Boot** 和 **Apache Dubbo** 构建的分布式支付系统，支持多种支付渠道、商户管理和代理商系统。

## 快速开始命令

### 基础架构（使用 Docker Compose）

```bash
cd doc/docker-compose
docker-compose up -d
```

启动的服务：Zookeeper:2181, ActiveMQ:8161/61616, MySQL:3306, Redis:6379, MongoDB:27017

### 构建命令

使用 `mvnw`（Maven wrapper）而非系统的 `mvn`：

```bash
# 1. 先构建核心模块（必须最先执行）
./mvnw -f xxpay-core clean install -Dmaven.test.skip=true

# 2. 构建服务层
./mvnw -f xxpay-service clean package -Dmaven.test.skip=true

# 3. 构建其他模块
./mvnw -f xxpay-pay clean package -Dmaven.test.skip=true
./mvnw -f xxpay-task clean package -Dmaven.test.skip=true
./mvnw -f xxpay-manage clean package -Dmaven.test.skip=true
./mvnw -f xxpay-merchant clean package -Dmaven.test.skip=true
./mvnw -f xxpay-agent clean compile -Dmaven.test.skip=true
./mvnw -f xxpay-consumer clean package -Dmaven.test.skip=true
./mvnw -f rbgi clean package -Dmaven.test.skip=true
```

### 启动顺序

1. 基础架构（Zookeeper、MySQL、Redis、ActiveMQ、MongoDB）
2. xxpay-flyway（数据库迁移）
3. xxpay-service（Dubbo 服务提供者）
4. xxpay-pay（支付核心）
5. xxpay-task（定时任务，需单节点部署）
6. xxpay-consumer（ActiveMQ 消费者）
7. rbgi（支付网关服务）
8. Web 门户（xxpay-manage、xxpay-merchant、xxpay-agent）

### 代码生成

```bash
cd xxpay-generator
mvn clean install mybatis-generator:generate
```

**重要**：生成后将 Model 拷贝到 `xxpay-core`，Mapper 拷贝到 `xxpay-service`。覆盖 Mapper 时请务必对比差异。

## 架构概览

### 微服务架构（Dubbo RPC）

项目采用典型的 RPC 微服务架构，**xxpay-service** 是核心服务提供者，所有数据库操作和共享业务逻辑都在这里实现并通过 Dubbo 暴露接口。

```
┌─────────────────────────────────────────────────────────────────┐
│                         Zookeeper (服务发现)                     │
└─────────────────────────────────────────────────────────────────┘
                            ▲
                            │
          ┌─────────────────┴───────────────────┐
          │                                     │
    ┌─────┴──────┐                      ┌──────┴────────┐
    │ Dubbo      │                      │ Dubbo         │
    │ Provider   │                      │ Consumer      │
    │(xxpay-     │  ◄──────────────────►│ (xxpay-pay,   │
    │ service)   │                      │  xxpay-task,  │
    └─────┬──────┘                      │  xxpay-*)     │
          │                             └──────┬────────┘
          │                                    │
    ┌─────┴────────────────────────────────────┴───────┐
    │           数据库层                              │
    │  MySQL + MongoDB + Redis + ActiveMQ             │
    └─────────────────────────────────────────────────┘
```

### 模块职责

| 模块 | 端口 | 职责 |
|:---|:---|:---|
| **xxpay-core** | - | 共享库：实体类、DTO、通用工具、**Dubbo 服务接口定义** |
| **xxpay-service** | 8190 | **核心业务逻辑层**：所有数据库操作、Dubbo 服务实现 |
| **xxpay-pay** | 3020 | 支付核心：处理与三方支付渠道的集成、回调 |
| **xxpay-task** | 8194 | 定时任务：对账、结算、补单（**需单节点部署**） |
| **xxpay-consumer** | - | ActiveMQ 消费者：处理商户通知、代付通知 |
| **rbgi** | - | 支付网关服务：对外 API、与 Coins/RBGI 集成 |
| **xxpay-manage** | 8193 | 运营管理平台：系统管理员界面 |
| **xxpay-merchant** | 8191 | 商户系统：商户界面 |
| **xxpay-agent** | 8192 | 代理商系统：代理商界面 |
| **xxpay-flyway** | - | 数据库迁移工具 |
| **xxpay-generator** | - | MyBatis 代码生成器 |

### Dubbo 服务接口

所有 Dubbo 服务接口定义在 `xxpay-core/src/main/java/org/xxpay/core/service/`，接口命名规范为 `I{ServiceName}Service`。

服务实现在 `xxpay-service` 中，使用 `@DubboService` 注解暴露。

消费者通过 `@DubboReference` 注入服务，参考 `RpcCommonService.java` 中的用法：

```java
@DubboReference(version = "1.0.0", timeout = 10000, retries = 0)
public IPayOrderService rpcPayOrderService;
```

### 支付渠道集成

支付渠道代码位于 `xxpay-pay/src/main/java/org/xxpay/pay/channel/`，每个渠道有独立的包。

核心接口：
- `BasePayNotify`：支付通知基类
- `BaseCashColl`：代付（提现）基类
- `PayNotifyInterface`：支付通知接口
- `CashCollInterface`：代付接口

### ActiveMQ 消息处理

- **生产者**：在 `xxpay-service` 和 `xxpay-pay` 中发送 MQ 消息
- **消费者**：在 `xxpay-consumer` 中处理消息，包括：
    - `Mq4MchPayNotify`：支付通知
    - `Mq4MchAgentpayNotify`：代付通知
    - `Mq4MchNotify`：商户通用通知

### 定时任务

定时任务位于 `xxpay-task/src/main/java/org/xxpay/task/`，包括：
- 对账任务
- 结算任务
- 补单任务（订单状态补偿）
- 通知重试任务
- MongoDB 同步任务

**重要**：xxpay-task 必须单节点部署，避免重复执行。

### 数据库迁移

Flyway 迁移脚本位于 `xxpay-flyway/src/main/resources/db/`：
- `migration/`：当前使用的迁移脚本
- `migration/back/`：已归档的迁移脚本
- `env/{local,dev,prod}/`：环境特定脚本

脚本命名规范：`V{version}__{description}.sql`

### 环境配置

项目使用 Spring Profile 区分环境：
- `local`：本地开发
- `dtg-stg`：测试环境
- `dtg-prod`：生产环境

配置文件位于各模块的 `application.yml`，使用环境变量覆盖配置：
- `ZOOKEEPER`：Zookeeper 地址
- `DATASOURCE_URL`、`DATASOURCE_USERNAME`、`DATASOURCE_PASSWORD`：数据库配置
- `REDIS_HOST`、`REDIS_PASSWORD`：Redis 配置
- `ACTIVEMQ_BROKER`、`ACTIVEMQ_USER`、`ACTIVEMQ_PASSWORD`：ActiveMQ 配置
- `MONGODB_URI`、`MONGODB_AUTHENTICATION_DATABASE`：MongoDB 配置

### 时区设置

系统强制使用 `Asia/Shanghai` 时区，在 Java、数据库和 Docker 容器中统一配置。

### MyBatis Plus 配置

- 使用 MyBatis Plus 3.x
- Mapper XML 位于 `classpath*:/mapper/*.xml`
- 一级缓存已关闭（`localCacheScope: STATEMENT`）以适应微服务架构
- 二级缓存已禁用

### rbgi 模块

`rbgi` 是支付网关服务，提供：
- 开放 API（`/api/` 路径）
- Coins/RBGI 渠道集成
- JWT 认证和 API Key 认证
- 域名健康监控和负载均衡

## 开发注意事项

### 修改代码时

1. **新增/修改数据库表**：在 `xxpay-flyway` 中创建 Flyway 迁移脚本
2. **新增实体类**：使用 `xxpay-generator` 生成，手动拷贝到 `xxpay-core` 和 `xxpay-service`
3. **新增业务逻辑**：
    - 在 `xxpay-core` 定义 Dubbo 服务接口
    - 在 `xxpay-service` 实现服务
    - 在消费者模块注入 `@DubboReference`
4. **新增支付渠道**：在 `xxpay-pay/channel/` 下创建新包，继承基类实现接口

### 性能调优相关

项目针对 AWS m7i 系列实例进行了优化：
- xxpay-service 运行在 m7i.xlarge（4 vCPU, 16GB RAM）
- xxpay-pay 运行在 m7i.2xlarge（8 vCPU, 32GB RAM）
- Dubbo 线程池、HikariCP 连接池、Redis 连接池已根据硬件配置调优

### 代码规范

- 日志使用 logback，配置在各模块的 `logback-spring.xml`
- 使用 Lombok 简化代码
- 异常处理使用统一的全局异常处理器
- 敏感信息通过环境变量注入，不要硬编码
