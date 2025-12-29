#!/usr/bin/env python3
"""
分批文档索引器
支持大规模文档的分批索引处理，提供进度跟踪、断点续传和内存优化
"""

import os
import sys
import json
import asyncio
import hashlib
from pathlib import Path
from typing import List, Dict, Any, Optional, Set
from datetime import datetime
from dataclasses import dataclass, asdict

# 添加脚本目录到 Python 路径
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))

from document_processor import DocumentProcessorFactory
from simple_vectorizer import SimpleDocumentVectorizer
from config_loader import Context7ConfigLoader


@dataclass
class IndexProgress:
    """索引进度跟踪"""
    total_files: int
    processed_files: int
    success_count: int
    failed_files: List[str]
    skipped_files: List[str]
    start_time: str
    last_update: str
    checkpoint: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'IndexProgress':
        return cls(**data)


@dataclass
class BatchConfig:
    """分批配置"""
    batch_size: int = 50  # 每批处理的文档数量
    max_concurrent: int = 5  # 并发处理数
    enable_checkpoint: bool = True  # 启用断点续传
    checkpoint_interval: int = 10  # 每处理 N 个文档保存一次检查点
    memory_limit_mb: int = 1024  # 内存限制（MB）
    skip_indexed: bool = True  # 跳过已索引的文档


class BatchDocumentIndexer:
    """分批文档索引器"""

    def __init__(self, config: Optional[BatchConfig] = None):
        self.config = config or BatchConfig()
        self.config_loader = Context7ConfigLoader()
        self.doc_processor_factory = DocumentProcessorFactory()

        # 获取插件根目录
        self.plugin_root = Path(os.environ.get('CLAUDE_PLUGIN_ROOT',
                                             script_dir.parent.parent.parent))

        # 内置文档路径
        self.builtin_docs_path = self.plugin_root / "docs"

        # 数据目录
        self.data_dir = Path(self.config_loader.load_config().get('cache', {}).get(
            'storage_path', str(script_dir.parent / "data")))
        self.checkpoint_file = self.data_dir / "index_checkpoint.json"

        # 初始化向量化引擎
        self.vectorizer = SimpleDocumentVectorizer(data_dir=str(self.data_dir))

        # 已索引文档集合（用于去重）
        self._indexed_docs: Set[str] = set()

    async def get_indexed_documents(self) -> Set[str]:
        """获取已索引文档ID集合"""
        try:
            documents = await self.vectorizer.list_documents("builtin")
            return {doc['doc_id'] for doc in documents}
        except Exception:
            return set()

    def _generate_doc_id(self, file_path: str) -> str:
        """生成文档ID（用于去重检查）"""
        file_stat = os.stat(file_path)
        content_hash = hashlib.md5(
            f"{file_path}:{file_stat.st_size}:{file_stat.st_mtime}".encode()
        ).hexdigest()[:12]
        return f"builtin_doc_{content_hash}"

    async def index_all_docs(self, docs_path: Optional[Path] = None) -> IndexProgress:
        """索引所有文档（分批处理）"""
        target_path = docs_path or self.builtin_docs_path

        print(f"🚀 开始分批索引文档...")
        print(f"📁 目标目录: {target_path}")
        print(f"⚙️  配置: 批次大小={self.config.batch_size}, 并发数={self.config.max_concurrent}")

        if not target_path.exists():
            print(f"❌ 目录不存在: {target_path}")
            return IndexProgress(
                total_files=0,
                processed_files=0,
                success_count=0,
                failed_files=[],
                skipped_files=[],
                start_time=datetime.now().isoformat(),
                last_update=datetime.now().isoformat()
            )

        # 查找所有支持的文档文件
        doc_files = self._find_documents(target_path)

        if not doc_files:
            print("❌ 未找到支持的文档文件")
            return IndexProgress(
                total_files=0,
                processed_files=0,
                success_count=0,
                failed_files=[],
                skipped_files=[],
                start_time=datetime.now().isoformat(),
                last_update=datetime.now().isoformat()
            )

        # 加载进度（如果启用断点续传）
        progress = await self._load_checkpoint(doc_files)

        print(f"📄 找到 {len(doc_files)} 个文档文件")

        # 获取已索引文档（用于去重）
        if self.config.skip_indexed:
            self._indexed_docs = await self.get_indexed_documents()
            print(f"✅ 已索引 {len(self._indexed_docs)} 个文档")

        # 分批处理
        await self._process_batches(doc_files, progress)

        # 保存最终状态
        await self._save_checkpoint(progress)

        # 输出统计报告
        self._print_summary(progress)

        return progress

    def _find_documents(self, docs_path: Path) -> List[Path]:
        """查找所有支持的文档文件"""
        supported_extensions = []
        for processor in self.doc_processor_factory.processors.values():
            supported_extensions.extend(processor.supported_extensions())

        doc_files = []
        for ext in supported_extensions:
            doc_files.extend(docs_path.rglob(f"*{ext}"))

        return sorted(set(doc_files))

    async def _process_batches(self, doc_files: List[Path], progress: IndexProgress):
        """分批处理文档"""
        total_batches = (len(doc_files) + self.config.batch_size - 1) // self.config.batch_size

        for batch_idx in range(total_batches):
            start_idx = batch_idx * self.config.batch_size
            end_idx = min(start_idx + self.config.batch_size, len(doc_files))
            batch_files = doc_files[start_idx:end_idx]

            print(f"\n📦 批次 {batch_idx + 1}/{total_batches} ({len(batch_files)} 个文件)")

            await self._process_batch(batch_files, progress)

            # 保存检查点
            if self.config.enable_checkpoint and progress.processed_files % self.config.checkpoint_interval == 0:
                await self._save_checkpoint(progress)

    async def _process_batch(self, batch_files: List[Path], progress: IndexProgress):
        """处理单个批次"""
        # 创建信号量控制并发
        semaphore = asyncio.Semaphore(self.config.max_concurrent)

        async def process_with_semaphore(doc_file: Path):
            async with semaphore:
                return await self._process_document(doc_file, progress)

        # 并发处理当前批次
        tasks = [process_with_semaphore(doc_file) for doc_file in batch_files]
        await asyncio.gather(*tasks, return_exceptions=True)

    async def _process_document(self, doc_file: Path, progress: IndexProgress) -> bool:
        """处理单个文档"""
        try:
            # 生成文档ID
            doc_id = self._generate_doc_id(str(doc_file))

            # 检查是否已索引
            if self.config.skip_indexed and doc_id in self._indexed_docs:
                progress.skipped_files.append(str(doc_file))
                progress.processed_files += 1
                return True

            # 处理文档
            document = await self.doc_processor_factory.process_document(str(doc_file))
            if not document:
                progress.skipped_files.append(str(doc_file))
                progress.processed_files += 1
                return False

            # 标记为内置文档
            document['metadata']['source'] = 'builtin'
            document['metadata']['category'] = self._categorize_doc(str(doc_file))
            document['doc_id'] = doc_id

            # 向量化存储
            await self.vectorizer.vectorize_and_store(document)

            progress.success_count += 1
            progress.processed_files += 1
            progress.last_update = datetime.now().isoformat()

            # 输出进度
            if progress.processed_files % 5 == 0:
                self._print_progress(progress)

            return True

        except Exception as e:
            error_msg = f"{doc_file}: {str(e)}"
            progress.failed_files.append(error_msg)
            progress.processed_files += 1
            print(f"❌ 处理失败: {doc_file.name} - {e}")
            return False

    def _categorize_doc(self, file_path: str) -> str:
        """根据文件路径确定文档分类"""
        path_obj = Path(file_path)
        relative_path = path_obj.relative_to(self.builtin_docs_path)

        if 'guides' in str(relative_path):
            return 'guide'
        elif 'rules' in str(relative_path):
            return 'standards'
        elif 'templates' in str(relative_path):
            return 'template'
        elif 'api' in str(relative_path):
            return 'api'
        else:
            return 'general'

    async def _load_checkpoint(self, doc_files: List[Path]) -> IndexProgress:
        """加载检查点"""
        if not self.config.enable_checkpoint or not self.checkpoint_file.exists():
            return IndexProgress(
                total_files=len(doc_files),
                processed_files=0,
                success_count=0,
                failed_files=[],
                skipped_files=[],
                start_time=datetime.now().isoformat(),
                last_update=datetime.now().isoformat()
            )

        try:
            with open(self.checkpoint_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                progress = IndexProgress.from_dict(data)
                progress.total_files = len(doc_files)
                print(f"🔄 从检查点恢复: 已处理 {progress.processed_files}/{len(doc_files)} 个文档")
                return progress
        except Exception as e:
            print(f"⚠️  无法加载检查点: {e}")
            return IndexProgress(
                total_files=len(doc_files),
                processed_files=0,
                success_count=0,
                failed_files=[],
                skipped_files=[],
                start_time=datetime.now().isoformat(),
                last_update=datetime.now().isoformat()
            )

    async def _save_checkpoint(self, progress: IndexProgress):
        """保存检查点"""
        if not self.config.enable_checkpoint:
            return

        try:
            self.checkpoint_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.checkpoint_file, 'w', encoding='utf-8') as f:
                json.dump(progress.to_dict(), f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️  保存检查点失败: {e}")

    def _print_progress(self, progress: IndexProgress):
        """打印进度"""
        percentage = (progress.processed_files / progress.total_files) * 100
        print(f"   进度: {progress.processed_files}/{progress.total_files} ({percentage:.1f}%) | "
              f"✅ {progress.success_count} | ❌ {len(progress.failed_files)} | ⏭️ {len(progress.skipped_files)}")

    def _print_summary(self, progress: IndexProgress):
        """打印统计摘要"""
        print(f"\n📊 索引完成统计")
        print(f"   总文档数: {progress.total_files}")
        print(f"   已处理: {progress.processed_files}")
        print(f"   ✅ 成功: {progress.success_count}")
        print(f"   ⏭️  跳过: {len(progress.skipped_files)}")
        print(f"   ❌ 失败: {len(progress.failed_files)}")

        if progress.failed_files:
            print(f"\n❌ 失败文档列表:")
            for error in progress.failed_files[:10]:
                print(f"   - {error}")
            if len(progress.failed_files) > 10:
                print(f"   ... 还有 {len(progress.failed_files) - 10} 个失败")

    async def list_indexed_documents(self):
        """列出已索引的文档"""
        print("\n📋 已索引的文档:")

        try:
            documents = await self.vectorizer.list_documents("builtin")

            if not documents:
                print("   暂无已索引的文档")
                return

            # 按分类分组
            by_category: Dict[str, List[Dict]] = {}
            for doc in documents:
                category = doc.get('metadata', {}).get('category', 'general')
                if category not in by_category:
                    by_category[category] = []
                by_category[category].append(doc)

            # 打印分组结果
            for category, docs in sorted(by_category.items()):
                print(f"\n   📂 {category.upper()} ({len(docs)} 个文档):")
                for doc in docs[:5]:  # 每个分类最多显示5个
                    print(f"      - 📄 {doc['title']} ({doc.get('chunk_count', 0)} 块)")
                if len(docs) > 5:
                    print(f"      ... 还有 {len(docs) - 5} 个文档")

        except Exception as e:
            print(f"❌ 获取文档列表失败: {e}")

    async def clear_index(self):
        """清除所有索引"""
        print("⚠️  警告: 此操作将删除所有已索引的文档")
        confirm = input("确认清除? (yes/no): ")

        if confirm.lower() != 'yes':
            print("❌ 操作已取消")
            return

        try:
            # 删除检查点文件
            if self.checkpoint_file.exists():
                self.checkpoint_file.unlink()

            # 删除数据库文件
            for db_file in self.data_dir.glob("*.db"):
                db_file.unlink()
                print(f"🗑️  已删除: {db_file.name}")

            print("✅ 索引已清除")

        except Exception as e:
            print(f"❌ 清除索引失败: {e}")


async def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="分批文档索引器")
    parser.add_argument('--batch-size', type=int, default=50, help='每批处理的文档数量')
    parser.add_argument('--concurrent', type=int, default=5, help='并发处理数')
    parser.add_argument('--no-checkpoint', action='store_true', help='禁用断点续传')
    parser.add_argument('--reindex', action='store_true', help='重新索引所有文档')
    parser.add_argument('--list', action='store_true', help='列出已索引的文档')
    parser.add_argument('--clear', action='store_true', help='清除所有索引')
    parser.add_argument('--path', type=str, help='指定要索引的目录路径')

    args = parser.parse_args()

    try:
        # 创建配置
        config = BatchConfig(
            batch_size=args.batch_size,
            max_concurrent=args.concurrent,
            enable_checkpoint=not args.no_checkpoint,
            skip_indexed=not args.reindex
        )

        indexer = BatchDocumentIndexer(config)

        # 列出已索引文档
        if args.list:
            await indexer.list_indexed_documents()
            return

        # 清除索引
        if args.clear:
            await indexer.clear_index()
            return

        # 执行索引
        docs_path = Path(args.path) if args.path else None
        await indexer.index_all_docs(docs_path)

        # 列出索引结果
        await indexer.list_indexed_documents()

    except KeyboardInterrupt:
        print("\n⚠️  索引被用户中断")
    except Exception as e:
        print(f"❌ 索引过程中发生错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
