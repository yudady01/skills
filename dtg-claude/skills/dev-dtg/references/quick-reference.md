# DTG-Pay 快速参考

## 技术栈

| 技术 | 版本 |
|------|------|
| Java | 11 |
| Spring Boot | 2.7.18 |
| Apache Dubbo | 3.2.14 |
| MyBatis-Plus | 3.5.7 |

## 模块端口

| 模块 | HTTP | Dubbo |
|------|------|-------|
| xxpay-service | 8190 | 28190 |
| xxpay-pay | 3020 | 23020 |
| xxpay-manage | 8193 | 28193 |
| xxpay-merchant | 8191 | 28191 |
| xxpay-agent | 8192 | 28192 |
| xxpay-task | 8194 | 28194 |
| xxpay-consumer | 3120 | 23120 |

## 支付状态

| 状态 | 值 |
|------|-----|
| INIT | 0 |
| PAYING | 1 |
| SUCCESS | 2 |
| FAIL | 3 |
| REFUND | 4 |

## 商户状态

| 状态 | 值 |
|------|-----|
| INIT | 0 |
| ACTIVE | 1 |
| STOP | 2 |

## 返回码规范

| 模块 | 前缀 |
|------|------|
| 公共 | 10xxx |
| 业务中心 | 11xxx |
| 商户系统 | 12xxx |

## 编译命令

```bash
# 编译核心模块
./mvnw -f xxpay-core clean install -Dmaven.test.skip=true

# 编译服务层
./mvnw -f xxpay-service clean package -Dmaven.test.skip=true

# 编译支付核心
./mvnw -f xxpay-pay clean package -Dmaven.test.skip=true
```

## 运行模块

```bash
# Maven 运行
mvn spring-boot:run

# JAR 运行
java -jar target/xxpay-pay-1.0.0.jar --spring.profiles.active=dtg-prod
```

## 部署顺序

1. xxpay-flyway
2. xxpay-core
3. xxpay-service
4. 其他业务模块

## Git 提交规范

```
EZPAY-xxx: 功能描述

示例：
EZPAY-730: 计算功能优化
EZPAY-799: 优化支付通道页面
```

## 常用支付渠道

| 渠道 | 常量 |
|------|------|
| 支付宝 | alipay |
| 微信支付 | wxpay |
| 银联 | unionpay |

## 环境变量

| 变量 | 说明 |
|------|------|
| ZOOKEEPER | Dubbo 注册中心 |
| REDIS_HOST | Redis 主机 |
| ACTIVEMQ_BROKER | ActiveMQ 地址 |
| NODE | 节点标识 |
