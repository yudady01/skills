#!/usr/bin/env python3
"""
内置文档索引脚本
"""

import os
import sys
import asyncio
from pathlib import Path

# 添加脚本目录到 Python 路径
script_dir = Path(__file__).parent / "scripts"
sys.path.insert(0, str(script_dir))

from document_processor import DocumentProcessorFactory
from simple_vectorizer import SimpleDocumentVectorizer

async def index_builtin_docs():
    """索引内置文档"""
    print("🚀 开始索引内置文档...")

    # 获取插件根目录
    plugin_root = Path(__file__).parent.parent.parent
    docs_path = plugin_root / "docs"

    if not docs_path.exists():
        print(f"❌ 文档目录不存在: {docs_path}")
        return 0

    print(f"📚 文档目录: {docs_path}")

    # 初始化组件
    processor_factory = DocumentProcessorFactory()
    data_dir = Path(__file__).parent / "data"
    vectorizer = SimpleDocumentVectorizer(str(data_dir))

    # 查找 Markdown 文件
    md_files = list(docs_path.rglob("*.md"))
    print(f"📄 找到 {len(md_files)} 个 Markdown 文件")

    indexed_count = 0

    for md_file in md_files:
        try:
            print(f"\n🔄 处理: {md_file.relative_to(docs_path)}")

            # 处理文档
            document = await processor_factory.process_document(str(md_file))
            if not document:
                print(f"⚠️  跳过文件: {md_file}")
                continue

            # 标记为内置文档
            document['metadata']['source'] = 'builtin'
            document['metadata']['category'] = categorize_doc(md_file, docs_path)
            document['doc_id'] = f"builtin_{document['doc_id']}"

            # 向量化存储
            vector_ids = await vectorizer.vectorize_and_store(document)

            indexed_count += 1
            print(f"✅ 索引成功: {document['title']} ({len(vector_ids)} 块)")

        except Exception as e:
            print(f"❌ 索引失败 {md_file}: {e}")

    print(f"\n📊 内置文档索引完成: {indexed_count} 个文档")

    # 列出已索引文档
    docs = await vectorizer.list_documents("builtin")
    print(f"\n📋 已索引的内置文档 ({len(docs)} 个):")
    for i, doc in enumerate(docs[:5], 1):  # 只显示前5个
        print(f"   {i}. 📄 {doc['title']}")
        print(f"      🆔 {doc['doc_id']}")
        print(f"      📊 {doc['format']} | {doc['chunk_count']} 块")

    if len(docs) > 5:
        print(f"      ... 还有 {len(docs) - 5} 个文档")

    return indexed_count

def categorize_doc(file_path, base_path):
    """文档分类"""
    relative = file_path.relative_to(base_path)
    parts = str(relative).lower()

    if 'guides' in parts:
        return 'guide'
    elif 'rules' in parts:
        return 'standards'
    elif 'templates' in parts:
        return 'template'
    else:
        return 'general'

async def test_search():
    """测试搜索功能"""
    print("\n🔍 测试搜索功能...")

    data_dir = Path(__file__).parent / "data"
    vectorizer = SimpleDocumentVectorizer(str(data_dir))

    test_queries = [
        "Spring Boot",
        "微服务",
        "配置",
        "架构"
    ]

    for query in test_queries:
        print(f"\n搜索: {query}")
        results = await vectorizer.search(query, limit=3)

        if results:
            for result in results:
                title = result['metadata'].get('title', '未知')
                score = result['similarity_score']
                preview = result['content'][:100] + "..." if len(result['content']) > 100 else result['content']
                print(f"   📄 {title} ({score:.2%})")
                print(f"      📝 {preview}")
        else:
            print("   ❌ 未找到相关文档")

async def main():
    """主函数"""
    try:
        # 索引文档
        indexed_count = await index_builtin_docs()

        if indexed_count > 0:
            # 测试搜索
            await test_search()
            print(f"\n🎉 索引和测试完成！成功索引 {indexed_count} 个文档")
        else:
            print("\n⚠️  没有文档被索引")

    except Exception as e:
        print(f"\n❌ 索引过程中发生错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())