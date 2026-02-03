# DTG-Pay 配置参考

## Dubbo 配置

```yaml
dubbo:
  application:
    name: xxpay-pay
    parameters:
      qos-enable: false
  scan:
    base-packages: org.xxpay
  protocol:
    name: dubbo
    port: 23020
    threads: 200
  registry:
    address: zookeeper://127.0.0.1:2181
  provider:
    timeout: 5000
    retries: 0
  consumer:
    timeout: 30000
    retries: 0
```

## Spring Boot 基础配置

```yaml
spring:
  application:
    name: xxpay-pay
  profiles:
    active: dtg-prod
  jackson:
    time-zone: Asia/Shanghai
    date-format: yyyy-MM-dd HH:mm:ss

server:
  port: 3020
  servlet:
    context-path: /
```

## MyBatis-Plus 配置

```yaml
mybatis-plus:
  mapper-locations: classpath*:mapper/**/*.xml
  type-aliases-package: org.xxpay.*.entity
  configuration:
    map-underscore-to-camel-case: true
    cache-enabled: false
  global-config:
    db-config:
      id-type: input
      logic-delete-field: deleted
      logic-delete-value: 1
      logic-not-delete-value: 0
```

## OkHttp 连接池配置

- 最大空闲连接：100
- 全局最大并发：500
- 单个三方最大并发：100
- 连接保持时间：45 秒

## 熔断器配置

```yaml
resilience4j:
  circuitbreaker:
    instances:
      merchantNotify:
        failure-rate-threshold: 50
        wait-duration-in-open-state: 60s
        sliding-window-size: 10
```

## 环境配置

### 环境列表

| 环境 | 说明 |
|------|------|
| local | 本地开发 |
| dtg-stg | 测试环境 |
| dtg-prod | 生产环境 |

### 关键环境变量

| 变量 | 说明 |
|------|------|
| ZOOKEEPER | Dubbo 注册中心地址 |
| DATASOURCE_URL | MySQL 数据库地址 |
| REDIS_HOST | Redis 主机地址 |
| REDIS_PASSWORD | Redis 密码 |
| ACTIVEMQ_BROKER | ActiveMQ 消息代理地址 |
| ACTIVEMQ_USER | ActiveMQ 用户名 |
| ACTIVEMQ_PASSWORD | ActiveMQ 密码 |
| MONGODB_URI | MongoDB 连接 URI |
| NODE | 服务节点标识 |

## 时区配置

项目统一使用 **Asia/Shanghai** 时区：

```yaml
# Spring Jackson
spring:
  jackson:
    time-zone: "Asia/Shanghai"
```

```yaml
# JDBC URL
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/xxpay?serverTimezone=GMT%2B0
```

```java
// Java 代码
@PostConstruct
public void setTimeZone() {
    TimeZone.setDefault(TimeZone.getTimeZone("Asia/Shanghai"));
}
```
