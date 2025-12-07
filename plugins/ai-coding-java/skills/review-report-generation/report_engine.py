#!/usr/bin/env python3
"""
智能代码审查报告引擎
负责将聚合的审查数据渲染为详细的Markdown报告
"""

import os
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional
from jinja2 import Environment, FileSystemLoader, Template
import yaml

from data_aggregator import ReviewDataAggregator


class ReportEngine:
    """代码审查报告引擎"""

    def __init__(self, template_dir: Optional[str] = None):
        """
        初始化报告引擎

        Args:
            template_dir: 模板目录路径，默认使用当前目录下的templates
        """
        if template_dir is None:
            # 获取当前脚本所在目录的templates子目录
            current_dir = Path(__file__).parent
            template_dir = current_dir / "templates"

        self.template_dir = Path(template_dir)
        self.template_dir.mkdir(exist_ok=True)

        # 初始化Jinja2环境
        self.jinja_env = Environment(
            loader=FileSystemLoader(str(self.template_dir)),
            autoescape=False,
            trim_blocks=True,
            lstrip_blocks=True
        )

        # 注册自定义过滤器
        self._register_custom_filters()

        self.aggregator = ReviewDataAggregator()

    def _register_custom_filters(self):
        """注册自定义Jinja2过滤器"""

        def priority_emoji(priority: str) -> str:
            """优先级转表情符号"""
            emoji_map = {
                "high": "🔴",
                "medium": "🟡",
                "low": "🟢"
            }
            return emoji_map.get(priority, "⚪")

        def grade_color(grade: str) -> str:
            """等级转颜色"""
            color_map = {
                "A": "🟢",
                "B": "🟡",
                "C": "🟠",
                "D": "🔴",
                "F": "⚫"
            }
            return color_map.get(grade, "⚪")

        def format_datetime(timestamp: str, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
            """格式化时间戳"""
            try:
                dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                return dt.strftime(format_str)
            except:
                return timestamp

        def risk_level_emoji(risk_level: str) -> str:
            """风险等级转表情符号"""
            emoji_map = {
                "high": "🚨",
                "medium": "⚠️",
                "low": "✅"
            }
            return emoji_map.get(risk_level, "❓")

        def format_file_size(size_bytes: int) -> str:
            """格式化文件大小"""
            if size_bytes < 1024:
                return f"{size_bytes} B"
            elif size_bytes < 1024 * 1024:
                return f"{size_bytes / 1024:.1f} KB"
            else:
                return f"{size_bytes / (1024 * 1024):.1f} MB"

        # 注册过滤器
        self.jinja_env.filters['priority_emoji'] = priority_emoji
        self.jinja_env.filters['grade_color'] = grade_color
        self.jinja_env.filters['format_datetime'] = format_datetime
        self.jinja_env.filters['risk_level_emoji'] = risk_level_emoji
        self.jinja_env.filters['format_file_size'] = format_file_size

    def generate_report(self,
                       review_data: Dict[str, Any],
                       template_name: str = "comprehensive_review.md.j2",
                       output_dir: str = "docs",
                       filename: Optional[str] = None) -> str:
        """
        生成代码审查报告

        Args:
            review_data: 聚合的审查数据
            template_name: 模板文件名
            output_dir: 输出目录
            filename: 自定义文件名（不包含扩展名）

        Returns:
            生成的报告文件路径
        """
        try:
            # 加载模板
            template = self.jinja_env.get_template(template_name)

            # 准备模板数据
            template_data = self._prepare_template_data(review_data)

            # 渲染报告
            report_content = template.render(**template_data)

            # 确定输出文件路径
            if filename is None:
                timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                filename = f"review-{timestamp}"

            output_dir = Path(output_dir)
            output_dir.mkdir(exist_ok=True)

            report_path = output_dir / f"{filename}.md"

            # 写入文件
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report_content)

            return str(report_path)

        except Exception as e:
            raise RuntimeError(f"报告生成失败: {str(e)}")

    def _prepare_template_data(self, review_data: Dict[str, Any]) -> Dict[str, Any]:
        """准备模板数据"""

        # 添加计算字段
        template_data = review_data.copy()

        # 添加生成时间
        template_data["generation_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 添加插件版本信息
        template_data["plugin_version"] = "1.0.0"

        # 添加AI模型信息
        template_data["ai_model"] = "Claude Sonnet 4.5"

        # 计算问题统计
        issues = review_data.get("issues", [])
        template_data["issue_statistics"] = self._calculate_issue_statistics(issues)

        # 生成执行摘要
        template_data["executive_summary"] = self._generate_executive_summary(review_data)

        # 生成下一步行动计划
        template_data["action_plan"] = self._generate_action_plan(review_data)

        return template_data

    def _calculate_issue_statistics(self, issues: list) -> Dict[str, Any]:
        """计算问题统计信息"""
        if not issues:
            return {
                "total": 0,
                "by_priority": {"high": 0, "medium": 0, "low": 0},
                "by_category": {},
                "by_source": {}
            }

        stats = {
            "total": len(issues),
            "by_priority": {"high": 0, "medium": 0, "low": 0},
            "by_category": {},
            "by_source": {}
        }

        for issue in issues:
            # 按优先级统计
            priority = issue.get("priority", "medium")
            stats["by_priority"][priority] = stats["by_priority"].get(priority, 0) + 1

            # 按类别统计
            category = issue.get("category", "general")
            stats["by_category"][category] = stats["by_category"].get(category, 0) + 1

            # 按来源统计
            source = issue.get("source", "unknown")
            stats["by_source"][source] = stats["by_source"].get(source, 0) + 1

        return stats

    def _generate_executive_summary(self, review_data: Dict[str, Any]) -> Dict[str, Any]:
        """生成执行摘要"""
        quality_metrics = review_data.get("quality_metrics", {})
        review_summary = review_data.get("review_summary", {})
        issues = review_data.get("issues", [])

        summary = {
            "overall_assessment": self._get_overall_assessment(quality_metrics),
            "key_findings": self._extract_key_findings(issues, quality_metrics),
            "critical_issues": [i for i in issues if i.get("priority") == "high"][:3],  # 最多3个关键问题
            "quality_trend": "stable",  # 可以基于历史数据计算
            "recommendations_priority": "high" if len([i for i in issues if i.get("priority") == "high"]) > 2 else "medium"
        }

        return summary

    def _get_overall_assessment(self, quality_metrics: Dict[str, Any]) -> str:
        """获取总体评估"""
        overall_score = quality_metrics.get("overall_score", 70)
        overall_grade = quality_metrics.get("overall_grade", "C")

        if overall_score >= 85:
            return f"优秀 (A级, {overall_score}分) - 代码质量很高，符合企业级标准"
        elif overall_score >= 75:
            return f"良好 ({overall_grade}级, {overall_score}分) - 代码质量较好，有少量改进空间"
        elif overall_score >= 65:
            return f"一般 ({overall_grade}级, {overall_score}分) - 代码质量中等，需要一些改进"
        elif overall_score >= 50:
            return f"较差 ({overall_grade}级, {overall_score}分) - 代码质量较低，需要重点改进"
        else:
            return f"差 ({overall_grade}级, {overall_score}分) - 代码质量很差，需要立即重构"

    def _extract_key_findings(self, issues: list, quality_metrics: Dict[str, Any]) -> list:
        """提取关键发现"""
        findings = []

        # 基于问题数量的发现
        high_count = len([i for i in issues if i.get("priority") == "high"])
        if high_count > 0:
            findings.append(f"发现 {high_count} 个高优先级问题需要立即处理")

        # 基于评分的发现
        health_score = quality_metrics.get("health_score", 70)
        if health_score < 60:
            findings.append(f"代码健康度较低 ({health_score}分)，建议进行全面重构")
        elif health_score < 80:
            findings.append(f"代码健康度中等 ({health_score}分)，有改进空间")

        # 基于架构的发现
        architecture_score = quality_metrics.get("architecture_score", 70)
        if architecture_score < 70:
            findings.append("架构设计存在优化空间")

        # 基于性能风险的发现
        performance_risk = quality_metrics.get("performance_risk", "medium")
        if performance_risk == "high":
            findings.append("存在较高的性能风险")

        return findings

    def _generate_action_plan(self, review_data: Dict[str, Any]) -> Dict[str, Any]:
        """生成行动计划"""
        issues = review_data.get("issues", [])
        quality_metrics = review_data.get("quality_metrics", {})

        # 按优先级分组问题
        high_issues = [i for i in issues if i.get("priority") == "high"]
        medium_issues = [i for i in issues if i.get("priority") == "medium"]
        low_issues = [i for i in issues if i.get("priority") == "low"]

        # 即时行动项 (1-2周)
        immediate_actions = []
        for issue in high_issues[:5]:  # 最多5个即时行动项
            immediate_actions.append({
                "action": f"修复问题: {issue.get('description', '未知问题')}",
                "location": issue.get('location', '未指定'),
                "estimated_time": "2-3天" if "复杂" in issue.get('description', '') else "1天",
                "priority": "高"
            })

        # 短期目标 (1个月)
        short_term_goals = []
        if medium_issues:
            short_term_goals.append(f"处理 {len(medium_issues)} 个中优先级问题")

        if quality_metrics.get("health_score", 70) < 80:
            short_term_goals.append("提升代码健康度至80分以上")

        short_term_goals.append("实施架构优化建议")
        short_term_goals.append("完善单元测试覆盖率")

        # 长期改进 (3个月+)
        long_term_improvements = [
            "建立代码质量监控体系",
            "实施持续集成和代码质量门禁",
            "定期进行架构评审和重构",
            "团队培训和最佳实践推广",
            "引入自动化代码质量检查工具"
        ]

        return {
            "immediate_actions": immediate_actions,
            "short_term_goals": short_term_goals,
            "long_term_improvements": long_term_improvements
        }

    def generate_from_agent_outputs(self,
                                  code_reviewer_output: str,
                                  architecture_analyzer_output: str = "",
                                  intelligent_diagnoser_output: str = "",
                                  quality_gate_output: str = "",
                                  output_dir: str = "docs") -> str:
        """
        从代理输出生成报告的便捷方法

        Args:
            code_reviewer_output: code-reviewer代理的输出
            architecture_analyzer_output: architecture-analyzer代理的输出
            intelligent_diagnoser_output: intelligent-diagnoser代理的输出
            quality_gate_output: 质量门禁的输出
            output_dir: 输出目录

        Returns:
            生成的报告文件路径
        """
        # 聚合数据
        review_data = self.aggregator.aggregate_review_data(
            code_reviewer_output=code_reviewer_output,
            architecture_analyzer_output=architecture_analyzer_output,
            intelligent_diagnoser_output=intelligent_diagnoser_output,
            quality_gate_output=quality_gate_output
        )

        # 生成报告
        return self.generate_report(review_data=review_data, output_dir=output_dir)

    def get_available_templates(self) -> list:
        """获取可用的模板列表"""
        template_files = []
        if self.template_dir.exists():
            for file_path in self.template_dir.glob("*.j2"):
                template_files.append(file_path.name)
        return sorted(template_files)

    def validate_template(self, template_name: str) -> bool:
        """验证模板文件是否存在且有效"""
        try:
            template = self.jinja_env.get_template(template_name)
            return True
        except:
            return False