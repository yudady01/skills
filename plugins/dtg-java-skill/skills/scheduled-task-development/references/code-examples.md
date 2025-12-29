# 定时任务代码示例

## 任务调度配置

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

## 定时任务示例

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

    /**
     * 代理商日终结算汇总
     * 每天凌晨 00:15 执行
     */
    @Scheduled(cron = "0 15 0 ? * *")
    public void agentSettDailyCollectTask() {
        try {
            log.info("[SettScheduled][agentSettDailyCollectTask] 代理商日终结算开始");

            Date yesterday = DateUtils.addDays(new Date(), -1);
            String billDate = DateFormatUtils.format(yesterday, "yyyyMMdd");

            int count = rpcCommonService.rpcSettDailyCollectService.agentCollect(billDate);

            log.info("[SettScheduled][agentSettDailyCollectTask] 代理商日终结算完成, 处理代理商数: {}", count);

        } catch (Exception e) {
            log.error("[SettScheduled][agentSettDailyCollectTask] 代理商日终结算异常", e);
        }
    }
}
```

## 数据同步服务

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

## 并发处理示例

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

## ActiveMQ 配置

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

## 对账单生成任务

```java
@Component
@Slf4j
public class MchBillScheduled {

    @Autowired
    private RpcCommonService rpcCommonService;

    @Value("${CONFIG_MCH_BILL_PATH}")
    private String mchBillPath;

    /**
     * 生成商户对账单
     * 每天凌晨 00:15 执行
     */
    @Scheduled(cron = "0 15 0 ? * *")
    public void buildMchBillTask() {
        try {
            log.info("[MchBillScheduled] 生成商户对账单开始");

            // 获取昨天的日期
            Date yesterday = DateUtils.addDays(new Date(), -1);
            String billDateStr = DateFormatUtils.format(yesterday, "yyyyMMdd");

            // 获取所有商户
            List<MchInfo> mchList = rpcCommonService.rpcMchInfoService.selectAll();

            for (MchInfo mch : mchList) {
                try {
                    // 生成对账单文件
                    String filePath = mchBillPath + billDateStr + "/" + mch.getMchId() + ".csv";

                    // 查询订单数据
                    List<PayOrder> orders = rpcCommonService.rpcPayOrderService.selectByMchIdAndDate(
                        mch.getMchId(), billDateStr
                    );

                    // 写入 CSV 文件
                    writeCsvFile(filePath, orders);

                    log.info("[MchBillScheduled] 商户对账单生成成功: mchId={}, 文件={}", mch.getMchId(), filePath);

                } catch (Exception e) {
                    log.error("[MchBillScheduled] 商户对账单生成失败: mchId={}", mch.getMchId(), e);
                }
            }

            log.info("[MchBillScheduled] 生成商户对账单完成");

        } catch (Exception e) {
            log.error("[MchBillScheduled] 生成商户对账单异常", e);
        }
    }

    private void writeCsvFile(String filePath, List<PayOrder> orders) throws IOException {
        File file = new File(filePath);
        file.getParentFile().mkdirs();

        try (BufferedWriter writer = Files.newBufferedWriter(Paths.get(filePath),
                StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING)) {

            // UTF-8 BOM
            writer.write(new byte[] {(byte) 0xef, (byte) 0xbb, (byte) 0xbf});

            // 写入表头
            writer.write("订单号,商户号,金额,状态,创建时间\n");

            // 写入数据
            for (PayOrder order : orders) {
                writer.write(String.format("%s,%s,%s,%s,%s\n",
                    order.getPayOrderId(),
                    order.getMchId(),
                    order.getAmount(),
                    order.getStatus(),
                    order.getCreateTime()
                ));
            }
        }
    }
}
```

## 汇率同步服务

```java
@Component
@Slf4j
public class FetchCryptoRateScheduled {

    @Autowired
    private OkexApiClient okexApiClient;

    @Autowired
    private BinanceApiClient binanceApiClient;

    @Autowired
    private RedisTemplate<String, Object> redisTemplate;

    /**
     * 抓取加密货币汇率
     * 每 10 秒执行一次
     */
    @Scheduled(cron = "*/10 * * * * ?")
    public void fetchCryptoRate() {
        try {
            log.info("[FetchCryptoRateScheduled] 开始抓取加密货币汇率");

            // 抓取 OKX 汇率
            BigDecimal okxRate = okexApiClient.getCnyUsdtRate();
            redisTemplate.opsForValue().set("CRYPTO:OKX:CNY_USDT", okxRate, 1, TimeUnit.HOURS);

            // 抓取 Binance 汇率
            BigDecimal binanceRate = binanceApiClient.getUsdtRate();
            redisTemplate.opsForValue().set("CRYPTO:BINANCE:USDT", binanceRate, 1, TimeUnit.HOURS);

            log.info("[FetchCryptoRateScheduled] 抓取加密货币汇率完成");

        } catch (Exception e) {
            log.error("[FetchCryptoRateScheduled] 抓取加密货币汇率异常", e);
        }
    }
}
```
