# CLAUDE.md

本文件为在此代码库中工作的 Claude Code (claude.ai/code) 提供指导。

## 项目概览

这是一个 Claude Code 市场，包含三个针对不同开发领域的专业技能/插件：

- **yudady-skills**: 一个包含翻译工具、SQL 脚本生成器和支付渠道集成开发技能的市场
- **位置**: `/Users/tommy/Documents/work.nosync/skills/`
- **结构**: 市场格式，包含 `.claude-plugin/marketplace.json` 和 `plugins/` 目录中的独立插件

## 插件架构

### 市场结构
```
.claude-plugin/marketplace.json    # 主市场配置
plugins/
├── en-to-zh-translator/          # 技术翻译技能
├── repeatable-sql/               # 数据库迁移脚本生成器
└── thirdparty-pay-channel/       # 支付集成开发技能
```

每个插件都遵循标准结构：
- `.claude-plugin/marketplace.json` - 插件元数据
- `skills/SKILL.md` - 带有 YAML frontmatter 的主要技能定义
- `README.md` - 插件文档
- `skills/scripts/` - Python 实用脚本
- `skills/assets/` - 模板和参考资料
- `skills/references/` - 文档和最佳实践

## 常用开发命令

### 插件测试和验证
```bash
# 验证插件结构（从项目根目录运行）
find plugins/ -name "SKILL.md" -exec grep -l "^---" {} \;

# 检查 marketplace.json 一致性
python -c "import json; print(json.load(open('.claude-plugin/marketplace.json'))['plugins'])"

# 测试插件中的 Python 脚本
python3 plugins/thirdparty-pay-channel/skills/scripts/generate_payment_handler.py --help
python3 plugins/repeatable-sql/skills/scripts/index_manager.py --help
```

### Python 脚本执行
所有 Python 脚本都位于 `plugins/*/skills/scripts/` 中，并使用 shebang `#!/usr/bin/env python3`。可以直接运行：

```bash
# 支付渠道开发
python3 plugins/thirdparty-pay-channel/skills/scripts/generate_payment_handler.py --channel-name NewPay --channel-code 1270 --support-recharge --support-withdraw --auth-type sign
python3 plugins/thirdparty-pay-channel/skills/scripts/validate_payment_handler.py --file Pay1270.java

# SQL 脚本生成
python3 plugins/repeatable-sql/skills/scripts/index_manager.py --database mysql
python3 plugins/repeatable-sql/skills/scripts/flyway_validator.py --directory migrations/

# 翻译验证
python3 plugins/en-to-zh-translator/skills/scripts/validate_translation.py --file translation.md
```

## 插件特定指南

### 支付渠道插件 (thirdparty-pay-channel)
- **用途**: 生成支付处理类并验证支付集成代码
- **关键文件**: `generate_payment_handler.py`、`validate_payment_handler.py`
- **模板**: `skills/assets/templates/` 中的 Java 支付处理模板
- **参考资料**: `skills/references/` 中的安全指南、API 文档、错误代码

### SQL 插件 (repeatable-sql)
- **用途**: 为 MySQL 和 PostgreSQL 生成幂等的数据库迁移脚本
- **关键文件**: `index_manager.py`、`table_migrator.py`、`flyway_validator.py`
- **模板**: `skills/assets/templates/` 中两种数据库的迁移脚本
- **模式**: 使用 MySQL 的 Dynamic_Create_Index 存储过程模式

### 翻译插件 (en-to-zh-translator)
- **用途**: 英中技术翻译，保留代码块和格式
- **关键文件**: `validate_translation.py`
- **参考资料**: 技术术语映射、质量指南、翻译示例

## 文件结构约定

### 技能定义格式
每个 `SKILL.md` 必须有 YAML frontmatter：
```yaml
---
name: plugin-name
description: 技能的简短描述
license: Apache 2.0  # 可选
---
```

### 插件元数据格式
每个插件的 `.claude-plugin/marketplace.json` 必须与技能名称匹配：
```json
{
  "name": "plugin-name",
  "description": "描述",
  "version": "1.0.0",
  "author": {"name": "yudady", "email": "yudady@gmail.com"}
}
```

## 关键集成点

### 环境变量
部署时，脚本使用 `${CLAUDE_PLUGIN_ROOT}` 来实现可移植路径

### 插件间依赖
- 支付渠道插件使用翻译插件进行 API 文档本地化
- SQL 插件模板被支付渠道插件引用用于数据库模式更改

### 外部工具集成
- Flyway 用于数据库迁移 (repeatable-sql)
- Jackson 用于 JSON 处理 (payment channel)
- 标准 Python 库用于文件处理和验证

## 开发工作流

1. **插件开发**: 编辑 `skills/SKILL.md` 和相关脚本
2. **本地测试**: 直接使用 Python 脚本并通过 `--help` 了解参数
3. **验证**: 确保 marketplace.json 引用与插件目录名称匹配
4. **文档**: 添加新功能时更新 README.md 文件
5. **一致性**: 保持目录、技能文件和元数据之间的命名约定