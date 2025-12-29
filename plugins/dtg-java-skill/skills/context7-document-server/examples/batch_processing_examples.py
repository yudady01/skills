#!/usr/bin/env python3
"""
分批索引和批量载入的实际使用示例
展示如何在不同场景下使用 batch_indexer 和 batch_loader
"""

import os
import sys
import asyncio
from pathlib import Path
from typing import List, Dict, Any

# 添加脚本目录到 Python 路径
script_dir = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(script_dir))

from batch_indexer import BatchDocumentIndexer, BatchConfig, IndexProgress
from batch_loader import BatchDocumentLoader, LoadConfig, Document


async def example_1_initial_indexing():
    """示例 1: 初始索引 - 首次建立文档索引"""
    print("\n" + "="*60)
    print("📚 示例 1: 初始索引建立")
    print("="*60)

    # 使用默认配置进行初始索引
    config = BatchConfig(
        batch_size=50,         # 每批处理 50 个文档
        max_concurrent=5,      # 5 个并发任务
        enable_checkpoint=True,# 启用断点续传
        skip_indexed=False     # 首次索引，不跳过
    )

    indexer = BatchDocumentIndexer(config)

    print("\n🔄 开始索引所有文档...")
    progress = await indexer.index_all_docs()

    print(f"\n✅ 索引完成!")
    print(f"   成功: {progress.success_count}")
    print(f"   失败: {len(progress.failed_files)}")
    print(f"   耗时: {progress.start_time} -> {progress.last_update}")


async def example_2_incremental_update():
    """示例 2: 增量更新 - 只索引新文档"""
    print("\n" + "="*60)
    print("🔄 示例 2: 增量更新索引")
    print("="*60)

    # 跳过已索引文档，只处理新文档
    config = BatchConfig(
        batch_size=100,        # 更大批次处理
        max_concurrent=8,      # 更高并发
        skip_indexed=True      # 跳过已索引
    )

    indexer = BatchDocumentIndexer(config)

    print("\n🔄 检查并索引新文档...")
    progress = await indexer.index_all_docs()

    print(f"\n✅ 更新完成!")
    print(f"   新增文档: {progress.success_count}")
    print(f"   跳过文档: {len(progress.skipped_files)}")


async def example_3_batch_query():
    """示例 3: 批量查询 - 分批载入并处理文档"""
    print("\n" + "="*60)
    print("🔍 示例 3: 批量查询文档")
    print("="*60)

    config = LoadConfig(
        batch_size=20,         # 每批载入 20 个文档
        enable_cache=True,     # 启用缓存
        cache_size=100         # 缓存 100 个文档
    )

    loader = BatchDocumentLoader(config)

    # 分批载入所有文档
    batch = 0
    all_docs: List[Document] = []

    while True:
        docs = await loader.load_batch(batch)

        if not docs:
            break

        all_docs.extend(docs)
        print(f"   批次 {batch}: 载入 {len(docs)} 个文档")

        batch += 1

        # 限制处理数量（示例）
        if len(all_docs) >= 50:
            break

    print(f"\n✅ 总共载入 {len(all_docs)} 个文档")


async def example_4_filtered_query():
    """示例 4: 过滤查询 - 按分类载入文档"""
    print("\n" + "="*60)
    print("🎯 示例 4: 按分类过滤查询")
    print("="*60)

    categories = ["guide", "standards", "template"]

    for category in categories:
        config = LoadConfig(
            batch_size=10,
            filter_category=category
        )

        loader = BatchDocumentLoader(config)
        docs = await loader.load_batch(batch=0)

        print(f"\n📂 分类 '{category}': {len(docs)} 个文档")
        for doc in docs[:3]:
            print(f"   - {doc.title}")


async def example_5_search_and_analyze():
    """示例 5: 搜索分析 - 搜索并分析相关文档"""
    print("\n" + "="*60)
    print("🔬 示例 5: 搜索和文档分析")
    print("="*60)

    loader = BatchDocumentLoader()

    # 搜索关键词
    queries = [
        "Spring Boot 配置",
        "Dubbo 服务",
        "微服务架构",
        "异常处理"
    ]

    for query in queries:
        docs = await loader.search_documents(query, limit=5)

        print(f"\n🔍 查询: '{query}'")
        print(f"   结果: {len(docs)} 个文档")

        for doc in docs[:2]:
            print(f"   - 📄 {doc.title}")
            print(f"     块数: {doc.chunk_count} | 格式: {doc.format}")


async def example_6_statistics_report():
    """示例 6: 统计报告 - 生成文档库统计信息"""
    print("\n" + "="*60)
    print("📊 示例 6: 文档库统计报告")
    print("="*60)

    loader = BatchDocumentLoader()
    stats = await loader.get_statistics()

    print(f"\n📈 文档库概况:")
    print(f"   总文档数: {stats['total_documents']}")
    print(f"   总块数: {stats['total_chunks']}")

    print(f"\n📂 文档分类分布:")
    for category, count in sorted(stats['by_category'].items()):
        percentage = (count / stats['total_documents'] * 100) if stats['total_documents'] > 0 else 0
        print(f"   {category:12} : {count:3} 个 ({percentage:5.1f}%)")

    print(f"\n📝 文档格式分布:")
    for format, count in sorted(stats['by_format'].items()):
        percentage = (count / stats['total_documents'] * 100) if stats['total_documents'] > 0 else 0
        print(f"   {format:8} : {count:3} 个 ({percentage:5.1f}%)")


async def example_7_custom_path_indexing():
    """示例 7: 自定义路径索引 - 索引指定目录的文档"""
    print("\n" + "="*60)
    print("📁 示例 7: 索引自定义目录")
    print("="*60)

    # 假设要索引项目中的额外文档
    custom_docs_path = Path("/path/to/your/docs")

    # 检查路径是否存在
    if not custom_docs_path.exists():
        print(f"⚠️  路径不存在: {custom_docs_path}")
        print("   请将此路径替换为实际路径")
        return

    config = BatchConfig(
        batch_size=30,
        max_concurrent=4
    )

    indexer = BatchDocumentIndexer(config)

    print(f"\n🔄 索引自定义目录: {custom_docs_path}")
    progress = await indexer.index_all_docs(custom_docs_path)

    print(f"\n✅ 索引完成: {progress.success_count} 个文档")


async def example_8_memory_optimized_loading():
    """示例 8: 内存优化 - 小批次大文档集处理"""
    print("\n" + "="*60)
    print("💾 示例 8: 内存优化载入")
    print("="*60)

    # 小批次配置，适合内存受限环境
    config = LoadConfig(
        batch_size=10,         # 小批次
        enable_cache=False,    # 禁用缓存节省内存
        filter_category="guide" # 只载入需要的分类
    )

    loader = BatchDocumentLoader(config)

    # 迭代处理所有文档（不一次性加载到内存）
    batch = 0
    total_processed = 0

    while True:
        docs = await loader.load_batch(batch)

        if not docs:
            break

        # 处理当前批次
        for doc in docs:
            # 这里进行你的处理逻辑
            total_processed += 1

        print(f"   批次 {batch}: 处理了 {len(docs)} 个文档 (总计: {total_processed})")

        batch += 1

        # 限制处理数量（示例）
        if total_processed >= 30:
            break

    print(f"\n✅ 处理完成，内存占用保持稳定")


async def main():
    """运行所有示例"""
    examples = [
        ("初始索引建立", example_1_initial_indexing),
        ("增量更新索引", example_2_incremental_update),
        ("批量查询文档", example_3_batch_query),
        ("按分类过滤查询", example_4_filtered_query),
        ("搜索和文档分析", example_5_search_and_analyze),
        ("文档库统计报告", example_6_statistics_report),
        ("索引自定义目录", example_7_custom_path_indexing),
        ("内存优化载入", example_8_memory_optimized_loading),
    ]

    print("\n" + "="*60)
    print("🚀 Context7 分批索引和批量载入使用示例")
    print("="*60)

    # 选择要运行的示例
    print("\n请选择要运行的示例:")
    for i, (name, _) in enumerate(examples, 1):
        print(f"   {i}. {name}")
    print(f"   0. 运行所有示例")

    try:
        choice = input("\n输入选择 (0-8): ").strip()

        if choice == "0":
            # 运行所有示例
            for name, example_func in examples:
                try:
                    await example_func()
                except Exception as e:
                    print(f"\n❌ 示例 '{name}' 执行失败: {e}")
        elif choice.isdigit() and 1 <= int(choice) <= len(examples):
            # 运行选定的示例
            idx = int(choice) - 1
            name, example_func = examples[idx]
            try:
                await example_func()
            except Exception as e:
                print(f"\n❌ 示例 '{name}' 执行失败: {e}")
                import traceback
                traceback.print_exc()
        else:
            print("❌ 无效的选择")

    except KeyboardInterrupt:
        print("\n\n⚠️  示例执行被用户中断")


if __name__ == "__main__":
    asyncio.run(main())
