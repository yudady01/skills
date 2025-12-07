#!/usr/bin/env python3
"""
基础功能测试脚本
"""

import os
import sys
import asyncio
from pathlib import Path

# 添加脚本目录到 Python 路径
script_dir = Path(__file__).parent / "scripts"
sys.path.insert(0, str(script_dir))

def test_document_processor():
    """测试文档处理器"""
    print("🧪 测试文档处理器...")
    try:
        from document_processor import DocumentProcessorFactory
        factory = DocumentProcessorFactory()
        processor = factory.get_processor("test.md")
        print(f"✅ 文档处理器创建成功: {processor}")
        return True
    except Exception as e:
        print(f"❌ 文档处理器测试失败: {e}")
        return False

def test_config_loader():
    """测试配置加载器"""
    print("\n🧪 测试配置加载器...")
    try:
        from config_loader import Context7ConfigLoader
        loader = Context7ConfigLoader()
        config = loader.load_config()
        print(f"✅ 配置加载成功: {len(config)} 项配置")
        return True
    except Exception as e:
        print(f"❌ 配置加载器测试失败: {e}")
        return False

def test_vectorizer():
    """测试向量化器"""
    print("\n🧪 测试向量化器...")
    try:
        from simple_vectorizer import SimpleDocumentVectorizer
        # 使用相对路径
        data_dir = Path(__file__).parent / "data"
        vectorizer = SimpleDocumentVectorizer(str(data_dir))
        print(f"✅ 向量化器创建成功: {data_dir}")
        return True
    except Exception as e:
        print(f"❌ 向量化器测试失败: {e}")
        return False

async def test_basic_functionality():
    """测试基本功能"""
    print("\n🧪 测试基本功能...")
    try:
        from simple_vectorizer import SimpleDocumentVectorizer
        from document_processor import DocumentProcessorFactory

        # 创建测试文档
        test_doc = {
            'doc_id': 'test_doc_001',
            'title': '测试文档',
            'content': '这是一个测试文档，包含 Spring Boot 和微服务相关内容。',
            'chunks': [
                '这是一个测试文档。',
                '它包含 Spring Boot 相关内容。',
                '还有微服务架构设计的内容。'
            ],
            'metadata': {'source': 'test', 'category': 'test'},
            'file_path': 'test.md',
            'format': 'markdown'
        }

        # 测试向量化存储
        data_dir = Path(__file__).parent / "data"
        vectorizer = SimpleDocumentVectorizer(str(data_dir))

        print("📝 向量化存储测试...")
        vector_ids = await vectorizer.vectorize_and_store(test_doc)
        print(f"✅ 向量化存储成功: {len(vector_ids)} 个块")

        # 测试搜索
        print("🔍 搜索测试...")
        results = await vectorizer.search("Spring Boot", limit=3)
        print(f"✅ 搜索成功: 找到 {len(results)} 个结果")

        # 测试文档摘要
        print("📄 文档摘要测试...")
        summary = await vectorizer.get_document_summary('test_doc_001')
        if summary:
            print(f"✅ 文档摘要成功: {summary['title']}")

        # 测试文档列表
        print("📋 文档列表测试...")
        documents = await vectorizer.list_documents()
        print(f"✅ 文档列表成功: {len(documents)} 个文档")

        return True
    except Exception as e:
        print(f"❌ 基本功能测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """主测试函数"""
    print("🚀 Context7 基础功能测试")
    print("=" * 50)

    tests = [
        test_document_processor,
        test_config_loader,
        test_vectorizer
    ]

    # 运行同步测试
    passed = 0
    for test in tests:
        if test():
            passed += 1

    # 运行异步测试
    print("\n" + "=" * 50)
    if asyncio.run(test_basic_functionality()):
        passed += 1

    print(f"\n📊 测试结果: {passed}/4 通过")

    if passed == 4:
        print("🎉 所有测试通过！Context7 功能正常。")
    else:
        print("⚠️  部分测试失败，请检查错误信息。")

if __name__ == "__main__":
    main()