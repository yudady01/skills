---
name: scheduled-task-development
description: This skill should be used when developing xxpay-task module (scheduled tasks) in dtg-pay project. It provides guidance for creating scheduled jobs, reconciliation services, and data synchronization tasks.
version: 1.0.0
tags: ["scheduled-task", "reconciliation", "settlement", "sync"]
---

# 定时任务开发技能

xxpay-task 是 dtg-pay 支付系统的后台任务调度模块，负责处理定时任务、异步任务和数据同步。

## 模块信息

- **模块名称**: xxpay-task
- **模块类型**: 定时任务
- **HTTP 端口**: 8194
- **Dubbo 端口**: 28194
- **主要职责**: 定时任务、对账服务、结算服务、数据同步
- **部署要求**: 单节点部署

## 核心技术栈

- **Spring Boot 2.7.18** - 应用框架
- **Apache Dubbo 3.2.14** - RPC 框架
- **Spring Task Scheduling** - 定时任务调度
- **ActiveMQ** - 消息队列
- **MySQL + MongoDB** - 数据存储

## 构建和运行

### 构建

```bash
# 使用 Maven Wrapper 构建（推荐）
./mvnw clean package

# 或使用系统 Maven
mvn clean package

# 跳过测试构建
./mvnw clean package -DskipTests
```

### 运行

```bash
# 本地开发环境运行
./mvnw spring-boot:run

# 指定 profile 运行
./mvnw spring-boot:run -Dspring-boot.run.profiles=dtg-stg

# 运行打包后的 jar
java -jar target/xxpay-task-1.0.0.jar --spring.profiles.active=dtg-prod
```

### 测试

```bash
# 运行所有测试
./mvnw test

# 运行单个测试类
./mvnw test -Dtest=OkexApiClientTest

# 注意：大部分测试类使用 @Disabled 注解，需要手动移除才能运行
```

## 环境配置

### Profile 配置

项目支持三种 profile，通过环境变量 `spring.profiles.active` 配置：

- `local` - 本地开发环境
- `dtg-stg` - 测试环境
- `dtg-prod` - 生产环境

### 关键环境变量

| 变量名 | 说明 |
|--------|------|
| `NODE` | 服务节点标识，分布式环境下需唯一（影响订单 prefix） |
| `ZOOKEEPER` | Dubbo 注册中心地址 |
| `REDIS_HOST` | Redis 主机地址 |
| `REDIS_PASSWORD` | Redis 密码 |
| `ACTIVEMQ_BROKER` | ActiveMQ 消息代理地址 |
| `ACTIVEMQ_USER` | ActiveMQ 用户名 |
| `ACTIVEMQ_PASSWORD` | ActiveMQ 密码 |
| `CONFIG_MCH_BILL_PATH` | 商户对账单文件存储路径 |
| `CONFIG_EXCEL_PATH` | Excel 导出文件路径 |

## 核心架构

### Dubbo RPC 架构

xxpay-task 作为 Dubbo 消费者，通过 `RpcCommonService` 调用其他模块的服务：

- **xxpay-core** - 核心实体、接口定义和通用工具
- **xxpay-service** - 业务服务实现（通过 Dubbo RPC 调用）

所有 RPC 调用超时配置：
- 普通服务：10 秒
- 结算相关：60 秒
- 同步服务：60 分钟（大数据量同步）
- 分润报表：16 分钟

### 模块结构

```
org.xxpay.task
├── agentpay/          # 代付相关任务（状态补偿、初始化修复、解冻修复）
├── common/            # 公共组件（RPC 服务封装、Redis、配置）
├── crypto_rate/       # 加密货币汇率抓取（OKX、Binance、LFB）
├── data/              # 分润报表任务
├── fetch_order/       # 支付订单回调查单（代收/代付）
├── pay_order_excel/   # 支付订单 Excel 导出（MQ 消费）
├── reconciliation/    # 对账单生成
├── settlement/        # 结算任务（商户/代理商日终汇总）
├── statistics_balance/# 余额统计任务
├── sync/              # MySQL -> MongoDB 数据同步
├── utils/             # API 客户端（OKX、Binance、LFB）
└── whitelist/         # IP 白名单待审核任务
```

## 定时任务配置

### 任务调度配置

```java
@Configuration
@EnableScheduling
public class SchedulingConfig {

    @Bean(name = "scheduledTaskExecutor")
    public Executor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(15);
        executor.setMaxPoolSize(15);
        executor.setQueueCapacity(100);
        executor.setThreadNamePrefix("scheduled-task-");
        executor.setWaitForTasksToCompleteOnShutdown(true);
        executor.setAwaitTerminationSeconds(60);
        executor.setRejectedExecutionHandler(new ThreadPoolExecutor.CallerRunsPolicy());
        executor.initialize();
        return executor;
    }
}
```

### 主要定时任务

| 任务类 | Cron 表达式 | 说明 | 文件位置 |
|--------|------------|------|----------|
| `SettScheduled.mchSettDailyCollectTask` | `0 5 0 ? * *` | 商户日终结算 | settlement/scheduled/SettScheduled.java:34 |
| `SettScheduled.agentSettDailyCollectTask` | `0 15 0 ? * *` | 代理商日终结算 | settlement/scheduled/SettScheduled.java:56 |
| `MchBillScheduled.buildMchBillTask` | `0 15 0 ? * *` | 生成商户对账单 | reconciliation/scheduled/MchBillScheduled.java:49 |
| `FetchCallbackScheduled.runFetchOrder` | `0 0/1 * * * ?` | 回调查单（每分钟） | fetch_order/scheduled/FetchCallbackScheduled.java:56 |
| `FetchCryptoRateScheduled` | `*/10 * * * * ?` | 加密货币汇率同步 | crypto_rate/scheduled/FetchCryptoRateScheduled.java |
| `AgentpayStatusCompensationTask.compensateStuckOrders` | `0 */10 * * * ?` | 代付状态补偿 | agentpay/AgentpayStatusCompensationTask.java:54 |
| `PayOrderSyncService` | `*/30 * * * * ?` | MySQL -> MongoDB 同步 | sync/PayOrderSyncService.java:119 |
| `StatisticsScheduled` | `0 0 1 * * ?` | 余额统计 | statistics_balance/scheduled/StatisticsScheduled.java |

### 定时任务示例

```java
@Component
@Slf4j
public class SettScheduled {

    @Autowired
    private RpcCommonService rpcCommonService;

    /**
     * 商户日终结算汇总
     * 每天凌晨 00:05 执行
     */
    @Scheduled(cron = "0 5 0 ? * *")
    public void mchSettDailyCollectTask() {
        try {
            log.info("[SettScheduled][mchSettDailyCollectTask] 商户日终结算开始");

            // 获取昨天的日期
            Date yesterday = DateUtils.addDays(new Date(), -1);
            String billDate = DateFormatUtils.format(yesterday, "yyyyMMdd");

            // 执行结算汇总
            int count = rpcCommonService.rpcSettDailyCollectService.mchCollect(billDate);

            log.info("[SettScheduled][mchSettDailyCollectTask] 商户日终结算完成, 处理商户数: {}", count);

        } catch (Exception e) {
            log.error("[SettScheduled][mchSettDailyCollectTask] 商户日终结算异常", e);
        }
    }
}
```

## 消息队列

### 主要队列

| 队列名称 | 用途 |
|----------|------|
| `PRODUCE_PAY_EXCEL_QUEUE` | 支付订单 Excel 导出队列 |
| `PRODUCE_AG_PAY_EXCEL_QUEUE` | 代理商支付订单 Excel 导出队列 |
| `PRODUCE_MCH_PAY_EXCEL_QUEUE` | 商户支付订单 Excel 导出队列 |

### 消费者配置

```java
@Configuration
public class ActiveMqConf {

    @Value("${spring.activemq.broker-url}")
    private String brokerUrl;

    @Value("${spring.activemq.user}")
    private String user;

    @Value("${spring.activemq.password}")
    private String password;

    @Bean
    public ActiveMQConnectionFactory activeMQConnectionFactory() {
        ActiveMQConnectionFactory factory = new ActiveMQConnectionFactory();
        factory.setBrokerURL(brokerUrl);
        factory.setUserName(user);
        factory.setPassword(password);

        // 连接池配置
        factory.setMaxThreadPoolSize(10);
        factory.setReconnectOnException(true);

        return factory;
    }

    @Bean
    public JmsListenerContainerFactory jmsListenerContainerFactory() {
        DefaultJmsListenerContainerFactory factory = new DefaultJmsListenerContainerFactory();
        factory.setConnectionFactory(activeMQConnectionFactory());
        factory.setConcurrency("1-10");
        factory.setSessionTransacted(false);
        return factory;
    }
}
```

## 数据同步

### MySQL -> MongoDB 同步机制

xxpay-task 将 MySQL 支付订单数据同步到 MongoDB，用于高性能查询和报表生成。

**同步流程：**
1. 创建控制文档：每 5 分钟创建一个时间窗口
2. 首次同步：每 30 秒执行一次，同步状态 INIT → FIRST_SYNC_DONE
3. 二次同步：每 2 分钟执行一次，同步状态 FIRST_SYNC_DONE → SYNC_DONE
4. 数据清理：每天早上 6 点清理 7 天前的 MySQL 数据

**同步条件：** CreateTime OR UpdateTime（捕获延迟更新的订单）

**启动补偿：** 应用重启时，根据上次同步状态智能回溯，避免数据丢失

### 同步服务实现

```java
@Service
@Slf4j
public class PayOrderSyncService {

    @Autowired
    private MongoTemplate mongoTemplate;

    @Autowired
    private RpcCommonService rpcCommonService;

    /**
     * 同步支付订单到 MongoDB
     * 每 30 秒执行一次
     */
    @Scheduled(cron = "*/30 * * * * ?")
    public void syncPayOrder() {
        try {
            log.info("[PayOrderSyncService] 开始同步支付订单");

            // 查询需要同步的订单
            List<PayOrder> orders = rpcCommonService.rpcPayOrderService.selectNeedSync(1000);

            if (orders.isEmpty()) {
                log.info("[PayOrderSyncService] 没有需要同步的订单");
                return;
            }

            // 批量插入 MongoDB
            List<PayOrderDocument> documents = orders.stream()
                    .map(this::convertToDocument)
                    .collect(Collectors.toList());

            mongoTemplate.insertAll(documents);

            log.info("[PayOrderSyncService] 同步支付订单完成, 数量: {}", orders.size());

        } catch (Exception e) {
            log.error("[PayOrderSyncService] 同步支付订单异常", e);
        }
    }

    private PayOrderDocument convertToDocument(PayOrder order) {
        PayOrderDocument doc = new PayOrderDocument();
        doc.setPayOrderId(order.getPayOrderId());
        doc.setMchId(order.getMchId());
        doc.setAmount(order.getAmount());
        doc.setStatus(order.getStatus());
        // ... 其他字段
        return doc;
    }
}
```

## 汇率服务

项目从多个第三方 API 抓取加密货币汇率，并存储到 Redis：

- **OKX**：CNY/USDT、大额 C2C 汇率
- **Binance**：USDT 汇率
- **LFB**：USDT 汇率
- **Wealthmall**：USDT 汇率

同步频率：每 10 秒

## 开发注意事项

### 时间配置

- 默认时区：`Asia/Shanghai`
- Jackson 序列化：时间戳格式（毫秒）
- 所有定时任务基于服务器时间

### 日志规范

使用 `@Slf4j` 注解（Lombok），使用 MDC 记录 traceId，格式：`[功能模块][子模块]traceId:{}, 消息`

日志级别：INFO（业务流程）、WARN（告警）、ERROR（异常）

### 异常处理

- 定时任务必须捕获所有异常，防止影响调度器
- 不要在定时任务中重新抛出异常
- 使用 try-with-resources 或 finally 块清理资源（MDC、文件句柄）

### RPC 调用

- 所有 RPC 调用通过 `RpcCommonService` 进行
- 注意超时配置，特别是同步服务（60 分钟）
- 使用 `@DubboReference` 注解注入服务

### 并发处理

```java
@Service
@Slf4j
public class FetchCallbackScheduled {

    @Autowired
    private ThreadPoolTaskExecutor fetchCallbackExecutor;

    public void fetchCallback() {
        List<PayOrder> orders = getNeedFetchOrders();

        // 使用线程池并行处理
        CountDownLatch latch = new CountDownLatch(orders.size());

        for (PayOrder order : orders) {
            fetchCallbackExecutor.submit(() -> {
                try {
                    // 继承父线程的 MDC 上下文
                    MDC.put("traceId", MDC.get("traceId"));

                    fetchOrder(order);

                } finally {
                    MDC.clear();
                    latch.countDown();
                }
            });
        }

        // 等待所有任务完成
        latch.await();
    }
}
```

### 文件处理

- CSV 文件使用 UTF-8 BOM 格式（`{(byte) 0xef, (byte) 0xbb, (byte) 0xbf}`）
- 对账单路径按日期组织：`{mchBillPath}{billDateStr}/{mchId}.csv`
- Excel 导出文件默认保留 90 天

## 部署顺序

部署时需按以下顺序：
1. xxpay-flyway
2. xxpay-service
3. xxpay-pay
4. xxpay-task（**单节点部署**）
5. xxpay-manage
6. xxpay-agent
7. xxpay-merchant

## Git 提交规范

提交信息格式：`EZPAY-xxx: 功能描述`

示例：
- `EZPAY-730: 计算功能优化`
- `EZPAY-799: 优化支付通道页面`

## 相关模块

- **xxpay-core** - 核心模块（实体、接口、工具）
- **xxpay-service** - 业务服务实现
- **xxpay-manage** - 管理后台
- **xxpay-merchant** - 商户后台
- **xxpay-agent** - 代理商后台
- **xxpay-pay** - 支付网关
