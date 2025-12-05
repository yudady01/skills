# 🚀 从零开始：Claude Code 插件开发实战指南
本指南将带您创建一个名为 demo-toolkit 的插件项目。我们将实现以下功能：

- Command: 一个简单的 /greet 命令。
- Skill: 一个专门的 "Python 代码审查" 技能。
- Hook: 每次提交 Prompt 时自动记录日志。



## 目录应该看起来像这样

```shell
my-marketplace/                  # 您的市场根目录
├── .claude-plugin/
│   └── marketplace.json         # 市场配置文件
└── plugins/
    └── demo-toolkit/            # 您的第一个插件目录
        ├── .claude-plugin/
        │   └── plugin.json      # 插件元数据
        ├── commands/            # 存放自定义命令
        ├── skills/              # 存放技能
        ├── hooks/               # 存放钩子配置
        └── scripts/             # 存放执行脚本
```






这是一份基于您提供的详细资料整理而成的**实战指南**。我们将跳过单纯的概念堆砌，直接带您动手编写一个包含自定义命令、技能（Skill）和自动化钩子（Hook）的完整插件。

-----

# 🚀 从零开始：Claude Code 插件开发实战指南

本指南将带您创建一个名为 `demo-toolkit` 的插件项目。我们将实现以下功能：

1.  **Command**: 一个简单的 `/greet` 命令。
2.  **Skill**: 一个专门的 "Python 代码审查" 技能。
3.  **Hook**: 每次提交 Prompt 时自动记录日志。

-----

## 第一步：项目初始化与目录结构

首先，我们需要建立符合 Claude Code 标准的目录结构。这不仅是存放代码的地方，也是插件被识别的基础。

1.  **创建文件夹结构**
    在您的终端中执行（或手动创建）：

    ```bash
    mkdir -p my-marketplace/plugins/demo-toolkit/{commands,skills/python-reviewer,hooks,scripts}
    mkdir -p my-marketplace/.claude-plugin
    mkdir -p my-marketplace/plugins/demo-toolkit/.claude-plugin
    ```

2.  **最终结构预览**
    您的目录应该看起来像这样：

    ```text
    my-marketplace/                  # 您的市场根目录
    ├── .claude-plugin/
    │   └── marketplace.json         # 市场配置文件
    └── plugins/
        └── demo-toolkit/            # 您的第一个插件目录
            ├── .claude-plugin/
            │   └── plugin.json      # 插件元数据
            ├── commands/            # 存放自定义命令
            ├── skills/              # 存放技能
            ├── hooks/               # 存放钩子配置
            └── scripts/             # 存放执行脚本
    ```

-----

## 第二步：配置市场与插件身份

### 1\. 配置市场 (marketplace.json)

创建文件 `my-marketplace/.claude-plugin/marketplace.json`。这是 Claude Code 寻找插件的入口。

```json
{
  "name": "my-personal-marketplace",
  "owner": {
    "name": "Developer",
    "email": "dev@example.com"
  },
  "plugins": [
    {
      "name": "demo-toolkit",
      "source": "./plugins/demo-toolkit",
      "description": "我的第一个 Claude Code 实验插件。",
      "version": "1.0.0"
    }
  ]
}
```

### 2\. 配置插件 (plugin.json)

创建文件 `my-marketplace/plugins/demo-toolkit/.claude-plugin/plugin.json`。这是插件的“身份证”。

```json
{
  "name": "demo-toolkit",
  "version": "1.0.0",
  "description": "包含命令、技能和钩子的演示工具包。",
  "author": {
    "name": "Developer"
  },
  "license": "MIT",
  "commands": ["./commands/greet.md"],
  "hooks": "./hooks/hooks.json"
}
```

-----

## 第三步：开发核心组件

现在我们来填充实际的功能。

### 1\. 创建命令 (Command)

**目标**：输入 `/greet` 时，Claude 会礼貌地问候并报告当前时间。

创建文件 `plugins/demo-toolkit/commands/greet.md`：

```markdown
---
description: "向用户问好并报告时间"
argument-hint: "你的名字"
---
你好，{{ARG}}！
请以非常热情的方式向用户打招呼，并告诉用户现在的准确时间（精确到秒）。
```

### 2\. 创建技能 (Skill)

**目标**：让 Claude 在处理 Python 代码时，自动通过 `SKILL.md` 加载最佳实践，变身为代码审查专家。

创建文件 `plugins/demo-toolkit/skills/python-reviewer/SKILL.md`：

````markdown
---
name: python-reviewer
description: 专业的 Python 代码审查和最佳实践指导
when_to_use: 当用户要求编写、审查或重构 Python 代码时
allowed-tools:
  - Read
  - Edit
---

# Python 代码审查专家

## 审查原则
在审查或编写代码时，请严格遵守以下 PEP 8 标准：

1. **类型提示**：所有函数必须包含 Type Hints。
   ```python
   def calculate_sum(a: int, b: int) -> int:
       return a + b
````

2.  **文档字符串**：使用 Google Style 的 Docstrings。

3.  **异常处理**：不要使用裸露的 `except:`，必须捕获特定异常。

## 检查清单

- [ ] 是否使用了 f-strings 替代 .format()？
- [ ] 变量命名是否清晰（snake\_case）？
- [ ] 列表推导式是否被正确使用？

<!-- end list -->

````

### 3. 创建钩子 (Hook)
**目标**：每次用户提交 Prompt 时，在后台记录一条日志。

首先，创建执行脚本 `plugins/demo-toolkit/scripts/log.sh`：

```bash
#!/bin/bash
# 注意：确保给此文件执行权限 chmod +x log.sh
echo "[$(date)] User Prompt Submitted" >> ~/claude_plugin_debug.log
````

然后，创建钩子配置 `plugins/demo-toolkit/hooks/hooks.json`：

```json
{
  "UserPromptSubmit": [
    {
      "hooks": [
        {
          "type": "command",
          "command": "${CLAUDE_PLUGIN_ROOT}/scripts/log.sh"
        }
      ]
    }
  ]
}
```

*记得赋予脚本执行权限：*

```bash
chmod +x my-marketplace/plugins/demo-toolkit/scripts/log.sh
```

-----

## 第四步：本地安装与测试 (关键步骤)

在发布到 GitHub 之前，我们先在本地进行测试。请确保您已经安装并登录了 `claude` CLI。

1.  **进入市场目录**：

    ```bash
    cd my-marketplace
    ```

2.  **添加本地市场**：
    告诉 Claude Code 信任当前目录作为一个市场。

    ```bash
    claude plugin marketplace add --local .
    ```

3.  **安装插件**：
    从刚才添加的市场中安装插件。

    ```bash
    claude plugin install demo-toolkit
    ```

4.  **验证功能**：
    启动 Claude Code (`claude`) 并尝试以下操作：

    * **测试命令**：输入 `/greet 开发者`。
        * *预期*：Claude 会热情回复并报时。
    * **测试技能**：输入 “写一个简单的 Python 计算器函数”。
        * *预期*：Claude 会自动加载 `python-reviewer` 技能（您可以通过查看 verbose 日志或观察其是否使用了类型提示和 Google 风格文档来验证）。
    * **测试钩子**：检查日志文件。
        * *预期*：运行 `cat ~/claude_plugin_debug.log`，应该能看到刚才操作的时间戳记录。

-----

## 第五步：发布与分享

当您对插件满意后，就可以分享给团队或全世界了。

1.  **推送到 GitHub**：
    将 `my-marketplace` 文件夹作为一个仓库推送到 GitHub（例如：`github.com/yourname/my-claude-tools`）。

2.  **修改配置 (可选)**：
    如果希望别人直接引用 GitHub 链接，确保 `marketplace.json` 中的 `source` 字段指向正确的相对路径或 GitHub 对象（如果是单体仓库，保持相对路径通常即可）。

3.  **安装命令**：
    其他人只需运行一行命令即可使用您的所有工具：

    ```bash
    claude plugin marketplace add github.com/yourname/my-claude-tools
    claude plugin install demo-toolkit
    ```

-----

## 开发小贴士

* **路径引用**：在 Hook 脚本中始终使用 `${CLAUDE_PLUGIN_ROOT}`，因为用户安装插件后，您的脚本路径会发生变化，硬编码路径会导致脚本失效。
* **Skill 的触发**：Skill 不需要用户手动安装或调用。只要插件被安装，Claude 就会根据 `when_to_use` 的描述智能判断何时加载。描述写得越精准，触发越准确。
* **调试**：如果插件行为异常，可以使用 `/plugin list` 查看状态，或使用 `claude --verbose` 启动 CLI 查看详细加载日志。

现在，您已经掌握了构建 Claude Code 插件的核心能力。您可以尝试添加更多复杂的 `MCP Server` 或编写更强大的 `Agent` 来扩展您的开发工作流！