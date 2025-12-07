---
name: chrome-devtools-integration
description: 当用户要求"配置 Chrome DevTools MCP"、"设置 chrome 调试"、"修复 chrome 连接问题"、"安装 chrome devtools"或提及 Chrome DevTools MCP 服务器配置时使用此技能。提供 Chrome DevTools 模型上下文协议集成的全面指导。
version: 1.0.0
---

# Chrome DevTools 集成技能

此技能提供将 Chrome DevTools MCP（模型上下文协议）与 Claude Code 集成的全面指导，实现强大的浏览器自动化和调试功能。

## 核心概念

Chrome DevTools MCP 是一个模型上下文协议服务器，允许 AI 代理控制和检查实时 Chrome 浏览器。它通过标准化接口提供对 Chrome 强大调试功能的程序化访问。

### 关键能力

- **性能分析**：记录和分析浏览器性能轨迹
- **网络监控**：检查 HTTP 请求、响应和时间
- **控制台管理**：执行 JavaScript 并捕获控制台输出
- **可视化调试**：截图和页面快照
- **DOM 操作**：检查和修改页面元素
- **自动化**：点击、输入、导航和等待元素

## MCP 服务器配置

### 标准安装

全局安装 Chrome DevTools MCP：

```bash
npm install -g chrome-devtools-mcp@latest
```

### Claude Code 集成

在 `.mcp.json` 中配置 MCP 服务器：

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"],
      "env": {
        "CHROME_PATH": "${CHROME_PATH:-}",
        "HEADLESS": "${HEADLESS:-false}"
      }
    }
  }
}
```

### 环境变量

设置这些环境变量以自定义行为：

- `CHROME_PATH`：自定义 Chrome 可执行文件路径
- `HEADLESS`：在无头模式下运行 Chrome（true/false）
- `DEBUG_TIMEOUT`：操作默认超时时间（秒）

## 先决条件和设置

### 系统要求

- **Node.js**：v20.19 或更高版本
- **Chrome**：稳定版本或更新版本
- **npm**：用于包管理

### Chrome 安装验证

验证 Chrome 安装和版本：

```bash
# 检查 Chrome 版本
google-chrome --version  # Linux
chrome --version        # macOS

# 验证 Chrome 接受远程调试
chrome --remote-debugging-port=9222 --no-sandbox
```

### 网络和端口配置

Chrome DevTools MCP 使用这些默认配置：

- **调试端口**：9222（默认）
- **WebSocket**：用于实时通信
- **HTTP 端点**：用于 DevTools 协议访问

## 连接和故障排除

### 常见连接问题

#### Chrome 无响应
```
Error: Failed to connect to Chrome DevTools Protocol
```

**解决方案：**
1. 验证 Chrome 正在运行并启用了远程调试
2. 检查端口 9222 是否可用
3. 确保 Chrome 版本兼容

#### MCP 服务器启动失败
```
Error: chrome-devtools-mcp package not found
```

**解决方案：**
1. 运行 `npm install -g chrome-devtools-mcp@latest`
2. 检查 Node.js 版本兼容性
3. 验证 npm 注册表访问

### 诊断命令

使用验证脚本诊断问题：

```bash
# 运行全面诊断
python3 ./plugins/chrome-debug/skills/chrome-devtools-integration/scripts/setup-mcp.py

# 快速验证检查
./plugins/chrome-debug/scripts/validate-chrome.sh
```

## 性能分析设置

### 轨迹记录

开始性能轨迹记录：

```bash
# 开始轨迹收集
mcp call performance_start_trace

# 执行用户交互
# ... 用户执行操作 ...

# 停止并分析轨迹
mcp call performance_stop_trace
mcp call performance_analyze_insight
```

### 性能指标

Chrome DevTools MCP 提供这些性能指标：

- **加载指标**：首次内容绘制、最大内容绘制
- **运行时指标**：JavaScript 执行时间、内存使用
- **网络指标**：请求时间、响应大小
- **渲染指标**：帧率、布局偏移

## 安全考虑

### 远程调试安全

Chrome 的远程调试暴露了强大功能：

1. **网络暴露**：远程调试端口应设置防火墙
2. **代码执行**：可能执行任意 JavaScript
3. **数据访问**：可访问完整的页面内容和 Cookie

### 最佳实践

- 仅使用本地连接（localhost）
- 在生产环境中禁用远程调试
- 为远程访问实施身份验证
- 定期进行 Chrome 安全更新

## 集成模式

### 自动化测试工作流

```python
# 示例：自动化登录测试
async def test_login_flow(mcp_client):
    # 导航到登录页面
    await mcp_client.call("navigate", {"url": "http://localhost:8193/login"})

    # 等待页面加载
    await mcp_client.call("wait_for_load")

    # 填写凭据
    await mcp_client.call("type", {"selector": "#username", "text": "superadmin"})
    await mcp_client.call("type", {"selector": "#password", "text": "abc123456"})

    # 提交表单
    await mcp_client.call("click", {"selector": "#login-button"})

    # 验证成功
    await mcp_client.call("wait_for_selector", {"selector": ".dashboard"})
    screenshot = await mcp_client.call("take_screenshot")
    return screenshot
```

### 性能监控

```python
# 示例：性能监控设置
async def setup_performance_monitoring(mcp_client):
    # 开始性能轨迹
    await mcp_client.call("performance_start_trace")

    # 监控网络请求
    await mcp_client.call("list_network_requests")

    # 设置控制台日志记录
    await mcp_client.call("list_console_messages")
```

## 错误处理和恢复

### 常见错误场景

#### Chrome 崩溃
```javascript
// 重启 Chrome 并恢复会话
{
  "action": "restart_chrome",
  "restore_session": true,
  "timeout": 30000
}
```

#### 页面加载失败
```javascript
// 处理页面加载超时
{
  "action": "handle_load_timeout",
  "retry_count": 3,
  "fallback_url": "about:blank"
}
```

#### 元素未找到
```javascript
// 健壮的元素选择
{
  "action": "wait_for_element",
  "selectors": ["#primary-id", ".fallback-class", "[data-testid]"],
  "timeout": 10000
}
```

## 高级配置

### 自定义 Chrome 标志

使用特定标志配置 Chrome 进行调试：

```bash
chrome \
  --remote-debugging-port=9222 \
  --no-sandbox \
  --disable-dev-shm-usage \
  --disable-gpu \
  --user-data-dir=/tmp/chrome-debug
```

### 多实例管理

运行多个 Chrome 实例进行并行调试：

```json
{
  "chrome-devtools-1": {
    "command": "npx",
    "args": ["-y", "chrome-devtools-mcp@latest"],
    "env": {
      "CHROME_PORT": "9222"
    }
  },
  "chrome-devtools-2": {
    "command": "npx",
    "args": ["-y", "chrome-devtools-mcp@latest"],
    "env": {
      "CHROME_PORT": "9223"
    }
  }
}
```

## 其他资源

### 参考文件

详细技术规范和故障排除指南：
- **`references/api-reference.md`** - 完整的 MCP API 文档
- **`references/troubleshooting.md`** - 常见问题和解决方案
- **`references/performance-patterns.md`** - 性能分析模式

### 示例脚本

`examples/` 中的工作自动化示例：
- **`examples/login-automation.js`** - 完整的登录流程自动化
- **`examples/performance-analysis.js`** - 性能监控设置
- **`examples/network-monitoring.js`** - 网络请求分析

### 实用脚本

`scripts/` 中的辅助脚本：
- **`scripts/setup-mcp.py`** - 自动化 MCP 服务器设置
- **`scripts/validate-chrome.sh`** - Chrome 安装验证
- **`scripts/diagnose-mcp.py`** - 全面诊断工具

## 最佳实践

### 开发工作流

1. **启动 Chrome**：启用远程调试启动
2. **连接 MCP**：验证 MCP 服务器连接
3. **导航**：加载目标应用程序
4. **调试**：使用 DevTools 功能进行分析
5. **自动化**：实施可重复的测试模式
6. **监控**：持续跟踪性能和错误

### 代码组织

- 将配置与自动化逻辑分离
- 使用描述性的选择器策略
- 实施健壮的错误处理
- 记录操作用于调试和审计跟踪
- 每次会话后清理资源