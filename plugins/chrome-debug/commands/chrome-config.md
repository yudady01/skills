---
name: chrome-config
description: 配置 Chrome DevTools MCP 服务器、检查状态和管理插件设置
argument-hint: [--install] [--status] [--reset] [--verify]
allowed-tools: [Read, Write, Bash, mcp__ide__*]
---

# Chrome 配置命令

此命令管理 Chrome DevTools MCP 服务器配置、验证安装状态并处理插件设置。

## 参数

- `--install`: 安装 Chrome DevTools MCP 服务器和依赖项
- `--status`: 检查当前配置和服务器状态
- `--reset`: 将配置重置为默认值
- `--verify`: 验证所有组件是否正常工作

## 执行步骤

### --install 模式
1. **检查系统要求**
   - 验证 Node.js 版本（需要 v20.19+）
   - 检查 Chrome 浏览器安装
   - 验证 npm 包管理器可用性

2. **安装 MCP 服务器**
   - 通过 npm 全局安装 chrome-devtools-mcp
   - 验证安装成功
   - 测试基本功能

3. **创建配置文件**
   - 生成带服务器配置的 .mcp.json
   - 创建本地配置模板
   - 设置默认设置

4. **验证设置**
   - 测试 MCP 服务器连接
   - 验证 Chrome DevTools 协议访问
   - 运行基本功能测试

### --status 模式
1. **检查系统状态**
   - Node.js 版本检查
   - Chrome 浏览器检测
   - MCP 服务器安装验证

2. **配置分析**
   - 验证 .mcp.json 格式
   - 检查本地配置设置
   - 验证环境变量

3. **连接测试**
   - 测试 MCP 服务器启动
   - 验证 Chrome 远程调试
   - 检查端口可访问性

4. **报告生成**
   - 生成全面的状态报告
   - 识别潜在问题
   - 提供建议

### --reset 模式
1. **备份当前设置**
   - 保存现有配置文件
   - 记录当前设置
   - 创建回滚能力

2. **重置配置**
   - 删除损坏的配置文件
   - 重置为默认设置
   - 清理临时文件

3. **重新创建默认值**
   - 生成新的 .mcp.json
   - 创建新的本地配置模板
   - 设置标准默认值

4. **验证重置**
   - 测试新配置
   - 验证基本功能
   - 确认重置成功

### --verify 模式
1. **组件验证**
   - 测试所有插件组件
   - 验证技能配置
   - 检查命令集成

2. **集成测试**
   - 测试 MCP 服务器通信
   - 验证 Chrome DevTools 访问
   - 验证自动化工作流

3. **性能检查**
   - 测量响应时间
   - 检查资源使用
   - 验证稳定性

4. **生成报告**
   - 全面的验证报告
   - 性能指标
   - 优化建议

## 错误处理

### 安装错误
- Node.js 版本不兼容：提供升级说明
- Chrome 未找到：建议安装路径
- npm 权限：指导权限修复
- 网络问题：提供离线安装选项

### 配置错误
- 无效 JSON：修复语法错误
- 缺少字段：添加必需的配置
- 路径问题：更正文件路径
- 权限问题：解决访问权限

### 连接错误
- 端口冲突：建议替代端口
- Chrome 启动失败：提供故障排除
- MCP 服务器错误：重启服务
- 协议不匹配：更新配置

## 使用示例

### 安装 MCP 服务器
```bash
/chrome-config --install
```
完成 Chrome DevTools MCP 服务器及所有依赖项的安装。

### 检查状态
```bash
/chrome-config --status
```
显示所有组件和配置的全面状态。

### 重置配置
```bash
/chrome-config --reset
```
将所有配置文件重置为默认值。

### 验证安装
```bash
/chrome-config --verify
```
运行所有插件组件的全面验证。

## 输出格式

### 安装输出
```
🚀 Chrome DevTools MCP 安装
✅ Node.js 版本: v20.19.0 (兼容)
✅ Chrome 浏览器已找到: Google Chrome 120.0.6099.129
📦 正在安装 chrome-devtools-mcp@latest...
✅ MCP 服务器安装成功
📄 正在创建 .mcp.json 配置...
✅ 配置已创建
🔍 正在测试 MCP 服务器连接...
✅ 安装成功完成
```

### 状态输出
```
📊 Chrome 调试插件状态
✅ 系统要求已满足
  Node.js: v20.19.0 (✓)
  Chrome: 120.0.6099.129 (✓)
  npm: 10.2.3 (✓)

✅ MCP 服务器状态
  安装: 完成 (✓)
  版本: chrome-devtools-mcp@1.2.0 (✓)
  配置: 有效 (✓)

✅ 配置文件
  .mcp.json: 已找到且有效 (✓)
  chrome-debug.local.md: 已找到 (✓)
  环境变量: 已设置 (✓)

🔗 连接性
  MCP 服务器: 可访问 (✓)
  Chrome 调试端口: 9222 (✓)
  DevTools 协议: 可访问 (✓)
```

### 重置输出
```
🔄 Chrome 调试配置重置
💾 正在备份当前配置...
✅ 备份已创建: .claude/chrome-debug-backup-20241205.json
🗑️  正在移除旧的配置文件...
📄 正在创建新的默认配置...
✅ 配置已重置为默认值
🔍 正在验证新配置...
✅ 重置成功完成
```

## 配置文件

### .mcp.json 结构
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

### chrome-debug.local.md 模板
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

## 故障排除

### 常见问题

**MCP 服务器未找到**
```bash
# 重新安装 MCP 服务器
/chrome-config --install

# 检查 npm 全局包
npm list -g chrome-devtools-mcp
```

**Chrome 路径问题**
```bash
# 设置 Chrome 路径环境变量
export CHROME_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# 更新配置
/chrome-config --reset
```

**端口冲突**
```bash
# 终止现有 Chrome 进程
pkill -f "chrome.*remote-debugging"

# 使用不同端口
export CHROME_DEBUG_PORT=9223
```

### 手动验证

手动测试 MCP 服务器：
```bash
npx -y chrome-devtools-mcp@latest --help
```

测试 Chrome 远程调试：
```bash
chrome --remote-debugging-port=9222 --no-sandbox
```

## 最佳实践

### 维护
- 使用 `--status` 定期检查状态
- 保持 MCP 服务器更新
- 监控 Chrome 版本兼容性
- 更改前备份配置

### 安全
- 尽可能使用 HTTPS URL
- 保护本地配置文件
- 避免硬编码凭据
- 定期安全更新

### 性能
- 监控资源使用
- 优化 Chrome 启动标志
- 使用适当的超时值
- 清理临时文件

## 集成

此命令与以下组件集成：
- chrome-debug 命令：使用配置进行调试会话
- chrome-diagnose 命令：利用状态信息进行诊断
- chrome-devtools-integration 技能：提供 MCP 服务器专业知识
- dom-automation 技能：使用配置进行自动化工作流

## 相关命令

- `/chrome-debug`: 使用此配置的主要调试命令
- `/chrome-diagnose`: 使用配置数据诊断问题
- `/skill chrome-devtools-integration`: 获取 MCP 配置帮助
- `/skill dom-automation`: 获取自动化设置指导