import os
import json
import sqlite3
from pathlib import Path
from typing import List, Dict, Any, Optional
import hashlib
from datetime import datetime
import re

class SimpleDocumentVectorizer:
    """简化的文档向量化器，使用关键词匹配代替向量嵌入"""

    def __init__(self, data_dir: Optional[str] = None):
        self.data_dir = Path(data_dir) if data_dir else Path(__file__).parent.parent / "data"
        self.data_dir.mkdir(exist_ok=True)

        # 数据库路径
        self.vectors_db_path = self.data_dir / "vectors.db"
        self.metadata_db_path = self.data_dir / "metadata.db"

        # 初始化数据库
        self._init_databases()

    def _init_databases(self):
        """初始化数据库"""
        # 初始化向量数据库（使用关键词存储）
        conn = sqlite3.connect(str(self.vectors_db_path))
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS document_vectors (
                id TEXT PRIMARY KEY,
                doc_id TEXT NOT NULL,
                chunk_index INTEGER NOT NULL,
                content TEXT NOT NULL,
                keywords TEXT NOT NULL,
                metadata TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_doc_id ON document_vectors(doc_id)
        ''')

        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_keywords ON document_vectors(keywords)
        ''')

        conn.commit()
        conn.close()

        # 初始化元数据库
        conn = sqlite3.connect(str(self.metadata_db_path))
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS documents (
                doc_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                file_path TEXT NOT NULL,
                format TEXT NOT NULL,
                chunk_count INTEGER NOT NULL,
                metadata TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        conn.commit()
        conn.close()

    def _extract_keywords(self, text: str) -> str:
        """从文本中提取关键词"""
        # 简单的关键词提取：分词并过滤停用词
        # 移除标点符号并转小写
        text = re.sub(r'[^\w\s]', ' ', text.lower())

        # 分词
        words = text.split()

        # 简单的停用词列表
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
            'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these',
            'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him',
            'her', 'us', 'them', 'my', 'your', 'his', 'her', 'its', 'our', 'their',
            '的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一',
            '一个', '上', '也', '很', '到', '说', '要', '去', '你', '会', '着',
            '没有', '看', '好', '自己', '这', '那', '之', '与', '及', '或',
            '但', '而', '因为', '所以', '如果', '那么', '虽然', '可是', '然而'
        }

        # 过滤停用词和短词
        keywords = [word for word in words if word not in stop_words and len(word) > 2]

        # 返回去重后的关键词，用空格连接
        return ' '.join(list(set(keywords)))

    async def vectorize_and_store(self, document: Dict[str, Any]) -> List[str]:
        """向量化文档并存储到数据库（使用关键词）"""
        chunks = document['chunks']
        doc_id = document['doc_id']

        print(f"处理文档 {doc_id}，包含 {len(chunks)} 个块...")

        # 准备存储数据
        vector_ids = []

        conn = sqlite3.connect(str(self.vectors_db_path))
        cursor = conn.cursor()

        try:
            # 检查文档是否已存在，如果存在则删除旧的数据
            cursor.execute("DELETE FROM document_vectors WHERE doc_id = ?", (doc_id,))

            for i, chunk in enumerate(chunks):
                # 生成向量ID
                vector_id = f"{doc_id}_{i}"

                # 提取关键词作为"向量"
                keywords = self._extract_keywords(chunk)

                # 准备元数据
                metadata = {
                    "doc_id": doc_id,
                    "chunk_index": i,
                    "title": document.get('title', ''),
                    "format": document.get('format', ''),
                    "file_path": document.get('file_path', '')
                }

                # 存储关键词和元数据
                cursor.execute('''
                    INSERT INTO document_vectors
                    (id, doc_id, chunk_index, content, keywords, metadata)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    vector_id,
                    doc_id,
                    i,
                    chunk,
                    keywords,
                    json.dumps(metadata)
                ))

                vector_ids.append(vector_id)

            conn.commit()
            print(f"成功存储 {len(vector_ids)} 个文档块 for document {doc_id}")

        except Exception as e:
            conn.rollback()
            print(f"存储文档块时出错 {doc_id}: {e}")
            raise
        finally:
            conn.close()

        # 更新文档元数据
        await self._update_document_metadata(document)

        return vector_ids

    async def _update_document_metadata(self, document: Dict[str, Any]):
        """更新文档元数据"""
        conn = sqlite3.connect(str(self.metadata_db_path))
        cursor = conn.cursor()

        cursor.execute('''
            INSERT OR REPLACE INTO documents
            (doc_id, title, file_path, format, chunk_count, metadata, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            document['doc_id'],
            document.get('title', ''),
            document.get('file_path', ''),
            document.get('format', ''),
            len(document.get('chunks', [])),
            json.dumps(document.get('metadata', {})),
            datetime.now().isoformat()
        ))

        conn.commit()
        conn.close()

    async def search(self, query: str, scope: str = "all", limit: int = 5) -> List[Dict[str, Any]]:
        """搜索相关文档片段（基于关键词匹配）"""
        print(f"搜索: {query}")

        # 提取查询关键词
        query_keywords = self._extract_keywords(query).split()
        if not query_keywords:
            return []

        # 获取所有匹配的文档块
        conn = sqlite3.connect(str(self.vectors_db_path))
        cursor = conn.cursor()

        # 构建搜索条件
        where_conditions = []
        params = []

        if scope == "builtin":
            where_conditions.append("doc_id LIKE 'builtin_%'")
        elif scope == "user":
            where_conditions.append("doc_id NOT LIKE 'builtin_%'")

        # 为每个查询关键词添加条件
        for keyword in query_keywords:
            where_conditions.append("keywords LIKE ?")
            params.append(f"%{keyword}%")

        where_clause = " AND ".join(where_conditions)

        sql = f'''
            SELECT id, doc_id, chunk_index, content, keywords, metadata
            FROM document_vectors
            WHERE {where_clause}
            ORDER BY
                CASE
                    WHEN keywords LIKE ? THEN 1
                    ELSE 2
                END,
                length(keywords) DESC
            LIMIT ?
        '''

        # 第一个参数是完整匹配
        params.insert(0, f"%{query}%")
        params.append(limit)

        cursor.execute(sql, params)
        results = cursor.fetchall()
        conn.close()

        if not results:
            return []

        # 计算相关性分数
        scored_results = []
        for row in results:
            vector_id, doc_id, chunk_index, content, keywords, metadata_json = row

            # 计算相关性分数
            keyword_list = keywords.split()
            matches = sum(1 for qk in query_keywords if qk in keyword_list)
            score = matches / len(query_keywords) if query_keywords else 0

            # 计算包含查询的额外分数
            if query.lower() in content.lower():
                score += 0.5

            scored_results.append({
                'id': vector_id,
                'doc_id': doc_id,
                'chunk_index': chunk_index,
                'content': content,
                'metadata': json.loads(metadata_json) if metadata_json else {},
                'similarity_score': min(score, 1.0)  # 确保分数不超过1
            })

        # 按分数排序
        scored_results.sort(key=lambda x: x['similarity_score'], reverse=True)

        return scored_results[:limit]

    async def get_document_summary(self, doc_id: str) -> Optional[Dict[str, Any]]:
        """获取文档摘要"""
        conn = sqlite3.connect(str(self.metadata_db_path))
        cursor = conn.cursor()

        cursor.execute('''
            SELECT doc_id, title, file_path, format, chunk_count, metadata, created_at, updated_at
            FROM documents
            WHERE doc_id = ?
        ''', (doc_id,))

        result = cursor.fetchone()
        conn.close()

        if result:
            return {
                'doc_id': result[0],
                'title': result[1],
                'file_path': result[2],
                'format': result[3],
                'chunk_count': result[4],
                'metadata': json.loads(result[5]) if result[5] else {},
                'created_at': result[6],
                'updated_at': result[7]
            }

        return None

    async def list_documents(self, scope: str = "all") -> List[Dict[str, Any]]:
        """列出所有文档"""
        conn = sqlite3.connect(str(self.metadata_db_path))
        cursor = conn.cursor()

        if scope == "builtin":
            cursor.execute('''
                SELECT doc_id, title, file_path, format, chunk_count, metadata, created_at, updated_at
                FROM documents
                WHERE doc_id LIKE 'builtin_%'
                ORDER BY updated_at DESC
            ''')
        elif scope == "user":
            cursor.execute('''
                SELECT doc_id, title, file_path, format, chunk_count, metadata, created_at, updated_at
                FROM documents
                WHERE doc_id NOT LIKE 'builtin_%'
                ORDER BY updated_at DESC
            ''')
        else:
            cursor.execute('''
                SELECT doc_id, title, file_path, format, chunk_count, metadata, created_at, updated_at
                FROM documents
                ORDER BY updated_at DESC
            ''')

        results = cursor.fetchall()
        conn.close()

        documents = []
        for result in results:
            documents.append({
                'doc_id': result[0],
                'title': result[1],
                'file_path': result[2],
                'format': result[3],
                'chunk_count': result[4],
                'metadata': json.loads(result[5]) if result[5] else {},
                'created_at': result[6],
                'updated_at': result[7]
            })

        return documents

    async def delete_document(self, doc_id: str) -> bool:
        """删除文档"""
        try:
            # 删除向量
            conn = sqlite3.connect(str(self.vectors_db_path))
            cursor = conn.cursor()
            cursor.execute("DELETE FROM document_vectors WHERE doc_id = ?", (doc_id,))
            conn.commit()
            conn.close()

            # 删除元数据
            conn = sqlite3.connect(str(self.metadata_db_path))
            cursor = conn.cursor()
            cursor.execute("DELETE FROM documents WHERE doc_id = ?", (doc_id,))
            conn.commit()
            conn.close()

            return True
        except Exception as e:
            print(f"删除文档时出错 {doc_id}: {e}")
            return False