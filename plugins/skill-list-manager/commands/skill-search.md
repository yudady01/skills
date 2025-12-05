---
name: skill-search
description: 搜索和过滤技能，支持按名称、类别、描述进行模糊搜索
argument-hint: --query "搜索词" [--category category] [--description "描述搜索"] [--exact] [--count number]
allowed-tools: Read, Grep, Glob
---

# 技能搜索指令

## 指令用途

在可用技能中搜索匹配项，支持多种搜索条件和过滤选项，帮助用户快速找到需要的技能。

## 参数说明

- `--query`: 搜索关键词，支持技能名称的模糊匹配
- `--category`: 按类别过滤（payment、database、translation 等）
- `--description`: 在技能描述中搜索关键词
- `--exact`: 启用精确匹配模式
- `--count`: 限制返回结果数量，默认显示所有匹配项

## 搜索逻辑

### 默认搜索模式

1. **名称搜索**（--query）：
   - 在技能名称中查找关键词
   - 支持部分匹配
   - 不区分大小写
   - 支持中文和英文

2. **类别过滤**（--category）：
   - 只返回指定类别的技能
   - 精确匹配类别名称
   - 支持标准类别：payment、database、translation、development 等

3. **描述搜索**（--description）：
   - 在技能描述中查找关键词
   - 支持短语搜索
   - 匹配相关性和上下文

### 精确搜索模式（--exact）

- 技能名称必须完全匹配
- 类别必须精确匹配
- 描述搜索要求关键词完整出现

## 执行步骤

1. **加载技能数据**：
   - 读取 marketplace.json 配置
   - 解析插件列表
   - 收集技能元数据

2. **应用搜索条件**：
   - 如果指定了 --query，在技能名称中搜索
   - 如果指定了 --category，过滤出匹配的类别
   - 如果指定了 --description，在描述中搜索
   - 如果启用 --exact，使用精确匹配逻辑

3. **计算相关性分数**：
   - 完全匹配：100 分
   - 部分匹配：50-80 分
   - 模糊匹配：10-40 分
   - 多条件匹配累加分数

4. **排序和限制结果**：
   - 按相关性分数降序排列
   - 如果指定了 --count，限制结果数量
   - 确保结果包含足够的信息

5. **格式化输出**：
   - 显示匹配的技能列表
   - 包含匹配分数和匹配位置
   - 提供高亮显示关键词

## 输出格式

### 标准搜索结果
```
🔍 搜索结果："sql" - 找到 2 个匹配项

1. repeatable-sql:skills (95分)
   📂 类别：database
   📝 描述：可重复执行SQL技能生成器，专门用于创建幂等的数据库迁移脚本
   💡 匹配：名称完全匹配

2. thirdparty-pay-channel:skills (30分)
   📂 类别：payment
   📝 描述：支付渠道第三方集成开发技能，提供支付渠道处理类的快速生成
   💡 匹配：描述包含 "sql" 相关内容
```

### 类别过滤结果
```
🏷️  类别：database - 找到 1 个技能

📦 repeatable-sql:skills
   📝 描述：可重复执行SQL技能生成器，专门用于创建幂等的数据库迁移脚本
   📂 路径：./plugins/repeatable-sql
   ✅ 状态：可用
```

### 描述搜索结果
```
📖 描述搜索："翻译" - 找到 1 个匹配项

🌐 en-to-zh-translator:skills (100分)
   📂 类别：translation
   📝 描述：专业的英中翻译工具，专门处理技术和编程内容
   💡 匹配：描述完全包含搜索词
```

## 搜索技巧

### 高效搜索策略

1. **组合搜索**：
   ```bash
   /skill-search --query "sql" --category database
   ```

2. **精确匹配**：
   ```bash
   /skill-search --query "repeatable-sql" --exact
   ```

3. **描述搜索**：
   ```bash
   /skill-search --description "支付渠道集成"
   ```

4. **限制结果数量**：
   ```bash
   /skill-search --query "skill" --count 3
   ```

### 搜索建议

- **使用具体关键词**：避免过于通用的搜索词
- **尝试同义词**：如果搜索无结果，尝试相关词汇
- **使用类别过滤**：结合类别过滤提高精度
- **组合条件**：同时使用名称和描述搜索

## 支持的搜索类型

### 技能名称搜索
```bash
# 部分匹配
/skill-search --query "sql"

# 精确匹配
/skill-search --query "repeatable-sql" --exact

# 中文搜索
/skill-search --query "翻译"
```

### 类别过滤
```bash
# 标准类别
/skill-search --category payment
/skill-search --category database
/skill-search --category translation
```

### 描述搜索
```bash
# 关键词搜索
/skill-search --description "数据库"
/skill-search --description "支付集成"

# 短语搜索
/skill-search --description "可重复执行SQL"
```

## 高级功能

### 智能建议
如果搜索无结果，系统会提供：
- 拼写纠正建议
- 相关技能推荐
- 搜索技巧提示

### 搜索历史
保存最近的搜索查询，支持：
- 重复执行上次搜索
- 查看搜索历史
- 清除搜索记录

### 导出功能
```bash
# 导出搜索结果为 JSON
/skill-search --query "sql" --format json > search-results.json

# 导出为 CSV
/skill-search --category database --format csv > database-skills.csv
```

## 性能优化

- **缓存机制**：缓存技能数据，提高搜索速度
- **索引优化**：为常用搜索字段建立索引
- **结果分页**：大量结果时支持分页显示
- **异步搜索**：复杂搜索在后台执行

## 错误处理

**搜索无结果**：
- 提供搜索建议
- 推荐相关技能
- 显示可用类别列表

**参数错误**：
- 检查搜索词有效性
- 验证类别名称
- 提供使用示例

**数据加载失败**：
- 显示配置错误信息
- 提供修复建议
- 使用默认数据源

## 使用示例

1. **查找数据库相关技能**：
   ```bash
   /skill-search --category database
   ```

2. **搜索翻译功能**：
   ```bash
   /skill-search --query "翻译"
   ```

3. **在描述中搜索特定功能**：
   ```bash
   /skill-search --description "支付渠道"
   ```

4. **组合搜索最佳技能**：
   ```bash
   /skill-search --query "sql" --category database --count 5
   ```

5. **精确查找技能**：
   ```bash
   /skill-search --query "en-to-zh-translator" --exact
   ```