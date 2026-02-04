---
name: "atlas"
description: "macOS 专用的 ChatGPT Atlas 桌面应用 AppleScript 控制。仅当用户明确要求在 macOS 上控制 Atlas 标签页/书签/历史记录且已安装「ChatGPT Atlas」应用时使用；不要为一般浏览器任务或非 macOS 环境触发。"
---


# Atlas 控制 (macOS)

使用随附的 CLI 控制 Atlas 并检查本地浏览器数据。

## 快速开始

设置 CLI 的稳定路径：

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export ATLAS_CLI="$CODEX_HOME/skills/atlas/scripts/atlas_cli.py"
```

用户范围的技能安装在 `$CODEX_HOME/skills` 下（默认：`~/.codex/skills`）。

然后运行：

```bash
uv run --python 3.12 python "$ATLAS_CLI" app-name
uv run --python 3.12 python "$ATLAS_CLI" tabs --json
```

CLI 需要 `/Applications` 或 `~/Applications` 中的 Atlas 应用包：

- `ChatGPT Atlas`

如果 AppleScript 因权限错误而失败，请在系统设置 > 隐私与安全性 > 自动化中授予自动化权限，允许您的终端控制 ChatGPT Atlas。

## 标签页工作流

1. 列出标签页以获取 `window_id` 和 `tab_index`：

```bash
uv run --python 3.12 python "$ATLAS_CLI" tabs
```

2. 使用列表中的 `window_id` 和 `tab_index` 聚焦标签页：

```bash
uv run --python 3.12 python "$ATLAS_CLI" focus-tab <window_id> <tab_index>
```

3. 打开新标签页：

```bash
uv run --python 3.12 python "$ATLAS_CLI" open-tab "https://chatgpt.com/"
```

可选维护命令：

```bash
uv run --python 3.12 python "$ATLAS_CLI" reload-tab <window_id> <tab_index>
uv run --python 3.12 python "$ATLAS_CLI" close-tab <window_id> <tab_index>
```

## 书签和历史记录

Atlas 在 `~/Library/Application Support/com.openai.atlas/browser-data/host/` 下存储 Chromium 风格的配置文件数据。

列出书签：

```bash
uv run --python 3.12 python "$ATLAS_CLI" bookmarks --limit 100
```

搜索书签：

```bash
uv run --python 3.12 python "$ATLAS_CLI" bookmarks --search "docs"
```

搜索历史记录：

```bash
uv run --python 3.12 python "$ATLAS_CLI" history --search "openai docs" --limit 50
```

今天的历史记录（本地时间）：

```bash
uv run --python 3.12 python "$ATLAS_CLI" history --today --limit 200 --json
```

history 命令会将 SQLite 数据库复制到临时位置，以避免锁错误。

如果历史记录看起来过时或为空，请询问用户使用的是哪个 Atlas 安装，然后检查两个 Atlas 数据根目录并检查最近 `History` 文件的那个：

- `~/Library/Application Support/com.openai.atlas/browser-data/host/`
- `~/Library/Application Support/com.openai.atlas.beta/browser-data/host/`

## 参考

在调整数据路径或时间戳时，请阅读技能文件夹中的 `references/atlas-data.md`（例如，`$CODEX_HOME/skills/atlas/references/atlas-data.md`）。
