# OWASP Top 10 2025 详细参考

本参考文档为每个 OWASP Top 10 2025 漏洞类别提供详细的缓解措施和示例。

## A01:2025 - 访问控制失效

**描述**：访问控制强制执行策略，使用户无法超出其预期权限进行操作。失败通常导致未经授权的信息泄露、修改或数据销毁。

### 常见漏洞

- 通过修改 URL、应用状态或 HTML 页面绕过访问控制检查
- 不安全的直接对象引用（IDOR）
- API 端点缺少访问控制
- CORS 配置错误导致未经授权的 API 访问
- 权限提升（未经授权充当管理员）
- 服务器端请求伪造（SSRF）- 现已包含在此类别中

### 缓解策略

```csharp
// 好：服务器端访问控制检查
public async Task<Document> GetDocumentAsync(string documentId, ClaimsPrincipal user)
{
    var document = await _context.Documents.FindAsync(documentId)
        ?? throw new NotFoundException("Document not found");

    var userId = user.FindFirstValue(ClaimTypes.NameIdentifier);

    // 返回前验证所有权
    if (document.OwnerId != userId && !user.IsInRole("Admin"))
        throw new ForbiddenException("Access denied");

    return document;
}

// 坏：无授权检查
public async Task<Document> GetDocumentAsync(string documentId)
{
    return await _context.Documents.FindAsync(documentId);  // 易受攻击
}
```

**关键控制**：

- 实施默认拒绝的服务器端访问控制
- 使用速率限制防止自动化攻击
- 记录并警告访问控制失败
- 登出时使会话无效
- 在适当场合使用间接对象引用

### SSRF 预防

```csharp
using System.Net;

// 好：验证并限制 URL
public sealed class SsrfProtectedHttpClient(HttpClient httpClient)
{
    private static readonly HashSet<string> AllowedHosts = ["api.example.com", "cdn.example.com"];

    public async Task<HttpResponseMessage> FetchUrlAsync(string url, CancellationToken ct = default)
    {
        if (!Uri.TryCreate(url, UriKind.Absolute, out var uri))
            throw new ArgumentException("Invalid URL format");

        // 对照允许列表检查
        if (!AllowedHosts.Contains(uri.Host))
            throw new SecurityException("URL not in allowlist");

        // 阻止内部 IP
        if (IPAddress.TryParse(uri.Host, out var ip))
        {
            if (IsPrivateOrLoopback(ip))
                throw new SecurityException("Internal addresses not allowed");
        }
        else
        {
            // 解析主机名并检查 IP
            var addresses = await Dns.GetHostAddressesAsync(uri.Host, ct);
            if (addresses.Any(IsPrivateOrLoopback))
                throw new SecurityException("Hostname resolves to internal address");
        }

        return await httpClient.GetAsync(uri, ct);
    }

    private static bool IsPrivateOrLoopback(IPAddress ip) =>
        IPAddress.IsLoopback(ip) ||
        ip.ToString().StartsWith("10.") ||
        ip.ToString().StartsWith("192.168.") ||
        ip.ToString().StartsWith("172.16.");
}
```

---

## A02:2025 - 安全配置错误

**描述**：安全配置错误是最常见的问题，通常由不安全的默认配置、不完整的配置或临时配置导致。

### 常见漏洞

- 默认凭据未更改
- 启用了不必要的功能（端口、服务、页面、账户）
- 错误消息暴露敏感信息
- 缺少安全头
- 软件或安全补丁过时
- 云存储权限配置错误

### 缓解策略

```yaml
# 好：nginx 中的安全头
server {
    # 移除服务器版本
    server_tokens off;

    # 安全头
    add_header X-Content-Type-Options nosniff always;
    add_header X-Frame-Options DENY always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header Content-Security-Policy "default-src 'self'" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
    add_header Permissions-Policy "geolocation=(), microphone=(), camera=()" always;
}
```

**关键控制**：

- 实施可重复的加固流程
- 使用没有不必要功能的最小平台
- 定期审查和更新配置
- 实施自动化安全配置验证

---

## A03:2025 - 软件供应链故障

**描述**：与不受信任的依赖项、受损的 CI/CD 管道或软件组件验证不足相关的漏洞。

### 常见漏洞

- 使用已知漏洞的组件
- 依赖混淆攻击
- 包管理器中的域名欺骗
- 受损的 CI/CD 管道
- 未签名或未验证的更新

### 缓解策略

```json
// package.json - 使用锁定文件并验证完整性
{
  "dependencies": {
    "express": "4.18.2"
  },
  "scripts": {
    "audit": "npm audit --audit-level=high",
    "check-deps": "npm-check-updates"
  }
}
```

**关键控制**：

- 生成并维护 SBOM（软件物料清单）
- 使用软件成分分析（SCA）工具
- 使用校验和验证包完整性
- 在 CI/CD 中实施依赖审查
- 将依赖项固定到特定版本
- 对内部包使用私有包注册表

参见 `supply-chain-security` 技能以获取全面指导。

---

## A04:2025 - 加密失败

**描述**：与加密相关的失败，通常导致敏感数据暴露。

### 常见漏洞

- 明文传输数据（HTTP、SMTP、FTP）
- 旧或弱的加密算法（MD5、SHA1、DES）
- 默认或弱加密密钥
- 证书验证不当
- 静态敏感数据缺少加密

### 缓解策略

```csharp
using System.Security.Cryptography;

/// <summary>
/// 使用 PBKDF2 从密码派生加密密钥。
/// </summary>
public static byte[] DeriveKey(string password, byte[] salt, int keyLength = 32)
{
    using var pbkdf2 = new Rfc2898DeriveBytes(
        password,
        salt,
        iterations: 600000,  // OWASP 2023 推荐
        HashAlgorithmName.SHA256);

    return pbkdf2.GetBytes(keyLength);
}

/// <summary>
/// 使用密码派生密钥和 AES-GCM 加密数据。
/// </summary>
public static (byte[] Ciphertext, byte[] Salt, byte[] Nonce, byte[] Tag) EncryptData(
    byte[] data, string password)
{
    var salt = RandomNumberGenerator.GetBytes(16);
    var key = DeriveKey(password, salt);
    var nonce = RandomNumberGenerator.GetBytes(12);
    var tag = new byte[16];
    var ciphertext = new byte[data.Length];

    using var aes = new AesGcm(key, tagSizeInBytes: 16);
    aes.Encrypt(nonce, data, ciphertext, tag);

    CryptographicOperations.ZeroMemory(key);  // 清理密钥
    return (ciphertext, salt, nonce, tag);
}
```

**关键控制**：

- 对所有传输中的数据使用 TLS 1.2+
- 使用 AES-256 加密静态敏感数据
- 使用强密钥派生（Argon2id、PBKDF2）
- 实施正确的密钥管理和轮换
- 禁用已弃用的协议和密码

参见 `cryptography` 技能以获取全面指导。

---

## A05:2025 - 注入

**描述**：当不受信任的数据作为命令或查询的一部分发送给解释器时，会发生注入漏洞。

### 常见漏洞

- SQL 注入
- NoSQL 注入
- OS 命令注入
- LDAP 注入
- XPath 注入
- 跨站脚本（XSS）

### 缓解策略

```java
// 好：参数化查询
String query = "SELECT * FROM users WHERE username = ? AND password = ?";
PreparedStatement stmt = connection.prepareStatement(query);
stmt.setString(1, username);
stmt.setString(2, hashedPassword);
ResultSet rs = stmt.executeQuery();

// 坏：字符串拼接
String query = "SELECT * FROM users WHERE username = '" + username + "'";  // 易受攻击
```

**关键控制**：

- 使用参数化查询或预处理语句
- 使用带参数化查询的 ORM
- 实施严格的输入验证
- 根据上下文转义特殊字符
- 使用内容安全策略（CSP）预防 XSS

---

## A06:2025 - 不安全设计

**描述**：与设计和架构缺陷相关的风险，需要更多使用威胁建模、安全设计模式和参考架构。

### 常见漏洞

- 设计中缺少安全控制
- 缺少威胁建模
- 速率限制不足
- 缺少业务逻辑验证
- 关注点分离不充分

### 缓解策略

- 建立安全开发生命周期
- 使用威胁建模（STRIDE、DREAD）
- 尽早实施安全要求
- 使用安全设计模式
- 记录并审查安全假设

参见 `threat-modeling` 技能以获取全面指导。

---

## A07:2025 - 身份验证失败

**描述**：确认用户身份、身份验证和会话管理对于防范身份验证相关攻击至关重要。

### 常见漏洞

- 允许弱密码
- 缺少暴力破解防护
- 凭据填充漏洞
- 会话固定
- 缺少 MFA
- URL 中暴露会话 ID

### 缓解策略

```csharp
// 好：速率限制与账户锁定
public sealed class AuthenticationService(AppDbContext context, IPasswordHasher passwordHasher)
{
    private const int MaxAttempts = 5;
    private static readonly TimeSpan LockoutDuration = TimeSpan.FromMinutes(15);

    public async Task<User> AuthenticateAsync(string username, string password, CancellationToken ct)
    {
        var user = await context.Users.FirstOrDefaultAsync(u => u.Username == username, ct);

        if (user?.LockedUntil > DateTime.UtcNow)
            throw new AccountLockedException("Account temporarily locked");

        if (user is null || !passwordHasher.Verify(password, user.PasswordHash))
        {
            if (user is not null)
            {
                user.FailedAttempts++;
                if (user.FailedAttempts >= MaxAttempts)
                    user.LockedUntil = DateTime.UtcNow + LockoutDuration;
                await context.SaveChangesAsync(ct);
            }
            throw new InvalidCredentialsException("Invalid username or password");
        }

        user.FailedAttempts = 0;
        user.LockedUntil = null;
        await context.SaveChangesAsync(ct);
        return user;
    }
}
```

**关键控制**：

- 为所有用户实施 MFA
- 使用安全的密码哈希（Argon2id、bcrypt）
- 实施账户锁定
- 生成随机、不可预测的会话令牌
- 在登出时正确使会话无效

参见 `authentication-patterns` 技能以获取全面指导。

---

## A08:2025 - 数据完整性失败

**描述**：不防范完整性违规的代码和基础设施，例如使用不受信任的源作为插件、库或模块。

### 常见漏洞

- 不安全的反序列化
- CI/CD 管道完整性问题
- 未经签名验证的自动更新
- 数据完整性未验证

### 缓解策略

```csharp
using System.Security.Cryptography;

/// <summary>
/// 使用 HMAC 验证更新完整性。
/// </summary>
public static bool VerifyUpdate(byte[] updateData, string signature, byte[] secretKey)
{
    using var hmac = new HMACSHA256(secretKey);
    var computedHash = hmac.ComputeHash(updateData);
    var expectedSignature = Convert.ToHexString(computedHash).ToLowerInvariant();

    return CryptographicOperations.FixedTimeEquals(
        System.Text.Encoding.UTF8.GetBytes(expectedSignature),
        System.Text.Encoding.UTF8.GetBytes(signature));
}

public static void ApplyUpdate(byte[] updateData, string signature)
{
    if (!VerifyUpdate(updateData, signature, UpdateSecretKey))
        throw new IntegrityException("Update signature verification failed");
    // 应用更新...
}
```

**关键控制**：

- 对代码和数据使用数字签名
- 实施 CI/CD 管道安全
- 验证所有更新的完整性
- 避免不安全的反序列化

---

## A09:2025 - 日志和警报失败

**描述**：没有日志和监控，就无法检测入侵。

### 常见漏洞

- 登录、访问控制和输入验证失败未记录
- 警告和错误不生成或日志消息不足
- 日志未监控可疑活动
- 日志仅本地存储
- 警报阈值未设置或无效

### 缓解策略

```csharp
using Microsoft.Extensions.Logging;

// 配置结构化安全日志记录
public sealed class SecurityLogger(ILogger<SecurityLogger> logger)
{
    /// <summary>
    /// 以结构化格式记录安全事件。
    /// </summary>
    public void LogSecurityEvent(string eventType, string? userId, object details)
    {
        logger.LogWarning(
            "Security Event: {EventType} | User: {UserId} | Details: {@Details}",
            eventType, userId ?? "anonymous", details);
    }
}

// 记录身份验证事件
public sealed class LoggingAuthenticationService(
    ICredentialVerifier verifier,
    SecurityLogger securityLogger,
    IHttpContextAccessor httpContext)
{
    public async Task<User> AuthenticateAsync(string username, string password)
    {
        var ip = httpContext.HttpContext?.Connection.RemoteIpAddress?.ToString();
        var userAgent = httpContext.HttpContext?.Request.Headers.UserAgent.ToString();

        try
        {
            var user = await verifier.VerifyAsync(username, password);
            securityLogger.LogSecurityEvent("login_success", user.Id, new { Ip = ip });
            return user;
        }
        catch (InvalidCredentialsException)
        {
            securityLogger.LogSecurityEvent("login_failure", null, new
            {
                Username = username,
                Ip = ip,
                UserAgent = userAgent
            });
            throw;
        }
    }
}
```

**关键控制**：

- 记录身份验证和授权事件
- 实施集中式日志管理
- 为安全事件设置警报
- 保护日志完整性
- 保留日志用于事件响应

---

## A10:2025 - 异常情况处理不当

**描述**：2025 年新增。导致不可预测或不安全行为的错误和异常处理不当。

### 常见漏洞

- 失败开放而非安全失败
- 错误恢复不完整
- 异常处理不一致
- 通过错误消息泄漏信息
- 未处理异常导致的资源耗尽

### 缓解策略

```csharp
using Microsoft.Extensions.Logging;

/// <summary>
/// 处理具有安全错误处理的支付。
/// </summary>
public async Task<PaymentResult> ProcessPaymentAsync(PaymentData paymentData)
{
    try
    {
        ValidatePayment(paymentData);
        var result = await _paymentGateway.ProcessAsync(paymentData);
        return result;
    }
    catch (ValidationException ex)
    {
        _logger.LogWarning(ex, "Payment validation failed");
        throw new PaymentException("Invalid payment data");  // 通用消息
    }
    catch (TimeoutException)
    {
        _logger.LogError("Payment gateway timeout");
        throw new PaymentException("Service temporarily unavailable");
    }
    catch (Exception ex)
    {
        _logger.LogError(ex, "Unexpected payment error");
        // 安全失败 - 不处理支付
        throw new PaymentException("Payment processing failed");
    }
    finally
    {
        // 始终清理敏感数据
        paymentData.CardNumber = null;
        paymentData.Cvv = null;
    }
}
```

**关键控制**：

- 为失败场景设计
- 实施完整的错误处理
- 安全失败（错误时拒绝访问）
- 对用户使用通用错误消息
- 安全记录详细错误
- 彻底测试错误路径

---

## 总结表

| 类别 | 主要防御 | 次要防御 |
|----------|----------------|-------------------|
| A01 访问控制失效 | 服务器端访问检查 | 速率限制、日志记录 |
| A02 安全配置错误 | 加固配置 | 自动化验证 |
| A03 供应链 | SCA、SBOM | 代码签名、完整性检查 |
| A04 加密失败 | TLS 1.2+、AES-256 | 密钥管理、轮换 |
| A05 注入 | 参数化查询 | 输入验证、编码 |
| A06 不安全设计 | 威胁建模 | 安全设计模式 |
| A07 身份验证失败 | MFA、强哈希 | 账户锁定、监控 |
| A08 数据完整性 | 数字签名 | 管道安全 |
| A09 日志失败 | 集中式日志记录 | 警报、监控 |
| A10 异常处理 | 安全失败 | 完整错误处理 |
