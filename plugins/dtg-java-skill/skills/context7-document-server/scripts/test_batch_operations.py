#!/usr/bin/env python3
"""
分批索引和批量载入功能的测试脚本
用于验证 batch_indexer.py 和 batch_loader.py 的功能
"""

import os
import sys
import asyncio
import tempfile
from pathlib import Path

# 添加脚本目录到 Python 路径
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))

from batch_indexer import BatchDocumentIndexer, BatchConfig
from batch_loader import BatchDocumentLoader, LoadConfig


async def test_batch_indexing():
    """测试分批索引功能"""
    print("\n" + "="*60)
    print("🧪 测试 1: 分批索引功能")
    print("="*60)

    # 创建测试配置
    config = BatchConfig(
        batch_size=10,          # 小批次用于快速测试
        max_concurrent=2,       # 少量并发
        enable_checkpoint=True,
        skip_indexed=True
    )

    indexer = BatchDocumentIndexer(config)

    # 执行索引
    print("\n📝 开始索引测试...")
    progress = await indexer.index_all_docs()

    # 验证结果
    print(f"\n✅ 索引完成:")
    print(f"   总文档数: {progress.total_files}")
    print(f"   成功索引: {progress.success_count}")
    print(f"   跳过文档: {len(progress.skipped_files)}")
    print(f"   失败文档: {len(progress.failed_files)}")

    return progress.success_count > 0


async def test_batch_loading():
    """测试批量载入功能"""
    print("\n" + "="*60)
    print("🧪 测试 2: 批量载入功能")
    print("="*60)

    # 创建测试配置
    config = LoadConfig(
        batch_size=5,           # 小批次测试
        enable_cache=True,
        cache_size=20
    )

    loader = BatchDocumentLoader(config)

    # 载入第一批
    print("\n📦 载入第一批文档...")
    docs = await loader.load_batch(batch=0)

    print(f"\n✅ 载入完成:")
    print(f"   文档数量: {len(docs)}")

    for doc in docs[:3]:
        print(f"   - {doc.title} ({doc.chunk_count} 块)")

    # 测试缓存
    if docs:
        print("\n🔄 测试缓存功能...")
        cached_doc = await loader.load_document(docs[0].doc_id)
        if cached_doc and loader.cache:
            print(f"   ✅ 缓存大小: {loader.cache.size()}")

    return len(docs) > 0


async def test_document_statistics():
    """测试统计信息功能"""
    print("\n" + "="*60)
    print("🧪 测试 3: 统计信息功能")
    print("="*60)

    loader = BatchDocumentLoader()

    stats = await loader.get_statistics()

    print(f"\n📊 文档统计:")
    print(f"   总文档数: {stats['total_documents']}")
    print(f"   总块数: {stats['total_chunks']}")
    print(f"   缓存大小: {stats['cache_size']}")

    print(f"\n   按分类:")
    for category, count in sorted(stats['by_category'].items()):
        print(f"      {category}: {count}")

    print(f"\n   按格式:")
    for format, count in sorted(stats['by_format'].items()):
        print(f"      {format}: {count}")

    return stats['total_documents'] > 0


async def test_search_functionality():
    """测试搜索功能"""
    print("\n" + "="*60)
    print("🧪 测试 4: 搜索功能")
    print("="*60)

    loader = BatchDocumentLoader()

    # 测试搜索
    search_terms = ["Spring", "Boot", "Dubbo", "配置"]

    for term in search_terms:
        docs = await loader.search_documents(term, limit=3)
        print(f"\n🔍 搜索 '{term}': 找到 {len(docs)} 个文档")
        for doc in docs[:2]:
            print(f"   - {doc.title}")

    return True


async def test_checkpoint_recovery():
    """测试断点续传功能"""
    print("\n" + "="*60)
    print("🧪 测试 5: 断点续传功能")
    print("="*60)

    config = BatchConfig(
        batch_size=10,
        max_concurrent=2,
        enable_checkpoint=True
    )

    indexer = BatchDocumentIndexer(config)

    # 检查检查点文件
    if indexer.checkpoint_file.exists():
        print("   ✅ 检查点文件存在")
        print(f"   📁 路径: {indexer.checkpoint_file}")

        # 尝试加载检查点
        doc_files = indexer._find_documents(indexer.builtin_docs_path)
        progress = await indexer._load_checkpoint(doc_files)

        print(f"   📊 进度: {progress.processed_files}/{progress.total_files}")
    else:
        print("   ⚠️  检查点文件不存在（首次运行）")

    return True


async def test_filter_loading():
    """测试过滤载入功能"""
    print("\n" + "="*60)
    print("🧪 测试 6: 过滤载入功能")
    print("="*60)

    # 测试按分类过滤
    categories = ["guide", "standards", "template"]

    for category in categories:
        config = LoadConfig(
            batch_size=10,
            filter_category=category
        )

        loader = BatchDocumentLoader(config)
        docs = await loader.load_batch(batch=0)

        print(f"\n   分类 '{category}': {len(docs)} 个文档")

    return True


async def run_all_tests():
    """运行所有测试"""
    print("\n" + "="*60)
    print("🚀 Context7 分批索引和批量载入功能测试")
    print("="*60)

    tests = [
        ("分批索引", test_batch_indexing),
        ("批量载入", test_batch_loading),
        ("统计信息", test_document_statistics),
        ("搜索功能", test_search_functionality),
        ("断点续传", test_checkpoint_recovery),
        ("过滤载入", test_filter_loading),
    ]

    results = []

    for name, test_func in tests:
        try:
            result = await test_func()
            results.append((name, "✅ 通过" if result else "❌ 失败"))
        except Exception as e:
            results.append((name, f"❌ 错误: {e}"))
            import traceback
            traceback.print_exc()

    # 打印测试结果汇总
    print("\n" + "="*60)
    print("📋 测试结果汇总")
    print("="*60)

    for name, result in results:
        print(f"   {result} - {name}")

    passed = sum(1 for _, r in results if "✅" in r)
    total = len(results)

    print(f"\n   总计: {passed}/{total} 通过")
    print("="*60)

    return passed == total


if __name__ == "__main__":
    try:
        success = asyncio.run(run_all_tests())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  测试被用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
