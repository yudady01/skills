# xxpay-consumer 代码示例

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
@Service
@Slf4j
public class Mq4MchPayNotify extends Mq4MchNotify {

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
@Service
@Slf4j
public class Mq4MchAgentpayNotify extends Mq4MchNotify {

    @JmsListener(destination = "queue.consumer.notify.mch.agentpay", containerFactory = "jmsListenerContainerFactory")
    public void onMessage(String message) {
        log.info("[Mq4MchAgentpayNotify] 收到代付通知消息: {}", message);
        handle(message);
    }

    @Override
    protected JSONObject buildNotifyParams(PayOrder payOrder, MchInfo mchInfo) {
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

## 重试机制实现

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

## OkHttp 配置（支持代理）

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

## 时区配置

```java
@Configuration
public class TimeZoneConfig {

    @PostConstruct
    public void setDefaultTimezone() {
        TimeZone.setDefault(TimeZone.getTimeZone("Asia/Shanghai"));
    }
}
```
