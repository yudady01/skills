---
name: dtg:flyway-idempotent
description: 将 Flyway SQL 迁移脚本改造为幂等版本，确保可安全重复执行
---

# Flyway 幂等性改造 Skill

## 功能概述

该 Skill 帮助将非幂等的 Flyway SQL 迁移脚本改造为幂等版本，确保脚本可以安全地重复执行而不会导致错误或数据不一致。

## 适用场景

当您需要：
- 将现有的 Flyway 迁移脚本改造为可重复执行
- 修复因重复执行迁移脚本导致的问题
- 确保新编写的迁移脚本符合幂等性最佳实践
- 在测试环境中验证迁移脚本的幂等性

## 核心能力

| 能力 | 描述 |
|------|------|
| **列操作幂等化** | `ALTER TABLE ADD COLUMN` → 存在性检查 + 条件执行 |
| **索引操作幂等化** | `ALTER TABLE ADD INDEX` → 存在性检查 + 条件执行 |
| **表重命名幂等化** | `RENAME TABLE` → 备份表存在性检查 + 条件执行 |
| **数据迁移幂等化** | `INSERT INTO` → `INSERT IGNORE INTO` |
| **表创建幂等化** | `CREATE TABLE` → `CREATE TABLE IF NOT EXISTS` |
| **视图创建幂等化** | `CREATE VIEW` → `CREATE OR REPLACE VIEW` |

## 改造流程

### 1. 分析 SQL 脚本

读取并解析待改造的 SQL 迁移脚本，识别需要幂等化的操作类型。

### 2. 应用转换规则

根据识别的操作类型，应用相应的幂等性转换模式：

#### 2.1 ADD COLUMN 转换

将：
```sql
ALTER TABLE `table_name` ADD COLUMN `column_name` VARCHAR(255) NOT NULL;
```

转换为：
```sql
SET @col_exists = 0;
SELECT COUNT(*) INTO @col_exists
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'table_name'
  AND COLUMN_NAME = 'column_name';

SET @sql = IF(@col_exists = 0,
    'ALTER TABLE `table_name` ADD COLUMN `column_name` VARCHAR(255) NOT NULL',
    'SELECT ''Skip: column already exists'' AS message');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

#### 2.2 ADD INDEX 转换

将：
```sql
ALTER TABLE `table_name` ADD INDEX `idx_column_name` (`column_name`);
```

转换为：
```sql
SET @index_exists = 0;
SELECT COUNT(*) INTO @index_exists
FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'table_name'
  AND INDEX_NAME = 'idx_column_name';

SET @sql = IF(@index_exists = 0,
    'ALTER TABLE `table_name` ADD INDEX `idx_column_name` (`column_name`)',
    'SELECT ''Skip: index already exists'' AS message');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

#### 2.3 INSERT 转换

将：
```sql
INSERT INTO target_table (col1, col2, ...)
SELECT col1, col2, ...
FROM source_table
WHERE condition;
```

转换为：
```sql
INSERT IGNORE INTO target_table (col1, col2, ...)
SELECT col1, col2, ...
FROM source_table
WHERE condition;
```

#### 2.4 RENAME TABLE 转换

将：
```sql
RENAME TABLE `source_table` TO `backup_table_name`;
```

转换为：
```sql
SET @backup_exists = 0;
SELECT COUNT(*) INTO @backup_exists
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'backup_table_name';

SET @sql = IF(@backup_exists = 0,
    'RENAME TABLE `source_table` TO `backup_table_name`',
    'SELECT ''Skip: backup table already exists'' AS message');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

#### 2.5 CREATE TABLE 转换

将：
```sql
CREATE TABLE `table_name` (...);
```

转换为：
```sql
CREATE TABLE IF NOT EXISTS `table_name` (...);
```

#### 2.6 CREATE VIEW 转换

将：
```sql
CREATE VIEW `view_name` AS SELECT ...;
```

转换为：
```sql
CREATE OR REPLACE VIEW `view_name` AS SELECT ...;
```

### 3. 验证脚本

改造完成后，验证脚本是否符合要求：

- ✅ 语法正确（使用 SQL Linter 检查）
- ✅ 逻辑正确（符合预期的幂等性行为）
- ✅ 保留原有功能（改造前后首次执行结果一致）

### 4. 输出结果

输出改造后的脚本，并附上改造摘要，包括：
- 改造的语句数量
- 应用的转换类型
- 任何需要注意的警告

## 验证检查清单

在将改造后的脚本部署到生产环境前，请确保通过以下验证：

| 检查项 | 验证方法 |
|--------|----------|
| ✅ 语法正确 | 使用 SQL Linter 检查 |
| ✅ 首次执行成功 | 在测试数据库执行 |
| ✅ 重复执行不报错 | 连续执行两次验证 |
| ✅ 行为一致性 | 对比改造前后首次执行结果 |
| ✅ 无数据丢失 | 对比数据一致性和完整性 |

## 使用示例

用户提供一个 SQL 脚本：

```sql
-- 非幂等版本
ALTER TABLE `users` ADD COLUMN `phone` VARCHAR(20);
CREATE INDEX `idx_email` ON `users` (`email`);
```

经过该 Skill 改造后输出：

```sql
-- 幂等版本
SET @col_exists = 0;
SELECT COUNT(*) INTO @col_exists
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'users'
  AND COLUMN_NAME = 'phone';

SET @sql = IF(@col_exists = 0,
    'ALTER TABLE `users` ADD COLUMN `phone` VARCHAR(20)',
    'SELECT ''Skip: column already exists'' AS message');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @index_exists = 0;
SELECT COUNT(*) INTO @index_exists
FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'users'
  AND INDEX_NAME = 'idx_email';

SET @sql = IF(@index_exists = 0,
    'CREATE INDEX `idx_email` ON `users` (`email`)',
    'SELECT ''Skip: index already exists'' AS message');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

## 注意事项

1. **数据库名称**: 该 Skill 针对 MySQL 8+ 数据库设计，使用 `INFORMATION_SCHEMA` 进行存在性检查
2. **事务处理**: 改造后的脚本应在事务中执行，以确保原子性
3. **回滚脚本**: 幂等化改造不应影响回滚脚本的编写
4. **性能影响**: 存在性检查会轻微增加脚本执行时间，但确保了安全性
5. **保留注释**: 尽可能保留原有脚本中的注释，以增强可读性

## 扩展性

如需支持其他数据库或更多的操作类型，请参考 `scripts/idempotent_patterns.md` 中的模式参考。

## 参考资源

- [Flyway 幂等性改造验证报告](../../doc/EZPAY-768_2025-12-16_Flyway脚本幂等性改造验证报告.md)
- [Flyway 官方文档 - SQL-based migrations](https://flywaydb.org/documentation/concepts/migrations#sql-based-migrations)
- [MySQL INFORMATION_SCHEMA 文档](https://dev.mysql.com/doc/refman/8.0/en/information-schema.html)
