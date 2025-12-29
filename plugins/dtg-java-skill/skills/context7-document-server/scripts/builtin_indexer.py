#!/usr/bin/env python3
"""
内置文档索引器
自动索引 ai-coding-java 插件中的内置文档
"""

import os
import sys
import asyncio
from pathlib import Path
from typing import List, Dict, Any

# 添加脚本目录到 Python 路径
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))

from document_processor import DocumentProcessorFactory
from simple_vectorizer import SimpleDocumentVectorizer
from config_loader import Context7ConfigLoader

class BuiltinDocumentIndexer:
    def __init__(self):
        self.config_loader = Context7ConfigLoader()
        self.doc_processor_factory = DocumentProcessorFactory()

        # 获取插件根目录
        self.plugin_root = Path(os.environ.get('CLAUDE_PLUGIN_ROOT',
                                             script_dir.parent.parent.parent))

        # 内置文档路径
        self.builtin_docs_path = self.plugin_root / "docs"

        # 初始化向量化引擎
        data_dir = self.config_loader.load_config().get('cache', {}).get('storage_path',
                                                                      str(script_dir.parent / "data"))
        self.vectorizer = SimpleDocumentVectorizer(data_dir=data_dir)

    async def index_all_builtin_docs(self):
        """索引所有内置文档"""
        print("🚀 开始索引内置文档...")
        print(f"📁 插件根目录: {self.plugin_root}")
        print(f"📚 文档目录: {self.builtin_docs_path}")

        if not self.builtin_docs_path.exists():
            print(f"❌ 文档目录不存在: {self.builtin_docs_path}")
            return 0

        # 查找所有支持的文档文件
        supported_extensions = []
        for processor in self.doc_processor_factory.processors.values():
            supported_extensions.extend(processor.supported_extensions())

        doc_files = []
        for ext in supported_extensions:
            doc_files.extend(self.builtin_docs_path.rglob(f"*{ext}"))

        if not doc_files:
            print("❌ 未找到支持的文档文件")
            return 0

        print(f"📄 找到 {len(doc_files)} 个文档文件")

        indexed_count = 0
        errors = []

        for doc_file in doc_files:
            try:
                print(f"\n🔄 正在处理: {doc_file.relative_to(self.builtin_docs_path)}")

                # 处理文档
                document = await self.doc_processor_factory.process_document(str(doc_file))
                if not document:
                    print(f"⚠️  跳过不支持的文件: {doc_file}")
                    continue

                # 标记为内置文档
                document['metadata']['source'] = 'builtin'
                document['metadata']['category'] = self._categorize_doc(str(doc_file))
                document['doc_id'] = f"builtin_{document['doc_id']}"

                # 向量化存储
                vector_ids = await self.vectorizer.vectorize_and_store(document)

                indexed_count += 1
                print(f"✅ 索引成功: {document['title']} ({len(vector_ids)} 块)")

            except Exception as e:
                error_msg = f"❌ 索引失败 {doc_file}: {e}"
                print(error_msg)
                errors.append(error_msg)

        print(f"\n📊 内置文档索引完成")
        print(f"✅ 成功索引: {indexed_count} 个文档")
        if errors:
            print(f"❌ 失败: {len(errors)} 个文档")
            for error in errors:
                print(f"   {error}")

        return indexed_count

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

    async def list_indexed_documents(self):
        """列出已索引的内置文档"""
        print("\n📋 已索引的内置文档:")

        try:
            documents = await self.vectorizer.list_documents("builtin")

            if not documents:
                print("   暂无已索引的内置文档")
                return

            for i, doc in enumerate(documents, 1):
                print(f"   {i}. 📄 {doc['title']}")
                print(f"      🆔 {doc['doc_id']}")
                print(f"      📊 {doc['format']} | {doc['chunk_count']} 块")
                print(f"      📂 {doc['file_path']}")
                print()

        except Exception as e:
            print(f"❌ 获取文档列表失败: {e}")

async def main():
    """主函数"""
    try:
        indexer = BuiltinDocumentIndexer()

        # 检查是否应该列出文档
        if len(sys.argv) > 1 and sys.argv[1] == '--list':
            await indexer.list_indexed_documents()
            return

        # 索引所有内置文档
        await indexer.index_all_builtin_docs()

        # 列出索引结果
        await indexer.list_indexed_documents()

    except KeyboardInterrupt:
        print("\n⚠️  索引被用户中断")
    except Exception as e:
        print(f"❌ 索引过程中发生错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())