-- ============================================================
-- Flyway 幂等性改造示例
-- ============================================================
-- 本文件展示了将非幂等 Flyway SQL 迁移脚本改造为幂等版本
-- 的实际对比示例。
-- ============================================================

-- ============================================================
-- 示例 1: 添加列 + 添加索引
-- ============================================================

-- ============================================================
-- [改造前] 非幂等版本
-- ============================================================
/*
-- 问题：重复执行会报错 "Duplicate column name" 和 "Duplicate key name"
ALTER TABLE `users` ADD COLUMN `phone` VARCHAR(20) NOT NULL DEFAULT '';
ALTER TABLE `users` ADD INDEX `idx_phone` (`phone`);
*/

-- ============================================================
-- [改造后] 幂等版本
-- ============================================================
-- 添加列：检查列是否存在
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

-- 添加索引：检查索引是否存在
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

-- ============================================================
-- 示例 2: 表备份 + 数据迁移
-- ============================================================

-- ============================================================
-- [改造前] 非幂等版本
-- ============================================================
/*
-- 问题：重复执行会报错 "Table 'backup_table' already exists"
RENAME TABLE `users` TO `users_backup_20241216`;

-- 创建新表
CREATE TABLE `users_new` (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL DEFAULT '',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY idx_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 问题：重复执行会因为唯一键冲突报错
INSERT INTO `users_new` (id, name, email, phone, created_at)
SELECT id, name, email, phone, created_at
FROM `users_backup_20241216`;
*/

-- ============================================================
-- [改造后] 幂等版本
-- ============================================================
-- 备份表：检查目标表是否存在
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

-- 创建新表：使用 IF NOT EXISTS
CREATE TABLE IF NOT EXISTS `users_new` (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL DEFAULT '',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY idx_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 数据迁移：使用 INSERT IGNORE 处理冲突
INSERT IGNORE INTO `users_new` (id, name, email, phone, created_at)
SELECT id, name, email, phone, created_at
FROM `users_backup_20241216`;

-- ============================================================
-- 示例 3: 创建视图
-- ============================================================

-- ============================================================
-- [改造前] 非幂等版本
-- ============================================================
/*
-- 问题：重复执行会报错 "Table 'view_name' already exists"
CREATE VIEW `user_active_view` AS
SELECT id, name, email
FROM users
WHERE status = 'active';
*/

-- ============================================================
-- [改造后] 幂等版本
-- ============================================================
-- 创建视图：使用 CREATE OR REPLACE
CREATE OR REPLACE VIEW `user_active_view` AS
SELECT id, name, email
FROM users_new
WHERE status = 'active';

-- ============================================================
-- 示例 4: 复杂场景 - 多表联合操作
-- ============================================================

-- ============================================================
-- [改造前] 非幂等版本
-- ============================================================
/*
-- 添加新列到订单表
ALTER TABLE `orders` ADD COLUMN `customer_phone` VARCHAR(20);

-- 添加索引
ALTER TABLE `orders` ADD INDEX `idx_customer_phone` (`customer_phone`);
ALTER TABLE `orders` ADD UNIQUE INDEX `idx_order_reference` (`order_reference`);

-- 备份旧数据
RENAME TABLE `orders` TO `orders_backup_20241216`;

-- 创建新订单表（带完整结构）
CREATE TABLE `orders_new` (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    order_reference VARCHAR(50) NOT NULL,
    customer_id BIGINT UNSIGNED NOT NULL,
    customer_phone VARCHAR(20) NOT NULL DEFAULT '',
    total_amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY idx_order_reference (order_reference),
    KEY idx_customer_id (customer_id),
    KEY idx_customer_phone (customer_phone),
    KEY idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 迁移数据
INSERT INTO `orders_new` (id, order_reference, customer_id, total_amount, status, created_at, updated_at)
SELECT id, order_reference, customer_id, total_amount, status, created_at, updated_at
FROM `orders_backup_20241216`;
*/

-- ============================================================
-- [改造后] 幂等版本
-- ============================================================
-- 1. 添加新列到订单表
SET @col_exists = 0;
SELECT COUNT(*) INTO @col_exists
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'orders'
  AND COLUMN_NAME = 'customer_phone';

SET @sql = IF(@col_exists = 0,
    'ALTER TABLE `orders` ADD COLUMN `customer_phone` VARCHAR(20) NOT NULL DEFAULT ''''',
    'SELECT ''Skip: column customer_phone already exists'' AS message');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- 2. 添加索引（普通索引）
SET @index_exists = 0;
SELECT COUNT(*) INTO @index_exists
FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'orders'
  AND INDEX_NAME = 'idx_customer_phone';

SET @sql = IF(@index_exists = 0,
    'ALTER TABLE `orders` ADD INDEX `idx_customer_phone` (`customer_phone`)',
    'SELECT ''Skip: index idx_customer_phone already exists'' AS message');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- 3. 添加唯一索引
SET @index_exists = 0;
SELECT COUNT(*) INTO @index_exists
FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'orders'
  AND INDEX_NAME = 'idx_order_reference';

SET @sql = IF(@index_exists = 0,
    'ALTER TABLE `orders` ADD UNIQUE INDEX `idx_order_reference` (`order_reference`)',
    'SELECT ''Skip: index idx_order_reference already exists'' AS message');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- 4. 备份旧数据
SET @backup_exists = 0;
SELECT COUNT(*) INTO @backup_exists
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'orders_backup_20241216';

SET @sql = IF(@backup_exists = 0,
    'RENAME TABLE `orders` TO `orders_backup_20241216`',
    'SELECT ''Skip: backup table orders_backup_20241216 already exists'' AS message');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- 5. 创建新订单表（带完整结构）
CREATE TABLE IF NOT EXISTS `orders_new` (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    order_reference VARCHAR(50) NOT NULL,
    customer_id BIGINT UNSIGNED NOT NULL,
    customer_phone VARCHAR(20) NOT NULL DEFAULT '',
    total_amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY idx_order_reference (order_reference),
    KEY idx_customer_id (customer_id),
    KEY idx_customer_phone (customer_phone),
    KEY idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 6. 迁移数据（使用 INSERT IGNORE 处理可能的冲突）
INSERT IGNORE INTO `orders_new` (id, order_reference, customer_id, customer_phone, total_amount, status, created_at, updated_at)
SELECT id, order_reference, customer_id,
    IFNULL(customer_phone, '') AS customer_phone,
    total_amount, status, created_at, updated_at
FROM `orders_backup_20241216`;

-- ============================================================
-- 验证提示
-- ============================================================
/*
要验证幂等性，请执行以下步骤：

1. 在测试数据库中首次执行改造后的脚本
   - 应该成功执行，完成所有操作

2. 在同一数据库中再次执行改造后的脚本
   - 应该成功执行，显示 "Skip" 消息
   - 不应该报任何错误

3. 对比数据：
   - 检查表结构是否正确
   - 检查索引是否正确创建
   - 检查数据是否完整
   - 对比改造前后首次执行结果应一致

4. 检查输出：
   - 每个幂等操作应显示 "Skip" 消息（已存在时）或实际执行结果
   - 使用 SHOW WARNINGS 查看是否有警告
*/
