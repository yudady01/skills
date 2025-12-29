import os
import json
import sqlite3
from pathlib import Path
from typing import List, Dict, Any, Optional
import hashlib
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle
from datetime import datetime

class DocumentVectorizer:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2", data_dir: Optional[str] = None):
        self.model_name = model_name
        self.data_dir = Path(data_dir) if data_dir else Path(__file__).parent.parent / "data"
        self.data_dir.mkdir(exist_ok=True)

        # 向量数据库路径
        self.vectors_db_path = self.data_dir / "vectors.db"
        self.metadata_db_path = self.data_dir / "metadata.db"

        # 初始化模型（延迟加载）
        self.model = None

        # 初始化数据库
        self._init_databases()

    def _load_model(self):
        """延迟加载模型"""
        if self.model is None:
            print(f"Loading sentence transformer model: {self.model_name}")
            self.model = SentenceTransformer(self.model_name)
            print("Model loaded successfully")

    def _init_databases(self):
        """初始化数据库"""
        # 初始化向量数据库（使用 SQLite 存储向量）
        conn = sqlite3.connect(str(self.vectors_db_path))
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS document_vectors (
                id TEXT PRIMARY KEY,
                doc_id TEXT NOT NULL,
                chunk_index INTEGER NOT NULL,
                content TEXT NOT NULL,
                vector BLOB NOT NULL,
                metadata TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_doc_id ON document_vectors(doc_id)
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

    async def vectorize_and_store(self, document: Dict[str, Any]) -> List[str]:
        """向量化文档并存储到数据库"""
        self._load_model()

        chunks = document['chunks']
        doc_id = document['doc_id']

        # 生成向量嵌入
        print(f"Vectorizing document {doc_id} with {len(chunks)} chunks...")
        embeddings = self.model.encode(chunks)

        # 准备存储数据
        vector_ids = []

        conn = sqlite3.connect(str(self.vectors_db_path))
        cursor = conn.cursor()

        try:
            # 检查文档是否已存在，如果存在则删除旧的向量
            cursor.execute("DELETE FROM document_vectors WHERE doc_id = ?", (doc_id,))

            for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
                # 生成向量ID
                vector_id = f"{doc_id}_{i}"

                # 序列化向量
                vector_blob = pickle.dumps(embedding)

                # 准备元数据
                metadata = {
                    "doc_id": doc_id,
                    "chunk_index": i,
                    "title": document.get('title', ''),
                    "format": document.get('format', ''),
                    "file_path": document.get('file_path', '')
                }

                # 存储向量和元数据
                cursor.execute('''
                    INSERT INTO document_vectors
                    (id, doc_id, chunk_index, content, vector, metadata)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    vector_id,
                    doc_id,
                    i,
                    chunk,
                    vector_blob,
                    json.dumps(metadata)
                ))

                vector_ids.append(vector_id)

            conn.commit()
            print(f"Successfully stored {len(vector_ids)} vectors for document {doc_id}")

        except Exception as e:
            conn.rollback()
            print(f"Error storing vectors for document {doc_id}: {e}")
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
        """搜索相关文档片段"""
        self._load_model()

        # 生成查询向量
        print(f"Searching for: {query}")
        query_embedding = self.model.encode([query])

        # 获取所有向量
        conn = sqlite3.connect(str(self.vectors_db_path))
        cursor = conn.cursor()

        if scope == "builtin":
            # 只搜索内置文档
            cursor.execute('''
                SELECT id, doc_id, chunk_index, content, vector, metadata
                FROM document_vectors
                WHERE doc_id LIKE 'builtin_%'
            ''')
        elif scope == "user":
            # 只搜索用户文档
            cursor.execute('''
                SELECT id, doc_id, chunk_index, content, vector, metadata
                FROM document_vectors
                WHERE doc_id NOT LIKE 'builtin_%'
            ''')
        else:
            # 搜索所有文档
            cursor.execute('''
                SELECT id, doc_id, chunk_index, content, vector, metadata
                FROM document_vectors
            ''')

        results = cursor.fetchall()
        conn.close()

        if not results:
            return []

        # 计算相似度
        similarities = []
        query_vec = query_embedding[0]

        for row in results:
            vector_id, doc_id, chunk_index, content, vector_blob, metadata_json = row

            # 反序列化向量
            stored_vector = pickle.loads(vector_blob)

            # 计算余弦相似度
            similarity = np.dot(query_vec, stored_vector) / (
                np.linalg.norm(query_vec) * np.linalg.norm(stored_vector)
            )

            similarities.append({
                'id': vector_id,
                'doc_id': doc_id,
                'chunk_index': chunk_index,
                'content': content,
                'metadata': json.loads(metadata_json) if metadata_json else {},
                'similarity_score': float(similarity)
            })

        # 按相似度排序
        similarities.sort(key=lambda x: x['similarity_score'], reverse=True)

        # 返回前 N 个结果
        return similarities[:limit]

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
            print(f"Error deleting document {doc_id}: {e}")
            return False