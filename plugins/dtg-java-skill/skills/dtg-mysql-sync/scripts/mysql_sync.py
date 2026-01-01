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
from datetime import datetime, timedelta

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

    def find_create_time_column(self, table_name: str) -> Optional[str]:
        """
        查找表的创建时间字段

        Args:
            table_name: 表名

        Returns:
            创建时间字段名，如果找不到则返回 None
        """
        cursor = self.source_conn.cursor()
        cursor.execute("""
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_schema = %s AND table_name = %s
        """, (self.source.database, table_name))

        columns = {row['COLUMN_NAME']: row['DATA_TYPE'] for row in cursor.fetchall()}

        # 常见的创建时间字段名（按优先级排序，大小写不敏感）
        time_column_patterns = [
            'CreateTime',
            'create_time',
            'created_at',
            'create_at',
            'ctime',
            'created_time',
            'gmt_create',
            'add_time',
            'reg_time'
        ]

        # 查找匹配的字段（大小写不敏感）
        for pattern in time_column_patterns:
            for column_name in columns.keys():
                if column_name.lower() == pattern.lower():
                    # 确保是时间类型
                    if columns[column_name] in ['datetime', 'timestamp', 'date', 'time']:
                        return column_name  # 返回实际的字段名（保持原始大小写）

        return None

    def get_row_count(self, table_name: str, is_source: bool = True, days: Optional[int] = None, time_column: Optional[str] = None) -> int:
        """
        获取表的行数

        Args:
            table_name: 表名
            is_source: 是否为源数据库
            days: 天数过滤（仅源数据库）
            time_column: 时间字段名

        Returns:
            行数
        """
        conn = self.source_conn if is_source else self.target_conn
        cursor = conn.cursor()

        sql = f"SELECT COUNT(*) as count FROM {table_name}"

        # 添加时间过滤条件
        if is_source and days and time_column:
            date_threshold = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d %H:%M:%S')
            sql += f" WHERE {time_column} >= '{date_threshold}'"

        cursor.execute(sql)
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

    def _display_sync_info(self, table_name: str, source_rows: int, target_rows: int, column_count: int, time_filter: Optional[str] = None) -> None:
        """
        显示同步信息给用户确认

        Args:
            table_name: 表名
            source_rows: 源表行数
            target_rows: 目标表行数
            column_count: 列数
            time_filter: 时间过滤条件
        """
        if RICH_AVAILABLE:
            # 使用 Rich 显示漂亮的表格
            from rich.table import Table as RichTable
            from rich.panel import Panel

            # 创建信息表格
            info_table = RichTable(title="📋 同步信息", show_header=True, header_style="bold cyan")
            info_table.add_column("项目", style="cyan")
            info_table.add_column("值", style="yellow")

            # 源数据库信息
            info_table.add_row("源数据库", f"{self.source.host}:{self.source.port}/{self.source.database}")
            info_table.add_row("目标数据库", f"{self.target.host}:{self.target.port}/{self.target.database}")
            info_table.add_row("表名", f"[bold]{table_name}[/bold]")
            info_table.add_row("列数", f"{column_count}")
            if time_filter:
                info_table.add_row("时间过滤", f"[cyan]{time_filter}[/cyan]")
            info_table.add_row("源表数据量", f"{source_rows:,} 行")
            info_table.add_row("目标表现有数据", f"{target_rows:,} 行")

            console.print(info_table)

            # 警告信息
            if target_rows > 0:
                console.print(Panel(
                    f"[bold red]⚠️  警告: 目标表已有 {target_rows:,} 行数据[/bold red]\n"
                    f"[yellow]这些数据将被清除并替换为源表数据[/yellow]",
                    title="操作提示",
                    border_style="red"
                ))
            else:
                console.print(Panel(
                    f"[green]✓ 目标表为空，将直接复制数据[/green]",
                    title="操作提示",
                    border_style="green"
                ))
        else:
            # 简单文本输出
            print("\n=== 同步信息 ===")
            print(f"源数据库: {self.source.host}:{self.source.port}/{self.source.database}")
            print(f"目标数据库: {self.target.host}:{self.target.port}/{self.target.database}")
            print(f"表名: {table_name}")
            print(f"列数: {column_count}")
            print(f"源表数据量: {source_rows:,} 行")
            print(f"目标表现有数据: {target_rows:,} 行")
            if target_rows > 0:
                print(f"\n⚠️  警告: 目标表的 {target_rows:,} 行数据将被清除！")

    def _confirm_sync(self) -> bool:
        """
        请求用户确认是否执行同步

        Returns:
            用户是否确认
        """
        try:
            response = input("\n[yellow]是否开始同步? [y/N]: [/yellow]").strip().lower()
            return response in ['y', 'yes', '是']
        except (EOFError, KeyboardInterrupt):
            return False

    def _display_dry_run_preview(self, source_rows: int, target_rows: int) -> None:
        """
        显示 Dry-run 预览信息

        Args:
            source_rows: 源表行数
            target_rows: 目标表行数
        """
        if RICH_AVAILABLE:
            from rich.panel import Panel

            # 计算批次数
            batch_count = (source_rows + self.BATCH_SIZE - 1) // self.BATCH_SIZE

            preview_msg = f"[bold cyan]👀 预览模式 (DRY-RUN)[/bold cyan]\n\n"
            preview_msg += f"[yellow]将执行以下操作:[/yellow]\n"
            preview_msg += f"  1. [red]清除目标表[/red] {target_rows:,} 行数据\n"
            preview_msg += f"  2. [green]从源表复制[/green] {source_rows:,} 行数据\n"
            preview_msg += f"  3. 分 [cyan]{batch_count}[/cyan] 批次处理（每批 {self.BATCH_SIZE} 行）\n\n"
            preview_msg += f"[bold green]✓ 这是预览模式，不会执行任何实际操作[/bold green]"
            preview_msg += f"\n[dim]去掉 --dry-run 参数后再次运行以执行同步[/dim]"

            console.print(Panel(
                preview_msg,
                title="预览模式",
                border_style="cyan"
            ))
        else:
            print("\n=== 预览模式 (DRY-RUN) ===")
            print(f"将执行以下操作:")
            print(f"  1. 清除目标表 {target_rows:,} 行数据")
            print(f"  2. 从源表复制 {source_rows:,} 行数据")
            batch_count = (source_rows + self.BATCH_SIZE - 1) // self.BATCH_SIZE
            print(f"  3. 分 {batch_count} 批次处理（每批 {self.BATCH_SIZE} 行）")
            print(f"\n✓ 这是预览模式，不会执行任何实际操作")
            print(f"去掉 --dry-run 参数后再次运行以执行同步")

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

    def sync_table(self, table_name: str, force: bool = False, days: int = 10, dry_run: bool = False) -> Dict[str, Any]:
        """
        同步表数据

        Args:
            table_name: 表名
            force: 强制同步（跳过确认）
            days: 只同步最近 N 天的数据（默认 10 天，0 表示同步全部）
            dry_run: 预览模式，只显示信息不执行实际操作

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
            'error': None,
            'time_filter': None,
            'failed_batches': 0,
            'batch_errors': []
        }

        time_column = None
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

            # 3.5 检测时间字段（如果需要时间过滤）
            if days > 0:
                time_column = self.find_create_time_column(table_name)
                if time_column:
                    result['time_filter'] = f"{days}天 ({time_column})"
                    console.print(f"[cyan]使用时间过滤: 最近 {days} 天 (字段: {time_column})[/cyan]")
                else:
                    console.print(f"[yellow]未找到时间字段，将同步全部数据[/yellow]")

            # 4. 获取源表行数
            source_rows = self.get_row_count(table_name, is_source=True, days=days if days > 0 else None, time_column=time_column)
            result['source_rows'] = source_rows
            console.print(f"[cyan]源表数据: {source_rows:,} 行[/cyan]")

            # 5. 获取目标表行数
            target_rows_before = self.get_row_count(table_name, is_source=False)
            result['target_rows_before'] = target_rows_before

            # 6. 显示同步信息并请求用户确认
            self._display_sync_info(table_name, source_rows, target_rows_before, len(columns), time_filter=result['time_filter'])

            # Dry-run 模式：只显示预览，不执行实际操作
            if dry_run:
                self._display_dry_run_preview(source_rows, target_rows_before)
                result['success'] = True
                result['dry_run'] = True
                result['source_rows'] = source_rows
                result['target_rows_before'] = target_rows_before
                result['deleted_rows'] = target_rows_before  # 预计删除
                result['inserted_rows'] = source_rows  # 预计插入
                return result

            if not force:
                if not self._confirm_sync():
                    console.print("[yellow]同步已取消[/yellow]")
                    result['error'] = '用户取消操作'
                    return result

            # 7. 开始同步（不使用大事务，每批提交）
            with console.status("[bold yellow]开始同步..."):
                # 禁用外键检查
                self.disable_foreign_key_checks()

                try:
                    # 清除目标表数据
                    if target_rows_before > 0:
                        deleted = self.clear_target_table(table_name)
                        result['deleted_rows'] = deleted
                        console.print(f"[yellow]清除 {deleted:,} 行旧数据[/yellow]")

                    # 获取源数据并批量插入（每批独立提交）
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

                            inserted_total, failed_batches, batch_errors = self._batch_insert_with_progress(
                                table_name, columns, progress, task, time_column, days
                            )
                    else:
                        # 不使用 rich 的简单进度显示
                        inserted_total, failed_batches, batch_errors = self._batch_insert_simple(table_name, columns, source_rows, time_column, days)

                    result['inserted_rows'] = inserted_total
                    result['failed_batches'] = failed_batches
                    result['batch_errors'] = batch_errors

                    # 标记完成（即使有失败批次也视为完成）
                    result['success'] = True

                    if failed_batches > 0:
                        console.print(f"[yellow]⚠ 同步完成: {inserted_total:,} 行 (失败 {failed_batches} 批)[/yellow]")
                    else:
                        console.print(f"[green]✓ 同步完成: {inserted_total:,} 行[/green]")

                finally:
                    # 恢复外键检查
                    self.enable_foreign_key_checks()

        except Exception as e:
            # 不再回滚，只记录错误
            result['error'] = str(e)
            result['success'] = False
            console.print(f"[red]✗ 同步失败: {e}[/red]")

        return result

    def _batch_insert_with_progress(self, table_name: str, columns: List[str], progress, task, time_column: Optional[str] = None, days: int = 0) -> tuple:
        """
        使用 Rich 进度条的批量插入
        每批独立提交，失败时继续处理下一批

        Returns:
            (inserted_total, failed_batches, batch_errors)
        """
        inserted_total = 0
        failed_batches = 0
        batch_errors = []
        offset = 0
        batch_num = 0
        source_rows = progress.tasks[task].total

        while offset < source_rows:
            batch_num += 1

            # 分批获取数据
            cursor = self.source_conn.cursor(DictCursor)
            columns_str = ', '.join(columns)

            # 构建查询语句
            sql = f"SELECT {columns_str} FROM {table_name}"
            if days > 0 and time_column:
                date_threshold = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d %H:%M:%S')
                sql += f" WHERE {time_column} >= '{date_threshold}'"
            sql += f" LIMIT {self.BATCH_SIZE} OFFSET {offset}"

            cursor.execute(sql)
            batch_data = cursor.fetchall()

            if not batch_data:
                break

            # 插入目标表（每批独立事务）
            try:
                target_cursor = self.target_conn.cursor()
                columns_str = ', '.join(columns)
                placeholders = ', '.join(['%s'] * len(columns))

                insert_sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
                values = [[row[col] for col in columns] for row in batch_data]
                target_cursor.executemany(insert_sql, values)

                # 提交这一批
                self.target_conn.commit()
                inserted_total += len(batch_data)

            except Exception as e:
                # 记录错误，但继续处理下一批
                failed_batches += 1
                error_msg = f"批次 {batch_num} (offset {offset}): {str(e)}"
                batch_errors.append(error_msg)
                console.print(f"[red]✗ 批次 {batch_num} 失败: {e}[/red]")

            progress.update(task, advance=len(batch_data))
            offset += len(batch_data)

            # 如果没有更多数据了，提前退出
            if len(batch_data) < self.BATCH_SIZE:
                break

        return inserted_total, failed_batches, batch_errors

    def _batch_insert_simple(self, table_name: str, columns: List[str], source_rows: int, time_column: Optional[str] = None, days: int = 0) -> tuple:
        """
        简单的批量插入（不使用 Rich）
        每批独立提交，失败时继续处理下一批

        Returns:
            (inserted_total, failed_batches, batch_errors)
        """
        inserted_total = 0
        failed_batches = 0
        batch_errors = []
        offset = 0
        batch_num = 0

        while offset < source_rows:
            batch_num += 1

            # 分批获取数据
            cursor = self.source_conn.cursor(DictCursor)
            columns_str = ', '.join(columns)

            # 构建查询语句
            sql = f"SELECT {columns_str} FROM {table_name}"
            if days > 0 and time_column:
                date_threshold = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d %H:%M:%S')
                sql += f" WHERE {time_column} >= '{date_threshold}'"
            sql += f" LIMIT {self.BATCH_SIZE} OFFSET {offset}"

            cursor.execute(sql)
            batch_data = cursor.fetchall()

            if not batch_data:
                break

            # 插入目标表（每批独立事务）
            try:
                target_cursor = self.target_conn.cursor()
                columns_str = ', '.join(columns)
                placeholders = ', '.join(['%s'] * len(columns))

                insert_sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
                values = [[row[col] for col in columns] for row in batch_data]
                target_cursor.executemany(insert_sql, values)

                # 提交这一批
                self.target_conn.commit()
                inserted_total += len(batch_data)
                print(f"  进度: {min(offset + len(batch_data), source_rows)}/{source_rows} 行")

            except Exception as e:
                # 记录错误，但继续处理下一批
                failed_batches += 1
                error_msg = f"批次 {batch_num} (offset {offset}): {str(e)}"
                batch_errors.append(error_msg)
                print(f"  ✗ 批次 {batch_num} 失败: {e}")

            offset += len(batch_data)

            # 如果没有更多数据了，提前退出
            if len(batch_data) < self.BATCH_SIZE:
                break

        return inserted_total, failed_batches, batch_errors

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
            table.add_column("失败批次", justify="right", style="red")
            table.add_column("状态", justify="center")

            for result in results:
                failed_batches = result.get('failed_batches', 0)
                status = "[green]成功[/green]" if result['success'] else "[red]失败[/red]"
                if failed_batches > 0:
                    status = f"[yellow]部分成功[/yellow]"

                table.add_row(
                    result['table_name'],
                    f"{result['source_rows']:,}",
                    f"{result['deleted_rows']:,}",
                    f"{result['inserted_rows']:,}",
                    f"{failed_batches}" if failed_batches > 0 else "-",
                    status
                )

            console.print(table)

            # 统计信息
            total_source = sum(r['source_rows'] for r in results)
            total_deleted = sum(r['deleted_rows'] for r in results)
            total_inserted = sum(r['inserted_rows'] for r in results)
            total_failed_batches = sum(r.get('failed_batches', 0) for r in results)
            success_count = sum(1 for r in results if r['success'])

            stats_msg = f"[bold]总计:[/bold]\n"
            stats_msg += f"  源数据: {total_source:,} 行\n"
            stats_msg += f"  删除: {total_deleted:,} 行\n"
            stats_msg += f"  插入: {total_inserted:,} 行\n"
            if total_failed_batches > 0:
                stats_msg += f"  [red]失败批次: {total_failed_batches}[/red]\n"
            stats_msg += f"  成功: {success_count}/{len(results)} 表"

            console.print(Panel(
                stats_msg,
                title="同步统计",
                border_style="blue" if total_failed_batches == 0 else "yellow"
            ))

            # 显示失败批次详情
            for result in results:
                if result.get('batch_errors'):
                    console.print(Panel(
                        "\n".join(result['batch_errors'][:5]),  # 只显示前5个错误
                        title=f"[bold red]失败批次详情: {result['table_name']}[/bold red]",
                        border_style="red"
                    ))
                    if len(result['batch_errors']) > 5:
                        console.print(f"[dim]... 还有 {len(result['batch_errors']) - 5} 个错误[/dim]")

        else:
            # 简单的文本报告
            print("\n=== 数据同步报告 ===")
            for result in results:
                failed_batches = result.get('failed_batches', 0)
                status = "成功" if result['success'] else "失败"
                if failed_batches > 0:
                    status = f"部分成功 ({failed_batches} 批失败)"

                print(f"{result['table_name']}: 源={result['source_rows']:,}, "
                      f"删除={result['deleted_rows']:,}, 插入={result['inserted_rows']:,}, "
                      f"状态={status}")

                # 显示错误详情
                if result.get('batch_errors'):
                    print("  失败批次详情:")
                    for error in result['batch_errors'][:5]:
                        print(f"    - {error}")
                    if len(result['batch_errors']) > 5:
                        print(f"    ... 还有 {len(result['batch_errors']) - 5} 个错误")


def parse_args() -> tuple:
    """
    解析命令行参数

    Returns:
        (table_name, force, days, dry_run, source_config, target_config)
    """
    parser = argparse.ArgumentParser(
        description='MySQL 8 数据同步工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s --table pay_order
  %(prog)s -t pay_order --dry-run    # 预览模式，不执行实际操作
  %(prog)s -t pay_order --force
  %(prog)s -t pay_order --days 7
  %(prog)s -t pay_order --days 0  # 同步全部数据
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

    parser.add_argument(
        '--dry-run',
        action='store_true',
        dest='dry_run',
        help='预览模式，显示同步信息但不执行实际操作'
    )

    parser.add_argument(
        '-d', '--days',
        type=int,
        default=10,
        help='只同步最近 N 天的数据（默认 10 天，0 表示同步全部）'
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

    return args.table, args.force, args.days, args.dry_run, source_config, target_config


def main() -> int:
    """主函数"""
    try:
        console.print("[bold cyan]MySQL 8 数据同步工具[/bold cyan]\n")

        # 解析参数
        table_name, force, days, dry_run, source_config, target_config = parse_args()

        # Dry-run 模式提示
        if dry_run:
            console.print("[bold cyan]👀 预览模式 (DRY-RUN)[/bold cyan]\n")

        # 创建同步器
        synchronizer = MySQLDataSynchronizer(source_config, target_config)

        # 连接数据库
        synchronizer.connect()

        # 执行同步
        result = synchronizer.sync_table(table_name, force=force, days=days, dry_run=dry_run)

        # 只有在非 dry-run 模式下才显示详细报告
        if not dry_run:
            synchronizer.display_sync_report([result])
        else:
            console.print("\n[bold green]✓ 预览完成[/bold green]")
            console.print(f"[dim]运行不带 --dry-run 参数的命令以执行实际同步[/dim]\n")

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
