---
name: payment-core-development
description: This skill should be used when developing xxpay-pay module (payment core) in dtg-pay project. It provides guidance for payment gateway integration, payment channel implementation, and callback handling.
version: 1.0.0
tags: ["payment", "payment-gateway", "channel-integration", "callback"]
---

# 支付核心开发技能

xxpay-pay 是 DTG 支付系统的支付处理微服务，负责对接第三方支付渠道、处理支付/代付/转账业务，以及管理商户回调通知。

## 模块信息

- **模块名称**: xxpay-pay
- **模块类型**: 支付核心
- **HTTP 端口**: 3020
- **Dubbo 端口**: 23020
- **主要职责**: 支付渠道对接、支付订单处理、商户通知

## 核心技术栈

- **Spring Boot 2.7.18** - 应用框架
- **Apache Dubbo 3.2.14** - RPC 框架（Zookeeper 作为注册中心）
- **MyBatis Plus 3.5.7** - ORM 框架
- **MySQL** - 主数据库
- **MongoDB** - 文档存储（支付订单同步）
- **Redis** - 缓存
- **ActiveMQ** - 消息队列
- **OkHttp 4.12.0** - HTTP 客户端

## 构建和运行

### 编译项目

```bash
# 编译（跳过测试）
./mvnw clean package -Dmaven.test.skip=true

# 编译（包含测试）
./mvnw clean package

# 需要先编译依赖模块
./mvnw -f ../xxpay-core clean install -Dmaven.test.skip=true
```

### 运行应用

```bash
# 开发环境运行
mvn spring-boot:run

# 生产环境运行（指定环境）
java -jar target/xxpay-pay-1.0.0.jar --spring.profiles.active=dtg-prod
```

### 运行测试

```bash
# 运行所有测试
mvn test

# 运行单个测试类
mvn test -Dtest=PayOrderControllerTest

# 运行分润测试套件（55 个测试用例）
mvn test -Dtest=ProfitSharingTestSuite
```

## 代码架构

### 分层结构

```
Controller 层 (ctrl/)  →  Service 层 (service/)  →  Channel 层 (channel/)
     ↓                      ↓                          ↓
REST API 接口          业务逻辑处理              第三方支付通道适配器
```

### 核心接口和抽象类

| 类名 | 位置 | 用途 |
|------|------|------|
| `BaseController` | ctrl/common/ | 所有 Controller 的基类，提供参数解析、分页等通用方法 |
| `BasePayNotify` | channel/ | 支付回调通知的抽象基类，所有支付通道回调服务继承此类 |
| `BasePayment` | channel/ | 支付下单的抽象基类 |
| `BaseService` | channel/ | 通道服务的基类，提供通用方法 |
| `PaymentInterface` | channel/ | 支付通道接口定义 |
| `TransNotifyInterface` | channel/ | 代付通知接口定义 |

### RPC 服务调用

通过 `RpcCommonService` 调用 xxpay-service 提供的 Dubbo 服务。关键配置：
- 默认超时：10 秒（部分服务如 IPayOrderService 为 20 秒）
- 重试次数：0
- 注意：consumer 超时（30 秒）必须 >= xxpay-service 的 provider 超时（60 秒）

## 支付通道实现模式

每个支付通道独立封装在 `channel/` 目录下，标准结构：

```
channel/{channel_name}/
├── {ChannelName}Config.java        # 配置类（读取 yaml 配置）
├── {ChannelName}DepositChannel.java # 支付通道（继承 BasePayment）
├── {ChannelName}PaymentService.java # 支付服务
├── {ChannelName}TransNotifyService.java # 代付通知服务（继承 BaseTransNotify）
├── {ChannelName}SignUtils.java      # 签名工具类
└── model/                           # 请求/响应模型
```

### 支付通道实现示例

```java
// channel/catpay/CatpayDepositChannel.java
@Service
@Slf4j
public class CatpayDepositChannel extends BasePayment {

    @Autowired
    private CatpayConfig catpayConfig;

    @Autowired
    private CatpaySignUtils catpaySignUtils;

    @Override
    public JSONObject getPayParam(PayOrder payOrder, String payOrderId) {
        // 组装支付参数
        JSONObject paramMap = new JSONObject();
        paramMap.put("merchantId", catpayConfig.getMerchantId());
        paramMap.put("orderId", payOrderId);
        paramMap.put("amount", payOrder.getAmount());
        paramMap.put("notifyUrl", catpayConfig.getNotifyUrl());

        // 签名
        String sign = catpaySignUtils.getSign(paramMap);
        paramMap.put("sign", sign);

        return paramMap;
    }

    @Override
    public JSONObject doPay(PayOrder payOrder, JSONObject payParam) {
        // 执行支付请求
        String response = OkHttpClientUtil.doPostFormUrlencoded(
            catpayConfig.getPayUrl(),
            payParam.toMap()
        );

        return JSON.parseObject(response);
    }
}
```

### 回调通知实现示例

```java
// channel/catpay/CatpayPayNotifyService.java
@Service
@Slf4j
public class CatpayPayNotifyService extends BasePayNotify {

    @Autowired
    private CatpaySignUtils catpaySignUtils;

    @Override
    public String getChannelName() {
        return "catpay";
    }

    @Override
    public JSONObject verifyNotifyParams(JSONObject params) {
        // 验证回调参数
        if (params == null || params.isEmpty()) {
            return buildFailResp("参数为空");
        }

        // 验证签名
        String sign = params.getString("sign");
        String calculatedSign = catpaySignUtils.getSign(params);

        if (!sign.equals(calculatedSign)) {
            return buildFailResp("签名验证失败");
        }

        return buildSuccessResp();
    }

    @Override
    public PayOrder queryPayOrder(String payOrderId) {
        // 查询订单状态
        return rpcCommonService.rpcPayOrderService.findByPayOrderId(payOrderId);
    }
}
```

## 环境配置

支持多环境配置：`local`、`dtg-stg`、`dtg-prod`

### 关键环境变量

| 变量 | 说明 |
|------|------|
| `ZOOKEEPER` | Dubbo 注册中心地址 |
| `REDIS_HOST` / `REDIS_PASSWORD` | Redis 连接 |
| `ACTIVEMQ_BROKER` / `ACTIVEMQ_USER` / `ACTIVEMQ_PASSWORD` | ActiveMQ 连接 |
| `NODE` | 服务节点标识（分布式环境下每个节点不同） |

### 配置文件结构

```yaml
# application.yml
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

server:
  port: 3020

# 支付通道配置
setting:
  configuration:
    catpay:
      payUrl: https://pay.catpay.com/api/pay
      queryUrl: https://pay.catpay.com/api/query
      notifyUrl: https://your-domain.com/api/pay/notify/catpay
```

## OkHttp 连接池配置

优化后的连接池配置：
- 最大空闲连接：100
- 全局最大并发：500
- 单个三方最大并发：100
- 连接保持时间：45 秒

各支付通道可独立配置连接池参数。

### OkHttp 配置示例

```java
@Configuration
public class OkHttpConfiguration {

    @Bean
    public OkHttpClient okHttpClient() {
        return new OkHttpClient.Builder()
                .connectTimeout(30, TimeUnit.SECONDS)
                .readTimeout(30, TimeUnit.SECONDS)
                .writeTimeout(30, TimeUnit.SECONDS)
                .connectionPool(new ConnectionPool(100, 45, TimeUnit.SECONDS))
                .build();
    }
}
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

## 熔断器

使用 Resilience4j 防止故障商户拖垮通知系统。版本 1.7.1 兼容 Java 11。

### 熔断配置示例

```yaml
resilience4j:
  circuitbreaker:
    instances:
      merchantNotify:
        failure-rate-threshold: 50
        wait-duration-in-open-state: 60s
        sliding-window-size: 10
```

## 测试

### 单元测试示例

```java
@SpringBootTest
class PayOrderServiceTest {

    @Autowired
    private PayOrderService payOrderService;

    @Test
    void shouldCreatePayOrder() {
        PayOrder order = new PayOrder();
        order.setMchId("MCH001");
        order.setAmount(10000L);

        String payOrderId = payOrderService.createPayOrder(order);

        assertNotNull(payOrderId);
        assertTrue(payOrderId.startsWith("PAY"));
    }
}
```

### 集成测试

使用 JUnit 5 + 嵌入式 Redis 进行集成测试。

## 开发指南

### 添加新支付通道

1. 在 `channel/` 下创建新目录
2. 实现继承 `BasePayment` 的支付通道类
3. 实现继承 `BasePayNotify` 的回调通知类
4. 在 `application.yml` 中添加通道配置
5. 参考现有通道如 `catpay`、`toppay`、`aci` 的实现

### 支付通道配置模板

```yaml
setting:
  configuration:
    {channel_name}:
      enabled: true
      payUrl: https://pay.example.com/api/pay
      queryUrl: https://pay.example.com/api/query
      notifyUrl: https://your-domain.com/api/pay/notify/{channel_name}
      merchantId: your_merchant_id
      secretKey: your_secret_key
```

## Git 提交规范

遵循项目规范：`EZPAY-xxx: 功能描述`

示例：
```
EZPAY-730: 计算功能优化
EZPAY-799: 优化支付通道页面
```

## 注意事项

1. **RPC 调用超时**: 注意 consumer 超时必须 >= provider 超时
2. **连接池配置**: 根据第三方 API 限流配置合理的连接数
3. **签名验证**: 所有回调必须验证签名
4. **幂等处理**: 订单处理需要幂等，防止重复处理
5. **日志记录**: 关键步骤记录日志，便于问题排查
6. **异常处理**: 使用 `@SneakyThrows` 简化异常处理
