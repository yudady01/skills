#!/usr/bin/env python3
"""
内置文档索引脚本（简化版）
"""

import os
import sys
import asyncio
from pathlib import Path

# 添加脚本目录到 Python 路径
script_dir = Path("plugins/ai-coding-java/skills/context7-document-server/scripts")
if script_dir.exists():
    sys.path.insert(0, str(script_dir))
else:
    print("❌ 脚本目录不存在")
    sys.exit(1)

async def main():
    try:
        from document_processor import DocumentProcessorFactory
        from simple_vectorizer import SimpleDocumentVectorizer

        print("🚀 开始索引内置文档...")

        # 获取文档路径
        docs_path = Path("plugins/ai-coding-java/docs")
        if not docs_path.exists():
            print(f"❌ 文档目录不存在: {docs_path}")
            return 0

        print(f"📚 文档目录: {docs_path}")

        # 查找 Markdown 文件
        md_files = list(docs_path.rglob("*.md"))
        print(f"📄 找到 {len(md_files)} 个 Markdown 文件")

        if not md_files:
            print("❌ 未找到 Markdown 文件")
            return 0

        # 初始化组件
        processor_factory = DocumentProcessorFactory()
        data_dir = Path("plugins/ai-coding-java/skills/context7-document-server/data")
        data_dir.mkdir(exist_ok=True)
        vectorizer = SimpleDocumentVectorizer(str(data_dir))

        indexed_count = 0

        for md_file in md_files:
            try:
                relative_path = md_file.relative_to(docs_path)
                print(f"\n🔄 处理: {relative_path}")

                # 处理文档
                document = await processor_factory.process_document(str(md_file))
                if not document:
                    print(f"⚠️  跳过文件: {md_file}")
                    continue

                # 标记为内置文档
                document['metadata']['source'] = 'builtin'
                document['metadata']['category'] = categorize_doc(relative_path)
                document['doc_id'] = f"builtin_{document['doc_id']}"

                # 向量化存储
                vector_ids = await vectorizer.vectorize_and_store(document)

                indexed_count += 1
                print(f"✅ 索引成功: {document['title']} ({len(vector_ids)} 块)")

            except Exception as e:
                print(f"❌ 索引失败 {md_file}: {e}")

        print(f"\n📊 内置文档索引完成: {indexed_count} 个文档")

        # 测试搜索
        await test_search(vectorizer)

        return indexed_count

    except ImportError as e:
        print(f"❌ 导入错误: {e}")
        return 0
    except Exception as e:
        print(f"❌ 索引过程中发生错误: {e}")
        import traceback
        traceback.print_exc()
        return 0

def categorize_doc(relative_path):
    """文档分类"""
    parts = str(relative_path).lower()

    if 'guides' in parts:
        return 'guide'
    elif 'rules' in parts:
        return 'standards'
    elif 'templates' in parts:
        return 'template'
    else:
        return 'general'

async def test_search(vectorizer):
    """测试搜索功能"""
    print("\n🔍 测试搜索功能...")

    test_queries = [
        "Spring Boot",
        "微服务",
        "配置",
        "架构",
        "编码规范"
    ]

    for query in test_queries:
        print(f"\n搜索: '{query}'")
        try:
            results = await vectorizer.search(query, limit=3)

            if results:
                for result in results:
                    title = result['metadata'].get('title', '未知')
                    score = result['similarity_score']
                    print(f"   📄 {title} (相关性: {score:.2%})")
            else:
                print("   ❌ 未找到相关文档")
        except Exception as e:
            print(f"   ❌ 搜索错误: {e}")

if __name__ == "__main__":
    print("🧪 Context7 内置文档索引测试")
    print("=" * 50)

    indexed_count = asyncio.run(main())

    print("\n" + "=" * 50)
    if indexed_count > 0:
        print(f"🎉 索引完成！成功索引 {indexed_count} 个文档")
        print("✅ Context7 基础功能验证成功")
    else:
        print("⚠️  没有文档被索引")
        print("❌ Context7 基础功能验证失败")