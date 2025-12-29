---
name: dubbo-provider-development
description: This skill should be used when developing xxpay-service module (Dubbo service provider) in dtg-pay project. It provides comprehensive guidance for creating Dubbo services, database operations, and business logic implementation.
version: 1.0.0
tags: ["dubbo", "service-provider", "mybatis-plus", "mysql", "mongodb"]
---

# Dubbo 服务提供者开发技能

xxpay-service 是 dtg-pay 支付系统的核心服务层，作为 Dubbo 服务提供者，封装了所有数据库操作和公共业务逻辑。

## 模块信息

- **模块名称**: xxpay-service
- **模块类型**: Dubbo 服务提供者
- **HTTP 端口**: 8190
- **Dubbo 端口**: 28190
- **主要职责**: 数据库操作、业务逻辑封装、Dubbo 服务暴露

## 核心技术栈

- **Spring Boot 2.x** - 应用框架
- **Dubbo 3.2.14** - 分布式服务框架（RPC），使用 Zookeeper 做服务注册发现
- **MyBatis Plus 3.5.7** - ORM 框架
- **MySQL** - 主数据库，使用 HikariCP 连接池
- **MongoDB** - 文档存储
- **Redis** - 缓存
- **ActiveMQ** - 消息队列

## 构建和运行

### 编译

```bash
# 从项目根目录编译（需先编译 xxpay-core）
./mvnw -f xxpay-core clean install -Dmaven.test.skip=true
./mvnw -f xxpay-service clean package -Dmaven.test.skip=true
```

### 运行

```bash
# 开发环境
mvn spring-boot:run

# 或直接运行 jar
java -jar target/xxpay-service-1.0.0.jar
```

### 测试

```bash
# 运行所有测试
mvn test

# 运行单个 Mapper 测试
mvn test -Dtest=AgentAccountMapperTest

# 运行单个 Service 测试
mvn test -Dtest=AgentAccountServiceImplV2Test
```

## 项目结构

```
src/main/java/org/xxpay/service/
├── XxPayServiceApplication.java  # 启动类
├── controller/                   # REST API 控制器（极少使用，主要是 Dubbo 服务）
├── impl/                        # 服务实现类（主要业务逻辑）
├── dao/mapper/                  # MyBatis Mapper 接口
├── common/                      # 公共工具类和枚举
├── task/                        # 定时任务
├── mq/                          # ActiveMQ 消息监听器和发送器
├── mongo/                       # MongoDB 相关
│   ├── document/               # 文档实体
│   ├── repository/             # MongoDB Repository
│   └── service/                # MongoDB 服务层
└── springboot/                  # Spring Boot 配置
    ├── activemq/               # ActiveMQ 配置
    ├── redis/                  # Redis 配置
    ├── mongo/                  # MongoDB 配置
    ├── jackson/                # JSON 序列化配置
    └── bean/                   # Bean 配置
```

## 服务接口定义

服务接口定义在 `xxpay-core/src/main/java/org/xxpay/core/service/`，以 `I` 开头命名（如 `IAgentAccountService`）。

所有服务实现类在 `impl/` 包下，实现对应的接口并用 `@Service` 注解暴露为 Dubbo 服务。

### Dubbo 服务实现示例

```java
// src/main/java/org/xxpay/service/impl/AgentAccountServiceImplV2.java
@Service
@DubboService(version = "1.0.0", group = "dtg-pay", timeout = 10000, retries = 0)
@Slf4j
public class AgentAccountServiceImplV2 implements IAgentAccountService {

    @Autowired
    private AgentAccountMapper agentAccountMapper;

    @Autowired
    private RpcUtil rpcUtil;

    @Override
    public AgentAccount getAgentAccount(String agentId) {
        // 业务逻辑实现
        return agentAccountMapper.selectByAgentId(agentId);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public int updateAgentBalance(String agentId, Long amount) {
        // 事务操作
        return agentAccountMapper.updateBalance(agentId, amount);
    }
}
```

## MyBatis Mapper

Mapper 接口在 `dao/mapper/` 包下，XML 映射文件在 `src/main/resources/mapper/`。

### Mapper 示例

```java
// src/main/java/org/xxpay/service/dao/mapper/AgentAccountMapper.java
@Mapper
public interface AgentAccountMapper extends BaseMapper<AgentAccount> {

    @Select("SELECT * FROM agent_account WHERE agent_id = #{agentId}")
    AgentAccount selectByAgentId(String agentId);

    @Update("UPDATE agent_account SET balance = balance + #{amount} WHERE agent_id = #{agentId}")
    int updateBalance(@Param("agentId") String agentId, @Param("amount") Long amount);
}
```

## Dubbo 配置

### Provider 配置

```yaml
dubbo:
  application:
    name: xxpay-service
    version: 1.0.0
  registry:
    address: zookeeper://${ZOOKEEPER:localhost:2181}
  protocol:
    name: dubbo
    port: 28190
    threads: 200
    heartbeat: 60000
  provider:
    timeout: 60000
    retries: 0
    delay: 0
    version: 1.0.0
    group: dtg-pay
```

### 性能配置

| 环境 | Provider 线程数 | Consumer 线程数 | 超时时间 |
|------|---------------|----------------|---------|
| local/dev | 100 | 50 | 60 秒 |
| dtg-stg | 200 | 100 | 60 秒 |
| dtg-prod | 200 | 100 | 60 秒 |

## 数据库连接池配置

### HikariCP 配置

| 环境 | minimum-idle | maximum-pool-size |
|------|-------------|-------------------|
| local/dev | 30 | 150 |
| dtg-stg | 50 | 200 |
| dtg-prod | 50 | 150 |

生产环境 maximum-pool-size 150 是根据 Dubbo threads (200) × 0.7 ≈ 140 计算，考虑事务时间较长设为 150。

### 配置示例

```yaml
spring:
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://${DB_HOST:localhost}:${DB_PORT:3306}/${DB_NAME:xxpay}?useSSL=false&serverTimezone=GMT%2B0
    username: ${DB_USERNAME:root}
    password: ${DB_PASSWORD:password}
    hikari:
      maximum-pool-size: 150
      minimum-idle: 50
      connection-timeout: 30000
      idle-timeout: 600000
      max-lifetime: 1800000
```

## 业务领域

### 核心实体

- **Mch** (Merchant) - 商户
- **Agent** - 代理商
- **PayOrder** - 支付订单
- **TransOrder** - 转账订单
- **Agentpay** - 代付
- **PayPassage** - 支付通道
- **Sett** (Settlement) - 结算
- **Account** - 账户

### 服务命名规范

- 商户相关: `MchXxxService`
- 代理商相关: `AgentXxxService`
- 支付相关: `PayXxxService`
- 通道相关: `PayPassageXxxService` / `AgentpayPassageXxxService`
- 结算相关: `SettXxxService`

## 消息队列

ActiveMQ 用于异步通知和处理：

- `Mq4PayOrderListener` - 支付订单消息监听
- `Mq4MchNotify` - 商户通知
- `Mq4MchAgentpayNotify` - 代付通知

### 消息发送示例

```java
@Service
@Slf4j
public class PayOrderMessageService {

    @Autowired
    private JmsTemplate jmsTemplate;

    public void sendPayOrderMessage(PayOrder payOrder) {
        jmsTemplate.convertAndSend("queue.pay.order", payOrder);
        log.info("支付订单消息已发送: {}", payOrder.getPayOrderId());
    }
}
```

## MongoDB 集成

### 文档实体

```java
// src/main/java/org/xxpay/service/mongo/document/PayOrderDocument.java
@Document(collection = "pay_order")
@Data
public class PayOrderDocument {

    @Id
    private String id;

    @Field("pay_order_id")
    private String payOrderId;

    @Field("mch_id")
    private String mchId;

    @Field("amount")
    private Long amount;

    @Field("status")
    private Integer status;

    @Field("create_time")
    private LocalDateTime createTime;
}
```

### Repository

```java
// src/main/java/org/xxpay/service/mongo/repository/PayOrderRepository.java
public interface PayOrderRepository extends MongoRepository<PayOrderDocument, String> {

    PayOrderDocument findByPayOrderId(String payOrderId);

    List<PayOrderDocument> findByMchIdAndCreateTimeBetween(
        String mchId, LocalDateTime start, LocalDateTime end);
}
```

## 环境配置

通过 `spring.profiles.active` 切换环境：

- **local** - 本地开发（SQL 日志开启）
- **dtg-stg** - 测试环境
- **dtg-prod** - 生产环境

### 关键环境变量

| 变量 | 说明 |
|------|------|
| `ZOOKEEPER` | Zookeeper 地址 |
| `DATASOURCE_URL` | MySQL 数据库地址 |
| `DATASOURCE_USERNAME` | 数据库用户名 |
| `DATASOURCE_PASSWORD` | 数据库密码 |
| `REDIS_HOST` | Redis 主机 |
| `REDIS_PASSWORD` | Redis 密码 |
| `ACTIVEMQ_BROKER` | ActiveMQ 地址 |
| `ACTIVEMQ_USER` | ActiveMQ 用户 |
| `ACTIVEMQ_PASSWORD` | ActiveMQ 密码 |
| `MONGODB_URI` | MongoDB 连接 URI |
| `MONGODB_AUTHENTICATION_DATABASE` | MongoDB 认证数据库 |
| `NODE` | 服务节点标识（如 E1, E2）|

## Redis 连接池

- min-idle: 10
- max-active: 50
- max-idle: 30

### 配置示例

```yaml
spring:
  redis:
    host: ${REDIS_HOST:localhost}
    port: ${REDIS_PORT:6379}
    password: ${REDIS_PASSWORD:}
    database: 0
    timeout: 2000ms
    lettuce:
      pool:
        max-active: 50
        max-idle: 30
        min-idle: 10
```

## 开发指南

### 添加新服务

1. 在 `xxpay-core/src/main/java/org/xxpay/core/service/` 创建接口
2. 在 `xxpay-service/src/main/java/org/xxpay/service/impl/` 创建实现类
3. 添加 `@Service` 和 `@DubboService` 注解
4. 编写业务逻辑
5. 编写单元测试

### 添加新 Mapper

1. 在 `dao/mapper/` 创建 Mapper 接口
2. 继承 `BaseMapper<T>` 获得基础 CRUD 方法
3. 添加自定义查询方法
4. 在 `src/main/resources/mapper/` 创建 XML 映射文件（如需要）

### 事务处理

```java
@Override
@Transactional(rollbackFor = Exception.class)
public int updateAgentBalance(String agentId, Long amount) {
    // 事务操作
    AgentAccount account = agentAccountMapper.selectByAgentId(agentId);
    account.setBalance(account.getBalance() + amount);
    return agentAccountMapper.updateById(account);
}
```

## 注意事项

1. **时区**: 统一使用 `Asia/Shanghai`
2. **优雅关闭**: 超时时间 15 秒
3. **JSON**: 日期输出为时间戳（`write-dates-as-timestamps: true`）
4. **日志**: 使用 SLF4J，通过 `@Slf4j` 注解
5. **事务**: 需要 `@Transactional` 时手动添加
6. **MyBatis XML**: 可以放在 `src/main/java/` 或 `src/main/resources/mapper/`

## Git 提交规范

提交信息格式：`EZPAY-xxx: 功能描述`

示例：
- `EZPAY-730: 计算功能优化`
- `EZPAY-799: 优化支付通道页面`
