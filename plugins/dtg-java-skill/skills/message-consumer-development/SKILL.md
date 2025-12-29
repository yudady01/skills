---
name: message-consumer-development
description: xxpay-consumer 消息消费者模块开发技能。提供 ActiveMQ 消息消费、商户通知和重试机制的完整指导。
version: 1.0.0
tags: ["message-consumer", "activemq", "notification", "retry"]
---

# 消息消费者开发技能

xxpay-consumer 是 DTG-PAY 支付系统的消费者模块，负责处理商户通知（支付通知和代付通知）。

## 模块信息

| 属性 | 值 |
|------|-----|
| 模块名称 | xxpay-consumer |
| 模块类型 | 消息消费者 |
| HTTP 端口 | 3120 |
| Dubbo 端口 | 23120 |
| 主要职责 | 商户通知处理、ActiveMQ 消息消费 |

## 核心技术栈

| 技术 | 版本 |
|------|------|
| Spring Boot | 2.7.18 |
| Apache Dubbo | 3.2.14 |
| ActiveMQ | 最新 |
| OkHttp | 最新 |

## 构建和运行

```bash
# 编译核心模块（依赖）
./mvnw -f ../xxpay-core clean install -Dmaven.test.skip=true

# 编译当前模块
./mvnw clean package -Dmaven.test.skip=true

# 使用 Maven 运行
./mvnw spring-boot:run

# 或直接运行 JAR
java -jar target/xxpay-consumer-1.0.0.jar
```

## 环境配置

项目通过 `spring.profiles.active` 切换环境：
- `local` - 本地开发环境
- `dtg-stg` - 测试环境
- `dtg-prod` - 生产环境

## 架构设计

### Dubbo RPC 消费者

本模块是 Dubbo 服务的消费者，通过 `RpcCommonService` 调用远程服务：
- `IPayOrderService` - 支付订单服务
- `IMchNotifyService` - 商户通知服务
- `IMchInfoService` - 商户信息服务

### ActiveMQ 消息消费

本模块监听 ActiveMQ 队列，处理商户通知：
- `Mq4MchPayNotify` - 处理支付通知队列 (`queue.consumer.notify.mch.pay`)
- `Mq4MchAgentpayNotify` - 处理代付通知队列 (`queue.consumer.notify.mch.agentpay`)

### 消息处理流程

```
1. 接收 MQ 消息（JSON 格式）
2. 解析商户信息（通过 Dubbo RPC）
3. 使用 HTTP POST 发送通知到商户回调 URL
4. 根据响应判断是否成功：
   - 返回 "success" - 标记通知成功
   - 其他响应 - 延迟重试（最多 5 次，每次间隔递增：1分钟、2分钟...）
```

## 代码结构

```
src/main/java/org/xxpay/consumer/
├── XxpayConsumerApplication.java    # Spring Boot 启动类
├── Implementation/
│   ├── Mq4MchNotify.java            # 商户通知基类
│   ├── Mq4MchPayNotify.java         # 支付通知处理
│   └── Mq4MchAgentpayNotify.java    # 代付通知处理
├── service/
│   └── RpcCommonService.java        # Dubbo 服务引用
└── springboot/
    ├── activemq/ActiveMqConf.java   # ActiveMQ 配置
    ├── jackson/JacksonConfig.java   # JSON 序列化配置
    └── okhttp/OkHttpConfiguration.java # HTTP 客户端配置
```

详细代码见 `references/code-examples.md`

## ActiveMQ 配置

### 连接池配置参数

| 参数 | 值 | 说明 |
|------|---|------|
| 最大连接数 | 30 | 连接池最大连接数 |
| 消费者并发 | 10-30 | 最小10个，最大30个消费者 |
| 每批消息数 | 20 | 每次处理的消息数量 |
| 异步发送 | 启用 | 提高性能 |
| 消息压缩 | 启用 | 减少网络传输 |

## 重试机制

### 重试策略

| 重试次数 | 延迟时间 |
|---------|---------|
| 第1次 | 1 分钟 |
| 第2次 | 2 分钟 |
| 第3次 | 4 分钟 |
| 第4次 | 8 分钟 |
| 第5次 | 16 分钟 |

详细代码见 `references/code-examples.md`

## 代理 HTTP 请求

商户通知支持通过代理服务器发送（针对不同平台）：

### 代理配置

```yaml
http:
  proxy:
    platforms:
      ezpay:
        host: proxy.ezpay.com
        port: 8080
        username: ezpay_user
        password: ezpay_pass
      724pay:
        host: proxy.724pay.com
        port: 8080
```

## 时区设置

全局时区：`Asia/Shanghai`

## 依赖关系

- `xxpay-core` - 公共模块（实体类、工具类、常量）
- Dubbo 3.2.14 - RPC 框架
- Spring Boot 2.7.18 - 应用框架
- ActiveMQ - 消息队列
- OkHttp - HTTP 客户端

## 相关模块

- `xxpay-core` - 公共模块和实体类
- `xxpay-service` - Dubbo 服务提供者
- `xxpay-pay` - 支付核心系统
- `xxpay-manage` - 运营管理平台 (端口 8193)
- `xxpay-merchant` - 商户系统 (端口 8191)
- `xxpay-agent` - 代理商系统 (端口 8192)
- `xxpay-task` - 定时任务 (端口 8194)
- `xxpay-flyway` - 数据库迁移
