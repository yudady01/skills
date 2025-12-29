#!/usr/bin/env python3
"""
批量文档载入器
支持分批从向量数据库载入文档，提供内存优化和智能缓存
"""

import os
import sys
import json
import asyncio
from pathlib import Path
from typing import List, Dict, Any, Optional, Iterator, Callable
from dataclasses import dataclass
from datetime import datetime
import sqlite3
from contextlib import contextmanager

# 添加脚本目录到 Python 路径
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))

from config_loader import Context7ConfigLoader


@dataclass
class LoadConfig:
    """批量载入配置"""
    batch_size: int = 20  # 每批载入的文档数量
    enable_cache: bool = True  # 启用缓存
    cache_size: int = 100  # 缓存文档数量
    filter_category: Optional[str] = None  # 按分类过滤
    filter_source: Optional[str] = None  # 按来源过滤
    min_chunk_count: Optional[int] = None  # 最小块数过滤


@dataclass
class DocumentChunk:
    """文档块"""
    chunk_id: str
    doc_id: str
    content: str
    metadata: Dict[str, Any]
    embedding: Optional[List[float]] = None


@dataclass
class Document:
    """文档"""
    doc_id: str
    title: str
    content: str
    format: str
    file_path: str
    metadata: Dict[str, Any]
    chunks: List[DocumentChunk]
    chunk_count: int
    indexed_at: Optional[str] = None


class DocumentCache:
    """文档缓存"""

    def __init__(self, max_size: int = 100):
        self.max_size = max_size
        self._cache: Dict[str, Document] = {}
        self._access_order: List[str] = []

    def get(self, doc_id: str) -> Optional[Document]:
        """获取缓存的文档"""
        if doc_id in self._cache:
            # 更新访问顺序
            self._access_order.remove(doc_id)
            self._access_order.append(doc_id)
            return self._cache[doc_id]
        return None

    def put(self, doc: Document):
        """缓存文档"""
        if doc.doc_id in self._cache:
            # 更新访问顺序
            self._access_order.remove(doc.doc_id)
            self._access_order.append(doc.doc_id)
            self._cache[doc.doc_id] = doc
        else:
            # 添加新文档
            if len(self._cache) >= self.max_size:
                # LRU 淘汰
                oldest = self._access_order.pop(0)
                del self._cache[oldest]
            self._cache[doc.doc_id] = doc
            self._access_order.append(doc.doc_id)

    def clear(self):
        """清空缓存"""
        self._cache.clear()
        self._access_order.clear()

    def size(self) -> int:
        """缓存大小"""
        return len(self._cache)


class BatchDocumentLoader:
    """批量文档载入器"""

    def __init__(self, config: Optional[LoadConfig] = None):
        self.config = config or LoadConfig()
        self.config_loader = Context7ConfigLoader()

        # 数据目录
        script_dir = Path(__file__).parent
        self.data_dir = Path(self.config_loader.load_config().get('cache', {}).get(
            'storage_path', str(script_dir.parent / "data")))

        # 数据库文件
        self.metadata_db = self.data_dir / "metadata.db"
        self.vectors_db = self.data_dir / "vectors.db"

        # 缓存
        self.cache = DocumentCache(max_size=self.config.cache_size) if self.config.enable_cache else None

    @contextmanager
    def _get_db_connection(self, db_path: Path):
        """获取数据库连接"""
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()

    async def list_documents(self, batch: int = 0, scope: str = "all") -> List[Dict[str, Any]]:
        """列出文档（分批）"""
        if not self.metadata_db.exists():
            return []

        offset = batch * self.config.batch_size
        limit = self.config.batch_size

        with self._get_db_connection(self.metadata_db) as conn:
            # 构建查询（根据实际的数据库架构）
            if self.config.filter_source or self.config.filter_category:
                query = """
                    SELECT doc_id, title, file_path, format, chunk_count, metadata, created_at, updated_at
                    FROM documents
                    WHERE 1=1
                """
                params = []

                # 添加过滤条件
                if self.config.filter_source:
                    query += " AND json_extract(metadata, '$.source') = ?"
                    params.append(self.config.filter_source)
                if self.config.filter_category:
                    query += " AND json_extract(metadata, '$.category') = ?"
                    params.append(self.config.filter_category)

                # 按 scope 过滤
                if scope == "builtin":
                    query += " AND doc_id LIKE 'builtin_%'"
                elif scope == "user":
                    query += " AND doc_id NOT LIKE 'builtin_%'"

                query += " ORDER BY updated_at DESC LIMIT ? OFFSET ?"
                params.extend([limit, offset])

                cursor = conn.execute(query, params)
            else:
                if scope == "builtin":
                    cursor = conn.execute("""
                        SELECT doc_id, title, file_path, format, chunk_count, metadata, created_at, updated_at
                        FROM documents
                        WHERE doc_id LIKE 'builtin_%'
                        ORDER BY updated_at DESC
                        LIMIT ? OFFSET ?
                    """, (limit, offset))
                elif scope == "user":
                    cursor = conn.execute("""
                        SELECT doc_id, title, file_path, format, chunk_count, metadata, created_at, updated_at
                        FROM documents
                        WHERE doc_id NOT LIKE 'builtin_%'
                        ORDER BY updated_at DESC
                        LIMIT ? OFFSET ?
                    """, (limit, offset))
                else:
                    cursor = conn.execute("""
                        SELECT doc_id, title, file_path, format, chunk_count, metadata, created_at, updated_at
                        FROM documents
                        ORDER BY updated_at DESC
                        LIMIT ? OFFSET ?
                    """, (limit, offset))

            rows = cursor.fetchall()

            return [dict(row) for row in rows]

    async def load_document(self, doc_id: str) -> Optional[Document]:
        """载入单个文档"""
        # 检查缓存
        if self.cache:
            cached = self.cache.get(doc_id)
            if cached:
                return cached

        if not self.metadata_db.exists():
            return None

        with self._get_db_connection(self.metadata_db) as conn:
            cursor = conn.execute(
                "SELECT doc_id, title, file_path, format, chunk_count, metadata, created_at, updated_at FROM documents WHERE doc_id = ?",
                (doc_id,)
            )
            row = cursor.fetchone()

            if not row:
                return None

            doc_data = dict(row)

        # 载入文档块
        chunks = await self._load_chunks(doc_id)

        # 解析元数据
        metadata = doc_data.get('metadata', '{}')
        if isinstance(metadata, str):
            metadata = json.loads(metadata)

        doc = Document(
            doc_id=doc_data['doc_id'],
            title=doc_data['title'],
            content='',  # 完整内容不存储在元数据中，需要从块重组
            format=doc_data['format'],
            file_path=doc_data['file_path'],
            metadata=metadata,
            chunks=chunks,
            chunk_count=doc_data.get('chunk_count', len(chunks)),
            indexed_at=doc_data.get('updated_at')  # 使用 updated_at 作为索引时间
        )

        # 从块重建内容
        if chunks:
            doc.content = '\n\n'.join([chunk.content for chunk in chunks])

        # 缓存文档
        if self.cache:
            self.cache.put(doc)

        return doc

    async def _load_chunks(self, doc_id: str) -> List[DocumentChunk]:
        """载入文档块"""
        if not self.vectors_db.exists():
            return []

        chunks = []
        with self._get_db_connection(self.vectors_db) as conn:
            # 根据 actual schema: document_vectors 表
            cursor = conn.execute(
                "SELECT id, doc_id, chunk_index, content, keywords, metadata FROM document_vectors WHERE doc_id = ? ORDER BY chunk_index",
                (doc_id,)
            )
            rows = cursor.fetchall()

            for row in rows:
                chunk_data = dict(row)
                # 解析元数据
                metadata = chunk_data.get('metadata', '{}')
                if isinstance(metadata, str):
                    metadata = json.loads(metadata)

                chunks.append(DocumentChunk(
                    chunk_id=chunk_data['id'],
                    doc_id=chunk_data['doc_id'],
                    content=chunk_data['content'],
                    metadata=metadata,
                    embedding=None  # 简化版本不使用 embedding
                ))

        return chunks

    async def load_batch(self, batch: int = 0) -> List[Document]:
        """载入一批文档"""
        docs_data = await self.list_documents(batch)

        if not docs_data:
            return []

        print(f"📦 载入批次 {batch} ({len(docs_data)} 个文档)")

        # 并发载入文档
        tasks = [self.load_document(doc['doc_id']) for doc in docs_data]
        results = await asyncio.gather(*tasks)

        # 过滤 None 值
        documents = [doc for doc in results if doc is not None]

        return documents

    async def iterate_all_documents(self, callback: Callable[[Document], None]):
        """迭代所有文档（分批载入）"""
        batch = 0
        total_docs = 0

        while True:
            docs = await self.load_batch(batch)

            if not docs:
                break

            for doc in docs:
                await callback(doc)
                total_docs += 1

            batch += 1

            print(f"   已处理 {total_docs} 个文档")

    async def search_documents(self, query: str, limit: int = 10) -> List[Document]:
        """搜索文档（通过关键词匹配）"""
        if not self.vectors_db.exists():
            return []

        # 先从 document_vectors 中搜索匹配的块
        with self._get_db_connection(self.vectors_db) as conn:
            cursor = conn.execute(
                """
                SELECT DISTINCT doc_id
                FROM document_vectors
                WHERE content LIKE ? OR keywords LIKE ?
                LIMIT ?
                """,
                (f"%{query}%", f"%{query}%", limit * 2)  # 获取更多候选
            )
            rows = cursor.fetchall()

        if not rows:
            return []

        # 获取唯一的 doc_id 列表
        doc_ids = list(set([row['doc_id'] for row in rows]))[:limit]

        # 载入完整文档
        tasks = [self.load_document(doc_id) for doc_id in doc_ids]
        results = await asyncio.gather(*tasks)

        return [doc for doc in results if doc is not None]

    async def get_statistics(self) -> Dict[str, Any]:
        """获取统计信息"""
        stats = {
            'total_documents': 0,
            'total_chunks': 0,
            'by_category': {},
            'by_format': {},
            'oldest_doc': None,
            'newest_doc': None,
            'cache_size': self.cache.size() if self.cache else 0
        }

        if not self.metadata_db.exists():
            return stats

        with self._get_db_connection(self.metadata_db) as conn:
            # 总文档数
            cursor = conn.execute("SELECT COUNT(*) as count FROM documents")
            stats['total_documents'] = cursor.fetchone()['count']

            # 按分类统计（从 metadata JSON 中提取）
            cursor = conn.execute("""
                SELECT json_extract(metadata, '$.category') as category, COUNT(*) as count
                FROM documents
                GROUP BY category
            """)
            for row in cursor.fetchall():
                stats['by_category'][row['category'] or 'general'] = row['count']

            # 按格式统计
            cursor = conn.execute("""
                SELECT format, COUNT(*) as count
                FROM documents
                GROUP BY format
            """)
            for row in cursor.fetchall():
                stats['by_format'][row['format']] = row['count']

            # 最早和最新的文档（使用 created_at 和 updated_at）
            cursor = conn.execute("SELECT MIN(created_at) as oldest, MAX(updated_at) as newest FROM documents")
            row = cursor.fetchone()
            stats['oldest_doc'] = row['oldest']
            stats['newest_doc'] = row['newest']

        # 总块数（从 document_vectors 表）
        if self.vectors_db.exists():
            with self._get_db_connection(self.vectors_db) as conn:
                cursor = conn.execute("SELECT COUNT(*) as count FROM document_vectors")
                stats['total_chunks'] = cursor.fetchone()['count']

        return stats

    def clear_cache(self):
        """清空缓存"""
        if self.cache:
            self.cache.clear()
            print("✅ 缓存已清空")


async def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="批量文档载入器")
    parser.add_argument('--batch-size', type=int, default=20, help='每批载入的文档数量')
    parser.add_argument('--batch', type=int, default=0, help='要载入的批次号')
    parser.add_argument('--doc-id', type=str, help='载入指定文档ID')
    parser.add_argument('--search', type=str, help='搜索文档')
    parser.add_argument('--category', type=str, help='按分类过滤')
    parser.add_argument('--source', type=str, help='按来源过滤')
    parser.add_argument('--stats', action='store_true', help='显示统计信息')
    parser.add_argument('--no-cache', action='store_true', help='禁用缓存')
    parser.add_argument('--clear-cache', action='store_true', help='清空缓存')

    args = parser.parse_args()

    try:
        # 创建配置
        config = LoadConfig(
            batch_size=args.batch_size,
            enable_cache=not args.no_cache,
            filter_category=args.category,
            filter_source=args.source
        )

        loader = BatchDocumentLoader(config)

        # 清空缓存
        if args.clear_cache:
            loader.clear_cache()
            return

        # 显示统计信息
        if args.stats:
            stats = await loader.get_statistics()
            print("\n📊 文档统计:")
            print(f"   总文档数: {stats['total_documents']}")
            print(f"   总块数: {stats['total_chunks']}")
            print(f"   缓存大小: {stats['cache_size']}")
            print(f"\n   按分类:")
            for category, count in sorted(stats['by_category'].items()):
                print(f"      {category}: {count}")
            print(f"\n   按格式:")
            for format, count in sorted(stats['by_format'].items()):
                print(f"      {format}: {count}")
            print(f"\n   时间范围:")
            print(f"      最早: {stats['oldest_doc']}")
            print(f"      最新: {stats['newest_doc']}")
            return

        # 载入指定文档
        if args.doc_id:
            doc = await loader.load_document(args.doc_id)
            if doc:
                print(f"\n📄 文档: {doc.title}")
                print(f"   ID: {doc.doc_id}")
                print(f"   格式: {doc.format}")
                print(f"   块数: {doc.chunk_count}")
                print(f"   内容长度: {len(doc.content)} 字符")
            else:
                print(f"❌ 未找到文档: {args.doc_id}")
            return

        # 搜索文档
        if args.search:
            docs = await loader.search_documents(args.search)
            print(f"\n🔍 搜索结果: '{args.search}' ({len(docs)} 个文档)")
            for doc in docs:
                print(f"\n   📄 {doc.title}")
                print(f"      ID: {doc.doc_id} | 块数: {doc.chunk_count}")
            return

        # 载入批次
        docs = await loader.load_batch(args.batch)
        print(f"\n📦 批次 {args.batch} 载入完成 ({len(docs)} 个文档)")
        for doc in docs[:5]:
            print(f"   - 📄 {doc.title} ({doc.chunk_count} 块)")
        if len(docs) > 5:
            print(f"   ... 还有 {len(docs) - 5} 个文档")

    except Exception as e:
        print(f"❌ 载入过程中发生错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
