---
name: payChannel-thirdparty
description: 专业的支付渠道第三方集成开发技能，提供支付渠道处理类的快速生成、最佳实践指南、安全验证和代码模板。支持代收(Recharge)、代付(Withdraw)、余额查询等功能模块的标准化开发，包含签名验证、加密解密、银行映射等常用工具类。用于开发新的支付渠道集成、重构现有支付代码、支付安全审计、支付接口测试等场景。
---

# 支付渠道第三方集成开发技能

## 快速开始

### 创建新的支付渠道处理类
```bash
# 使用代码生成脚本
python scripts/generate_payment_handler.py --channel-name NewPay --channel-code 1270 --support-recharge --support-withdraw --auth-type sign
```

### 验证现有支付代码
```bash
# 代码质量检查
python scripts/validate_payment_handler.py --file Pay1270.java
```

## 支付渠道类型

### 认证方式分类
- **签名认证**：MD5/SHA256 + 私钥 (如：Pay1268, Pay1256)
- **Token认证**：Bearer Token (如：Pay1260)
- **AES加密**：AES/CBC/PKCS5Padding (如：Pay1255)
- **无认证**：直接API调用 (如：Pay1265余额查询)

### 功能支持分类
- **代收Only**：仅支持充值 (如：Pay1265)
- **代付Only**：仅支持提现 (如：Pay1268)
- **全功能**：支持代收+代付+余额查询 (如：Pay1256, Pay1266)

## 核心组件开发指南

### 1. PaymentConfig 配置
```java
private static final PaymentConfig PAYMENT_CONFIG = PaymentConfig.builder()
    .rechargeApiPath("/api/deposit")           // 代收API路径
    .rechargeQueryApiPath("/api/deposit/info")  // 代收查询API路径
    .rechargeNotifyPrint("success")             // 代收回调响应
    .queryBalanceApiPath("/api/balance")        // 余额查询API路径
    .withdrawApiPath("/api/withdraw")           // 代付API路径
    .withdrawNotifyPrint("success")             // 代付回调响应
    .jumpMode(JumpMode.REDIRECT)                // 跳转模式
    .build();
```

### 2. 签名生成模式

#### MD5签名 (最常用)
```java
private String generateSign(String functionName, TreeMap<String, Object> sortedMap, String privateKey) {
    String queryString = paymentUtils.toUrlQueryEncodedString(sortedMap, StringPool.AMPERSAND);
    String textToBeSigned = queryString + SIGN_SUFFIX_WITH_API_KEY + privateKey;
    String sign = DigestUtils.md5Hex(textToBeSigned);
    return sign.toUpperCase(); // 或小写，根据三方要求
}
```

#### SHA256+MD5双重签名 (高安全)
```java
private String generateSign(String functionName, Map<String, Object> parameters, String signKey, Set<String> excludedKeys) {
    // 1. 排除指定字段
    Map<String, Object> needSignParamMap = new TreeMap<>(parameters);
    for (String exclude : excludedKeys) {
        needSignParamMap.remove(exclude);
    }

    // 2. 组合参数+私钥
    String textToBeSigned = paymentUtils.convertToQueryString(needSignParamMap) + signKey;

    // 3. SHA256然后MD5
    String sha256Hex = DigestUtils.sha256Hex(textToBeSigned);
    String signUpperCase = DigestUtils.md5Hex(sha256Hex).toUpperCase();

    return signUpperCase;
}
```

#### HMAC-SHA256签名 (Webhook)
```java
private boolean isValidHmacSign(String functionName, NotifyDto notify, String signKey) {
    String webhookId = notify.getHeaders().get("webhook-id");
    String webhookTimestamp = notify.getHeaders().get("webhook-timestamp");
    String webhookSignature = notify.getHeaders().get("webhook-signature");
    String rawBody = notify.getRawBodyString();

    String textToBeSigned = webhookId + "." + webhookTimestamp + "." + rawBody;
    byte[] hmacBytes = new HmacUtils(HmacAlgorithms.HMAC_SHA_256, signKey.getBytes())
        .hmac(textToBeSigned.getBytes(StandardCharsets.UTF_8));

    String ourSignature = Base64.getEncoder().encodeToString(hmacBytes);
    return verifySignature(webhookSignature, ourSignature);
}
```

### 3. 银行名称映射
```java
private static final Map<String, String> BANK_NAME_MAPPING = Map.of(
    "004", "臺灣銀行",
    "005", "土地銀行",
    "006", "合庫商銀",
    "007", "第一銀行",
    "008", "華南銀行"
    // ... 更多银行映射
);

private String getThirdPartyBankName(String bankCode) {
    return BANK_NAME_MAPPING.getOrDefault(bankCode, "提現不支援的銀行");
}
```

### 4. AES加密解密
```java
public static String decrypt(String doubleBase64Cipher, String secretKey, String secretIv) throws Exception {
    byte[] key = deriveKey(secretKey);    // 32 bytes
    byte[] iv  = deriveIv(secretIv);      // 16 bytes

    byte[] innerB64Bytes = Base64.getDecoder().decode(doubleBase64Cipher);
    String innerB64 = new String(innerB64Bytes, StandardCharsets.UTF_8);
    byte[] raw = Base64.getDecoder().decode(innerB64);

    Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
    cipher.init(Cipher.DECRYPT_MODE, new SecretKeySpec(key, "AES"), new IvParameterSpec(iv));
    byte[] plain = cipher.doFinal(raw);
    return new String(plain, StandardCharsets.UTF_8);
}
```

## 错误处理最佳实践

### 1. 响应处理
```java
@Override
public void handleWithdrawResponse(String response, WithdrawResultVo withdrawResultVo) throws Exception {
    log.info("{}[代付回應] response: {}", LOG_PREFIX, response);
    Map<String, Object> resBody = objectMapper.readValue(response, new TypeReference<>() {});

    String code = String.valueOf(resBody.get("code"));
    boolean isSuccess = SUCCESS_RESPONSE_CODE.equals(code);
    withdrawResultVo.setIsSuccess(isSuccess);

    if (!isSuccess) {
        withdrawResultVo.setRespCode(code);
        withdrawResultVo.setResData(String.valueOf(resBody.get("data"))); // 保存错误详情
        withdrawResultVo.setRespMessage(String.valueOf(resBody.get("msg")));
    }
}
```

### 2. 异常处理
```java
@Override
public RechargeNotifyResult handleRechargeNotify(NotifyDto notify, ChannelMerchantAccountEntity account) {
    try {
        // 业务逻辑
        return NotifyResultUtils.rechargeNotifySuccess(callbackOrderNo, amount, fee);
    } catch (Exception e) {
        log.error("{}[代收回調處理] 失败", LOG_PREFIX, e);
        return NotifyResultUtils.rechargeNotifyFail(notify.getOrderId(), "代收失敗解析錯誤: " + e.getMessage());
    }
}
```

## 安全性检查清单

### 必须验证项目
- [ ] 签名验证逻辑正确性
- [ ] 金额精度处理（整数/小数位数）
- [ ] 订单号重复检查
- [ ] 回调IP白名单（如果支持）
- [ ] 敏感信息日志脱敏
- [ ] SQL注入防护
- [ ] 超时设置

### 推荐安全措施
- [ ] 使用枚举定义状态码和常量
- [ ] 参数验证和边界检查
- [ ] 异常信息不暴露内部错误
- [ ] 重试机制和幂等性设计
- [ ] 监控和告警设置

## 常见问题解决

### Q: 如何处理三方回调格式不统一？
A: 使用适配器模式，创建统一的回调处理接口，不同的三方实现各自的解析逻辑。

### Q: 签名验证失败怎么办？
A: 检查参数排序、编码格式、大小写、空值处理等细节，使用调试日志输出中间结果。

### Q: 如何处理银行代码映射？
A: 创建统一的银行代码映射表，支持三方不同银行代码的转换。

## 测试模板

### 单元测试示例
```java
@Test
void testGenerateSign() {
    // Given
    TreeMap<String, Object> params = new TreeMap<>();
    params.put("amount", "1000");
    params.put("orderNo", "TEST001");

    // When
    String sign = paymentHandler.generateSign("测试", params, "testKey");

    // Then
    assertThat(sign).isNotEmpty();
    assertThat(sign).hasSize(32); // MD5 length
}
```

### 集成测试示例
```java
@Test
void testWithdrawFlow() {
    // 模拟完整的代付流程
    WithdrawParameterDto dto = createMockWithdrawDto();
    Map<String, Object> request = paymentHandler.generateWithdrawRequest(dto);
    String response = paymentHandler.doWithdrawApi(testUrl, request, dto.getChannelMerchantAccountVo());

    WithdrawResultVo resultVo = new WithdrawResultVo();
    paymentHandler.handleWithdrawResponse(response, resultVo);

    assertThat(resultVo.getIsSuccess()).isTrue();
}
```

## 参考资源

- **完整API文档**：见 [references/api_documentation.md](references/api_documentation.md)
- **安全指南**：见 [references/security_guide.md](references/security_guide.md)
- **错误代码表**：见 [references/error_codes.md](references/error_codes.md)
- **银行代码映射**：见 [assets/bank_mappings.json](assets/bank_mappings.json)
- **代码模板**：见 [assets/templates/](assets/templates/)