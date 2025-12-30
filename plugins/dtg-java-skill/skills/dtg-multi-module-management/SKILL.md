---
name: dtg-multi-module-management
description: dtg-pay 多模块 Maven 项目管理
version: 3.0.0
tags: ["multi-module", "maven", "project-structure", "module-detection"]
---

# dtg-pay 多模块项目管理

## 项目结构

```
dtg-pay (父项目: org.dtg:dtg-pay:1.0.0)
├── rbgi              # RBGI 银行支付网关 (8195)
├── xxpay-agent       # 代理商系统接口 (8192)
├── xxpay-consumer    # 商户通知消费者 (3120)
├── xxpay-core        # 公共方法、实体 Bean、API 接口定义
├── xxpay-flyway      # 数据库迁移
├── xxpay-manage      # 运营管理平台接口 (8193)
├── xxpay-merchant    # 商户系统接口 (8191)
├── xxpay-task        # 定时任务 (8194)
├── xxpay-pay         # 支付核心 (3020)
└── xxpay-service     # Dubbo 服务生产者 (8190)
```

## 模块信息表

| 模块 | HTTP端口 | Dubbo端口 | 类型 | 对应技能 |
|------|----------|-----------|------|---------|
| rbgi | 8195 | - | 银行网关 | - |
| xxpay-agent | 8192 | 28192 | 代理商系统 | dtg-admin-panel-development |
| xxpay-consumer | 3120 | 23120 | 通知消费者 | - |
| xxpay-core | - | - | 公共模块 | dtg-common-module-development |
| xxpay-flyway | - | - | 数据库迁移 | - |
| xxpay-manage | 8193 | 28193 | 运营平台 | dtg-admin-panel-development |
| xxpay-merchant | 8191 | 28191 | 商户系统 | dtg-admin-panel-development |
| xxpay-task | 8194 | 28194 | 定时任务 | - |
| xxpay-pay | 3020 | 23020 | 支付核心 | dtg-payment-core-development |
| xxpay-service | 8190 | 28190 | Dubbo 服务提供者 | - |

## 模块依赖关系

```
xxpay-pay, xxpay-manage, xxpay-merchant, xxpay-agent, xxpay-task, xxpay-consumer, rbgi
    ↓ 依赖
xxpay-core (公共API、实体、常量)
    ↓ Dubbo RPC 调用
xxpay-service (Dubbo 服务提供者)
    ↓
MySQL + MongoDB + Redis + ActiveMQ
```

## 部署顺序

1. xxpay-flyway - 数据库迁移
2. xxpay-service - 业务服务
3. xxpay-pay - 支付核心
4. xxpay-task - 定时任务
5. xxpay-manage - 运营平台
6. xxpay-agent - 代理商系统
7. xxpay-merchant - 商户系统

## 编译命令

```bash
# 首先编译核心模块
./mvnw -f xxpay-core clean install -Dmaven.test.skip=true

# 编译服务层
./mvnw -f xxpay-service clean package -Dmaven.test.skip=true

# 编译其他模块
./mvnw -f xxpay-pay clean package -Dmaven.test.skip=true
./mvnw -f xxpay-task clean package -Dmaven.test.skip=true
./mvnw -f xxpay-manage clean package -Dmaven.test.skip=true
./mvnw -f xxpay-agent clean package -Dmaven.test.skip=true
./mvnw -f xxpay-merchant clean package -Dmaven.test.skip=true
./mvnw -f xxpay-consumer clean package -Dmaven.test.skip=true
./mvnw -f rbgi clean package -Dmaven.test.skip=true
```

## 环境配置

### 环境
- `local` - 本地开发
- `dtg-stg` - 测试环境
- `dtg-prod` - 生产环境

### 关键环境变量

| 变量 | 说明 |
|------|------|
| `ZOOKEEPER` | Zookeeper 注册中心地址 |
| `DATASOURCE_URL` | MySQL 数据库地址 |
| `REDIS_HOST` | Redis 主机地址 |
| `ACTIVEMQ_BROKER` | ActiveMQ 消息代理地址 |
| `MONGODB_URI` | MongoDB 连接 URI |
| `NODE` | 服务节点标识 |

## 核心架构概念

### 1. Dubbo RPC 通信模型
- `RpcBaseParam` - RPC 调用入参基类
- `RpcBaseResult` - RPC 返回值基类

### 2. 服务接口定义
- Dubbo 服务接口定义在 `xxpay-core/src/main/java/org/xxpay/core/service/`
- 以 `I` 开头命名
- 服务实现在 `xxpay-service`

### 3. 支付通道架构
- 策略模式，位于 `xxpay-pay/src/main/java/org/xxpay/pay/channel/`
- 继承 `BasePayment` 实现支付下单
- 继承 `BasePayNotify` 实现回调通知

### 4. 消息队列
ActiveMQ 用于异步处理：
- `Mq4PayOrderListener` - 支付订单消息
- `Mq4MchNotify` - 商户通知
- `Mq4MchAgentpayNotify` - 代付通知

## 时区设置

项目统一使用 **Asia/Shanghai** 时区：
- **应用层**: `TimeZone.setDefault()`
- **Jackson**: `spring.jackson.time-zone: Asia/Shanghai`
- **数据库**: `serverTimezone=GMT%2B0`

## Git 提交规范

`EZPAY-xxx: 功能描述`

示例：
```
EZPAY-730: 计算功能优化
EZPAY-799: 优化支付通道页面
```
