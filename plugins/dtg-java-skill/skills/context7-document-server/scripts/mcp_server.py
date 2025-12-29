#!/usr/bin/env python3
"""
Context7 MCP Server Implementation
基于 MCP 协议的智能文档处理和检索服务器
"""

import asyncio
import json
import logging
import sys
from pathlib import Path
from typing import List, Dict, Any

# 添加脚本目录到 Python 路径
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))

from config_loader import Context7ConfigLoader
from document_processor import DocumentProcessorFactory
from simple_vectorizer import SimpleDocumentVectorizer
from builtin_indexer import BuiltinDocumentIndexer

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Context7MCPServer:
    """Context7 MCP 服务器实现"""

    def __init__(self):
        """初始化服务器"""
        self.config_loader = None
        self.vectorizer = None
        self.doc_processor_factory = None
        self.builtin_indexer = None
        self.config = {}

        # 尝试加载配置，如果失败则运行配置向导
        try:
            self._load_configuration()
        except Exception as e:
            logger.warning(f"配置加载失败: {e}")
            self._run_configuration_wizard()
            # 重新尝试加载配置
            self._load_configuration()

    def _load_configuration(self):
        """加载配置"""
        self.config_loader = Context7ConfigLoader()
        self.doc_processor_factory = DocumentProcessorFactory()

        # 加载配置
        self.config = self.config_loader.load_config()
        logger.info("Configuration loaded successfully")

        # 初始化向量化引擎
        data_dir = self.config.get('cache', {}).get('storage_path',
                                                   str(Path(__file__).parent.parent / "data"))
        self.vectorizer = SimpleDocumentVectorizer(data_dir=data_dir)

        # 初始化内置文档索引器
        self.builtin_indexer = BuiltinDocumentIndexer()
        self.builtin_indexer.config_loader = self.config_loader
        self.builtin_indexer.vectorizer = self.vectorizer
        self.builtin_indexer.doc_processor_factory = self.doc_processor_factory

        # 确保内置文档已索引
        asyncio.create_task(self._ensure_builtin_indexed())

    def _run_configuration_wizard(self):
        """运行配置向导"""
        try:
            # 动态导入配置向导
            from config_wizard import Context7ConfigWizard
            import config_wizard
            config_wizard.main()
        except ImportError:
            logger.error("配置向导不可用，请手动创建配置文件")
            print("❌ 配置文件缺失且自动配置向导不可用")
            print("请手动创建 ~/.claude/context7.json 配置文件")
            sys.exit(1)
        except Exception as e:
            logger.error(f"配置向导运行失败: {e}")
            print(f"❌ 自动配置失败: {e}")
            sys.exit(1)

    async def _ensure_builtin_indexed(self):
        """确保内置文档已索引"""
        try:
            await self.builtin_indexer.index_all_builtin_docs()
            logger.info("Built-in documents indexing completed")
        except Exception as e:
            logger.error(f"Built-in indexing failed: {e}")

    # MCP 工具函数
    async def search_documents(self, query: str, scope: str = "all", limit: int = 5) -> str:
        """搜索文档"""
        try:
            results = await self.vectorizer.search(query, scope, limit)
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
                output.append(f"   📝 内容预览: {preview}\n")

            return "\n".join(output)
        except Exception as e:
            return f"❌ 搜索失败: {str(e)}"

    async def index_document(self, path: str, format: str = "md", category: str = "") -> str:
        """索引文档"""
        try:
            # 检查文件是否存在
            if not Path(path).exists():
                return f"❌ 文件不存在: {path}"

            # 处理文档
            document = await self.doc_processor_factory.process_document(path)
            if not document:
                return f"❌ 不支持的文件格式: {Path(path).suffix}"

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

    async def get_document_summary(self, doc_id: str) -> str:
        """获取文档摘要"""
        try:
            summary = await self.vectorizer.get_document_summary(doc_id)
            if not summary:
                return f"❌ 文档未找到: {doc_id}"

            metadata = summary.get('metadata', {})
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

            if metadata:
                output.append("\n📋 元数据:")
                for key, value in metadata.items():
                    output.append(f"   {key}: {value}")

            return "\n".join(output)
        except Exception as e:
            return f"❌ 获取文档摘要失败: {str(e)}"

    async def list_documents(self, scope: str = "all") -> str:
        """列出文档"""
        try:
            documents = await self.vectorizer.list_documents(scope)
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
        except Exception as e:
            return f"❌ 列出文档失败: {str(e)}"

# 全局服务器实例
_server_instance = None

def get_server():
    """获取服务器实例"""
    global _server_instance
    if _server_instance is None:
        _server_instance = Context7MCPServer()
    return _server_instance

# MCP 工具函数导出
async def mcp__context7_doc_server__search_documents(query: str, scope: str = "all", limit: int = 5) -> str:
    """搜索文档"""
    server = get_server()
    return await server.search_documents(query, scope, limit)

async def mcp__context7_doc_server__index_document(path: str, format: str = "md", category: str = "") -> str:
    """索引文档"""
    server = get_server()
    return await server.index_document(path, format, category)

async def mcp__context7_doc_server__get_document_summary(doc_id: str) -> str:
    """获取文档摘要"""
    server = get_server()
    return await server.get_document_summary(doc_id)

async def mcp__context7_doc_server__list_documents(scope: str = "all") -> str:
    """列出文档"""
    server = get_server()
    return await server.list_documents(scope)

async def main():
    """主函数 - 用于独立运行和测试"""
    try:
        print("🚀 Context7 MCP 服务器启动中...")

        # 创建服务器实例（会自动处理配置）
        server = get_server()

        print("✅ Context7 MCP 服务器启动成功")
        print("📚 可用工具:")
        print("   - mcp__context7_doc_server__search_documents")
        print("   - mcp__context7_doc_server__index_document")
        print("   - mcp__context7_doc_server__get_document_summary")
        print("   - mcp__context7_doc_server__list_documents")

        # 测试搜索功能
        print("\n🔍 测试搜索功能...")
        results = await server.search_documents("Spring Boot", "builtin", 3)
        print(f"找到 {len(await server.vectorizer.search('Spring Boot', 'builtin', 3))} 个相关文档")

        # 列出所有文档
        print("\n📚 列出所有文档...")
        documents = await server.vectorizer.list_documents("all")
        print(f"共 {len(documents)} 个已索引文档")

        print("\n🎉 Context7 MCP 服务器运行正常!")

        # 保持服务器运行
        print("\n按 Ctrl+C 停止服务器...")
        while True:
            await asyncio.sleep(1)

    except KeyboardInterrupt:
        print("\n⚠️ 服务器被用户中断")
    except Exception as e:
        print(f"❌ 服务器错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())