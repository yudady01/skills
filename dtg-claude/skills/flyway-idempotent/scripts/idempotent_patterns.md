# Flyway 幂等性模式速查表

本文档提供 Flyway SQL 迁移脚本幂等性改造的各种模式参考，适用于 MySQL 8+ 数据库。

---

## 目录

- [ADD COLUMN 模式](#add-column-模式)
- [ADD INDEX 模式](#add-index-模式)
- [INSERT IGNORE 模式](#insert-ignore-模式)
- [RENAME TABLE 模式](#rename-table-模式)
- [CREATE TABLE 模式](#create-table-模式)
- [CREATE VIEW 模式](#create-view-模式)

---

## ADD COLUMN 模式

### 使用场景

向现有表添加新列时，需要确保如果列已存在则跳过操作。

### 模式模板

```sql
-- 检查列是否存在
SET @col_exists = 0;
SELECT COUNT(*) INTO @col_exists
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = '{TABLE_NAME}'
  AND COLUMN_NAME = '{COLUMN_NAME}';

-- 条件执行
SET @sql = IF(@col_exists = 0,
    'ALTER TABLE `{TABLE_NAME}` ADD COLUMN `{COLUMN_NAME}` {COLUMN_DEFINITION}',
    'SELECT ''Skip: column already exists'' AS message');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

### 替换变量

| 变量 | 说明 | 示例 |
|------|------|------|
| `{TABLE_NAME}` | 表名 | `users` |
| `{COLUMN_NAME}` | 列名 | `phone` |
| `{COLUMN_DEFINITION}` | 列完整定义 | `VARCHAR(20) NOT NULL DEFAULT ''` |

### 实际示例

```sql
-- 检查列是否存在
SET @col_exists = 0;
SELECT COUNT(*) INTO @col_exists
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'users'
  AND COLUMN_NAME = 'phone';

-- 条件执行
SET @sql = IF(@col_exists = 0,
    'ALTER TABLE `users` ADD COLUMN `phone` VARCHAR(20) NOT NULL DEFAULT ''''',
    'SELECT ''Skip: column already exists'' AS message');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

### 注意事项

- 反引号（`）用于引用表名和列名，以处理保留字或特殊字符
- 单引号在 SET @sql 中需要转义为两个单引号（''）

---

## ADD INDEX 模式

### 使用场景

向表添加索引时，需要确保如果索引已存在则跳过操作。

### 模式模板

```sql
-- 检查索引是否存在
SET @index_exists = 0;
SELECT COUNT(*) INTO @index_exists
FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = '{TABLE_NAME}'
  AND INDEX_NAME = '{INDEX_NAME}';

-- 条件执行
SET @sql = IF(@index_exists = 0,
    'ALTER TABLE `{TABLE_NAME}` ADD {INDEX_TYPE} `{INDEX_NAME}` ({INDEX_COLUMNS}) {INDEX_OPTIONS}',
    'SELECT ''Skip: index already exists'' AS message');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

### 替换变量

| 变量 | 说明 | 示例 |
|------|------|------|
| `{TABLE_NAME}` | 表名 | `users` |
| `{INDEX_NAME}` | 索引名 | `idx_email` |
| `{INDEX_TYPE}` | 索引类型 | `INDEX`, `UNIQUE INDEX`, `FULLTEXT INDEX` |
| `{INDEX_COLUMNS}` | 索引列 | `(`email`)`, `(`first_name`, `last_name`)` |
| `{INDEX_OPTIONS}` | 索引选项 | `USING BTREE`, `USING HASH` |

### 实际示例

```sql
-- 检查索引是否存在
SET @index_exists = 0;
SELECT COUNT(*) INTO @index_exists
FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'users'
  AND INDEX_NAME = 'idx_email';

-- 条件执行
SET @sql = IF(@index_exists = 0,
    'ALTER TABLE `users` ADD INDEX `idx_email` (`email`) USING BTREE',
    'SELECT ''Skip: index already exists'' AS message');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

### 注意事项

- 注意区分主键索引（PRIMARY）和普通索引
- 复合索引使用逗号分隔列名

---

## INSERT IGNORE 模式

### 使用场景

将数据从一个表迁移到另一个表时，使用 INSERT IGNORE 自动处理主键或唯一键冲突。

### 模式模板

```sql
INSERT IGNORE INTO `{TARGET_TABLE}` ({TARGET_COLUMNS})
SELECT {SOURCE_COLUMNS}
FROM `{SOURCE_TABLE}`
WHERE {WHERE_CONDITION};
```

### 替换变量

| 变量 | 说明 | 示例 |
|------|------|------|
| `{TARGET_TABLE}` | 目标表名 | `users_archive` |
| `{TARGET_COLUMNS}` | 目标列 | `id, name, email` |
| `{SOURCE_COLUMNS}` | 源列 | `id, user_name, user_email` |
| `{SOURCE_TABLE}` | 源表名 | `users` |
| `{WHERE_CONDITION}` | 筛选条件 | `created_at < '2024-01-01'` |

### 实际示例

```sql
INSERT IGNORE INTO `users_archive` (id, name, email, created_at)
SELECT id, name, email, created_at
FROM `users`
WHERE is_deleted = 1;
```

### 注意事项

- INSERT IGNORE 会静默跳过冲突记录，不会报错
- 如果需要知道跳过了多少记录，可以通过 ROW_COUNT() 检查
- 确保目标表有适当的主键或唯一索引，否则 IGNORE 不会生效

---

## RENAME TABLE 模式

### 使用场景

重命名表（例如备份表）时，需要确保目标表名未被占用。

### 模式模板

```sql
-- 检查目标表是否已存在
SET @backup_exists = 0;
SELECT COUNT(*) INTO @backup_exists
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = '{TARGET_TABLE}';

-- 条件执行
SET @sql = IF(@backup_exists = 0,
    'RENAME TABLE `{SOURCE_TABLE}` TO `{TARGET_TABLE}`',
    'SELECT ''Skip: backup table already exists'' AS message');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

### 替换变量

| 变量 | 说明 | 示例 |
|------|------|------|
| `{SOURCE_TABLE}` | 源表名 | `users` |
| `{TARGET_TABLE}` | 目标表名 | `users_backup_20241216` |

### 实际示例

```sql
-- 检查目标表是否已存在
SET @backup_exists = 0;
SELECT COUNT(*) INTO @backup_exists
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'users_backup_20241216';

-- 条件执行
SET @sql = IF(@backup_exists = 0,
    'RENAME TABLE `users` TO `users_backup_20241216`',
    'SELECT ''Skip: backup table already exists'' AS message');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

### 注意事项

- RENAME TABLE 是原子操作，会自动获取表的元数据锁
- 确保在重命名前没有其他会话持有表的锁

---

## CREATE TABLE 模式

### 使用场景

创建表时，确保如果表已存在则跳过操作。

### 模式模板

```sql
CREATE TABLE IF NOT EXISTS `{TABLE_NAME}` (
    {COLUMN_DEFINITIONS}
    {CONSTRAINTS}
) {ENGINE} {CHARSET};
```

### 替换变量

| 变量 | 说明 | 示例 |
|------|------|------|
| `{TABLE_NAME}` | 表名 | `audit_logs` |
| `{COLUMN_DEFINITIONS}` | 列定义 | `id BIGINT PRIMARY KEY, action VARCHAR(50)` |
| `{CONSTRAINTS}` | 约束定义 | `KEY idx_action (action)` |
| `{ENGINE}` | 存储引擎 | `ENGINE=InnoDB` |
| `{CHARSET}` | 字符集 | `DEFAULT CHARSET=utf8mb4` |

### 实际示例

```sql
CREATE TABLE IF NOT EXISTS `audit_logs` (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    user_id BIGINT UNSIGNED NOT NULL,
    action VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY idx_user_action (user_id, action)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

### 注意事项

- IF NOT EXISTS 仅检查表是否存在，不会检查表结构是否一致
- 如果表已存在但结构不同，CREATE TABLE IF NOT EXISTS 会静默跳过

---

## CREATE VIEW 模式

### 使用场景

创建或更新视图时，确保操作幂等。

### 模式模板

```sql
CREATE OR REPLACE VIEW `{VIEW_NAME}` AS
SELECT {SELECT_LIST}
FROM {TABLE_SOURCE}
WHERE {WHERE_CONDITION};
```

### 替换变量

| 变量 | 说明 | 示例 |
|------|------|------|
| `{VIEW_NAME}` | 视图名 | `user_active_view` |
| `{SELECT_LIST}` | 选择列表 | `id, name, email` |
| `{TABLE_SOURCE}` | 表源 | `users LEFT JOIN profiles ON users.id = profiles.user_id` |
| `{WHERE_CONDITION}` | 筛选条件 | `users.status = 'active'` |

### 实际示例

```sql
CREATE OR REPLACE VIEW `user_active_view` AS
SELECT u.id, u.name, u.email, p.avatar_url
FROM users u
LEFT JOIN profiles p ON u.id = p.user_id
WHERE u.status = 'active';
```

### 注意事项

- CREATE OR REPLACE VIEW 会替换已存在的同名视图
- 确保视图的查询结果符合预期，替换是不可逆的

---

## 组合使用示例

```sql
-- 示例：多个幂等操作的组合

-- 1. 添加新列
SET @col_exists = 0;
SELECT COUNT(*) INTO @col_exists
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'users'
  AND COLUMN_NAME = 'phone';

SET @sql = IF(@col_exists = 0,
    'ALTER TABLE `users` ADD COLUMN `phone` VARCHAR(20) NOT NULL DEFAULT ''''',
    'SELECT ''Skip: column already exists'' AS message');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- 2. 添加索引
SET @index_exists = 0;
SELECT COUNT(*) INTO @index_exists
FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'users'
  AND INDEX_NAME = 'idx_phone';

SET @sql = IF(@index_exists = 0,
    'ALTER TABLE `users` ADD INDEX `idx_phone` (`phone`)',
    'SELECT ''Skip: index already exists'' AS message');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- 3. 备份数据
SET @backup_exists = 0;
SELECT COUNT(*) INTO @backup_exists
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'users_backup_20241216';

SET @sql = IF(@backup_exists = 0,
    'RENAME TABLE `users` TO `users_backup_20241216`',
    'SELECT ''Skip: backup table already exists'' AS message');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- 4. 创建新表
CREATE TABLE IF NOT EXISTS `users_new` (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL DEFAULT '',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY idx_email (email),
    KEY idx_phone (phone)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 5. 迁移数据
INSERT IGNORE INTO `users_new` (id, name, email, phone, created_at)
SELECT id, name, email, phone, created_at
FROM `users_backup_20241216`;
```

---

## 参考资源

- [Flyway 幂等性改造验证报告](../../../doc/EZPAY-768_2025-12-16_Flyway脚本幂等性改造验证报告.md)
- [MySQL INFORMATION_SCHEMA 文档](https://dev.mysql.com/doc/refman/8.0/en/information-schema.html)
- [MySQL PREPARE 语句文档](https://dev.mysql.com/doc/refman/8.0/en/sql-prepared-statements.html)
