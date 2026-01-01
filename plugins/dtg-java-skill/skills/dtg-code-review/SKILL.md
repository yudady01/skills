---
name: dtg-code-review
description: This skill should be used when the user asks to "code review", "review code", "check code quality", "analyze code", "security review", "OWASP", "find vulnerabilities", "check for bugs", or mentions code quality, security issues, static analysis, code smells, or code inspection. Provides OWASP Top 10 security checks, enterprise-grade Java code review, Dubbo service security, MyBatis-Plus injection prevention, and automated issue identification for Spring Boot 2.7 + Dubbo 3 microservices.
version: 3.0.0
tags:
  - code-review
  - security
  - spring-boot
  - dubbo
  - quality
  - static-analysis
---

# DTG 代码审查

智能化 Spring Boot 2.7 + Dubbo 3 微服务代码审查技能，提供全面的安全检查和质量评估。

## 何时使用此技能

在以下情况下使用此技能：

- 审查 Spring Boot + Dubbo 微服务代码的安全漏洞
- 检查 MyBatis-Plus 查询的注入风险
- 验证 Dubbo 服务接口安全性
- 评估微服务架构设计质量
- 审查支付敏感代码（加密、签名、回调）
- 检查配置文件安全风险
- 进行企业级 Java 代码质量审查

## OWASP Top 10 2025 快速参考 (Spring Boot)

| 排名 | 漏洞 | Spring Boot 缓解措施 |
|------|--------------|----------------|
| A01 | 访问控制失效 | `@PreAuthorize`、自定义拦截器、Dubbo Filter |
| A02 | 安全配置错误 | 禁用 Actuator 端点、生产环境配置分离、配置加密 |
| A03 | 软件供应链故障 | 依赖扫描 (OWASP Dependency-Check)、SBOM、验证依赖 |
| A04 | 加密失败 | JCE Provider、配置加密 (Jasypt)、TLS 1.3 |
| A05 | 注入 | MyBatis-Plus 参数化、输入验证、CSRF 防护 |
| A06 | 不安全设计 | 纵深防御、安全设计模式、限流熔断 |
| A07 | 身份验证失败 | JWT + Redis、会话管理、MFA 集成 |
| A08 | 数据完整性失败 | 数字签名、防篡改机制、审计日志 |
| A09 | 日志和警报失败 | Logback/SLF4J、集中式日志 (ELK)、异常监控 |
| A10 | 异常处理不当 | `@ControllerAdvice`、通用错误响应、安全失败 |

**详细缓解措施**：参见 [OWASP Top 10 2025 参考](references/owasp-top-10-2025.md)

## Java/Spring Boot 核心安全编码原则

### 1. 输入验证 (JSR-303/380 + Spring Validation)

**永远不要信任用户输入。** 在服务器端验证所有输入。

```java
// ✅ 好：使用 Bean Validation 注解
import javax.validation.constraints.*;
import org.hibernate.validator.constraints.Length;

public class PayOrderCreateRequest {

    @NotBlank(message = "商户号不能为空")
    @Pattern(regexp = "^[A-Z0-9]{8,32}$", message = "商户号格式错误")
    private String mchId;

    @NotNull(message = "金额不能为空")
    @DecimalMin(value = "0.01", message = "金额最小为 0.01")
    @DecimalMax(value = "999999.99", message = "金额最大为 999999.99")
    private BigDecimal amount;

    @NotBlank(message = "支付渠道不能为空")
    @Pattern(regexp = "^[A-Z0-9_]{2,16}$", message = "渠道码格式错误")
    private String payChannelId;

    @Length(max = 128, message = "回调URL长度不能超过128")
    @Pattern(regexp = "^https?://[\\w\\-]+(\\.[\\w\\-]+)+[/#?]?.*$", message = "回调URL格式错误")
    private String notifyUrl;
}

// Controller 层验证
@RestController
@RequestMapping("/api/payOrder")
public class PayOrderController {

    @PostMapping("/create")
    public Result<PayOrder> createOrder(@Valid @RequestBody PayOrderCreateRequest request) {
        // 验证通过，处理业务逻辑
        return Result.success(payOrderService.createOrder(request));
    }
}

// ❌ 坏：无验证
public PayOrder createOrder(PayOrderRequest request) {
    return payOrderService.save(request);  // 危险！
}
```

### 2. MyBatis-Plus 防注入 (SQL Injection Prevention)

**始终使用 MyBatis-Plus 的条件构造器或 Mapper 方法。**

```java
// ✅ 好：使用 QueryWrapper (参数化查询)
@Service
public class PayOrderServiceImpl extends ServiceImpl<PayOrderMapper, PayOrder> implements PayOrderService {

    public PayOrder getByOrderNo(String orderNo) {
        return lambdaQuery()
                .eq(PayOrder::getPayOrderId, orderNo)
                .one();
    }

    public List<PayOrder> listByMchIdAndStatus(String mchId, Byte status) {
        return lambdaQuery()
                .eq(PayOrder::getMchId, mchId)
                .eq(PayOrder::getStatus, status)
                .orderByDesc(PayOrder::getCreateTime)
                .list();
    }
}

// ✅ 好：使用 @Select 注解 (参数化)
@Mapper
public interface PayOrderMapper extends BaseMapper<PayOrder> {

    @Select("SELECT * FROM pay_order WHERE pay_order_id = #{orderNo} AND mch_id = #{mchId}")
    PayOrder selectByOrderNoAndMchId(@Param("orderNo") String orderNo, @Param("mchId") String mchId);
}

// ❌ 坏：字符串拼接 (SQL 注入漏洞)
@Select("SELECT * FROM pay_order WHERE pay_order_id = '${orderNo}'")  // 易受攻击！
PayOrder selectByOrderNo(@Param("orderNo") String orderNo);
```

### 3. Dubbo 服务安全

```java
// ✅ 好：使用 Token 验证的 Dubbo Filter
@Activate(group = {Constants.PROVIDER})
public class TokenValidationFilter implements Filter {

    @Override
    public Result invoke(Invoker<?> invoker, Invocation invocation) {
        String token = RpcContext.getContext().getAttachment("authToken");

        if (!isValidToken(token)) {
            return new Result(1, "Invalid authentication token", null);
        }

        return invoker.invoke(invocation);
    }
}

// ✅ 好：服务接口权限控制
@Service(version = "1.0.0")
public class PayOrderServiceImpl implements PayOrderService {

    @Override
    @DubboServiceAuth(permission = "pay:order:create")
    public PayOrder createOrder(PayOrderCreateRequest request) {
        // 业务逻辑
    }
}
```

### 4. 密码和敏感数据加密

```java
// ✅ 好：使用 BCrypt 或 Argon2 进行密码哈希
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.argon2.Argon2PasswordEncoder;

@Service
public class UserService {

    private final BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder(12);

    public void createUser(UserCreateRequest request) {
        User user = new User();
        user.setUsername(request.getUsername());
        user.setPassword(passwordEncoder.encode(request.getPassword()));  // 安全哈希
        user.setSalt(generateRandomSalt());
        userRepository.save(user);
    }
}

// ✅ 好：使用 Jasypt 加密配置
# application.yml
jasypt:
  encryptor:
    password: ${JASYPT_ENCRYPTOR_PASSWORD}
    algorithm: PBEWITHHMACSHA512ANDAES_256
    iv-generator-classname: org.jasypt.iv.RandomIvGenerator

# 加密数据库密码
spring:
  datasource:
    password: ENC(gQ4lJz7G3xK3R8hN0xM3pQ==)
```

### 5. 支付签名验证 (Signature Verification)

```java
// ✅ 好：统一的签名验证工具
@Component
public class PaySignatureValidator {

    /**
     * 验证支付回调签名
     * @param params 参数Map（不包含sign字段）
     * @param sign 待验证签名
     * @param key 商户密钥
     */
    public boolean verifyCallbackSign(Map<String, String> params, String sign, String key) {
        // 1. 参数排序
        TreeMap<String, String> sortedParams = new TreeMap<>(params);
        sortedParams.remove("sign");

        // 2. 拼接参数
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<String, String> entry : sortedParams.entrySet()) {
            if (StringUtils.isNotBlank(entry.getValue())) {
                sb.append(entry.getKey()).append("=").append(entry.getValue()).append("&");
            }
        }
        sb.append("key=").append(key);

        // 3. MD5 签名
        String calculatedSign = DigestUtils.md5Hex(sb.toString()).toUpperCase();

        return calculatedSign.equals(sign);
    }
}
```

### 6. 安全的异常处理

```java
// ✅ 好：统一异常处理，不暴露内部细节
@RestControllerAdvice
public class GlobalExceptionHandler {

    private static final Logger logger = LoggerFactory.getLogger(GlobalExceptionHandler.class);

    @ExceptionHandler(SQLException.class)
    public Result<Void> handleSQLException(SQLException ex) {
        logger.error("Database error: {}", ex.getMessage(), ex);
        return Result.fail(500, "系统繁忙，请稍后重试");  // 不暴露数据库错误
    }

    @ExceptionHandler(AuthenticationException.class)
    public Result<Void> handleAuthException(AuthenticationException ex) {
        logger.warn("Authentication failed: {}", ex.getMessage());
        return Result.fail(401, "认证失败");  // 通用错误消息
    }
}

// ❌ 坏：暴露内部错误
@ExceptionHandler(SQLException.class)
public Result<Void> handleSQLException(SQLException ex) {
    return Result.fail(500, ex.getMessage());  // 易受攻击 - 暴露数据库信息
}
```

## 支付系统安全审查清单

### 支付订单处理

- [ ] 订单号使用 UUID 或雪花算法生成，确保唯一性
- [ ] 金额使用 `BigDecimal`，不使用 `double`/`float`
- [ ] 支付回调进行签名验证
- [ ] 重复回调幂等处理
- [ ] 订单状态机严格控制状态转换
- [ ] 敏感字段（银行卡号、密码）加密存储

### 支付渠道集成

```java
// ✅ 好：支付渠道基类模板
public abstract class AbstractPayChannel<T extends PayConfig> {

    /**
     * 验证回调签名
     */
    protected abstract boolean verifySign(Map<String, String> params);

    /**
     * 解析回调参数
     */
    protected abstract PayCallbackResult parseCallback(Map<String, String> params);

    /**
     * 统一回调处理模板方法
     */
    public final PayOrderProcessResult handleCallback(Map<String, String> params) {
        // 1. 签名验证
        if (!verifySign(params)) {
            return PayOrderProcessResult.fail("签名验证失败");
        }

        // 2. 解析回调
        PayCallbackResult callback = parseCallback(params);

        // 3. 幂等检查
        PayOrder existingOrder = payOrderService.getByOrderNo(callback.getOrderNo());
        if (existingOrder.getStatus() == PayStatus.SUCCESS) {
            return PayOrderProcessResult.success("订单已处理");
        }

        // 4. 更新订单
        return payOrderService.updateOrderStatus(callback);
    }
}
```

### Dubbo 服务安全

- [ ] 所有服务接口添加版本号控制
- [ ] 敏感服务添加 Token 验证 Filter
- [ ] 超时配置合理（避免资源耗尽）
- [ ] 负载均衡和容错策略配置
- [ ] 服务降级和熔断配置

### 配置安全

```yaml
# ✅ 好：生产环境配置示例
spring:
  profiles:
    active: prod

  # 禁用 Actuator 敏感端点
  management:
    endpoints:
      web:
        exposure:
          include: health,info
          exclude: env,configprops,beans
    endpoint:
      health:
        show-details: never  # 生产环境不显示详情

# Dubbo 安全配置
dubbo:
  provider:
    timeout: 5000
    token: true  # 启用 Token 验证
  protocol:
    name: dubbo
    # 生产环境使用 Hessian2 序列化（更安全）
    serialization: hessian2
```

## 代码质量度量指标

| 指标 | 阈值 | 说明 |
|------|------|------|
| 圈复杂度 | ≤ 10 | 单方法复杂度 |
| 方法行数 | ≤ 50 | 单方法代码行数 |
| 类行数 | ≤ 500 | 单类代码行数 |
| 测试覆盖率 | ≥ 70% | 单元测试覆盖率 |
| 重复代码率 | ≤ 5% | 代码重复度 |

## Spring Boot 常见安全问题

### 1. Actuator 端点泄露

```yaml
# ❌ 危险：生产环境暴露所有端点
management:
  endpoints:
    web:
      exposure:
        include: "*"

# ✅ 安全：仅暴露必要端点
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics
    endpoint:
      health:
        show-details: when-authorized
```

### 2. CORS 配置不当

```java
// ❌ 危险：允许所有来源
@Configuration
public class CorsConfig {
    @Bean
    public CorsFilter corsFilter() {
        CorsConfiguration config = new CorsConfiguration();
        config.addAllowedOrigin("*");  // 危险！
        // ...
    }
}

// ✅ 安全：明确指定允许的来源
@Configuration
public class CorsConfig {
    @Bean
    public CorsFilter corsFilter() {
        CorsConfiguration config = new CorsConfiguration();
        config.addAllowedOrigin("https://trusted-domain.com");
        config.setAllowCredentials(true);
        config.addAllowedHeader("*");
        config.addAllowedMethod("GET");
        config.setMaxAge(3600L);
        // ...
    }
}
```

### 3. 敏感信息日志泄露

```java
// ❌ 危险：记录敏感信息
log.info("User login: username={}, password={}", username, password);

// ✅ 安全：脱敏处理
log.info("User login: username={}, password=****", username);
```

## 快速决策树

**您正在解决什么安全问题？**

1. **SQL 注入** → 使用 MyBatis-Plus 条件构造器，禁止字符串拼接
2. **XSS** → 输入验证 + 输出编码 + CSP 头
3. **CSRF** → Spring Security `@CsrfToken`
4. **会话管理** → Spring Session + Redis
5. **Dubbo 服务安全** → Token 验证 Filter + 权限控制
6. **支付回调安全** → 签名验证 + 幂等处理
7. **配置安全** → Jasypt 加密 + 环境隔离
8. **日志安全** → 脱敏处理 + 集中式日志

## 参考资料

- [OWASP Top 10 2025 详细参考](references/owasp-top-10-2025.md) - 完整的缓解措施和示例
- [CWE Top 25 参考](references/cwe-top-25.md) - 最危险的软件弱点

## 相关技能

| 技能 | 关系 |
|-------|-------------|
| `dtg-springboot-project-setup` | Spring Boot 项目配置和最佳实践 |
| `dtg-payment-core-development` | 支付核心模块开发 |
| `dtg-intelligent-architecture-analysis` | 智能架构分析 |
| `dtg-admin-panel-development` | 管理后台开发 |

## 版本历史

- v3.0.0 (2025-12-31): 专注 Spring Boot 2.7 + Dubbo 3 微服务代码审查，替换 C# 示例为 Java
- v1.0.0 (2025-12-26): 初始版本，通用安全编码指南

---

**最后更新**：2025-12-31 | **适用技术栈**：Spring Boot 2.7.18 + Dubbo 3.2.14
