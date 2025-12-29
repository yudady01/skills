---
name: review-report-generation
description: 智能代码审查报告生成技能，为ai-coding-java插件的review命令提供详细的Markdown报告输出
license: Apache 2.0
version: 1.0.0
tags:
  - report-generation
  - code-review
  - markdown
  - documentation
---

# 智能代码审查报告生成技能

## 🎯 技能概述

为 ai-coding-java 插件的代码审查功能提供企业级报告生成能力，自动将智能代码审查结果转换为详细的 Markdown 报告。

## 🔧 核心功能

### 📊 数据聚合
- 收集 code-reviewer 代理的分析结果
- 整合 architecture-analyzer 和 intelligent-diagnoser 的洞察
- 聚合质量门禁检查结果
- 汇总量化评分和问题分类

### 📋 报告生成
- 基于 Jinja2 模板的 Markdown 报告渲染
- 包含完整的四大核心内容：问题清单、质量评分、架构分析、审查记录
- 自动生成时间戳和版本信息
- 支持历史对比和趋势分析

### 💾 文件持久化
- 自动保存到项目 `docs/` 目录
- 按时间戳命名的报告文件管理
- 支持增量报告和历史追踪
- 提供报告文件路径和摘要信息

## 🏗️ 技术架构

### 模块组成
- **report_engine.py**: 核心报告引擎，负责模板渲染和文件生成
- **data_aggregator.py**: 数据聚合器，收集和整理各代理的分析结果
- **templates/**: 报告模板库，包含多种报告格式模板

### 依赖要求
```python
jinja2>=3.1.0           # Markdown 模板引擎
pyyaml>=6.0             # YAML 配置处理
```

## 📋 报告内容结构

### 综合审查报告
1. **审查概述**: 时间、范围、文件统计
2. **智能质量评估**: 总体评分、健康度、架构合理性
3. **详细问题清单**: 高中低优先级问题和修复建议
4. **架构分析**: 服务边界评估、模式识别、优化建议
5. **审查记录**: 代理分析结果、检查统计、智能总结
6. **行动计划**: 即时行动项、短期目标、长期改进

## 🚀 使用方式

### 自动触发
当用户执行 `/review` 命令时，技能自动在后台生成报告：
```bash
# 用户执行常规审查
/review

# 自动生成报告到
docs/review-2025-12-07-14-30-25.md
```

### 手动调用
也可以直接调用技能生成报告：
```python
from .report_engine import ReportEngine

engine = ReportEngine()
report_path = engine.generate_report(
    review_data=review_results,
    output_dir="docs/"
)
```

## 📊 报告特色

### AI驱动分析
- 集成多个AI代理的专业分析结果
- 智能问题分类和优先级排序
- 基于最佳实践的架构优化建议

### 企业级格式
- 标准化的报告结构和内容组织
- 适合技术管理和团队协作的报告格式
- 包含具体修复建议和代码示例

### 质量趋势跟踪
- 支持历史报告对比分析
- 代码质量变化趋势识别
- 改进指标和成熟度评估

## 🔧 配置选项

### 报告设置
```yaml
report_config:
  output_dir: "docs/"
  include_history: true
  max_history_reports: 10
  template_name: "comprehensive_review.md.j2"

scoring:
  weights:
    architecture: 0.3
    quality: 0.25
    complexity: 0.25
    performance: 0.2
```

## 🎯 优势特点

- **无感知增强**: 不改变现有用户体验，自动在后台生成报告
- **内容全面**: 包含用户需求的四大核心内容方面
- **格式专业**: 企业级Markdown报告，便于查阅和分享
- **历史追踪**: 支持质量趋势分析和改进对比
- **易于维护**: 模块化设计，便于后续功能扩展