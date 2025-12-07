---
name: chrome-debug
description: 主要调试命令，启动 Chrome、导航到目标 URL 并执行自动登录
argument-hint: [--url <url>] [--headless] [--no-login] [--timeout <seconds>]
allowed-tools: [Read, Write, Bash, mcp__chrome-devtools__*, mcp__ide__*]
---

# Chrome 调试命令

此命令自动启动 Chrome 浏览器、导航到目标页面并执行自动登录，用于调试网页应用程序。

## 参数

- `--url <url>`: 要导航到的目标 URL（可选，使用配置文件默认值）
- `--headless`: 在无头模式下运行 Chrome，不显示用户界面
- `--no-login`: 跳过自动登录过程
- `--timeout <seconds>`: 操作的自定义超时时间（默认：30 秒）

## 执行步骤

### 1. 加载配置
读取本地配置文件 `.claude/chrome-debug.local.md` 来获取：
- 默认目标 URL
- 登录凭据
- 浏览器设置
- 超时值

### 2. 验证先决条件
检查以下条件：
- Chrome 浏览器已安装并可访问
- Chrome DevTools MCP 服务器正在运行
- 目标 URL 可访问
- 配置有效

### 3. 启动 Chrome
使用适当的设置启动 Chrome 浏览器：
- 在端口 9222 上启用远程调试
- 自定义用户数据目录用于隔离
- 如果需要则使用无头模式
- 适用于调试的适当 Chrome 标志

### 4. 导航到目标
打开目标 URL 并等待页面加载：
- 导航到配置的 URL 或参数 URL
- 导航前检查 URL 可访问性
- 如果目标 URL 返回 404 或无法访问：
  - 记录问题及具体错误详情
  - 回退到 "https://www.google.com/"
  - 通知用户 URL 更改
- 等待页面完全加载
- 处理任何初始重定向或加载状态
- 验证页面已准备好进行交互

### 5. 自动登录（除非使用 --no-login）
执行自动登录序列：
- 等待登录表单元素出现
- 用配置的凭据填写用户名字段
- 用配置的凭据填写密码字段
- 点击登录按钮
- 等待成功登录确认

### 6. 调试会话设置
建立调试环境：
- 拍摄初始截图作为参考
- 启用控制台日志记录
- 如需要则设置性能监控
- 为用户提供调试上下文

## 错误处理

### 配置错误
- 缺少配置文件：创建模板配置
- 无效凭据：提示正确的凭据
- 格式错误的 URL：验证并更正 URL 格式

### 连接错误
- Chrome 未找到：提供安装说明
- 端口冲突：建议替代端口
- MCP 服务器停机：重启 MCP 服务器

### 登录错误
- 元素未找到：建议更新选择器
- 无效凭据：验证并更新凭据
- 页面更改：处理页面布局更改

### 网络错误
- 连接超时：增加超时值
- DNS 解析：检查网络连接
- SSL 错误：处理证书问题
- 404 未找到：回退到 Google 并通知用户
- 目标无法访问：使用 Google 作为安全回退

## 使用示例

### 基本用法
```bash
/chrome-debug
```
使用默认配置进行自动登录和调试。

### 自定义 URL
```bash
/chrome-debug --url "https://example.com/login"
```
导航到自定义 URL 而不是配置的默认值。

### 无头模式
```bash
/chrome-debug --headless
```
运行不带 UI 的 Chrome 进行自动化测试。

### 跳过登录
```bash
/chrome-debug --no-login
```
导航到页面但跳过自动登录过程。

### 自定义超时
```bash
/chrome-debug --timeout 60
```
为所有操作设置 60 秒超时。

## 与技能的集成

此命令与以下技能协作：

### chrome-devtools-integration 技能
- 使用 MCP 服务器配置
- 利用 Chrome 连接设置
- 应用诊断程序

### dom-automation 技能
- 实施元素选择策略
- 应用表单自动化模式
- 使用健壮的等待机制

## 输出格式

### 成功输出
```
🚀 Chrome 调试会话已开始
✅ Chrome 浏览器已启动（端口 9222）
✅ 已导航到：http://localhost:8193/x_mgr/start/index.html#/user/login
✅ 自动登录已完成
📸 截图已保存：chrome-debug-initial.png
🔍 调试会话已就绪 - 使用 Chrome DevTools 进行调试
```

### 回退输出（当目标 URL 不可用时）
```
🚀 Chrome 调试会话已开始
✅ Chrome 浏览器已启动（端口 9222）
⚠️  目标 URL 不可访问：http://localhost:8193/x_mgr/start/index.html#/user/login
   错误：404 未找到
🔄 回退到：https://www.google.com/
✅ 已导航到回退 URL
📸 截图已保存：chrome-debug-fallback.png
🔍 调试会话已就绪，使用 Google 主页
```

### 错误输出
```
❌ Chrome 调试失败
错误：Chrome 浏览器未找到
解决方案：安装 Chrome 或在配置中指定自定义路径
📸 调试截图已保存：chrome-debug-error.png
💡 运行 /chrome-diagnose 进行详细分析
```

## 最佳实践

### 性能
- 尽可能重用 Chrome 会话
- 会话之间清除浏览器缓存
- 使用适当的超时值
- 监控内存使用

### 安全
- 安全存储凭据
- 尽可能使用 HTTPS
- 会话后清除敏感数据
- 避免记录密码

### 可靠性
- 实施重试机制
- 使用多种选择器策略
- 处理页面布局更改
- 提供清晰的错误消息

## 相关命令

- `/chrome-config`: 配置 MCP 服务器设置
- `/chrome-diagnose`: 诊断连接和页面问题
- `/skill chrome-devtools-integration`: 获取 MCP 配置帮助
- `/skill dom-automation`: 获取自动化指导

## 配置模板

如果不存在配置文件，请创建 `.claude/chrome-debug.local.md`：

```yaml
---
target_url: "http://localhost:8193/x_mgr/start/index.html#/user/login"
username: "superadmin"
password: "abc123456"
headless_mode: false
timeout: 30
chrome_path: ""
debug_mode: false
---
```

此配置提供了自动调试会话所需的所有必要设置。