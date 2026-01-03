---
name: dtg-chrome-skill
description: Chrome DevTools MCP 集成技能，提供持久化配置的浏览器自动化能力。用于需要控制浏览器、执行页面操作、截图、内容抓取等场景。当用户请求启动调试模式 Chrome、浏览器自动化操作（点击、输入、截图）、页面内容分析或抓取、Web 应用测试或调试、查看浏览器状态或标签页时使用。
---

# dtg-chrome-skill

Chrome DevTools MCP 集成技能，提供持久化用户配置的浏览器自动化能力。

## 核心功能

- 🚀 **一键启动**: 启动带用户数据的调试模式 Chrome（保留登录状态、书签）
- 🤖 **自动化操作**: 点击、输入、拖拽、截图等浏览器操作
- 📊 **内容获取**: 页面快照、截图、控制台日志、网络请求
- 🎯 **精确控制**: 基于 A11y 树的元素定位，支持表单填写和文件上传

## 快速开始

### 1. 启动调试模式 Chrome

```bash
# 赋予执行权限（首次运行）
chmod +x scripts/launch-connected-chrome.sh

# 启动 Chrome（会自动关闭现有实例并重新打开）
./scripts/launch-connected-chrome.sh
```

脚本会：
- 关闭当前运行的 Chrome
- 以调试模式启动 Chrome（端口 9222）
- 保留所有用户数据（登录状态、书签、扩展）

### 2. 验证连接

```bash
./scripts/validate-chrome.sh
```

验证项目：
- 端口 9222 是否开放
- HTTP 连接是否正常
- Chrome 进程状态
- MCP 配置检查

### 3. 在 Claude Desktop 中使用

启动 Chrome 后，可以直接在 Claude Desktop 中使用自然语言控制浏览器：

```
"列出当前所有标签页"
"给页面截个图"
"点击登录按钮"
"在搜索框输入 'Chrome DevTools'"
```

## 工作流程

### 典型页面操作

1. **获取页面快照**（必需，获取元素 uid）
   ```
   用户: "看看页面上有什么"
   调用: take_snapshot()
   ```

2. **执行操作**（使用快照中的 uid）
   ```
   用户: "点击提交按钮"
   调用: click(uid="button-123")
   ```

3. **等待并验证**
   ```
   用户: "等待加载完成"
   调用: wait_for(text="操作成功")
   ```

### 表单填写

```
用户: "填写登录表单，用户名 admin，密码 123456"
```

推荐使用 `fill_form` 批量填写：
```json
{
  "elements": [
    {"uid": "input-username", "value": "admin"},
    {"uid": "input-password", "value": "123456"}
  ]
}
```

### 页面导航

```
用户: "打开 GitHub 并搜索 Chrome DevTools"
```
执行流程：
1. `navigate_page(url="https://github.com")`
2. `take_snapshot()` 找搜索框
3. `fill(uid="search-input", value="Chrome DevTools")`
4. `press_key(key="Enter")`

## MCP 配置

配置文件: `scripts/config.json`

需要在 Claude Desktop 配置中添加：

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "-y",
        "chrome-devtools-mcp@latest",
        "--browser-url=http://127.0.0.1:9222"
      ]
    }
  }
}
```

配置路径: `~/Library/Application Support/Claude/claude_desktop_config.json`

## 重要提示

- ⚠️ **不要手动打开普通 Chrome 窗口**：调试模式下会使用默认配置目录，手动打开普通窗口可能导致调试断开
- ✅ **关闭方式**：使用完毕后完全退出 Chrome，然后正常启动即可恢复
- 📍 **端口占用**：如果端口 9222 被占用，需要修改脚本中的 PORT 变量

## 常见问题

### Chrome 无法启动
```bash
# 检查是否有残留进程
pkill -9 "Google Chrome"
# 重新运行启动脚本
./scripts/launch-connected-chrome.sh
```

### MCP 连接失败
```bash
# 运行验证脚本检查状态
./scripts/validate-chrome.sh
```

### 无法找到元素
- 确保先调用 `take_snapshot()` 获取最新页面结构
- 使用快照返回的 uid，而非手动猜测
- 检查元素是否在 iframe 中（需要先切换上下文）

## 资源

### scripts/

- **launch-connected-chrome.sh**: 启动调试模式 Chrome（带用户数据）
- **validate-chrome.sh**: 验证 Chrome DevTools MCP 连接状态

### references/

- **mcp-tools.md**: 完整的 MCP 工具参考文档
  - 页面管理工具（list_pages, new_page, select_page 等）
  - 交互工具（click, fill, hover, drag 等）
  - 内容获取（take_snapshot, take_screenshot）
  - 高级操作（upload_file, handle_dialog, emulate）
  - 性能分析和网络监控

查看完整工具文档：`references/mcp-tools.md`
