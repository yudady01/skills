# Global Claude Skills

本地自定义技能集合，包含英中翻译和 SQL 相关技能。

## 可用技能

| 技能 | 描述 |
|------|------|
| `en2zh` | 专业的英中翻译工具，专门处理技术和编程内容 |
| `repeatable-sql` | 可重复执行的 SQL 技能 |

## 安装步骤

在 Claude Code 中运行以下命令安装此插件市场：

```bash
claude-plugin install /Users/tommy/Documents/work.nosync/yudady/skills/global-claude
```

## 目录结构

```
global-claude/
├── .claude-plugin/
│   └── marketplace.json
├── README.md
└── skills/
    ├── en2zh/
    │   ├── README.md
    │   └── skills/
    │       ├── SKILL.md
    │       ├── assets/
    │       ├── references/
    │       └── scripts/
    └── repeatable-sql/
        └── skills/
            └── SKILL.md
```

## 添加新技能

1. 在 `skills/` 目录下创建新的技能文件夹
2. 在技能文件夹下创建 `skills/SKILL.md` 文件
3. 更新 `.claude-plugin/marketplace.json`，添加新技能配置

## 更新技能

如果技能文件已更新，重新运行安装命令即可：

```bash
claude-plugin install /Users/tommy/Documents/work.nosync/yudady/skills/global-claude
```
