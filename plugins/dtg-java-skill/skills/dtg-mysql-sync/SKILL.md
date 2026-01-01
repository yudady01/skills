---
name: dtg-mysql-sync
description: This skill should be used when the user enters "dtg-mysql-sync <table_name>" or asks to "sync MySQL data", "copy MySQL table", "MySQL data replication", "database sync", or mentions MySQL 8 data synchronization between nodes. Provides MySQL 8 database table data synchronization from Node 1 to Node 2 with data clearing, batch processing, and time filtering. If the user enters dtg-mysql-sync without a table name, ask for the table name.
version: 3.0.0
tags: ["mysql", "data-sync", "replication", "mysql-8", "database-operations", "xxpay"]
---

# MySQL 8 数据同步

用于同步 MySQL 8 数据库的表数据，从 Node 1（源）完整复制到 Node 2（目标）。

## 使用方式

```bash
# 预览模式（推荐先使用预览模式查看同步信息）
python3 ${CLAUDE_PLUGIN_ROOT}/skills/dtg-mysql-sync/scripts/mysql_sync.py --table <table_name> --dry-run

# 基本用法（默认同步最近 10 天数据）
python3 ${CLAUDE_PLUGIN_ROOT}/skills/dtg-mysql-sync/scripts/mysql_sync.py --table <table_name>

# 强制同步（跳过确认）
python3 ${CLAUDE_PLUGIN_ROOT}/skills/dtg-mysql-sync/scripts/mysql_sync.py --table <table_name> --force

# 同步指定天数的数据
python3 ${CLAUDE_PLUGIN_ROOT}/skills/dtg-mysql-sync/scripts/mysql_sync.py --table <table_name> --days 7

# 同步全部数据
python3 ${CLAUDE_PLUGIN_ROOT}/skills/dtg-mysql-sync/scripts/mysql_sync.py --table <table_name> --days 0

# 自定义连接
python3 ${CLAUDE_PLUGIN_ROOT}/skills/dtg-mysql-sync/scripts/mysql_sync.py \
  --table <table_name> \
  --source-host <host> --source-port <port> \
  --target-host <host> --target-port <port>
```

## 数据库连接配置

| 节点 | Host | Port | Database | User |
|------|------|------|----------|------|
| Node 1 (源) | 127.0.0.1 | 3307 | xxpay | dtgMysqlTest |
| Node 2 (目标) | 127.0.0.1 | 3306 | xxpay | root |

## 功能

- **时间过滤**: 默认同步最近 10 天数据（自动检测时间字段）
- **无事务模式**: 每批独立提交，避免大事务限制
- **容错处理**: 失败批次继续处理，显示详细错误
- **自动清除**: 同步前清除目标表数据
- **批量复制**: 每批 1000 行，适合大数据量
- **进度反馈**: 实时显示同步进度
- **详细报告**: 显示成功/失败批次详情

## 参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--table` | 必需 | 要同步的表名 |
| `--dry-run` | false | 预览模式，显示同步信息但不执行实际操作 |
| `--days` | 10 | 只同步最近 N 天的数据（0 = 全部） |
| `--force` | false | 跳过确认直接执行 |

## 依赖

```bash
pip install pymysql rich
```

## 参考

详细说明见 `references/mysql-sync-best-practices.md`
