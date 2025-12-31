# CWE Top 25 最危险的软件弱点

本参考文档涵盖 CWE（通用弱点枚举）Top 25 最危险的软件弱点，包括示例和缓解措施。

## 概述

CWE Top 25 代表最常见和最有影响力的安全弱点。了解这些弱点有助于在开发和代码审查期间确定安全工作的优先级。

## 关键弱点（Top 10）

### CWE-787: 越界写入

**描述**：写入数据超出分配内存的边界。

**受影响语言**：C、C++、汇编

```c
// 易受攻击：缓冲区溢出
char buffer[10];
strcpy(buffer, userInput);  // 无边界检查

// 安全：使用有界函数
char buffer[10];
strncpy(buffer, userInput, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';
```

**缓解措施**：使用内存安全语言或有界内存函数。

---

### CWE-79: 跨站脚本（XSS）

**描述**：网页生成期间输入的中和不当。

**受影响语言**：所有 Web 框架

```javascript
// 易受攻击：直接 DOM 插入
element.innerHTML = userInput;

// 安全：使用 textContent 或清理
element.textContent = userInput;
// 或
element.innerHTML = DOMPurify.sanitize(userInput);
```

**缓解措施**：

- 上下文感知输出编码
- 内容安全策略（CSP）
- 使用自动转义的框架

---

### CWE-89: SQL 注入

**描述**：SQL 命令中特殊元素的中和不当。

```csharp
// 易受攻击：字符串插值
var query = $"SELECT * FROM users WHERE id = {userId}";  // SQL 注入

// 安全：使用 SqlCommand 的参数化查询
using var cmd = new SqlCommand("SELECT * FROM users WHERE id = @id", connection);
cmd.Parameters.AddWithValue("@id", userId);

// 安全：使用 EF Core 的参数化查询
var user = await context.Users.FirstOrDefaultAsync(u => u.Id == userId);
```

**缓解措施**：

- 使用参数化查询
- 使用 ORM
- 输入验证
- 存储过程

---

### CWE-416: 释放后使用

**描述**：引用已释放的内存。

**受影响语言**：C、C++

```c
// 易受攻击
char *ptr = malloc(SIZE);
free(ptr);
strcpy(ptr, "data");  // 释放后使用

// 安全：释放后将指针设置为 NULL
free(ptr);
ptr = NULL;
```

**缓解措施**：使用智能指针（C++），将释放的指针设置为 NULL。

---

### CWE-78: OS 命令注入

**描述**：OS 命令中特殊元素的中和不当。

```csharp
// 易受攻击：带有用户输入的 shell 命令
Process.Start("cmd", $"/c dir {directory}");  // 命令注入

// 安全：使用 ArgumentList 的 Process（无 shell 解释）
using var process = new Process
{
    StartInfo = new ProcessStartInfo
    {
        FileName = "ls",  // 或 Windows 上的 "cmd"
        UseShellExecute = false,
        RedirectStandardOutput = true
    }
};
process.StartInfo.ArgumentList.Add(directory);  // 安全：ArgumentList 正确转义
process.Start();
```

**缓解措施**：

- 尽可能避免 shell 命令
- 使用参数化 API
- 严格的输入验证

---

### CWE-20: 输入验证不当

**描述**：未验证或错误验证输入。

```csharp
using System.Text.RegularExpressions;

// 易受攻击：无验证
public string GetFile(string filename)
{
    return File.ReadAllText($"/data/{filename}");  // 路径遍历
}

// 安全：验证和清理
public partial class FileService
{
    [GeneratedRegex(@"^[a-zA-Z0-9_-]+\.txt$")]
    private static partial Regex SafeFilenameRegex();

    public string GetFile(string filename)
    {
        if (!SafeFilenameRegex().IsMatch(filename))
            throw new ArgumentException("Invalid filename");

        var basePath = Path.GetFullPath("/data");
        var filePath = Path.GetFullPath(Path.Combine("/data", filename));

        if (!filePath.StartsWith(basePath, StringComparison.OrdinalIgnoreCase))
            throw new SecurityException("Path traversal detected");

        return File.ReadAllText(filePath);
    }
}
```

**缓解措施**：

- 在服务器端验证所有输入
- 使用允许列表验证
- 检查类型、范围、长度和格式

---

### CWE-125: 越界读取

**描述**：从分配的内存边界外读取数据。

**受影响语言**：C、C++

```c
// 易受攻击
int array[10];
int value = array[index];  // 未检查 index

// 安全
if (index >= 0 && index < 10) {
    int value = array[index];
}
```

**缓解措施**：边界检查，使用安全替代方案。

---

### CWE-22: 路径遍历

**描述**：对受限目录的路径名限制不当。

```csharp
// 易受攻击
[HttpGet("download")]
public IActionResult Download(string filename)
{
    return PhysicalFile($"/uploads/{filename}", "application/octet-stream");  // 路径遍历
}

// 安全
[HttpGet("download")]
public IActionResult Download(string filename)
{
    var basePath = Path.GetFullPath("/uploads");
    var filePath = Path.GetFullPath(Path.Combine("/uploads", filename));

    if (!filePath.StartsWith(basePath, StringComparison.OrdinalIgnoreCase))
        return Forbid();

    if (!System.IO.File.Exists(filePath))
        return NotFound();

    return PhysicalFile(filePath, "application/octet-stream");
}
```

**缓解措施**：

- 规范化路径
- 对照基本目录验证
- 移除路径遍历序列

---

### CWE-352: 跨站请求伪造（CSRF）

**描述**：强迫已认证用户执行非预期操作。

```html
<!-- 易受攻击：无 CSRF 保护 -->
<form action="/transfer" method="POST">
    <input name="amount" value="1000">
    <input name="to" value="attacker">
</form>

<!-- 安全：包含 CSRF 令牌 -->
<form action="/transfer" method="POST">
    <input name="csrf_token" value="{{ csrf_token }}">
    <input name="amount" value="1000">
    <input name="to" value="recipient">
</form>
```

**缓解措施**：

- Anti-CSRF 令牌
- SameSite Cookie 属性
- 验证 Origin/Referer 头

---

### CWE-434: 不受限制的危险文件类型上传

**描述**：允许上传服务器可以执行的文件。

```csharp
// 易受攻击：无验证
[HttpPost("upload")]
public async Task<IActionResult> Upload(IFormFile file)
{
    await using var stream = new FileStream($"/uploads/{file.FileName}", FileMode.Create);
    await file.CopyToAsync(stream);  // 危险：任意文件上传
    return Ok();
}

// 安全：验证文件类型和内容
[HttpPost("upload")]
public async Task<IActionResult> Upload(IFormFile file)
{
    HashSet<string> allowedExtensions = [".png", ".jpg", ".gif"];
    HashSet<string> allowedMimeTypes = ["image/png", "image/jpeg", "image/gif"];

    // 检查扩展名
    var ext = Path.GetExtension(file.FileName).ToLowerInvariant();
    if (!allowedExtensions.Contains(ext))
        return BadRequest("Invalid file type");

    // 检查内容类型
    if (!allowedMimeTypes.Contains(file.ContentType))
        return BadRequest("Invalid content type");

    // 检查魔术字节
    using var reader = new BinaryReader(file.OpenReadStream());
    var header = reader.ReadBytes(8);
    if (!IsValidImage(header))
        return BadRequest("Invalid file content");

    // 生成安全文件名
    var safeName = $"{Guid.NewGuid()}{ext}";
    var filePath = Path.Combine("/uploads", safeName);

    await using var stream = new FileStream(filePath, FileMode.Create);
    file.OpenReadStream().Position = 0;
    await file.CopyToAsync(stream);

    return Ok(new { FileName = safeName });
}

private static bool IsValidImage(byte[] header) =>
    header.Length >= 8 &&
    (header[..3].SequenceEqual([0xFF, 0xD8, 0xFF]) ||  // JPEG
     header[..8].SequenceEqual([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]) ||  // PNG
     header[..6].SequenceEqual("GIF89a"u8.ToArray()));  // GIF
```

**缓解措施**：

- 验证文件扩展名和 MIME 类型
- 检查文件内容/魔术字节
- 存储在 Web 根目录之外
- 重命名上传的文件

---

## 重要弱点（11-25）

### CWE-862: 缺少授权

服务器未验证用户是否有权执行操作。

### CWE-476: 空指针解引用

解引用空指针，导致崩溃。

### CWE-287: 身份验证不当

未正确验证声称的身份。

### CWE-190: 整数溢出

计算超出整数边界。

### CWE-502: 不受信任数据的反序列化

反序列化攻击者控制的数据。

### CWE-77: 命令注入

类似于 CWE-78，更广泛的命令注入范围。

### CWE-119: 缓冲区溢出

对内存边界内操作的限制不当。

### CWE-798: 硬编码凭据

将凭据嵌入源代码。

### CWE-918: 服务器端请求伪造（SSRF）

服务器向攻击者指定的 URL 发出请求。

### CWE-306: 关键功能缺少身份验证

关键功能无需身份验证即可访问。

### CWE-362: 竞争条件

检查时到使用时（TOCTOU）漏洞。

### CWE-269: 权限管理不当

未正确管理用户权限。

### CWE-94: 代码注入

注入由应用程序执行的代码。

### CWE-863: 授权不正确

授权检查存在但有缺陷。

### CWE-276: 默认权限不正确

默认权限过于宽松。

---

## 按语言快速参考

| 语言 | 高风险 CWE | 主要缓解措施 |
|----------|---------------|---------------------|
| C/C++ | CWE-787、CWE-125、CWE-416、CWE-476 | 边界检查、智能指针、ASAN |
| Java | CWE-89、CWE-79、CWE-502、CWE-78 | 预处理语句、编码、输入验证 |
| Python | CWE-89、CWE-78、CWE-22、CWE-94 | 参数化查询、subprocess 列表、路径验证 |
| JavaScript | CWE-79、CWE-94、CWE-352 | DOMPurify、CSP、CSRF 令牌 |
| C# | CWE-89、CWE-79、CWE-502、CWE-78 | EF Core、Razor 编码、输入验证 |

---

## 资源

- [CWE Top 25 官方列表](https://cwe.mitre.org/top25/)
- [MITRE CWE 数据库](https://cwe.mitre.org/)
- [OWASP Top 10 映射](https://owasp.org/www-project-top-ten/)
