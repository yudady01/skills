# Skill List Manager

一个专为 Claude Code 设计的技能列表管理插件，提供动态技能发现、验证和搜索功能。

## 功能特性

- **动态技能列表**: 自动从 marketplace.json 读取技能信息
- **技能验证**: 验证技能存在性和内容质量
- **智能搜索**: 按名称、类别、描述搜索技能
- **表格格式**: 清晰的表格显示格式
- **中文支持**: 完全中文界面和文档

## 安装方法

### 方法 1: 从 GitHub 安装
```bash
git clone https://github.com/yudady/skill-list-manager.git ~/.claude/plugins/skill-list-manager
```

### 方法 2: 下载压缩包
1. 从 GitHub 下载最新版本的压缩包
2. 解压到 `~/.claude/plugins/skill-list-manager`

### 方法 3: 项目本地安装
将插件复制到项目的 `.claude/plugins/` 目录：
```bash
cp -r skill-list-manager ~/.claude/plugins/
```

## 使用方法

### 斜线指令

#### `/skill-list-enhanced`
显示增强的技能列表：
```bash
/skill-list-enhanced
/skill-list-enhanced --format table
/skill-list-enhanced --category database
/skill-list-enhanced --validate
```

**参数**:
- `--format`: 显示格式 (table, json)，默认 table
- `--category`: 按类别过滤技能
- `--validate`: 验证技能状态

#### `/skill-validate`
验证技能配置和质量：
```bash
/skill-validate
/skill-validate --plugin-name repeatable-sql
/skill-validate --all
```

**参数**:
- `--plugin-name`: 验证特定插件
- `--all`: 验证所有技能

#### `/skill-search`
搜索技能：
```bash
/skill-search --query "翻译"
/skill-search --category payment
/skill-search --description "数据库"
```

**参数**:
- `--query`: 搜索关键词
- `--category`: 按类别搜索
- `--description`: 在描述中搜索

## 配置选项

在项目根目录创建 `.claude/skill-list-manager.local.md` 来配置插件：

```markdown
---
marketplace_path: ".claude-plugin/marketplace.json"
default_format: "table"
auto_validate: true
validation_strict: true
---

插件本地配置
```

**配置字段**:
- `marketplace_path`: marketplace.json 文件路径 (默认: .claude-plugin/marketplace.json)
- `default_format`: 默认显示格式 (table/json)
- `auto_validate`: 是否自动验证技能 (true/false)
- `validation_strict`: 严格验证模式 (true/false)

## 技能结构

插件会自动发现和分析以下技能结构：

```
plugins/
├── plugin-name/
│   ├── skills/
│   │   └── skill-name/
│   │       └── SKILL.md
│   ├── .claude-plugin/
│   │   └── marketplace.json
│   └── README.md
```

## 验证标准

插件会对技能进行以下验证：

### 基础验证
- [ ] 文件结构完整性
- [ ] 必需文件存在
- [ ] YAML frontmatter 语法正确
- [ ] 基本字段完整性

### 质量验证
- [ ] 描述清晰具体
- [ ] 触发条件明确
- [ ] 内容结构合理
- [ ] 示例和引用完整

### 最佳实践验证
- [ ] 命名规范符合标准
- [ ] 路径引用使用 CLAUDE_PLUGIN_ROOT
- [ ] 文档格式规范
- [ ] 渐进式披露原则

## 输出示例

### 技能列表 (表格格式)
```
┌─────────────────────────────┬──────────────┬──────────────────────────────────────┬───────────┐
│ 技能名称                     │ 类别        │ 描述                                  │ 状态      │
├─────────────────────────────┼──────────────┼──────────────────────────────────────┼───────────┤
│ thirdparty-pay-channel:skills │ 支付        │ 支付渠道第三方集成开发技能             │ ✅ 有效    │
│ repeatable-sql:skills       │ 数据库       │ 可重复执行SQL技能生成器                │ ✅ 有效    │
│ en-to-zh-translator:skills  │ 翻译         │ 专业的英中翻译工具                     │ ⚠️ 警告    │
└─────────────────────────────┴──────────────┴──────────────────────────────────────┴───────────┘
```

### 验证报告
```
技能验证报告
============

✅ thirdparty-pay-channel:skills
   - 结构完整
   - 描述清晰
   - 质量良好

⚠️ repeatable-sql:skills
   - 结构完整
   - 描述清晰
   - 缺少使用示例

❌ en-to-zh-translator:skills
   - frontmatter 语法错误
   - 描述过于简单
   - 缺少触发条件说明
```

## 开发指南

### 插件结构
```
skill-list-manager/
├── .claude-plugin/
│   └── plugin.json          # 插件清单
├── commands/                # 斜线指令
│   ├── skill-list-enhanced.md
│   ├── skill-validate.md
│   └── skill-search.md
├── agents/                  # 代理
│   └── skill-validator.md
├── skills/                  # 技能
│   └── skill-management/
│       └── SKILL.md
├── scripts/                 # 工具脚本
│   ├── validate_skill.py
│   └── parse_marketplace.py
└── README.md               # 插件文档
```

### 扩展功能
- 添加新的验证规则
- 支持更多输出格式
- 集成更多 marketplace 格式
- 添加技能使用统计

## 故障排除

### 常见问题

**Q: 技能列表显示为空**
A: 检查 marketplace.json 文件是否存在且格式正确

**Q: 验证失败但技能实际可用**
A: 检查验证配置，可以尝试降低验证严格度

**Q: 搜索结果不准确**
A: 确保搜索关键词正确，可以尝试不同的搜索参数

### 调试模式

使用以下命令启用详细输出：
```bash
/skill-list-enhanced --validate --format json
```

## 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 创建 Pull Request

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 更新日志

### v1.0.0
- 初始版本发布
- 支持基础技能列表显示
- 实现技能验证功能
- 添加技能搜索功能