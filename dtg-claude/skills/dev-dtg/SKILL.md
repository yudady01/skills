---
name: dtg:dev-dtg
description: This skill should be used when the user asks to "DTG-Pay development", "xxpay development", "create payment service", "add payment channel", "integrate Alipay/WeChat Pay", "Dubbo microservice development", "Spring Boot payment system", or mentions DTG-Pay, xxpay modules, payment gateway, payment channel, or multi-module Maven project with Dubbo. Provides specialized development guidance for DTG-Pay/xxpay distributed payment system including Dubbo RPC services, payment channel integration, multi-module Maven project structure, and Spring Boot 2.7 + Dubbo 3.2 best practices.
version: 2.1.0
tags: ["dtg-pay", "payment-system", "dubbo", "spring-boot", "java", "xxpay"]
---

# DTG-Pay 开发指南

DTG-Pay（内部代号 xxpay）是基于 **Spring Boot 2.7.18** + **Apache Dubbo 3.2.14** 的企业级分布式支付系统，支持多支付渠道集成、商户管理和代理结算。

## 技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| Java | 11 | 编程语言 |
| Spring Boot | 2.7.18 | 应用框架 |
| Apache Dubbo | 3.2.14 | RPC 微服务框架 |
| MyBatis-Plus | 3.5.7 | ORM 框架 |
| MySQL | 8.0.33 | 主数据库 |
| Redis | - | 缓存 |
| ActiveMQ | - | 消息队列 |
| MongoDB | - | 文档存储 |

## 项目架构

### 微服务模块

| 模块 | HTTP 端口 | Dubbo 端口 | 职责 |
|------|----------|-----------|------|
| xxpay-core | - | - | 公共模块：实体、DTO、Dubbo 接口定义 |
| xxpay-service | 8190 | 28190 | **核心服务提供者**：数据库操作、业务逻辑 |
| xxpay-pay | 3020 | 23020 | 支付核心：支付渠道集成、回调处理 |
| xxpay-manage | 8193 | 28193 | 运营平台：系统管理界面 |
| xxpay-merchant | 8191 | 28191 | 商户系统：商户管理界面 |
| xxpay-agent | 8192 | 28192 | 代理商系统：代理商管理界面 |
| xxpay-task | 8194 | 28194 | 定时任务：对账、结算（**单节点部署**） |
| xxpay-consumer | 3120 | 23120 | 消息消费者：商户/代付通知处理 |
| xxpay-flyway | - | - | 数据库迁移工具 |

### Dubbo RPC 架构

```
┌─────────────────────────────────────────────────────────────────┐
│                    Zookeeper (服务发现)                          │
└─────────────────────────────────────────────────────────────────┘
                            ▲
                            │ Dubbo RPC
          ┌─────────────────┴───────────────────┐
          │                                     │
    ┌─────┴──────┐                      ┌──────┴────────┐
    │ Provider    │  ◄──────────────────►│ Consumer      │
    │(xxpay-      │  Dubbo Services      │ (xxpay-pay,   │
    │ service)    │                      │  xxpay-*, etc)│
    └─────┬──────┘                      └──────┬────────┘
          │                                     │
    ┌─────┴────────────────────────────────────┴───────┐
    │     MySQL + MongoDB + Redis + ActiveMQ          │
    └─────────────────────────────────────────────────┘
```

## 核心开发规范

### Dubbo 服务定义

所有 Dubbo 服务接口定义在 `xxpay-core/src/main/java/org/xxpay/core/service/`：

```java
// 服务接口（定义在 xxpay-core）
public interface IPayOrderService {
    PayOrderQueryRet query(PayOrderQueryParam param);
}

// 服务实现（在 xxpay-service）
@DubboService(version = "1.0.0")
public class PayOrderServiceImpl implements IPayOrderService {
    // 实现代码
}

// 服务引用（在其他模块）
@DubboReference(version = "1.0.0", timeout = 10000, retries = 0)
private IPayOrderService rpcPayOrderService;
```

### 支付状态常量

| 状态 | 值 | 说明 |
|------|-----|------|
| INIT | 0 | 初始化 |
| PAYING | 1 | 支付中 |
| SUCCESS | 2 | 成功 |
| FAIL | 3 | 失败 |
| REFUND | 4 | 已退款 |

### 返回码规范

| 模块 | 前缀 | 示例 |
|------|------|------|
| 公共 | 10xxx | 10001=参数错误 |
| 业务中心 | 11xxx | 11001=订单不存在 |
| 商户系统 | 12xxx | 12001=商户不存在 |

### RPC 通信基类

```java
// RPC 请求基类
@Data
public class RpcBaseParam implements Serializable {
    private String rpcSrcSysId;      // 调用方系统ID
    private String rpcDateTime;      // 调用时间
    private String rpcSeqNo;         // 通讯流水号
    private Integer rpcSignType;     // 签名方式 (0-明文, 1-SHA1)
    private String rpcSign;          // RPC签名
    private String bizSeqNo;         // 业务流水号
}

// RPC 响应基类
@Data
public class RpcBaseResult extends RpcBaseParam {
    private String rpcRetCode;       // 返回码 (0000=成功)
    private String rpcRetMsg;        // 返回描述
}
```

## 构建与部署

### 编译顺序

使用项目自带的 `mvnw`（Maven Wrapper）而非系统 `mvn`：

```bash
# 1. 编译核心模块（必须最先执行）
./mvnw -f xxpay-core clean install -Dmaven.test.skip=true

# 2. 编译服务提供者
./mvnw -f xxpay-service clean package -Dmaven.test.skip=true

# 3. 编译其他模块（按需）
./mvnw -f xxpay-pay clean package -Dmaven.test.skip=true
./mvnw -f xxpay-task clean package -Dmaven.test.skip=true
```

### 部署顺序

1. 基础架构（Zookeeper、MySQL、Redis、ActiveMQ、MongoDB）
2. xxpay-flyway（数据库迁移）
3. xxpay-service（Dubbo 服务提供者）
4. xxpay-pay（支付核心）
5. xxpay-task（定时任务，**单节点**）
6. xxpay-consumer（消息消费者）
7. Web 门户（xxpay-manage、xxpay-merchant、xxpay-agent）

### 环境配置

项目使用 Spring Profile 区分环境：
- `local` - 本地开发
- `dtg-stg` - 测试环境
- `dtg-prod` - 生产环境

```bash
# 运行时指定环境
java -jar target/xxpay-pay-1.0.0.jar --spring.profiles.active=dtg-prod
```

### 关键环境变量

| 变量 | 说明 |
|------|------|
| ZOOKEEPER | Dubbo 注册中心地址 |
| DATASOURCE_URL / DATASOURCE_USERNAME / DATASOURCE_PASSWORD | 数据库配置 |
| REDIS_HOST / REDIS_PASSWORD | Redis 配置 |
| ACTIVEMQ_BROKER / ACTIVEMQ_USER / ACTIVEMQ_PASSWORD | ActiveMQ 配置 |
| NODE | 服务节点标识 |
| MONGODB_URI | MongoDB 连接字符串 |

## 支付渠道开发

### 渠道目录结构

```
channel/{channel_name}/
├── {ChannelName}Config.java        # 配置类（支付参数、回调地址）
├── {ChannelName}DepositChannel.java # 支付通道（继承 BasePayment）
├── {ChannelName}PaymentService.java # 支付服务
├── {ChannelName}SignUtils.java      # 签名工具
└── model/                           # 请求/响应模型
```

### 支付流程

```
支付下单: Controller → 参数验证 → 创建订单 → 调用支付通道 → 返回支付信息
回调通知: 接收回调 → 验证签名 → 查询订单 → 更新状态 → 发送商户通知 → MQ通知
```

## Git 提交规范

```
EZPAY-xxx: 功能描述

示例：
EZPAY-730: 计算功能优化
EZPAY-799: 优化支付通道页面
```

## 代码生成

```bash
cd xxpay-generator
mvn clean install mybatis-generator:generate
```

**重要**：生成后将 Model 拷贝到 `xxpay-core`，Mapper 拷贝到 `xxpay-service`。

## 参考资源

### 快速参考（references/）

- **`references/quick-reference.md`** - 技术栈、端口、状态码、编译命令速查
- **`references/code-examples.md`** - 实体类、DTO、服务示例代码
- **`references/architecture.md`** - 详细架构指南
- **`references/configuration.md`** - Dubbo、数据库、缓存配置参考

### 详细指南（docs/guides/）

- **`getting-started.md`** - 快速开始指南
- **`project-setup.md`** - 项目初始化
- **`microservice-development.md`** - 微服务开发指南
- **`dubbo-configuration.md`** - Dubbo 高级配置
- **`multi-module-project.md`** - 多模块项目开发
- **`problem-diagnosis.md`** - 问题诊断指南
- **`architecture-analysis.md`** - 架构分析指南
- **`agents.md`** - 代理系统说明
- **`intelligent-features.md`** - 智能功能指南
- **`best-practices.md`** - Spring Boot + Dubbo 最佳实践

### 开发规范（docs/rules/）

- **`coding-standards.md`** - 编码规范
- **`architecture-principles.md`** - 架构原则
- **`project-context.md`** - 项目上下文规则
- **`documentation-criteria.md`** - 文档规范

### 文档模板（docs/templates/）

- **`prd.md`** - 产品需求文档模板
- **`adr.md`** - 架构决策记录模板
- **`design.md`** - 设计文档模板
- **`intelligent-review.md`** - 智能审查报告模板

### 代码示例（examples/）

- **`dubbo-service-example.java`** - Dubbo 服务接口定义示例
- **`dubbo-service-impl-example.java`** - Dubbo 服务实现示例
- **`dubbo-reference-example.java`** - Dubbo 服务引用示例
- **`entity-example.java`** - MyBatis-Plus 实体类示例
- **`channel-example.java`** - 支付通道实现示例
