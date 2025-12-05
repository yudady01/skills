# Chrome Debug Plugin

Chrome DevTools 集成插件，为 Claude Code 提供强大的 Web 应用调试、自动化操作和性能分析能力。

## 功能特性

- 🚀 **一键调试**: 自动启动 Chrome 并导航到目标页面
- 🔐 **自动登录**: 支持预设凭据的自动登录流程
- 🎯 **DOM 操作**: 强大的元素检查、选择和自动化操作
- 📊 **性能分析**: 集成 Chrome DevTools Performance API
- 📸 **截图和快照**: 页面可视化调试支持
- 🔍 **错误诊断**: 智能连接和页面访问问题分析
- 🔄 **智能回退**: 当目标 URL 不可用时自动回退到 Google

## 安装要求

- Node.js v20.19+
- Chrome 稳定版本或更新版本
- npm 包管理器

## 快速开始

### 1. 配置目标设置

创建配置文件 `.claude/chrome-debug.local.md`：

```yaml
---
target_url: "http://localhost:8193/x_mgr/start/index.html#/user/login"
username: "superadmin"
password: "abc123456"
headless_mode: false
timeout: 30
chrome_path: ""
---
```

### 2. 使用命令

```bash
# 启动调试会话（自动登录）
/chrome-debug

# 配置 MCP 服务器
/chrome-config --install

# 诊断连接问题
/chrome-diagnose --url "http://localhost:8193"
```

**注意**: 如果目标 URL 返回 404 或无法访问，插件会自动：
1. 显示错误信息
2. 回退到 https://www.google.com/
3. 继续调试会话
4. 建议更新配置文件中的正确 URL

## 命令参考

### `/chrome-debug`
主调试命令，一键启动 Chrome 并开始调试会话。

**参数**:
- `--url <url>`: 目标 URL（可选，使用配置文件中的默认值）
- `--headless`: 无头模式运行
- `--no-login`: 跳过自动登录

**示例**:
```bash
/chrome-debug
/chrome-debug --url "https://example.com" --headless
```

### `/chrome-config`
管理 Chrome DevTools MCP 服务器配置。

**参数**:
- `--install`: 安装 MCP 服务器
- `--status`: 检查服务器状态
- `--reset`: 重置配置

**示例**:
```bash
/chrome-config --install
/chrome-config --status
```

### `/chrome-diagnose`
诊断连接和页面访问问题。

**参数**:
- `--url <url>`: 要测试的 URL
- `--verbose`: 详细输出模式

**示例**:
```bash
/chrome-diagnose
/chrome-diagnose --url "http://localhost:8193" --verbose
```

## 技能使用

### Chrome DevTools 集成技能
当您询问以下问题时自动触发：
- "如何配置 Chrome DevTools MCP？"
- "Chrome 连接问题如何解决？"
- "性能分析数据如何获取？"

### DOM 自动化技能
当您需要以下操作时自动触发：
- "如何自动登录这个页面？"
- "怎样选择和操作页面元素？"
- "如何批量处理页面交互？"

## 高级配置

### 环境变量

- `CHROME_PATH`: 自定义 Chrome 可执行文件路径
- `HEADLESS`: 默认无头模式设置 (true/false)
- `DEBUG_TIMEOUT`: 操作超时时间（秒）

### 多用户配置

支持为不同项目创建不同的配置文件：

```bash
# 项目特定配置
.claude/chrome-debug.project1.local.md
.claude/chrome-debug.project2.local.md
```

## 故障排除

### 常见问题

**Q: Chrome 启动失败**
A: 检查 Chrome 安装路径，使用 `/chrome-diagnose` 获取详细诊断

**Q: MCP 服务器连接失败**
A: 运行 `/chrome-config --reset` 重置配置，确保网络连接正常

**Q: 自动登录失败**
A: 检查页面元素是否发生变化，使用 `--verbose` 模式查看详细日志

**Q: 目标 URL 返回 404 错误**
A: 插件会自动回退到 Google 首页继续调试会话。要修复：
- 检查目标服务器是否运行
- 更新 `.claude/chrome-debug.local.md` 中的 `target_url`
- 使用 `/chrome-diagnose` 检查 URL 可访问性

**Q: 为什么自动打开了 Google 而不是我的网站**
A: 这说明您的目标 URL (如 http://localhost:8193) 返回了 404 或无法访问。
插件会自动回退到 Google 确保调试会话可以继续。您可以通过以下方式解决：
1. 启动您的本地服务器
2. 更新配置文件中的正确 URL
3. 使用 `--url` 参数指定正确的 URL

### 调试模式

启用详细日志输出：

```bash
export DEBUG=chrome-debug:*
/chrome-debug --verbose
```

## 贡献指南

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License

---

基于 [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) 项目构建。