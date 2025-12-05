---
name: skill-management
description: 当用户询问"如何管理技能"、"技能列表怎么用"、"技能验证方法"、"技能搜索功能"或"技能发现和组织"时使用此技能。提供技能管理最佳实践、验证标准和工作流程指导。
version: 1.0.0
---

# 技能管理

本技能提供 Claude Code 技能的完整管理工作流程，包括技能发现、验证、组织和优化。

## 核心概念

技能管理是维护高质量 Claude Code 插件生态系统的关键实践。通过系统化的管理方法，确保技能的有效性、可用性和持续改进。

## 技能发现工作流程

### 1. 自动发现机制

Claude Code 通过以下机制自动发现技能：

```
plugins/
├── plugin-name/
│   ├── skills/
│   │   └── skill-name/
│   │       └── SKILL.md       # 必需文件
│   └── .claude-plugin/
│       └── marketplace.json   # 市场配置
```

**发现过程**：
- 扫描 `skills/` 目录下的所有子目录
- 查找包含 `SKILL.md` 文件的技能目录
- 读取 YAML frontmatter 中的元数据
- 注册技能到系统中

### 2. 市场配置解析

使用 `/skill-list-enhanced` 指令动态解析 marketplace.json：

**必需字段**：
- `name`: 市场名称
- `plugins`: 插件列表数组

**插件字段**：
- `name`: 插件名称
- `description`: 插件描述
- `source`: 插件源路径
- `category`: 插件类别

## 技能验证标准

### 基础验证（必需）

使用 `/skill-validate` 指令执行：

**文件结构验证**：
```
✓ 技能目录存在
✓ SKILL.md 文件存在
✓ 目录命名规范（kebab-case）
✓ 必需子目录存在（如需要）
```

**Frontmatter 验证**：
```
✓ YAML 格式正确
✓ name 字段存在
✓ description 字段存在
✓ description 使用第三人称
✓ 包含具体触发短语
```

**内容验证**：
```
✓ 标题结构正确
✓ 段落组织合理
✓ 长度适中（1500-2000 词）
✓ 使用祈使/不定式形式
```

### 质量验证（推荐）

**描述质量**：
- 具体触发短语（"create X", "configure Y"）
- 第三人称表述（"This skill should be used when..."）
- 避免模糊描述

**内容质量**：
- 渐进式披露原则
- 核心内容在 SKILL.md
- 详细内容移至 references/
- 实用示例在 examples/

**最佳实践验证**：
- 使用 CLAUDE_PLUGIN_ROOT 环境变量
- 避免硬编码路径
- 正确的命名约定
- 完整的资源引用

## 技能组织和分类

### 类别系统

使用标准类别组织技能：

**开发工具类**：
- `development`: 通用开发工具
- `testing`: 测试相关工具
- `deployment`: 部署和发布
- `validation`: 验证和检查

**领域专业类**：
- `database`: 数据库相关
- `payment`: 支付集成
- `translation`: 翻译工具
- `api`: API 开发

**系统管理类**：
- `management`: 管理和配置
- `monitoring`: 监控和分析
- `security`: 安全和合规
- `automation`: 自动化工具

### 命名约定

**技能目录命名**：
- 使用 kebab-case 格式
- 描述性命名
- 避免通用名称

**正确示例**：
```
✓ api-integration-testing/
✓ database-migration-tools/
✓ payment-channel-development/
```

**错误示例**：
```
✗ utils/
✗ tools/
✗ misc/
```

## 搜索和过滤

### 使用 `/skill-search` 指令

**按名称搜索**：
```bash
/skill-search --query "翻译"
```

**按类别过滤**：
```bash
/skill-search --category database
```

**按描述搜索**：
```bash
/skill-search --description "支付渠道"
```

**组合搜索**：
```bash
/skill-search --query "SQL" --category database
```

### 高级搜索技巧

**模糊搜索**：
- 使用部分关键词
- 支持中文和英文
- 不区分大小写

**精确匹配**：
- 使用引号包围短语
- 搜索完整技能名称
- 匹配特定描述片段

## 技能质量提升

### 内容优化策略

**增强触发条件**：
1. 分析实际使用情况
2. 添加常见查询短语
3. 包含同义词和相关术语
4. 定期更新触发列表

**改进内容结构**：
1. 遵循渐进式披露原则
2. 保持 SKILL.md 简洁
3. 将详细内容移至 references/
4. 提供实用示例

### 性能优化

**减少上下文使用**：
- SKILL.md 控制在 1500-2000 词
- 详细内容按需加载
- 避免重复信息

**提高响应速度**：
- 优化技能加载逻辑
- 使用缓存（如需要）
- 减少外部依赖

## 故障排除

### 常见问题解决

**技能不显示**：
```bash
# 验证技能存在
/skill-validate --all

# 检查 marketplace.json
/skill-list-enhanced --validate
```

**搜索结果不准确**：
```bash
# 使用更精确的关键词
/skill-search --query "确切短语"

# 检查类别标签
/skill-list-enhanced --format json
```

**验证失败**：
1. 检查文件结构
2. 验证 frontmatter 格式
3. 确认必需字段存在
4. 查看详细错误信息

## 高级功能

### 自定义配置

创建 `.claude/skill-list-manager.local.md`：

```markdown
---
marketplace_path: ".claude-plugin/marketplace.json"
default_format: "table"
auto_validate: true
validation_strict: false
---

自定义配置说明
```

### 批量操作

**验证所有技能**：
```bash
/skill-validate --all
```

**更新技能索引**：
```bash
/skill-list-enhanced --refresh
```

**生成技能报告**：
```bash
/skill-list-enhanced --format json > skills-report.json
```

## 最佳实践

### 技能设计原则

1. **单一职责**：每个技能专注于特定领域
2. **触发明确**：包含具体的使用场景
3. **内容精简**：核心信息在主文件，详细信息在引用
4. **示例完整**：提供可工作的代码示例

### 维护策略

1. **定期验证**：使用 `/skill-validate` 检查技能状态
2. **更新文档**：保持描述和内容最新
3. **收集反馈**：根据用户使用情况改进技能
4. **版本管理**：使用语义化版本号

## 附加资源

### 参考文件

详细指南和高级技巧：
- **`references/validation-standards.md`** - 完整验证标准
- **`references/advanced-patterns.md`** - 高级设计模式
- **`references/troubleshooting.md`** - 故障排除指南

### 示例文件

工作示例：
- **`examples/skill-structure/`** - 标准技能结构示例
- **`examples/marketplace-config.json`** - 市场配置示例
- **`examples/validation-script.py`** - 自定义验证脚本

### 工具脚本

实用工具：
- **`scripts/validate-skill.py`** - 技能验证工具
- **`scripts/parse-marketplace.py`** - 市场配置解析
- **`scripts/generate-report.py`** - 技能报告生成