---
name: context7-document-server
description: 基于 MCP 协议的智能文档处理和检索服务器，为 Spring Boot + Dubbo 微服务开发提供专业文档知识库支持（支持分批索引和批量载入）
license: Apache 2.0
version: 2.0.0
tags:
  - documentation
  - retrieval
  - vector-search
  - mcp-server
  - spring-boot-docs
  - knowledge-management
  - batch-indexing
  - bulk-loading
---

# Context7 智能文档服务器

Context7 是专门为 Spring Boot 2.7 + Dubbo 3 微服务开发设计的智能文档服务器，提供强大的文档处理、向量化检索和知识管理能力。

**🆕 v2.0 新特性**：
- **分批索引处理** - 支持大规模文档的高效分批索引
- **批量载入优化** - 智能缓存和分批载入，减少内存占用
- **断点续传** - 索引过程可中断恢复，支持大规模处理
- **进度跟踪** - 实时显示索引进度和统计信息

## 🚀 核心能力

### 📚 混合文档支持
- **内置企业级文档** - 4,512+ 行权威 Spring Boot + Dubbo 开发指南
- **用户自定义文档** - 支持项目特定文档、设计文档、API 文档
- **多格式支持** - Markdown、PDF、HTML、文本文件
- **智能分类管理** - 自动分类和标签管理

### 🔍 智能检索引擎
- **语义检索** - 基于向量的语义理解和检索
- **关键词检索** - 精确术语匹配
- **混合检索** - 结合语义和关键词的最佳效果
- **上下文感知** - 理解开发场景和问题背景

### ⚡ 开发场景优化
- **问题解决检索** - 快速找到错误解决方案
- **最佳实践查找** - 检索架构设计和编码规范
- **配置参考搜索** - 快速找到配置示例
- **API 文档查询** - 接口使用方法和示例代码

## 🎯 使用场景

### 1. 开发过程中
```bash
# 查找配置示例
/docs-search "Spring Boot Redis 配置"

# 查找最佳实践
/docs-search "微服务事务处理最佳实践"

# 解决问题
/docs-search "Dubbo 服务发现失败"
```

### 2. 代码审查时
```bash
# 验证编码规范
/docs-search "Java 异常处理最佳实践"

# 检查架构模式
/docs-search "领域驱动设计聚合设计"
```

### 3. 学习培训
```bash
# 学习新技术
/docs-search "Spring Boot 2.7 新特性"

# 了解架构模式
/docs-search "微服务架构模式选择"
```

## 🔧 技术特性

### 性能优化
- **响应时间 < 5秒** - 满足开发场景性能要求
- **智能缓存** - 常用查询结果缓存
- **增量索引** - 只处理变更的文档
- **异步处理** - 支持并发文档处理

### 🆕 分批索引 (v2.0)
- **批次处理** - 默认每批处理 50 个文档，可配置
- **并发控制** - 支持 1-10 个并发处理任务
- **断点续传** - 每 10 个文档自动保存检查点
- **内存优化** - 内存限制可配置（默认 1GB）
- **去重处理** - 自动跳过已索引文档

### 🆕 批量载入 (v2.0)
- **分批载入** - 每批载入 20 个文档，减少内存占用
- **LRU 缓存** - 最近使用的文档保持在内存中
- **智能过滤** - 支持按分类、来源过滤载入
- **统计信息** - 实时显示文档和块数统计

### 企业级特性
- **文档版本管理** - 支持文档版本跟踪
- **访问控制** - 基于分类的访问权限
- **审计日志** - 完整的查询和索引日志
- **数据安全** - 本地存储，数据不外泄

## 📊 文档统计

### 内置文档库 (4,512行)
- **快速开始指南** (281行)
- **项目设置指南** (610行)
- **编码规范** (592行)
- **架构原则** (673行)
- **微服务开发** (1,166行)
- **Dubbo 配置** (855行)
- **设计模板** (335行)

### 支持的用户文档类型
- **设计文档** - PRD、技术设计、架构文档
- **API 文档** - 接口规范、使用示例
- **配置文档** - 环境配置、部署配置
- **知识文档** - 最佳实践、问题解决方案

## 📝 使用指南

### 分批索引 (batch_indexer.py)

**基本用法**：
```bash
# 索引所有内置文档（默认配置）
python3 scripts/batch_indexer.py

# 列出已索引的文档
python3 scripts/batch_indexer.py --list
```

**高级配置**：
```bash
# 自定义批次大小和并发数
python3 scripts/batch_indexer.py --batch-size 100 --concurrent 10

# 重新索引所有文档（跳过去重）
python3 scripts/batch_indexer.py --reindex

# 禁用断点续传
python3 scripts/batch_indexer.py --no-checkpoint

# 索引指定目录
python3 scripts/batch_indexer.py --path /path/to/docs

# 清除所有索引
python3 scripts/batch_indexer.py --clear
```

### 批量载入 (batch_loader.py)

**基本用法**：
```bash
# 载入第一批文档
python3 scripts/batch_loader.py --batch 0

# 载入指定文档
python3 scripts/batch_loader.py --doc-id builtin_doc_abc123

# 搜索文档
python3 scripts/batch_loader.py --search "Spring Boot"
```

**高级配置**：
```bash
# 查看统计信息
python3 scripts/batch_loader.py --stats

# 按分类过滤载入
python3 scripts/batch_loader.py --category guide --batch 0

# 自定义批次大小
python3 scripts/batch_loader.py --batch-size 50 --batch 0

# 禁用缓存
python3 scripts/batch_loader.py --no-cache

# 清空缓存
python3 scripts/batch_loader.py --clear-cache
```

### Python API 使用

**分批索引**：
```python
import asyncio
from scripts.batch_indexer import BatchDocumentIndexer, BatchConfig

async def index_docs():
    # 创建配置
    config = BatchConfig(
        batch_size=100,        # 每批处理 100 个文档
        max_concurrent=8,      # 8 个并发任务
        enable_checkpoint=True,# 启用断点续传
        skip_indexed=True      # 跳过已索引文档
    )

    # 创建索引器
    indexer = BatchDocumentIndexer(config)

    # 执行索引
    progress = await indexer.index_all_docs()

    print(f"成功索引 {progress.success_count} 个文档")

asyncio.run(index_docs())
```

**批量载入**：
```python
import asyncio
from scripts.batch_loader import BatchDocumentLoader, LoadConfig

async def load_docs():
    # 创建配置
    config = LoadConfig(
        batch_size=30,         # 每批载入 30 个文档
        enable_cache=True,     # 启用缓存
        cache_size=200,        # 缓存 200 个文档
        filter_category="guide" # 只载入指南类文档
    )

    # 创建载入器
    loader = BatchDocumentLoader(config)

    # 载入第一批
    docs = await loader.load_batch(batch=0)

    for doc in docs:
        print(f"{doc.title}: {doc.chunk_count} 块")

    # 获取统计信息
    stats = await loader.get_statistics()
    print(f"总文档数: {stats['total_documents']}")

asyncio.run(load_docs())
```