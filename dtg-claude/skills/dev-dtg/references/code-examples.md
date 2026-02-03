# DTG-Pay 代码示例

## 实体类模板

### 基础实体类

```java
@Data
public abstract class BaseEntity {
    @TableId(type = IdType.ASSIGN_ID)
    private Long id;

    @TableField(fill = FieldFill.INSERT)
    @Builder.Default
    private LocalDateTime createTime = LocalDateTime.now();

    @TableField(fill = FieldFill.INSERT_UPDATE)
    private LocalDateTime updateTime;
}
```

### 支付订单实体

```java
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@TableName("pay_order")
public class PayOrder {

    @TableId(type = IdType.INPUT)
    private String payOrderId;

    @TableField("mch_id")
    private String mchId;

    @TableField("amount")
    private Long amount;

    @TableField(value = "create_time", fill = FieldFill.INSERT)
    private LocalDateTime createTime;

    @TableField(value = "update_time", fill = FieldFill.INSERT_UPDATE)
    private LocalDateTime updateTime;

    @TableField("status")
    private Integer status;  // INIT(0), PAYING(1), SUCCESS(2), FAIL(3), REFUND(4)
}
```

### 商户信息实体

```java
@Data
@TableName("mch_info")
public class MchInfo {
    @TableId(type = IdType.INPUT)
    private String mchId;

    @TableField("mch_name")
    private String mchName;

    @TableField("mch_type")
    @I18n(prefix = "mch.type")
    private Integer mchType;

    @TableField("status")
    private Integer status;  // INIT(0), ACTIVE(1), STOP(2)
}
```

## RPC 通信模型

### RpcBaseParam（入参基类）

```java
@Data
public class RpcBaseParam implements Serializable {
    private String rpcSrcSysId;      // 调用方 ID
    private String rpcDateTime;      // 调用时间
    private String rpcSeqNo;         // 随机通讯码
    private Integer rpcSignType;     // 签名方式 (0-明文, 1-SHA1)
    private String rpcSign;          // RPC 签名
    private String bizSeqNo;         // 业务流水号
}
```

### RpcBaseResult（返回值基类）

```java
@Data
public class RpcBaseResult extends RpcBaseParam {
    private String rpcRetCode;       // 返回码 (0000=成功)
    private String rpcRetMsg;        // 返回错误描述
}
```

## 服务接口定义

```java
package org.xxpay.core.service;

public interface IPayOrderService {
    /**
     * 根据支付订单号查询
     */
    PayOrder findByPayOrderId(String payOrderId);

    /**
     * 创建支付订单
     */
    int insert(PayOrder payOrder);

    /**
     * 更新支付订单
     */
    int update(PayOrder payOrder);
}
```

## Dubbo 服务实现

```java
@Service
@DubboService(version = "${app.dubbo.version}", group = "${app.dubbo.group}")
@Slf4j
public class PayOrderServiceImpl implements IPayOrderService {

    private final PayOrderMapper payOrderMapper;
    private final RedisTemplate<String, Object> redisTemplate;

    @Override
    @Cacheable(value = "payOrder", key = "#payOrderId")
    public PayOrder findByPayOrderId(String payOrderId) {
        return payOrderMapper.selectById(payOrderId);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    @CacheEvict(value = "payOrder", key = "#payOrder.payOrderId")
    public int insert(PayOrder payOrder) {
        return payOrderMapper.insert(payOrder);
    }
}
```

## Controller 模板

```java
@RestController
@RequestMapping("/api/pay_order")
@Slf4j
public class PayOrderController {

    @Autowired
    private IPayOrderService payOrderService;

    @GetMapping("/{payOrderId}")
    public RpcBaseResult getPayOrder(@PathVariable String payOrderId) {
        RpcBaseResult result = new RpcBaseResult();
        PayOrder payOrder = payOrderService.findByPayOrderId(payOrderId);
        result.setRpcRetCode(RetEnum.RET_COMM_SUCCESS.getCode());
        return result;
    }
}
```

## 常量定义

### PayConstant（支付常量）

```java
public class PayConstant {
    /** 支付渠道 */
    public static final String PAY_CHANNEL_ALIPAY = "alipay";
    public static final String PAY_CHANNEL_WECHAT = "wxpay";
    public static final String PAY_CHANNEL_UNIONPAY = "unionpay";

    /** 订单状态 */
    public static final int PAY_STATUS_INIT = 0;
    public static final int PAY_STATUS_PAYING = 1;
    public static final int PAY_STATUS_SUCCESS = 2;
    public static final int PAY_STATUS_FAIL = 3;
    public static final int PAY_STATUS_REFUND = 4;

    /** 支付方式 */
    public static final String PAY_MODE_ALIPAY_SDK = "alipay_sdk";
    public static final String PAY_MODE_WECHAT_SDK = "wxpay_sdk";
}
```

### MchConstant（商户常量）

```java
public class MchConstant {
    /** 商户状态 */
    public static final int MCH_STATUS_INIT = 0;
    public static final int MCH_STATUS_ACTIVE = 1;
    public static final int MCH_STATUS_STOP = 2;

    /** 业务类型 */
    public static final int MCH_BIZ_TYPE_PAY = 1;
    public static final int MCH_BIZ_TYPE_AGENTPAY = 2;
}
```

### RedisConstant（Redis 常量）

```java
public class RedisConstant {
    public static final String PREFIX = "xxpay:";
    public static final String USER_TOKEN = PREFIX + "user:token:";
    public static final String PAY_ORDER = PREFIX + "pay:order:";
    public static final int EXPIRE_HOUR = 3600;
    public static final int EXPIRE_DAY = 86400;
}
```

## 工具类

### 签名工具类

```java
public class SignatureUtils {

    public static String generateSign(Map<String, Object> params, String secretKey) {
        TreeMap<String, Object> sortedParams = new TreeMap<>(params);
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<String, Object> entry : sortedParams.entrySet()) {
            if (entry.getValue() != null && !"".equals(entry.getValue())) {
                sb.append(entry.getKey()).append("=").append(entry.getValue()).append("&");
            }
        }
        sb.append("key=").append(secretKey);
        return DigestUtils.md5Hex(sb.toString());
    }

    public static boolean verifySign(Map<String, Object> params, String sign, String secretKey) {
        String calculatedSign = generateSign(params, secretKey);
        return calculatedSign.equalsIgnoreCase(sign);
    }
}
```

### 日期工具类

```java
public class DateUtils {
    public static long getCurrentTimestamp() {
        return System.currentTimeMillis();
    }

    public static String genSeqNo(String prefix) {
        String dateTime = DateFormatUtils.format(new Date(), "yyyyMMddHHmmss");
        String random = RandomStringUtils.randomNumeric(6);
        return prefix + dateTime + random;
    }
}
```

### HTTP 客户端工具类

```java
public class OkHttpClientUtil {
    private static final OkHttpClient CLIENT = new OkHttpClient.Builder()
            .connectTimeout(30, TimeUnit.SECONDS)
            .readTimeout(30, TimeUnit.SECONDS)
            .build();

    public static String doPostJson(String url, String jsonBody) {
        try {
            RequestBody body = RequestBody.create(
                MediaType.parse("application/json; charset=utf-8"),
                jsonBody
            );
            Request request = new Request.Builder().url(url).post(body).build();
            Response response = CLIENT.newCall(request).execute();
            if (response.isSuccessful() && response.body() != null) {
                return response.body().string();
            }
            return null;
        } catch (Exception e) {
            throw new RuntimeException("HTTP 请求失败", e);
        }
    }
}
```

## 异常处理

```java
public class ServiceException extends RuntimeException {
    private RetEnum retEnum;
    private String extraMsg;

    public ServiceException(RetEnum retEnum) {
        super(retEnum.getMessage());
        this.retEnum = retEnum;
    }

    public ServiceException(RetEnum retEnum, String extraMsg) {
        super(retEnum.getMessage() + ": " + extraMsg);
        this.retEnum = retEnum;
        this.extraMsg = extraMsg;
    }
}
```

## 配置类

### OkHttp 配置

```java
@Configuration
public class OkHttpConfig {
    @Bean
    public OkHttpClient okHttpClient() {
        return new OkHttpClient.Builder()
                .connectTimeout(30, TimeUnit.SECONDS)
                .readTimeout(30, TimeUnit.SECONDS)
                .connectionPool(new ConnectionPool(20, 5, TimeUnit.MINUTES))
                .build();
    }
}
```
