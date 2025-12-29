# RBGI 银行网关代码示例

## 配置管理

### RBGI 银行 API 配置
```yaml
setting:
  configuration:
    rbgi:
      # UAT 环境
      uat:
        baseUrl: https://public-uat-partners.rbsoftech.online:7443/api/uat/v1
        merchantId: your_merchant_id
        secretKey: your_secret_key

      # 生产环境
      prod:
        baseUrl: https://fin-api-prod.rbsoftech.online/api/v2
        merchantId: your_merchant_id
        secretKey: your_secret_key
```

### 配置类
```java
@Component
@ConfigurationProperties(prefix = "setting.configuration.rbgi")
@Data
public class RbgiConfig {

    private String baseUrl;
    private String merchantId;
    private String secretKey;

    // 根据环境获取配置
    public String getApiUrl(String env) {
        return baseUrl + "/" + env;
    }
}
```

## 认证通道实现

### IAuth 接口
```java
public interface IAuth {

    /**
     * 生成认证请求参数
     */
    JSONObject generateAuthRequest(AuthRequest authRequest);

    /**
     * 执行认证 API 调用
     */
    JSONObject doAuthApi(JSONObject request);

    /**
     * 处理认证响应
     */
    AuthResult handleAuthResponse(JSONObject response);

    /**
     * 处理认证回调
     */
    void handleAuthNotify(JSONObject notify);
}
```

### 认证实现示例
```java
@Service
@Slf4j
public class RbgiIAuth implements IAuth {

    @Autowired
    private RbgiConfig rbgiConfig;

    @Autowired
    private RbgiSignUtils signUtils;

    @Override
    public JSONObject generateAuthRequest(AuthRequest authRequest) {
        JSONObject request = new JSONObject();
        request.put("merchantId", rbgiConfig.getMerchantId());
        request.put("timestamp", System.currentTimeMillis());
        request.put("username", authRequest.getUsername());

        // 生成签名
        String sign = signUtils.generateSign(request);
        request.put("sign", sign);

        return request;
    }

    @Override
    public JSONObject doAuthApi(JSONObject request) {
        String url = rbgiConfig.getApiUrl("auth");

        String response = OkHttpClientUtil.doPostJson(
            url,
            request.toJSONString()
        );

        return JSON.parseObject(response);
    }

    @Override
    public AuthResult handleAuthResponse(JSONObject response) {
        AuthResult result = new AuthResult();

        if ("0000".equals(response.getString("retCode"))) {
            result.setSuccess(true);
            result.setToken(response.getString("token"));
        } else {
            result.setSuccess(false);
            result.setMessage(response.getString("retMsg"));
        }

        return result;
    }
}
```

## 入账通道实现

### CashIn 接口
```java
public interface CashIn {

    /**
     * 生成入账请求
     */
    JSONObject generateCashInRequest(CashInRequest request);

    /**
     * 执行入账 API
     */
    JSONObject doCashInApi(JSONObject request);

    /**
     * 处理入账响应
     */
    CashInResult handleCashInResponse(JSONObject response);

    /**
     * 处理入账回调
     */
    void handleCashInNotify(JSONObject notify);
}
```

### 入账实现示例
```java
@Service
@Slf4j
public class In1001 implements CashIn {

    @Autowired
    private RbgiConfig rbgiConfig;

    @Autowired
    private RbgiSignUtils signUtils;

    @Override
    public JSONObject generateCashInRequest(CashInRequest request) {
        JSONObject req = new JSONObject();
        req.put("merchantId", rbgiConfig.getMerchantId());
        req.put("orderId", request.getOrderId());
        req.put("amount", request.getAmount());
        req.put("account", request.getAccount());
        req.put("timestamp", System.currentTimeMillis());

        // 签名
        String sign = signUtils.generateSign(req);
        req.put("sign", sign);

        return req;
    }

    @Override
    public JSONObject doCashInApi(JSONObject request) {
        String url = rbgiConfig.getApiUrl("cashIn");

        String response = OkHttpClientUtil.doPostJson(
            url,
            request.toJSONString()
        );

        return JSON.parseObject(response);
    }
}
```

## 出账通道实现

### CashOut 接口
```java
public interface CashOut {

    /**
     * 生成出账请求
     */
    JSONObject generateCashOutRequest(CashOutRequest request);

    /**
     * 执行出账 API
     */
    JSONObject doCashOutApi(JSONObject request);

    /**
     * 处理出账响应
     */
    CashOutResult handleCashOutResponse(JSONObject response);

    /**
     * 处理出账回调
     */
    void handleCashOutNotify(JSONObject notify);
}
```

### 出账实现示例
```java
@Service
@Slf4j
public class Out1003 implements CashOut {

    @Autowired
    private RbgiConfig rbgiConfig;

    @Autowired
    private RbgiSignUtils signUtils;

    @Override
    public JSONObject generateCashOutRequest(CashOutRequest request) {
        JSONObject req = new JSONObject();
        req.put("merchantId", rbgiConfig.getMerchantId());
        req.put("orderId", request.getOrderId());
        req.put("amount", request.getAmount());
        req.put("bankAccount", request.getBankAccount());
        req.put("bankName", request.getBankName());
        req.put("timestamp", System.currentTimeMillis());

        // 签名
        String sign = signUtils.generateSign(req);
        req.put("sign", sign);

        return req;
    }

    @Override
    public JSONObject doCashOutApi(JSONObject request) {
        String url = rbgiConfig.getApiUrl("cashOut");

        String response = OkHttpClientUtil.doPostJson(
            url,
            request.toJSONString()
        );

        return JSON.parseObject(response);
    }
}
```

## OkHttp 连接池配置

```java
@Configuration
public class OkHttpConfiguration {

    @Bean
    public OkHttpClient okHttpClient() {
        return new OkHttpClient.Builder()
                .connectTimeout(30, TimeUnit.SECONDS)
                .readTimeout(30, TimeUnit.SECONDS)
                .writeTimeout(30, TimeUnit.SECONDS)
                .connectionPool(new ConnectionPool(
                    80,  // 最大空闲连接
                    20,  // 最小空闲连接
                    5,   // 连接保持时间（分钟）
                    TimeUnit.MINUTES
                ))
                .build();
    }
}
```

## Swagger 配置

```java
@RestController
@RequestMapping("/api/generate")
@Tag(name = "generate", description = "生成接口")
public class GenerateController {

    @Operation(summary = "生成签名")
    @PostMapping("/sign")
    public JSONObject generateSign(@RequestBody SignRequest request) {
        // 实现
    }
}
```

## 控制器示例

```java
@RestController
@RequestMapping("/api/pay")
@Tag(name = "pay", description = "支付接口")
@Slf4j
public class PayController {

    @Autowired
    private CashIn cashInService;

    @Operation(summary = "处理入账")
    @PostMapping("/cashin")
    public ApiResponse handleCashIn(@RequestBody CashInRequest request) {
        log.info("收到入账请求: {}", request.getOrderId());

        // 生成请求
        JSONObject req = cashInService.generateCashInRequest(request);

        // 执行 API
        JSONObject response = cashInService.doCashInApi(req);

        // 处理响应
        CashInResult result = cashInService.handleCashInResponse(response);

        if (result.isSuccess()) {
            return ApiResponse.buildSuccess(result);
        } else {
            return ApiResponse.build(RetEnum.RET_COMM_OPERATE_FAIL, result.getMessage());
        }
    }
}
```
