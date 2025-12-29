#!/usr/bin/env python3
"""
Context7 简单文档服务器（测试版本）
不依赖 MCP，提供基础的文档处理和搜索功能
"""

import asyncio
import json
import sys
from pathlib import Path

# 添加脚本目录到 Python 路径
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))

from document_processor import DocumentProcessorFactory
from simple_vectorizer import SimpleDocumentVectorizer
from config_loader import Context7ConfigLoader

class SimpleContext7Server:
    def __init__(self):
        self.config_loader = Context7ConfigLoader()
        self.doc_processor_factory = DocumentProcessorFactory()

        # 加载配置
        try:
            self.config = self.config_loader.load_config()
            print("✅ 配置加载成功")
        except Exception as e:
            print(f"❌ 配置加载失败: {e}")
            self.config = {}

        # 初始化向量化引擎
        data_dir = self.config.get('cache', {}).get('storage_path',
                                                   str(script_dir.parent / "data"))
        self.vectorizer = SimpleDocumentVectorizer(data_dir=data_dir)

    async def search_documents(self, query: str, scope: str = "all", limit: int = 5):
        """搜索文档"""
        try:
            results = await self.vectorizer.search(query, scope, limit)
            return self._format_search_results(results)
        except Exception as e:
            return f"❌ 搜索失败: {str(e)}"

    async def index_document(self, file_path: str, category: str = ""):
        """索引文档"""
        try:
            # 检查文件是否存在
            if not Path(file_path).exists():
                return f"❌ 文件不存在: {file_path}"

            # 处理文档
            document = await self.doc_processor_factory.process_document(file_path)
            if not document:
                return f"❌ 不支持的文件格式: {Path(file_path).suffix}"

            # 添加分类信息
            if category:
                document['metadata']['category'] = category

            # 标记为用户文档
            document['metadata']['source'] = 'user'

            # 向量化存储
            vector_ids = await self.vectorizer.vectorize_and_store(document)

            return f"""✅ 文档索引成功
📄 文档ID: {document['doc_id']}
📝 标题: {document['title']}
🔢 分块数量: {len(vector_ids)}
📊 文档格式: {document['format']}"""
        except Exception as e:
            return f"❌ 索引失败: {str(e)}"

    async def get_document_summary(self, doc_id: str):
        """获取文档摘要"""
        try:
            summary = await self.vectorizer.get_document_summary(doc_id)
            if summary:
                return self._format_document_summary(summary)
            else:
                return f"❌ 文档未找到: {doc_id}"
        except Exception as e:
            return f"❌ 获取文档摘要失败: {str(e)}"

    async def list_documents(self, scope: str = "all"):
        """列出文档"""
        try:
            documents = await self.vectorizer.list_documents(scope)
            return self._format_document_list(documents)
        except Exception as e:
            return f"❌ 列出文档失败: {str(e)}"

    def _format_search_results(self, results):
        """格式化搜索结果"""
        if not results:
            return "❌ 未找到相关文档"

        output = ["🔍 搜索结果:"]
        for i, result in enumerate(results, 1):
            metadata = result.get('metadata', {})
            title = metadata.get('title', '未知标题')
            doc_id = result.get('doc_id', '')
            similarity = result.get('similarity_score', 0)
            content = result.get('content', '')

            output.append(f"\n{i}. 📄 {title}")
            output.append(f"   📊 相关性: {similarity:.2%}")
            output.append(f"   🆔 文档ID: {doc_id}")

            # 截取内容预览
            preview = content[:200] + "..." if len(content) > 200 else content
            output.append(f"   📝 内容预览: {preview}")

        return "\n".join(output)

    def _format_document_summary(self, summary):
        """格式化文档摘要"""
        output = [
            "📄 文档详情:",
            f"📝 标题: {summary.get('title', '未知')}",
            f"🆔 文档ID: {summary.get('doc_id', '')}",
            f"📂 文件路径: {summary.get('file_path', '')}",
            f"📊 格式: {summary.get('format', '')}",
            f"🔢 分块数量: {summary.get('chunk_count', 0)}",
            f"📅 创建时间: {summary.get('created_at', '')}",
            f"🔄 更新时间: {summary.get('updated_at', '')}"
        ]

        metadata = summary.get('metadata', {})
        if metadata:
            output.append("\n📋 元数据:")
            for key, value in metadata.items():
                output.append(f"   {key}: {value}")

        return "\n".join(output)

    def _format_document_list(self, documents):
        """格式化文档列表"""
        if not documents:
            return "📂 暂无文档"

        output = [f"📂 文档列表 (共 {len(documents)} 个文档):"]
        for i, doc in enumerate(documents, 1):
            title = doc.get('title', '未知标题')
            doc_id = doc.get('doc_id', '')
            format_type = doc.get('format', '')
            chunk_count = doc.get('chunk_count', 0)
            updated_at = doc.get('updated_at', '')

            output.append(f"\n{i}. 📄 {title}")
            output.append(f"   🆔 {doc_id}")
            output.append(f"   📊 {format_type} | {chunk_count} 块")
            output.append(f"   🔄 更新: {updated_at}")

        return "\n".join(output)

async def main():
    """测试主函数"""
    print("🚀 Context7 简单文档服务器测试")
    print("=" * 50)

    server = SimpleContext7Server()

    # 测试索引内置文档
    print("\n📚 测试索引内置文档...")
    try:
        from builtin_indexer import BuiltinDocumentIndexer
        indexer = BuiltinDocumentIndexer()
        count = await indexer.index_all_builtin_docs()
        print(f"✅ 索引完成，共索引 {count} 个文档")
    except Exception as e:
        print(f"❌ 索引失败: {e}")

    # 测试搜索
    print("\n🔍 测试搜索功能...")
    test_queries = [
        "Spring Boot 配置",
        "微服务架构",
        "编码规范",
        "数据库设计"
    ]

    for query in test_queries:
        print(f"\n搜索: {query}")
        result = await server.search_documents(query, limit=3)
        print(result)

    # 测试文档列表
    print("\n📋 测试文档列表...")
    result = await server.list_documents()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())