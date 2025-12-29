#!/usr/bin/env python3
"""
报告生成功能测试脚本
用于验证review-report-generation技能的功能
"""

import sys
import json
from pathlib import Path

# 添加skills目录到Python路径
current_dir = Path(__file__).parent
skills_dir = current_dir / "skills"
review_report_dir = skills_dir / "review-report-generation"
sys.path.insert(0, str(skills_dir))
sys.path.insert(0, str(review_report_dir))

def test_data_aggregator():
    """测试数据聚合器"""
    print("🧪 测试数据聚合器...")

    try:
        # 直接导入模块
        sys.path.insert(0, str(current_dir / "skills" / "review-report-generation"))
        import data_aggregator
        ReviewDataAggregator = data_aggregator.ReviewDataAggregator

        aggregator = ReviewDataAggregator()

        # 模拟代理输出
        code_reviewer_output = """
📋 智能代码审查报告

### 审查概述
- 审查时间: 2025-12-07 14:30:25
- 分析文件数: 15

### 智能质量评估
- 总体评分: B (75分)
- 代码健康度: 80%

### 发现的问题
🔴 高优先级问题
1. 潜在的SQL注入风险
   位置: UserRepository.java:45
   影响: 可能导致数据泄露
   建议: 使用参数化查询

🟡 中优先级问题
2. 方法过长
   位置: OrderService.java:120
   影响: 可读性和维护性
   建议: 重构为更小的方法

🟢 低优先级建议
3. 缺少注释
   位置: PaymentController.java
   影响: 代码理解难度
   建议: 添加方法注释
        """

        # 聚合数据
        aggregated_data = aggregator.aggregate_review_data(
            code_reviewer_output=code_reviewer_output
        )

        print(f"✅ 数据聚合成功:")
        print(f"   - 总问题数: {aggregated_data['review_summary']['total_issues']}")
        print(f"   - 高优先级: {aggregated_data['review_summary']['high_priority_count']}")
        print(f"   - 总体评分: {aggregated_data['quality_metrics']['overall_score']}")

        return True

    except Exception as e:
        print(f"❌ 数据聚合器测试失败: {e}")
        return False

def test_report_engine():
    """测试报告引擎"""
    print("\n🧪 测试报告引擎...")

    try:
        # 直接导入模块
        sys.path.insert(0, str(current_dir / "skills" / "review-report-generation"))
        import report_engine
        ReportEngine = report_engine.ReportEngine

        # 创建示例数据
        sample_data = {
            "review_summary": {
                "timestamp": "2025-12-07T14:30:25Z",
                "files_analyzed": 15,
                "total_issues": 3,
                "high_priority_count": 1,
                "medium_priority_count": 1,
                "low_priority_count": 1,
                "duration": "45秒"
            },
            "quality_metrics": {
                "overall_score": 75.5,
                "overall_grade": "B",
                "health_score": 80,
                "architecture_score": 70,
                "complexity_level": "medium",
                "performance_risk": "medium"
            },
            "issues": [
                {
                    "priority": "high",
                    "category": "security",
                    "description": "潜在的SQL注入风险",
                    "location": "UserRepository.java:45",
                    "impact": "可能导致数据泄露",
                    "fix_suggestion": "使用参数化查询",
                    "code_example": "@Query(\"SELECT u FROM User u WHERE u.username = :username\")",
                    "estimated_time": "2-3小时",
                    "source": "code-reviewer"
                },
                {
                    "priority": "medium",
                    "category": "maintainability",
                    "description": "方法过长，可读性差",
                    "location": "OrderService.java:120",
                    "impact": "维护困难",
                    "fix_suggestion": "重构为更小的方法",
                    "estimated_time": "1-2小时",
                    "source": "code-reviewer"
                },
                {
                    "priority": "low",
                    "category": "documentation",
                    "description": "缺少方法注释",
                    "location": "PaymentController.java",
                    "impact": "代码理解困难",
                    "fix_suggestion": "添加JavaDoc注释",
                    "estimated_time": "30分钟",
                    "source": "code-reviewer"
                }
            ],
            "architecture_analysis": {
                "service_boundaries": {
                    "assessment": "服务边界基本合理"
                },
                "architecture_patterns": ["微服务架构", "分层架构"],
                "optimization_suggestions": [
                    {
                        "category": "缓存优化",
                        "suggestion": "建议在查询频繁的方法上添加缓存"
                    }
                ]
            },
            "intelligent_insights": {
                "code_smells": ["长方法", "重复代码"],
                "performance_bottlenecks": ["数据库查询效率低"],
                "risk_assessment": {
                    "risk_level": "medium",
                    "risk_description": "存在一些需要关注的问题"
                }
            },
            "recommendations": [
                "优先修复高优先级安全问题",
                "加强代码注释和文档",
                "优化数据库查询性能"
            ]
        }

        # 初始化报告引擎
        engine = ReportEngine()

        # 检查可用模板
        templates = engine.get_available_templates()
        print(f"📄 可用模板: {templates}")

        if not templates:
            print("❌ 未找到模板文件")
            return False

        # 生成报告
        output_dir = current_dir / "docs"
        report_path = engine.generate_report(
            review_data=sample_data,
            template_name=templates[0],
            output_dir=str(output_dir),
            filename="test_review_report"
        )

        print(f"✅ 报告生成成功: {report_path}")

        # 验证报告文件
        if Path(report_path).exists():
            file_size = Path(report_path).stat().st_size
            print(f"📊 报告文件大小: {file_size} 字节")

            # 读取报告内容并检查关键信息
            with open(report_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if "智能代码审查报告" in content and "B 级" in content:
                print("✅ 报告内容验证通过")
                return True
            else:
                print("❌ 报告内容验证失败")
                return False
        else:
            print("❌ 报告文件不存在")
            return False

    except Exception as e:
        print(f"❌ 报告引擎测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_report_utils():
    """测试报告工具"""
    print("\n🧪 测试报告工具...")

    try:
        # 导入工具函数
        sys.path.insert(0, str(current_dir / "scripts"))
        from report_utils import ReportUtils

        # 测试报告统计
        stats = ReportUtils.get_report_statistics(str(current_dir / "docs"))
        print(f"📊 报告统计: 总数={stats['total_reports']}, 总大小={stats['total_size']}")

        # 测试报告历史
        history = ReportUtils.get_report_history(str(current_dir / "docs"), 5)
        print(f"📋 报告历史: {len(history)} 个报告")

        # 测试报告摘要提取
        if history:
            summary = ReportUtils.extract_report_summary(history[0]["path"])
            if summary:
                print(f"📄 最新报告摘要: 评分={summary.get('overall_grade', 'N/A')}")

        print("✅ 报告工具测试通过")
        return True

    except Exception as e:
        print(f"❌ 报告工具测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("🚀 开始测试AI智能代码审查报告生成功能\n")

    # 检查依赖
    try:
        import jinja2
        import yaml
        print("✅ 依赖检查通过")
    except ImportError as e:
        print(f"❌ 缺少依赖: {e}")
        print("请运行: pip install jinja2>=3.1.0 pyyaml>=6.0")
        return 1

    # 运行测试
    tests = [
        test_data_aggregator,
        test_report_engine,
        test_report_utils
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        if test():
            passed += 1

    print(f"\n📊 测试结果: {passed}/{total} 通过")

    if passed == total:
        print("🎉 所有测试通过！报告生成功能正常工作")

        # 显示使用示例
        print("\n💡 使用示例:")
        print("1. 执行代码审查:")
        print("   /review")
        print("2. 查看生成的报告:")
        print("   ls docs/review-*.md")
        print("3. 管理报告:")
        print("   python3 scripts/report_utils.py list")
        print("   python3 scripts/report_utils.py stats")

        return 0
    else:
        print("❌ 部分测试失败，请检查实现")
        return 1

if __name__ == "__main__":
    sys.exit(main())