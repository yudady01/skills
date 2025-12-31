---
name: dtg-code-review
description: 智能化代码审查技能，提供 OWASP Top 10 安全检查、企业级编码规范验证、架构质量评估和自动化问题识别。集成静态代码分析、安全漏洞扫描和代码质量度量功能。
allowed-tools: Read, Glob, Grep, Task
tags:
  - code-review
  - security
  - quality
  - static-analysis
---

# DTG 代码审查

编写安全代码的综合指南，涵盖 OWASP Top 10 2025、CWE Top 25 以及特定语言的安全模式。

## 何时使用此技能

在以下情况下使用此技能：

- 审查代码的安全漏洞
- 实现输入验证或输出编码
- 了解常见安全弱点（OWASP、CWE）
- 修复已识别的安全问题
- 编写安全敏感代码（身份验证、授权、数据处理）
- 进行安全代码审查

## OWASP Top 10 2025 快速参考

| 排名 | 漏洞 | 关键缓解措施 |
|------|--------------|----------------|
| A01 | 访问控制失效 | 服务器端访问检查、默认拒绝策略、CORS 限制 |
| A02 | 安全配置错误 | 硬化配置、移除默认值、禁用不必要的功能 |
| A03 | 软件供应链故障 | SCA、SBOM、验证依赖项、完整性检查 |
| A04 | 加密失败 | 强加密（AES-256）、TLS 1.2+、禁用已弃用的算法 |
| A05 | 注入 | 参数化查询、输入验证、上下文感知编码 |
| A06 | 不安全设计 | 威胁建模、安全设计模式、纵深防御 |
| A07 | 身份验证失败 | MFA、强密码、安全会话管理 |
| A08 | 数据完整性失败 | 数字签名、完整性验证、安全 CI/CD |
| A09 | 日志和警报失败 | 集中式日志记录、异常检测、审计跟踪 |
| A10 | 异常处理不当 | 安全失败、通用错误消息、完整的异常处理 |

**详细缓解措施**：参见 [OWASP Top 10 2025 参考](references/owasp-top-10-2025.md)

## 核心安全编码原则

### 1. 输入验证

**永远不要信任用户输入。** 在服务器端验证所有输入。

```csharp
using System.Text.RegularExpressions;

// 好：使用允许列表的服务器端验证
public static partial class InputValidation
{
    [GeneratedRegex(@"^[a-zA-Z0-9_]{3,20}$")]
    private static partial Regex UsernamePattern();

    /// <summary>
    /// 根据允许列表模式验证用户名。
    /// </summary>
    public static bool ValidateUsername(string username) =>
        !string.IsNullOrEmpty(username) && UsernamePattern().IsMatch(username);
}

// 坏：无验证
public string ProcessUsername(string username) => username;  // 危险！
```

**验证策略**：

- **允许列表验证**：定义允许的内容（推荐）
- **阻止列表验证**：定义不允许的内容（安全性较低）
- **类型检查**：确保正确的数据类型
- **范围检查**：验证值在预期范围内
- **长度限制**：防止缓冲区溢出和 DoS

### 2. 输出编码

根据上下文对输出进行编码以防止注入攻击。

| 上下文 | 编码方法 | 示例 |
|---------|----------------|---------|
| HTML 正文 | HTML 实体编码 | `&lt;script&gt;` |
| HTML 属性 | 属性编码 | `&#x27;` 用于 `'` |
| JavaScript | JavaScript 编码 | `\\x3Cscript\\x3E` |
| URL 参数 | URL 编码 | `%3Cscript%3E` |
| CSS | CSS 编码 | `\\3C script\\3E` |
| SQL | 参数化查询 | 使用预处理语句 |

### 3. 参数化查询（注入预防）

**始终对数据库操作使用参数化查询。**

```csharp
// 好：使用 SqlCommand 的参数化查询
using var cmd = new SqlCommand(
    "SELECT * FROM Users WHERE Username = @username AND Status = @status",
    connection);
cmd.Parameters.AddWithValue("@username", username);
cmd.Parameters.AddWithValue("@status", status);

// 好：使用 Dapper 的参数化查询
var users = await connection.QueryAsync<User>(
    "SELECT * FROM Users WHERE Username = @Username AND Status = @Status",
    new { Username = username, Status = status });

// 坏：字符串插值（SQL 注入漏洞）
var query = $"SELECT * FROM Users WHERE Username = '{username}'";  // 易受攻击
```

### 4. 身份验证安全

- **使用强密码哈希**：Argon2id、bcrypt、scrypt（参见 `cryptography` 技能）
- **实施 MFA**：基于时间的 OTP、硬件密钥、通行密钥
- **安全会话管理**：HttpOnly Cookie、安全标志、短过期时间
- **账户锁定**：防止暴力攻击
- **凭据存储**：永远不要存储明文密码

### 5. 授权安全

- **默认拒绝**：需要显式权限授予
- **服务器端检查**：永远不要依赖客户端授权
- **验证对象所有权**：检查用户可以访问请求的资源
- **使用间接引用**：将内部 ID 映射到用户特定的引用
- **实施 RBAC/ABAC**：使用结构化访问控制模型

### 6. 错误处理

```csharp
// 好：向用户返回通用错误消息，详细记录日志
public async Task<IActionResult> ProcessData([FromBody] DataRequest request)
{
    try
    {
        await _dataService.ProcessSensitiveDataAsync(request.Data);
        return Ok();
    }
    catch (DbException ex)
    {
        _logger.LogError(ex, "Database error processing request for user {UserId}", User.GetUserId());
        return StatusCode(500, new { error = "An error occurred" });
    }
}

// 坏：暴露内部细节
catch (DbException ex)
{
    return StatusCode(500, new { error = ex.Message });  // 易受攻击 - 暴露内部信息
}
```

**错误处理规则**：

- 向用户返回通用错误消息
- 在服务器端记录详细错误
- 永远不要暴露堆栈跟踪、数据库错误或内部路径
- 安全失败（错误时拒绝访问）

## 特定语言的模式

### JavaScript/TypeScript

```typescript
// XSS 预防 - 使用 textContent，而不是 innerHTML
element.textContent = userInput;  // 安全
element.innerHTML = userInput;    // 易受攻击

// 对于必须渲染的 HTML，使用 DOMPurify
import DOMPurify from 'dompurify';
element.innerHTML = DOMPurify.sanitize(userInput);

// 避免使用 eval() 和 Function()
eval(userInput);           // 易受攻击
new Function(userInput)(); // 易受攻击

// 使用严格模式
'use strict';
```

### C# / .NET

```csharp
// 安全进程执行 - 使用参数列表，避免 shell
using System.Diagnostics;

public static async Task<string> SafeExecuteAsync(string command, params string[] args)
{
    using var process = new Process
    {
        StartInfo = new ProcessStartInfo
        {
            FileName = command,
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,  // 安全：无 shell 解释
            CreateNoWindow = true
        }
    };

    foreach (var arg in args)
        process.StartInfo.ArgumentList.Add(arg);  // 安全：无需 shell 转义

    process.Start();
    var output = await process.StandardOutput.ReadToEndAsync();
    await process.WaitForExitAsync();
    return output;
}

// 坏：Shell 注入漏洞
Process.Start("cmd", $"/c dir {userInput}");  // 易受攻击

// 安全文件操作 - 防止路径遍历
public static class SafeFileAccess
{
    /// <summary>
    /// 安全读取文件，防止路径遍历攻击。
    /// </summary>
    public static string SafeReadFile(string baseDir, string filename)
    {
        var basePath = Path.GetFullPath(baseDir);
        var filePath = Path.GetFullPath(Path.Combine(baseDir, filename));

        if (!filePath.StartsWith(basePath, StringComparison.OrdinalIgnoreCase))
            throw new UnauthorizedAccessException("Path traversal detected");

        return File.ReadAllText(filePath);
    }
}

// 使用 Entity Framework 的参数化查询
var users = context.Users
    .Where(u => u.Username == username)  // 安全 - 参数化
    .ToList();

// 尽可能避免原始 SQL，需要时使用参数
var users = context.Users
    .FromSqlRaw("SELECT * FROM Users WHERE Username = {0}", username)
    .ToList();

// 用于 CSRF 保护防伪令牌
[ValidateAntiForgeryToken]
public IActionResult UpdateProfile(ProfileModel model)
{
    // 处理更新
}

// 使用数据注释的输入验证
public sealed class UserInput
{
    [Required]
    [StringLength(100, MinimumLength = 3)]
    [RegularExpression(@"^[a-zA-Z0-9_]+$")]
    public required string Username { get; init; }
}
```

## 安全代码审查清单

### 输入处理

- [ ] 在服务器端验证所有输入
- [ ] 尽可能使用允许列表验证
- [ ] 执行长度限制
- [ ] 执行类型检查
- [ ] 验证文件上传（类型、大小、内容）

### 输出编码

- [ ] 应用上下文适当的编码
- [ ] HTML/JS/SQL 中没有原始用户输入
- [ ] Content-Type 头设置正确
- [ ] X-Content-Type-Options: nosniff

### 身份验证

- [ ] 强密码哈希（Argon2id/bcrypt）
- [ ] 会话令牌随机且不可预测
- [ ] 登出时使会话无效
- [ ] 失败尝试后账户锁定
- [ ] 凭据仅通过 HTTPS 传输

### 授权

- [ ] 每个请求都有访问控制
- [ ] 默认拒绝策略
- [ ] 对象级授权检查
- [ ] 不暴露直接对象引用

### 数据保护

- [ ] 敏感数据静态加密
- [ ] 传输中的数据使用 TLS 1.2+
- [ ] URL 或日志中没有敏感数据
- [ ] 正确的密钥管理

### 错误处理

- [ ] 向用户返回通用错误消息
- [ ] 安全记录详细错误
- [ ] 不暴露堆栈跟踪
- [ ] 安全失败（错误时拒绝）

## 快速决策树

**您正在解决什么安全问题？**

1. **SQL/NoSQL 注入** → 使用参数化查询、ORM
2. **XSS（跨站脚本）** → 上下文感知输出编码、CSP
3. **CSRF** → 防伪令牌、SameSite Cookie
4. **身份验证** → 参见 `authentication-patterns` 技能
5. **授权** → 参见 `authorization-models` 技能
6. **加密** → 参见 `cryptography` 技能
7. **密钥/凭据** → 参见 `secrets-management` 技能
8. **API 安全** → 参见 `api-security` 技能

## 参考资料

- [OWASP Top 10 2025 详细参考](references/owasp-top-10-2025.md) - 完整的缓解措施和示例
- [CWE Top 25 参考](references/cwe-top-25.md) - 最危险的软件弱点
- [特定语言的模式](references/language-specific/) - 每种语言的安全指南

## 相关技能

| 技能 | 关系 |
|-------|-------------|
| `authentication-patterns` | 身份验证实现细节（JWT、OAuth、Passkeys） |
| `authorization-models` | 访问控制（RBAC、ABAC） |
| `cryptography` | 加密、哈希、TLS |
| `api-security` | 特定于 API 的安全模式 |
| `secrets-management` | 凭据和密钥处理 |

## 版本历史

- v1.0.0 (2025-12-26): 初始版本，包含 OWASP Top 10 2025、核心原则

---

**最后更新**：2025-12-26
