---
description: 完整智能代码审查 - 集成AI驱动的架构分析、问题诊断和最佳实践检查，自动生成详细报告
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, TodoWrite, Task]
---

# 智能代码审查

执行完整的智能代码审查，自动启用所有高级分析功能，包括AI驱动的架构分析、问题诊断和企业级最佳实践检查。

## 功能特性

### 🤖 智能分析
- AI驱动的代码模式识别和问题预测
- 自动架构分析和设计建议
- 智能问题诊断和根因分析
- 基于Spring Boot 2.7 + Dubbo 3的专业知识

### 🔍 审查维度
1. **代码质量检查**
   - 类型安全和复杂度分析
   - 性能影响评估
   - 代码异味自动识别
   - 潜在bug预测分析

2. **合规性验证**
   - 企业级Spring Boot 2.7合规性
   - Dubbo 3微服务规范验证
   - 编码标准和安全最佳实践
   - 文档完整性检查

3. **架构分析**
   - 微服务边界合理性分析
   - Dubbo服务设计模式检查
   - 数据一致性策略评估
   - 缓存架构合理性审查

4. **问题诊断**
   - 性能瓶颈智能识别
   - 安全漏洞自动扫描
   - 资源泄漏风险检测
   - 并发问题和分布式事务诊断

### 📊 输出报告
- **整体健康度评分**: 多维度综合评分
- **问题分类统计**: 按严重程度和类型分类
- **智能建议**: AI生成的具体改进建议和代码示例
- **架构优化方案**: 针对微服务架构的改进建议
- **性能和安全建议**: 基于代码分析的优化建议
- **📋 详细Markdown报告**: 自动生成并保存到 `docs/` 目录

## 使用方法

```bash
# 执行完整智能代码审查（自动生成报告）
/review
```

审查将自动：
1. 扫描当前项目的代码文件
2. 执行静态分析
3. 运行智能架构分析
4. 进行问题诊断
5. **生成详细报告和改进建议**
6. **自动保存Markdown报告到 `docs/` 目录**
7. **显示报告摘要和文件位置**

## 📋 报告功能

### 自动报告生成
审查完成后，系统会自动生成详细的Markdown报告并保存到项目目录：

```bash
# 报告自动保存到
docs/review-2025-12-07-14-30-25.md

# 查看所有历史报告
ls docs/review-*.md

# 查看最新报告
cat docs/review-$(ls -t docs/review-*.md | head -1 | cut -d'-' -f2-)
```

### 报告内容
生成的报告包含四个核心方面：

1. **🔍 详细问题清单和修复建议**
   - 高/中/低优先级问题分类
   - 具体修复建议（含代码示例）
   - 位置、影响、预估修复时间

2. **🎯 智能质量评估与趋势分析**
   - 总体评分（A/B/C/D/F等级）
   - 代码健康度、架构合理性
   - 历史对比和质量趋势

3. **🏗️ 架构分析和优化建议**
   - 服务边界评估（DDD原则）
   - 架构模式识别
   - 微服务设计改进建议

4. **📊 全面的审查记录和总结**
   - 代理分析结果记录
   - 检查项目统计
   - 技术债务分析和风险评估
   - 下一步行动计划

### 报告管理工具

```bash
# 查看报告历史
python3 scripts/report_utils.py list

# 查看报告统计
python3 scripts/report_utils.py stats

# 清理旧报告（保留最新20个）
python3 scripts/report_utils.py clean --keep 20

# 生成报告索引
python3 scripts/report_utils.py index

# 验证报告文件
python3 scripts/report_utils.py validate docs/review-2025-12-07-14-30-25.md
```

## 配置文件（可选）

项目级配置文件 `.ai-coding-review.json`:
```json
{
  "intelligent_analysis": true,
  "focus_areas": ["architecture", "performance"],
  "severity_threshold": "medium",
  "suggestions_limit": 15,
  "report_config": {
    "auto_generate": true,
    "output_dir": "docs/",
    "include_history": true,
    "template": "comprehensive_review.md.j2"
  }
}
```

## 📺 详细终端输出示例

当用户执行 `/review` 命令时，将显示详细的处理过程和结果信息：

```bash
$ /review

🔍 开始智能代码审查...
📁 输出目录: docs/
📄 模板: comprehensive_review.md.j2
📊 输入数据长度: 2,847 字符

🧠 智能分析完成，开始数据聚合...
📋 报告生成启动...
✅ 报告生成成功!
📄 报告文件: docs/review-2025-12-07-14-30-25.md
📊 文件大小: 5.7 KB

📊 报告摘要:
   🎯 总体评分: B 级 (75.5/100)
   💚 代码健康度: 80%
   🏗️  架构合理性: 70%
   🔴 高优先级问题: 1 个
   🟡 中优先级问题: 1 个
   🟢 低优先级建议: 1 个

📋 详细报告已生成到 docs/ 目录
✅ 代码审查完成，报告已自动保存

💡 使用以下命令查看报告:
   cat docs/review-2025-12-07-14-30-25.md

📊 管理报告:
   python3 scripts/report_utils.py list
   python3 scripts/report_utils.py stats
```