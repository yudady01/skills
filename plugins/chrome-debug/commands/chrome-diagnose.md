---
name: chrome-diagnose
description: 诊断 Chrome DevTools MCP 连接问题、页面可访问性问题并提供详细错误分析
argument-hint: [--url <url>] [--verbose] [--test-login] [--check-dependencies]
allowed-tools: [Read, Write, Bash, mcp__ide__*, WebFetch]
---

# Chrome 诊断命令

此命令执行全面诊断，以识别和解决 Chrome DevTools MCP 连接问题、页面可访问性问题和配置错误。

## 参数

- `--url <url>`: 要测试的特定 URL（可选，使用配置默认值）
- `--verbose`: 启用详细输出，包含逐步分析
- `--test-login`: 测试自动登录功能
- `--check-dependencies`: 验证所有系统依赖项

## 诊断类别

### 1. 系统环境检查
- **操作系统**：验证操作系统兼容性
- **Node.js 版本**：检查 v20.19+ 要求
- **Chrome 安装**：验证 Chrome 浏览器存在和版本
- **网络连接**：测试互联网和本地网络访问
- **端口可用性**：检查端口冲突和可用性

### 2. MCP 服务器状态
- **安装验证**：确认 chrome-devtools-mcp 已安装
- **版本兼容性**：检查 MCP 服务器版本兼容性
- **配置验证**：验证 .mcp.json 格式和内容
- **启动测试**：测试 MCP 服务器初始化
- **协议访问**：验证 DevTools 协议可访问性

### 3. Chrome 浏览器分析
- **安装路径**：检测 Chrome 可执行文件位置
- **版本检查**：验证 Chrome 版本兼容性
- **远程调试**：测试 Chrome 远程调试功能
- **权限问题**：检查 Chrome 启动权限
- **资源可用性**：验证内存和磁盘空间

### 4. 网络和 URL 测试
- **DNS 解析**：测试域名解析
- **HTTP/HTTPS 访问**：测试 URL 可访问性
- **404 未找到检测**：检查缺失页面并建议回退方案
- **SSL 证书**：验证 HTTPS 证书有效性
- **响应时间**：测量页面加载时间
- **内容分析**：分析页面结构和元素
- **回退 URL 测试**：验证 Google 可访问性作为回退选项

### 5. 登录功能测试
- **表单检测**：识别登录表单元素
- **选择器分析**：测试元素选择器策略
- **凭据验证**：验证登录凭据格式
- **提交测试**：测试表单提交流程
- **成功检测**：验证登录成功指标

## 诊断程序

### 系统环境诊断
```bash
# 操作系统信息
uname -a
sw_vers  # macOS
cat /etc/os-release  # Linux

# Node.js 版本检查
node --version
npm --version

# Chrome 检测
which google-chrome || which chrome
chrome --version
ls -la "/Applications/Google Chrome.app/Contents/MacOS/"
```

### 网络诊断
```bash
# 本地网络测试
ping -c 3 localhost
netstat -an | grep 9222

# URL 可访问性测试
curl -I "http://localhost:8193"
curl -I "https://www.google.com"

# DNS 解析
nslookup localhost
dig localhost
```

### MCP 服务器诊断
```bash
# 包安装检查
npm list -g chrome-devtools-mcp
npx -y chrome-devtools-mcp@latest --version

# 配置验证
python3 -c "import json; print(json.load(open('.mcp.json')))"

# 服务器启动测试
timeout 10s npx -y chrome-devtools-mcp@latest
```

### Chrome 功能测试
```bash
# Chrome 远程调试测试
chrome --remote-debugging-port=9222 --no-sandbox --headless &
sleep 3
curl http://localhost:9222/json/version
pkill -f chrome

# Chrome 路径检测
find /Applications -name "Google Chrome.app" 2>/dev/null
mdfind "kMDItemDisplayName == 'Google Chrome'" 2>/dev/null
```

## 错误分析和解决方案

### 系统要求错误

**Node.js 版本不兼容**
```
错误：检测到 Node.js v18.17.0。需要 v20.19+
解决方案：
1. 从 https://nodejs.org 安装 Node.js v20+
2. 使用 nvm：nvm install 20 && nvm use 20
3. 更新包管理器：brew install node@20
```

**Chrome 浏览器未找到**
```
错误：未检测到 Chrome 浏览器安装
解决方案：
1. 从 https://www.google.com/chrome/ 安装 Chrome
2. 设置 CHROME_PATH 环境变量
3. 使用自定义 Chrome 路径更新配置
```

### MCP 服务器错误

**包未安装**
```
错误：未找到 chrome-devtools-mcp 包
解决方案：
1. 运行：npm install -g chrome-devtools-mcp@latest
2. 检查 npm 全局路径：npm config get prefix
3. 验证 npm 权限：npm list -g
```

**配置文件无效**
```
错误：.mcp.json 格式无效
解决方案：
1. 验证 JSON 语法：python3 -m json.tool .mcp.json
2. 重置配置：/chrome-config --reset
3. 检查文件权限：ls -la .mcp.json
```

### 网络和连接错误

**端口已被占用**
```
错误：端口 9222 已被占用
解决方案：
1. 终止现有进程：lsof -ti:9222 | xargs kill
2. 使用不同端口：export CHROME_DEBUG_PORT=9223
3. 更新自定义端口配置
```

**URL 不可访问**
```
错误：目标 URL 无法访问：http://localhost:8193
解决方案：
1. 检查服务器状态：curl -I http://localhost:8193
2. 验证端口开放：netstat -an | grep 8193
3. 测试不同的 URL 或检查服务器日志
4. 自动回退：插件将自动回退到 https://www.google.com/
   - 调试会话将继续使用 Google 主页
   - 更新 .claude/chrome-debug.local.md 中的正确 URL 以供下次使用
```

### Chrome 启动错误

**权限被拒绝**
```
错误：Chrome 启动权限被拒绝
解决方案：
1. 检查文件权限：ls -la $(which chrome)
2. 使用适当的用户运行：sudo -u user chrome
3. 更新 Chrome 到最新版本
```

**沙箱问题**
```
错误：Chrome 沙箱初始化失败
解决方案：
1. 禁用沙箱：chrome --no-sandbox
2. 检查内核兼容性：uname -r
3. 更新系统包
```

## 使用示例

### 基本诊断
```bash
/chrome-diagnose
```
对默认配置运行全面诊断测试。

### 特定 URL 测试
```bash
/chrome-diagnose --url "https://example.com/login"
```
测试特定 URL 的可访问性和功能。

### 详细分析
```bash
/chrome-diagnose --verbose
```
启用详细的逐步诊断输出。

### 登录功能测试
```bash
/chrome-diagnose --test-login --verbose
```
测试自动登录过程并提供详细输出。

### 完整系统检查
```bash
/chrome-diagnose --check-dependencies --test-login --verbose
```
运行全面的系统和功能测试。

## 输出格式

### 成功报告
```
🔍 Chrome 调试插件诊断
✅ 系统环境
  操作系统：macOS 14.2.1 (✓)
  Node.js：v20.19.0 (✓)
  Chrome：120.0.6099.129 (✓)
  内存：16GB 可用 (✓)

✅ MCP 服务器状态
  安装：完成 (✓)
  版本：chrome-devtools-mcp@1.2.0 (✓)
  配置：有效 (✓)
  启动：成功 (✓)

✅ Chrome 浏览器
  路径：/Applications/Google Chrome.app (✓)
  版本：兼容 (✓)
  远程调试：工作正常 (✓)
  权限：充足 (✓)

✅ 网络连接
  本地网络：已连接 (✓)
  DNS 解析：工作正常 (✓)
  目标 URL：可访问 (✓)
  响应时间：245ms (✓)

🎯 总结：所有系统运行正常
```

### 带解决方案的错误报告
```
❌ Chrome 调试插件诊断
❌ 系统环境
  操作系统：macOS 14.2.1 (✓)
  Node.js：v18.17.0 (❌)
  Chrome：未找到 (❌)
  内存：16GB 可用 (✓)

🔧 推荐操作：
1. 更新 Node.js：
   nvm install 20 && nvm use 20

2. 安装 Chrome：
   brew install --cask google-chrome

3. 更新配置：
   /chrome-config --reset

💡 修复后运行：/chrome-diagnose --check-dependencies
```

### 详细技术信息
```
🔬 详细分析（详细模式）

[1/15] 检查 Node.js 版本...
  命令：node --version
  输出：v20.19.0
  状态：✓ 兼容（>= v20.19）

[2/15] 定位 Chrome 可执行文件...
  搜索路径：
    - /usr/bin/google-chrome
    - /usr/local/bin/chrome
    - /Applications/Google Chrome.app/Contents/MacOS/Google Chrome ✓
  找到：/Applications/Google Chrome.app/Contents/MacOS/Google Chrome

[3/15] 测试 Chrome 版本...
  命令：/Applications/Google Chrome.app/Contents/MacOS/Google Chrome --version
  输出：Google Chrome 120.0.6099.129
  状态：✓ 兼容

[4/15] 检查端口 9222 可用性...
  命令：lsof -i :9222
  输出：（无进程）
  状态：✓ 端口可用

[5/15] 测试 MCP 服务器安装...
  命令：npm list -g chrome-devtools-mcp
  输出：/usr/local/lib/node_modules/chrome-devtools-mcp@1.2.0
  状态：✓ 已安装

...（继续详细逐步分析）
```

## 与其他组件的集成

### Chrome 调试命令
- 使用诊断结果指导调试会话
- 自动应用配置修复
- 为失败会话提供错误上下文

### Chrome 配置命令
- 利用诊断数据进行配置更新
- 验证配置更改
- 长期监控配置健康状况

### 技能集成
- chrome-devtools-integration：提供 MCP 专业知识
- dom-automation：帮助解决自动化问题
- 错误分析指导技能选择和使用

## 自动修复

诊断命令可以自动修复常见问题：

- **重置配置**：`--auto-fix` 标志
- **重新安装依赖项**：`--reinstall` 标志
- **更新 Chrome 路径**：`--update-paths` 标志
- **清除缓存**：`--clean` 标志

## 最佳实践

### 定期维护
- 每周运行诊断以早期发现问题
- 使用详细模式进行详细故障排除
- 为团队参考记录自定义配置
- 保持 Chrome 和 Node.js 版本更新

### 故障排除工作流
1. 运行基本诊断：`/chrome-diagnose`
2. 分析错误模式并分类
3. 根据建议应用针对性修复
4. 使用以下命令验证修复：`/chrome-diagnose --verify`
5. 记录解决方案以供将来参考

### 性能监控
- 监控诊断执行时间
- 长期跟踪错误模式
- 优化诊断测试序列
- 缓存重复测试的结果

## 相关命令

- `/chrome-debug`: 主要调试命令
- `/chrome-config`: 配置管理
- `/skill chrome-devtools-integration`: MCP 专业知识
- `/skill dom-automation`: 自动化故障排除