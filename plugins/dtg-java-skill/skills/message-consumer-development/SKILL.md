---
name: message-consumer-development
description: This skill should be used when developing xxpay-consumer module (message consumer) in dtg-pay project. It provides guidance for ActiveMQ message consumption, merchant notification, and retry mechanisms.
version: 1.0.0
tags: ["message-consumer", "activemq", "notification", "retry"]
---

# 消息消费者开发技能

xxpay-consumer 是 DTG-PAY 支付系统的消费者模块，负责处理商户通知（支付通知和代付通知）。

## 模块信息

- **模块名称**: xxpay-consumer
- **模块类型**: 消息消费者
- **HTTP 端口**: 3120
- **Dubbo 端口**: 23120
- **主要职责**: 商户通知处理、ActiveMQ 消息消费

## 核心技术栈

- **Spring Boot 2.7.18** - 应用框架
- **Apache Dubbo 3.2.14** - RPC 框架
- **ActiveMQ** - 消息队列
- **OkHttp** - HTTP 客户端

## 构建和运行

### 编译项目

```bash
# 编译核心模块（依赖）
./mvnw -f ../xxpay-core clean install -Dmaven.test.skip=true

# 编译当前模块
./mvnw clean package -Dmaven.test.skip=true
```

### 运行应用

```bash
# 使用 Maven 运行
./mvnw spring-boot:run

# 或直接运行 JAR
java -jar target/xxpay-consumer-1.0.0.jar
```

默认端口：3120

### 环境配置

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

配置位于 `application.yml` 的 `dubbo` 节点。

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

## 商户通知实现

### 基类实现

```java
// Implementation/Mq4MchNotify.java
public abstract class Mq4MchNotify {

    @Autowired
    private RpcCommonService rpcCommonService;

    @Autowired
    private OkHttpClient okHttpClient;

    /**
     * 处理商户通知
     */
    public void handle(String message) {
        try {
            // 1. 解析消息
            JSONObject msgObj = JSON.parseObject(message);
            String payOrderId = msgObj.getString("payOrderId");

            // 2. 查询支付订单
            PayOrder payOrder = rpcCommonService.rpcPayOrderService
                .findByPayOrderId(payOrderId);

            // 3. 查询商户信息
            MchInfo mchInfo = rpcCommonService.rpcMchInfoService
                .findByMchId(payOrder.getMchId());

            // 4. 构建通知参数
            JSONObject notifyParams = buildNotifyParams(payOrder, mchInfo);

            // 5. 发送通知
            boolean success = sendNotify(mchInfo.getNotifyUrl(), notifyParams);

            if (success) {
                // 标记通知成功
                rpcCommonService.rpcMchNotifyService.updateSuccess(payOrderId);
            } else {
                // 标记通知失败，等待重试
                rpcCommonService.rpcMchNotifyService.increaseRetryCount(payOrderId);
            }

        } catch (Exception e) {
            log.error("处理商户通知异常", e);
        }
    }

    /**
     * 发送 HTTP 通知
     */
    protected boolean sendNotify(String url, JSONObject params) {
        try {
            // 构建请求体
            RequestBody body = RequestBody.create(
                MediaType.parse("application/json; charset=utf-8"),
                params.toJSONString()
            );

            // 构建请求
            Request request = new Request.Builder()
                .url(url)
                .post(body)
                .build();

            // 发送请求
            Response response = okHttpClient.newCall(request).execute();

            if (response.isSuccessful()) {
                String responseBody = response.body().string();
                // 判断商户返回是否成功
                return "success".equalsIgnoreCase(responseBody.trim());
            }

            return false;

        } catch (Exception e) {
            log.error("发送商户通知异常", e);
            return false;
        }
    }

    /**
     * 构建通知参数（子类实现）
     */
    protected abstract JSONObject buildNotifyParams(PayOrder payOrder, MchInfo mchInfo);
}
```

### 支付通知实现

```java
// Implementation/Mq4MchPayNotify.java
@Service
@Slf4j
public class Mq4MchPayNotify extends Mq4MchNotify {

    /**
     * 监听支付通知队列
     */
    @JmsListener(destination = "queue.consumer.notify.mch.pay", containerFactory = "jmsListenerContainerFactory")
    public void onMessage(String message) {
        log.info("[Mq4MchPayNotify] 收到支付通知消息: {}", message);
        handle(message);
    }

    @Override
    protected JSONObject buildNotifyParams(PayOrder payOrder, MchInfo mchInfo) {
        JSONObject params = new JSONObject();
        params.put("payOrderId", payOrder.getPayOrderId());
        params.put("mchId", payOrder.getMchId());
        params.put("amount", payOrder.getAmount());
        params.put("status", payOrder.getStatus());
        params.put("payTime", payOrder.getPayTime());

        // 签名
        String sign = calculateSign(params, mchInfo.getSecretKey());
        params.put("sign", sign);

        return params;
    }
}
```

### 代付通知实现

```java
// Implementation/Mq4MchAgentpayNotify.java
@Service
@Slf4j
public class Mq4MchAgentpayNotify extends Mq4MchNotify {

    /**
     * 监听代付通知队列
     */
    @JmsListener(destination = "queue.consumer.notify.mch.agentpay", containerFactory = "jmsListenerContainerFactory")
    public void onMessage(String message) {
        log.info("[Mq4MchAgentpayNotify] 收到代付通知消息: {}", message);
        handle(message);
    }

    @Override
    protected JSONObject buildNotifyParams(PayOrder payOrder, MchInfo mchInfo) {
        // 代付通知参数构建
        JSONObject params = new JSONObject();
        params.put("transOrderId", payOrder.getPayOrderId());
        params.put("mchId", payOrder.getMchId());
        params.put("amount", payOrder.getAmount());
        params.put("status", payOrder.getStatus());

        return params;
    }
}
```

## ActiveMQ 配置

### 连接池配置

```java
@Configuration
@EnableJms
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
        factory.setMaxThreadPoolSize(30);
        factory.setReconnectOnException(true);

        // 启用异步发送
        factory.setUseAsyncSend(true);
        factory.setAlwaysSyncSend(false);

        // 启用消息压缩
        factory.setUseCompression(true);

        return factory;
    }

    @Bean
    public JmsListenerContainerFactory jmsListenerContainerFactory() {
        DefaultJmsListenerContainerFactory factory = new DefaultJmsListenerContainerFactory();
        factory.setConnectionFactory(activeMQConnectionFactory());
        factory.setConcurrency("10-30");
        factory.setSessionTransacted(false);
        factory.setSessionAcknowledgeMode(Session.AUTO_ACKNOWLEDGE);
        return factory;
    }
}
```

### 配置参数

| 参数 | 值 | 说明 |
|------|---|------|
| 最大连接数 | 30 | 连接池最大连接数 |
| 消费者并发 | 10-30 | 最小10个，最大30个消费者 |
| 每批消息数 | 20 | 每次处理的消息数量 |
| 异步发送 | 启用 | 提高性能 |
| 消息压缩 | 启用 | 减少网络传输 |

## 线程池配置

```java
@Configuration
public class MqThread {

    @Bean(name = "mqExecutor")
    public Executor mqExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(10);
        executor.setMaxPoolSize(30);
        executor.setQueueCapacity(50);
        executor.setThreadNamePrefix("mq-consumer-");
        executor.setWaitForTasksToCompleteOnShutdown(true);
        executor.setAwaitTerminationSeconds(60);
        executor.setRejectedExecutionHandler(new ThreadPoolExecutor.CallerRunsPolicy());
        executor.initialize();
        return executor;
    }
}
```

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

### OkHttp 配置

```java
@Configuration
public class OkHttpConfiguration {

    @Value("${http.proxy.platforms}")
    private Map<String, ProxyConfig> proxyConfigs;

    @Bean
    public OkHttpClient okHttpClient() {
        OkHttpClient.Builder builder = new OkHttpClient.Builder()
                .connectTimeout(30, TimeUnit.SECONDS)
                .readTimeout(30, TimeUnit.SECONDS)
                .writeTimeout(30, TimeUnit.SECONDS);

        // 为不同平台配置代理
        builder.proxySelector(new ProxySelector() {
            @Override
            public List<Proxy> select(URI uri) {
                String platform = extractPlatformFromUrl(uri);
                ProxyConfig config = proxyConfigs.get(platform);

                if (config != null) {
                    return Collections.singletonList(
                        new Proxy(Proxy.Type.HTTP,
                            new InetSocketAddress(config.getHost(), config.getPort()))
                    );
                }

                return Collections.singletonList(Proxy.NO_PROXY);
            }

            @Override
            public void connectFailed(URI uri, SocketAddress sa, IOException ioe) {
                log.error("代理连接失败: {}", uri, ioe);
            }
        });

        return builder.build();
    }
}
```

## 重试机制

### 重试策略

| 重试次数 | 延迟时间 |
|---------|---------|
| 第1次 | 1 分钟 |
| 第2次 | 2 分钟 |
| 第3次 | 4 分钟 |
| 第4次 | 8 分钟 |
| 第5次 | 16 分钟 |

### 重试实现

```java
@Service
@Slf4j
public class MchNotifyRetryService {

    @Autowired
    private RpcCommonService rpcCommonService;

    @Scheduled(fixedDelay = 30000) // 每 30 秒执行一次
    public void retryFailedNotify() {
        try {
            // 查询需要重试的通知记录
            List<MchNotify> retryList = rpcCommonService.rpcMchNotifyService
                .selectRetryList(100);

            for (MchNotify notify : retryList) {
                int retryCount = notify.getRetryCount();

                if (retryCount >= 5) {
                    // 超过最大重试次数，标记为失败
                    rpcCommonService.rpcMchNotifyService
                        .markAsFailed(notify.getId());
                    continue;
                }

                // 计算下次重试时间
                long delayMinutes = (long) Math.pow(2, retryCount);
                LocalDateTime nextRetryTime = notify.getLastNotifyTime()
                    .plusMinutes(delayMinutes);

                if (LocalDateTime.now().isAfter(nextRetryTime)) {
                    // 执行重试
                    retryNotify(notify);
                }
            }

        } catch (Exception e) {
            log.error("[MchNotifyRetryService] 重试异常", e);
        }
    }
}
```

## 时区设置

全局时区：`Asia/Shanghai`

```java
@Configuration
public class TimeZoneConfig {

    @PostConstruct
    public void setDefaultTimezone() {
        TimeZone.setDefault(TimeZone.getTimeZone("Asia/Shanghai"));
    }
}
```

## 依赖关系

- `xxpay-core` - 公共模块（实体类、工具类、常量）
- Dubbo 3.2.14 - RPC 框架
- Spring Boot 2.7.18 - 应用框架
- ActiveMQ - 消息队列
- OkHttp - HTTP 客户端

## 相关模块（整个 DTG-PAY 项目）

- `xxpay-core` - 公共模块和实体类
- `xxpay-service` - Dubbo 服务提供者
- `xxpay-pay` - 支付核心系统
- `xxpay-manage` - 运营管理平台 (端口 8193)
- `xxpay-merchant` - 商户系统 (端口 8191)
- `xxpay-agent` - 代理商系统 (端口 8192)
- `xxpay-task` - 定时任务 (端口 8194)
- `xxpay-flyway` - 数据库迁移
