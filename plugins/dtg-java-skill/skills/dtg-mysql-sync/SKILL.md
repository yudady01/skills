---
name: dtg-mysql-sync
description: This skill should be used when the user enters "dtg-mysql-sync <table_name>" or asks to "sync MySQL data", "copy MySQL table", "MySQL data replication", "database sync", or mentions MySQL 8 data synchronization between nodes. Provides MySQL 8 database table data synchronization from Node 1 to Node 2 with data clearing and transaction safety. If the user enters dtg-mysql-sync without a table name, ask for the table name.
version: 3.0.0
tags: ["mysql", "data-sync", "replication", "mysql-8", "database-operations", "xxpay"]
---

# MySQL 8 数据同步

用于同步 MySQL 8 数据库的表数据，从 Node 1（源）完整复制到 Node 2（目标）。

## 使用方式

```bash
# 基本用法
python3 ${CLAUDE_PLUGIN_ROOT}/skills/dtg-mysql-sync/scripts/mysql_sync.py --table <table_name>

# 强制同步（跳过确认）
python3 ${CLAUDE_PLUGIN_ROOT}/skills/dtg-mysql-sync/scripts/mysql_sync.py --table <table_name> --force

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

- 自动清除目标表数据
- 批量复制数据（每批 1000 行）
- 事务安全（失败自动回滚）
- 进度反馈
- 详细的同步报告

## 依赖

```bash
pip install pymysql rich
```

## 参考

详细说明见 `references/mysql-sync-best-practices.md`
