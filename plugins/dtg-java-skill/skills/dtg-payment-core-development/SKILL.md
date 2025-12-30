---
name: dtg-payment-core-development
description: xxpay-pay 支付核心模块开发技能
version: 3.0.0
tags: ["payment", "payment-gateway", "channel-integration", "callback"]
---

# 支付核心开发技能

xxpay-pay 是 DTG 支付系统的支付处理微服务。

## 模块信息

| 属性 | 值 |
|------|-----|
| 模块名称 | xxpay-pay |
| 模块类型 | 支付核心 |
| HTTP 端口 | 3020 |
| Dubbo 端口 | 23020 |
| 主要职责 | 支付渠道对接、支付订单处理、商户通知 |

## 技术栈

| 技术 | 版本 |
|------|------|
| Java | 11 |
| Spring Boot | 2.7.18 |
| Apache Dubbo | 3.2.14 |
| MyBatis Plus | 3.5.7 |
| OkHttp | 4.12.0 |
| Resilience4j | 1.7.1 |

## 构建和运行

```bash
# 编译依赖模块
./mvnw -f ../xxpay-core clean install -Dmaven.test.skip=true

# 编译当前模块
./mvnw clean package -Dmaven.test.skip=true

# 运行
mvn spring-boot:run
# 或
java -jar target/xxpay-pay-1.0.0.jar --spring.profiles.active=dtg-prod
```

## 代码架构

### 分层结构
```
Controller (ctrl/) → Service (service/) → Channel (channel/)
     ↓                   ↓                    ↓
REST API           业务逻辑          第三方支付通道适配器
```

### 核心接口和抽象类

| 类名 | 用途 |
|------|------|
| `BaseController` | 所有 Controller 的基类 |
| `BasePayNotify` | 支付回调通知的抽象基类 |
| `BasePayment` | 支付下单的抽象基类 |
| `BaseService` | 通道服务的基类 |
| `PaymentInterface` | 支付通道接口定义 |
| `TransNotifyInterface` | 代付通知接口定义 |

### RPC 服务调用
- 默认超时：10 秒
- 重试次数：0
- consumer 超时（30 秒）必须 >= provider 超时（60 秒）

## 支付通道实现模式

```
channel/{channel_name}/
├── {ChannelName}Config.java        # 配置类
├── {ChannelName}DepositChannel.java # 支付通道（继承 BasePayment）
├── {ChannelName}PaymentService.java # 支付服务
├── {ChannelName}TransNotifyService.java # 代付通知服务
├── {ChannelName}SignUtils.java      # 签名工具类
└── model/                           # 请求/响应模型
```

## 支付流程

### 支付下单流程
```
1. 接收支付请求 (PayOrderController)
2. 参数验证
3. 创建支付订单
4. 调用支付通道 (BasePayment)
5. 返回支付信息
```

### 回调通知流程
```
1. 接收第三方回调 (PayNotifyController)
2. 验证回调签名
3. 查询订单状态
4. 更新订单状态
5. 发送商户通知 (ActiveMQ)
6. 返回成功响应
```

## 环境配置

### 环境
- `local` - 本地开发
- `dtg-stg` - 测试环境
- `dtg-prod` - 生产环境

### 关键环境变量

| 变量 | 说明 |
|------|------|
| `ZOOKEEPER` | Dubbo 注册中心地址 |
| `REDIS_HOST` / `REDIS_PASSWORD` | Redis 连接 |
| `ACTIVEMQ_BROKER` / `ACTIVEMQ_USER` / `ACTIVEMQ_PASSWORD` | ActiveMQ 连接 |
| `NODE` | 服务节点标识 |

### Dubbo 配置
```yaml
dubbo:
  application:
    name: xxpay-pay
  protocol:
    port: 23020
    threads: 200
  provider:
    timeout: 5000
  consumer:
    timeout: 30000
```

## OkHttp 连接池配置

- 最大空闲连接：100
- 全局最大并发：500
- 单个三方最大并发：100
- 连接保持时间：45 秒

## 熔断器配置

使用 Resilience4j 防止故障商户拖垮通知系统。

```yaml
resilience4j:
  circuitbreaker:
    instances:
      merchantNotify:
        failure-rate-threshold: 50
        wait-duration-in-open-state: 60s
        sliding-window-size: 10
```

## Git 提交规范

`EZPAY-xxx: 功能描述`

示例：
```
EZPAY-730: 计算功能优化
EZPAY-799: 优化支付通道页面
```
