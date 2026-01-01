#!/usr/bin/env python3
"""
MySQL 8 数据同步工具
用于将 MySQL Node 1 的表数据完整复制到 Node 2
支持自动清除目标表数据、事务安全和进度反馈
"""

import argparse
import sys
from typing import Optional, List, Dict, Any
from dataclasses import dataclass

import pymysql
from pymysql.cursors import DictCursor

try:
    from rich.console import Console
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
    from rich.table import Table
    from rich.panel import Panel
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False


if RICH_AVAILABLE:
    console = Console()
else:
    # 简单的控制台输出回退
    class Console:
        def print(self, msg, **kwargs):
            # 移除 rich 标签
            import re
            clean_msg = re.sub(r'\[.*?\]', '', msg)
            print(clean_msg)

        def status(self, msg):
            return self

        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

    console = Console()


@dataclass
class MySQLConnection:
    """MySQL 连接配置"""
    host: str
    port: int
    database: str
    user: str
    password: str
    charset: str = 'utf8mb4'


class MySQLSyncError(Exception):
    """MySQL 同步错误基类"""
    pass


class MySQLConnectionError(MySQLSyncError):
    """MySQL 连接错误"""
    pass


class MySQLTableNotFoundError(MySQLSyncError):
    """表不存在错误"""
    pass


class MySQLDataSyncError(MySQLSyncError):
    """数据同步错误"""
    pass


class MySQLDataSynchronizer:
    """MySQL 数据同步器"""

    # 默认连接配置
    NODE1_CONFIG = MySQLConnection(
        host='127.0.0.1',
        port=3307,
        database='xxpay',
        user='dtgMysqlTest',
        password='nhXzDmmxvSdBB37VKuFU8NJdx7bjrw'
    )

    NODE2_CONFIG = MySQLConnection(
        host='127.0.0.1',
        port=3306,
        database='xxpay',
        user='root',
        password='123456'
    )

    # 批量插入大小
    BATCH_SIZE = 1000

    def __init__(self, source: MySQLConnection, target: MySQLConnection):
        """
        初始化同步器

        Args:
            source: 源数据库配置 (Node 1)
            target: 目标数据库配置 (Node 2)
        """
        self.source = source
        self.target = target
        self.source_conn: Optional[pymysql.Connection] = None
        self.target_conn: Optional[pymysql.Connection] = None

    def connect(self) -> None:
        """建立数据库连接，确保源数据库和目标数据库都能连接成功"""
        # 先连接源数据库
        try:
            with console.status("[bold yellow]连接源数据库..."):
                self.source_conn = pymysql.connect(
                    host=self.source.host,
                    port=self.source.port,
                    user=self.source.user,
                    password=self.source.password,
                    database=self.source.database,
                    charset=self.source.charset,
                    cursorclass=DictCursor
                )
            console.print(f"[green]✓[/green] 源数据库连接成功 ({self.source.host}:{self.source.port}/{self.source.database})")
        except pymysql.Error as e:
            console.print(f"[red]✗[/red] 源数据库连接失败: {e}")
            raise MySQLConnectionError(f"无法连接源数据库 {self.source.host}:{self.source.port}: {e}")

        # 再连接目标数据库
        try:
            with console.status("[bold yellow]连接目标数据库..."):
                self.target_conn = pymysql.connect(
                    host=self.target.host,
                    port=self.target.port,
                    user=self.target.user,
                    password=self.target.password,
                    database=self.target.database,
                    charset=self.target.charset,
                    cursorclass=DictCursor
                )
            console.print(f"[green]✓[/green] 目标数据库连接成功 ({self.target.host}:{self.target.port}/{self.target.database})")
        except pymysql.Error as e:
            # 目标数据库连接失败，关闭源数据库连接
            if self.source_conn:
                self.source_conn.close()
                self.source_conn = None
            console.print(f"[red]✗[/red] 目标数据库连接失败: {e}")
            raise MySQLConnectionError(f"无法连接目标数据库 {self.target.host}:{self.target.port}: {e}")

    def close(self) -> None:
        """关闭数据库连接"""
        if self.source_conn:
            self.source_conn.close()
        if self.target_conn:
            self.target_conn.close()

    def check_table_exists(self, table_name: str, is_source: bool = True) -> bool:
        """
        检查表是否存在

        Args:
            table_name: 表名
            is_source: 是否为源数据库

        Returns:
            表是否存在
        """
        conn = self.source_conn if is_source else self.target_conn
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*) as count
            FROM information_schema.tables
            WHERE table_schema = %s AND table_name = %s
        """, (self.source.database if is_source else self.target.database, table_name))

        result = cursor.fetchone()
        return result['count'] > 0

    def get_table_columns(self, table_name: str) -> List[str]:
        """
        获取表的列名

        Args:
            table_name: 表名

        Returns:
            列名列表
        """
        cursor = self.source_conn.cursor()
        cursor.execute("""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_schema = %s AND table_name = %s
            ORDER BY ordinal_position
        """, (self.source.database, table_name))

        return [row['COLUMN_NAME'] for row in cursor.fetchall()]

    def get_row_count(self, table_name: str, is_source: bool = True) -> int:
        """
        获取表的行数

        Args:
            table_name: 表名
            is_source: 是否为源数据库

        Returns:
            行数
        """
        conn = self.source_conn if is_source else self.target_conn
        cursor = conn.cursor()

        cursor.execute(f"SELECT COUNT(*) as count FROM {table_name}")
        result = cursor.fetchone()
        return result['count']

    def disable_foreign_key_checks(self) -> None:
        """禁用外键检查"""
        cursor = self.target_conn.cursor()
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

    def enable_foreign_key_checks(self) -> None:
        """启用外键检查"""
        cursor = self.target_conn.cursor()
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

    def clear_target_table(self, table_name: str) -> int:
        """
        清除目标表数据

        Args:
            table_name: 表名

        Returns:
            删除的行数
        """
        cursor = self.target_conn.cursor()
        cursor.execute(f"DELETE FROM {table_name}")
        return cursor.rowcount

    def insert_target_data(self, table_name: str, columns: List[str], data: List[Dict[str, Any]]) -> int:
        """
        批量插入数据到目标表

        Args:
            table_name: 表名
            columns: 列名列表
            data: 数据列表

        Returns:
            插入的行数
        """
        if not data:
            return 0

        cursor = self.target_conn.cursor()
        columns_str = ', '.join(columns)
        placeholders = ', '.join(['%s'] * len(columns))

        sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"

        # 准备批量数据
        values = [[row[col] for col in columns] for row in data]
        cursor.executemany(sql, values)
        return cursor.rowcount

    def sync_table(self, table_name: str, force: bool = False) -> Dict[str, Any]:
        """
        同步表数据

        Args:
            table_name: 表名
            force: 强制同步（跳过确认）

        Returns:
            同步结果字典
        """
        result = {
            'table_name': table_name,
            'source_rows': 0,
            'target_rows_before': 0,
            'deleted_rows': 0,
            'inserted_rows': 0,
            'success': False,
            'error': None
        }

        try:
            # 1. 检查源表是否存在
            if not self.check_table_exists(table_name, is_source=True):
                raise MySQLTableNotFoundError(f"源表 '{table_name}' 不存在")

            # 2. 检查目标表是否存在
            if not self.check_table_exists(table_name, is_source=False):
                raise MySQLTableNotFoundError(f"目标表 '{table_name}' 不存在")

            # 3. 获取表结构
            columns = self.get_table_columns(table_name)
            console.print(f"[cyan]检测到 {len(columns)} 个列[/cyan]")

            # 4. 获取源表行数
            source_rows = self.get_row_count(table_name, is_source=True)
            result['source_rows'] = source_rows
            console.print(f"[cyan]源表数据: {source_rows:,} 行[/cyan]")

            # 5. 获取目标表行数
            target_rows_before = self.get_row_count(table_name, is_source=False)
            result['target_rows_before'] = target_rows_before

            if target_rows_before > 0 and not force:
                console.print(f"[yellow]⚠ 目标表已有 {target_rows_before:,} 行数据[/yellow]")

            # 6. 开始同步
            with console.status("[bold yellow]开始同步..."):
                # 禁用外键检查
                self.disable_foreign_key_checks()

                try:
                    # 清除目标表数据
                    if target_rows_before > 0:
                        deleted = self.clear_target_table(table_name)
                        result['deleted_rows'] = deleted
                        console.print(f"[yellow]清除 {deleted:,} 行旧数据[/yellow]")

                    # 获取源数据并批量插入
                    if RICH_AVAILABLE:
                        with Progress(
                            SpinnerColumn(),
                            TextColumn("[progress.description]{task.description}"),
                            BarColumn(),
                            TaskProgressColumn(),
                            console=console
                        ) as progress:
                            task = progress.add_task(
                                f"[cyan]复制数据[/cyan]",
                                total=source_rows
                            )

                            inserted_total = self._batch_insert_with_progress(
                                table_name, columns, progress, task
                            )
                    else:
                        # 不使用 rich 的简单进度显示
                        inserted_total = self._batch_insert_simple(table_name, columns, source_rows)

                    result['inserted_rows'] = inserted_total

                    # 提交事务
                    self.target_conn.commit()
                    result['success'] = True

                    console.print(f"[green]✓ 同步完成: {inserted_total:,} 行[/green]")

                finally:
                    # 恢复外键检查
                    self.enable_foreign_key_checks()

        except Exception as e:
            # 回滚事务
            if self.target_conn:
                self.target_conn.rollback()

            result['error'] = str(e)
            result['success'] = False
            console.print(f"[red]✗ 同步失败: {e}[/red]")

        return result

    def _batch_insert_with_progress(self, table_name: str, columns: List[str], progress, task) -> int:
        """使用 Rich 进度条的批量插入"""
        inserted_total = 0
        offset = 0
        source_rows = progress.tasks[task].total

        while offset < source_rows:
            # 分批获取数据
            cursor = self.source_conn.cursor(DictCursor)
            columns_str = ', '.join(columns)
            cursor.execute(
                f"SELECT {columns_str} FROM {table_name} LIMIT {self.BATCH_SIZE} OFFSET {offset}"
            )
            batch_data = cursor.fetchall()

            # 插入目标表
            if batch_data:
                inserted = self.insert_target_data(table_name, columns, batch_data)
                inserted_total += inserted

            progress.update(task, advance=len(batch_data))
            offset += len(batch_data)

        return inserted_total

    def _batch_insert_simple(self, table_name: str, columns: List[str], source_rows: int) -> int:
        """简单的批量插入（不使用 Rich）"""
        inserted_total = 0
        offset = 0

        while offset < source_rows:
            # 分批获取数据
            cursor = self.source_conn.cursor(DictCursor)
            columns_str = ', '.join(columns)
            cursor.execute(
                f"SELECT {columns_str} FROM {table_name} LIMIT {self.BATCH_SIZE} OFFSET {offset}"
            )
            batch_data = cursor.fetchall()

            # 插入目标表
            if batch_data:
                inserted = self.insert_target_data(table_name, columns, batch_data)
                inserted_total += inserted
                print(f"  进度: {min(offset + len(batch_data), source_rows)}/{source_rows} 行")

            offset += len(batch_data)

        return inserted_total

    def display_sync_report(self, results: List[Dict[str, Any]]) -> None:
        """
        显示同步报告

        Args:
            results: 同步结果列表
        """
        if RICH_AVAILABLE:
            table = Table(title="数据同步报告", show_header=True, header_style="bold magenta")
            table.add_column("表名", style="cyan", no_wrap=False)
            table.add_column("源行数", justify="right", style="green")
            table.add_column("删除", justify="right", style="yellow")
            table.add_column("插入", justify="right", style="green")
            table.add_column("状态", justify="center")

            for result in results:
                status = "[green]成功[/green]" if result['success'] else "[red]失败[/red]"
                table.add_row(
                    result['table_name'],
                    f"{result['source_rows']:,}",
                    f"{result['deleted_rows']:,}",
                    f"{result['inserted_rows']:,}",
                    status
                )

            console.print(table)

            # 统计信息
            total_source = sum(r['source_rows'] for r in results)
            total_deleted = sum(r['deleted_rows'] for r in results)
            total_inserted = sum(r['inserted_rows'] for r in results)
            success_count = sum(1 for r in results if r['success'])

            console.print(Panel(
                f"[bold]总计:[/bold]\n"
                f"  源数据: {total_source:,} 行\n"
                f"  删除: {total_deleted:,} 行\n"
                f"  插入: {total_inserted:,} 行\n"
                f"  成功: {success_count}/{len(results)} 表",
                title="同步统计",
                border_style="blue"
            ))
        else:
            # 简单的文本报告
            print("\n=== 数据同步报告 ===")
            for result in results:
                status = "成功" if result['success'] else "失败"
                print(f"{result['table_name']}: 源={result['source_rows']:,}, "
                      f"删除={result['deleted_rows']:,}, 插入={result['inserted_rows']:,}, "
                      f"状态={status}")


def parse_args() -> tuple:
    """
    解析命令行参数

    Returns:
        (table_name, force, source_config, target_config)
    """
    parser = argparse.ArgumentParser(
        description='MySQL 8 数据同步工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s --table pay_order
  %(prog)s -t pay_order --force
  %(prog)s -t pay_order --source-host 192.168.1.100 --source-port 3307
        """
    )

    parser.add_argument(
        '-t', '--table',
        required=True,
        help='要同步的表名（必需）'
    )

    parser.add_argument(
        '-f', '--force',
        action='store_true',
        help='强制同步，跳过确认'
    )

    # 源数据库配置（可选）
    parser.add_argument('--source-host', default='127.0.0.1', help='源数据库主机')
    parser.add_argument('--source-port', type=int, default=3307, help='源数据库端口')
    parser.add_argument('--source-database', default='xxpay', help='源数据库名')
    parser.add_argument('--source-user', default='dtgMysqlTest', help='源数据库用户')
    parser.add_argument('--source-password', default='nhXzDmmxvSdBB37VKuFU8NJdx7bjrw', help='源数据库密码')

    # 目标数据库配置（可选）
    parser.add_argument('--target-host', default='127.0.0.1', help='目标数据库主机')
    parser.add_argument('--target-port', type=int, default=3306, help='目标数据库端口')
    parser.add_argument('--target-database', default='xxpay', help='目标数据库名')
    parser.add_argument('--target-user', default='root', help='目标数据库用户')
    parser.add_argument('--target-password', default='123456', help='目标数据库密码')

    args = parser.parse_args()

    # 构建连接配置
    source_config = MySQLConnection(
        host=args.source_host,
        port=args.source_port,
        database=args.source_database,
        user=args.source_user,
        password=args.source_password
    )

    target_config = MySQLConnection(
        host=args.target_host,
        port=args.target_port,
        database=args.target_database,
        user=args.target_user,
        password=args.target_password
    )

    return args.table, args.force, source_config, target_config


def main() -> int:
    """主函数"""
    try:
        console.print("[bold cyan]MySQL 8 数据同步工具[/bold cyan]\n")

        # 解析参数
        table_name, force, source_config, target_config = parse_args()

        # 创建同步器
        synchronizer = MySQLDataSynchronizer(source_config, target_config)

        # 连接数据库
        synchronizer.connect()

        # 执行同步
        result = synchronizer.sync_table(table_name, force=force)

        # 显示报告
        synchronizer.display_sync_report([result])

        # 关闭连接
        synchronizer.close()

        # 返回状态码
        return 0 if result['success'] else 1

    except KeyboardInterrupt:
        console.print("\n[yellow]操作已取消[/yellow]")
        return 130
    except MySQLSyncError as e:
        console.print(f"[red]错误: {e}[/red]")
        return 1
    except Exception as e:
        console.print(f"[red]未预期的错误: {e}[/red]")
        return 1


if __name__ == '__main__':
    sys.exit(main())
