---
name: skill-list-enhanced
description: 显示增强的技能列表，支持动态读取 marketplace.json、多种格式输出和技能验证
argument-hint: [--format table|json] [--category category] [--validate] [--refresh]
allowed-tools: Read, Write, Bash
---

# 增强技能列表指令

## 指令用途

显示当前可用的技能列表，从 marketplace.json 动态读取配置，支持多种格式和验证功能。

## 参数说明

- `--format`: 输出格式，支持 `table`（表格）或 `json`（JSON），默认为 table
- `--category`: 按类别过滤技能，支持 payment、database、translation 等
- `--validate`: 验证技能状态和配置
- `--refresh`: 强制刷新技能列表缓存

## 执行步骤

1. **读取配置文件**：
   - 查找 `.claude-plugin/marketplace.json` 文件
   - 如果不存在，显示错误信息
   - 解析 JSON 配置

2. **处理插件列表**：
   - 遍历 plugins 数组
   - 提取每个插件的 name、description、category 信息
   - 如果指定了 --category，过滤出匹配的插件

3. **验证技能（可选）**：
   - 如果指定了 --validate，检查每个技能：
     - 技能目录是否存在
     - SKILL.md 文件是否存在
     - frontmatter 格式是否正确
     - 基础字段是否完整

4. **格式化输出**：
   - 表格格式：使用 Unicode 表格字符
   - JSON 格式：使用标准 JSON 结构
   - 包含状态信息（如果验证）

## 输出示例

### 表格格式
```
┌─────────────────────────────┬──────────────┬──────────────────────────────────────┬───────────┐
│ 技能名称                     │ 类别        │ 描述                                  │ 状态      │
├─────────────────────────────┼──────────────┼──────────────────────────────────────┼───────────┤
│ thirdparty-pay-channel:skills │ 支付        │ 支付渠道第三方集成开发技能             │ ✅ 有效    │
│ repeatable-sql:skills       │ 数据库       │ 可重复执行SQL技能生成器                │ ✅ 有效    │
│ en-to-zh-translator:skills  │ 翻译         │ 专业的英中翻译工具                     │ ✅ 有效    │
└─────────────────────────────┴──────────────┴──────────────────────────────────────┴───────────┘
```

### JSON 格式
```json
{
  "marketplace": {
    "name": "yudady-skills",
    "version": "1.0.0",
    "total_skills": 3
  },
  "skills": [
    {
      "name": "thirdparty-pay-channel:skills",
      "category": "payment",
      "description": "支付渠道第三方集成开发技能",
      "status": "valid",
      "path": "./plugins/thirdparty-pay-channel"
    }
  ]
}
```

## 错误处理

- **配置文件不存在**：显示提示信息，指导用户创建 marketplace.json
- **JSON 格式错误**：显示语法错误位置和修复建议
- **技能目录不存在**：标记为缺失状态，但不中断执行
- **权限问题**：显示权限错误和解决方案

## 使用技巧

1. **查看所有技能**：`/skill-list-enhanced`
2. **只查看数据库技能**：`/skill-list-enhanced --category database`
3. **验证所有技能**：`/skill-list-enhanced --validate`
4. **导出为 JSON**：`/skill-list-enhanced --format json`
5. **组合使用**：`/skill-list-enhanced --category payment --validate`

## 注意事项

- 默认查找当前目录下的 `.claude-plugin/marketplace.json`
- 支持相对路径和绝对路径
- 表格格式在终端中显示效果最佳
- JSON 格式适合程序化处理和脚本调用