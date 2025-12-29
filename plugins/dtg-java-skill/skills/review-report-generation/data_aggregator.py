#!/usr/bin/env python3
"""
智能代码审查数据聚合器
负责收集和整理各代理的分析结果，为报告生成提供结构化数据
"""

import json
import re
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass


@dataclass
class Issue:
    """代码问题数据结构"""
    priority: str  # "high", "medium", "low"
    category: str  # "architecture", "performance", "security", "style", etc.
    file_path: str
    line_number: Optional[int]
    description: str
    impact: str
    fix_suggestion: str
    code_example: Optional[str] = None
    estimated_time: Optional[str] = None


@dataclass
class QualityMetrics:
    """质量指标数据结构"""
    overall_score: float  # 0-100
    overall_grade: str    # A/B/C/D/F
    health_score: float   # 0-100
    architecture_score: float  # 0-100
    complexity_level: str    # "low", "medium", "high"
    performance_risk: str    # "low", "medium", "high"


class ReviewDataAggregator:
    """代码审查数据聚合器"""

    def __init__(self):
        self.issues: List[Issue] = []
        self.quality_metrics: Optional[QualityMetrics] = None
        self.architecture_analysis: Dict[str, Any] = {}
        self.review_summary: Dict[str, Any] = {}

    def parse_code_reviewer_output(self, output: str) -> Dict[str, Any]:
        """解析 code-reviewer 代理的输出"""
        data = {
            "issues": [],
            "quality_assessment": {},
            "recommendations": []
        }

        # 解析问题清单
        high_priority_issues = self._extract_issues_by_priority(output, "🔴")
        medium_priority_issues = self._extract_issues_by_priority(output, "🟡")
        low_priority_suggestions = self._extract_issues_by_priority(output, "🟢")

        data["issues"] = high_priority_issues + medium_priority_issues + low_priority_suggestions

        # 解析质量评估
        quality_match = re.search(r'总体评分[：:]\s*([A-F])', output)
        if quality_match:
            data["quality_assessment"]["overall_grade"] = quality_match.group(1)

        # 解析健康度评分
        health_match = re.search(r'代码健康度[：:]\s*(\d+)%', output)
        if health_match:
            data["quality_assessment"]["health_score"] = int(health_match.group(1))

        # 解析建议
        recommendations = self._extract_recommendations(output)
        data["recommendations"] = recommendations

        return data

    def parse_architecture_analyzer_output(self, output: str) -> Dict[str, Any]:
        """解析 architecture-analyzer 代理的输出"""
        data = {
            "service_boundaries": {},
            "architecture_patterns": [],
            "dependency_analysis": {},
            "optimization_suggestions": []
        }

        # 解析服务边界评估
        service_boundary_match = re.search(r'服务边界评估[：:]\s*([^\\n]+)', output)
        if service_boundary_match:
            data["service_boundaries"]["assessment"] = service_boundary_match.group(1).strip()

        # 解析架构模式
        patterns = re.findall(r'([A-Z][a-zA-Z]+模式|[a-zA-Z]+架构)', output)
        data["architecture_patterns"] = list(set(patterns))

        # 解析优化建议
        optimization_suggestions = self._extract_optimization_suggestions(output)
        data["optimization_suggestions"] = optimization_suggestions

        return data

    def parse_intelligent_diagnoser_output(self, output: str) -> Dict[str, Any]:
        """解析 intelligent-diagnoser 代理的输出"""
        data = {
            "code_smells": [],
            "performance_bottlenecks": [],
            "root_cause_analysis": {},
            "risk_assessment": {}
        }

        # 解析代码异味
        code_smells = self._extract_code_smells(output)
        data["code_smells"] = code_smells

        # 解析性能瓶颈
        bottlenecks = self._extract_performance_bottlenecks(output)
        data["performance_bottlenecks"] = bottlenecks

        return data

    def aggregate_review_data(self,
                            code_reviewer_output: str,
                            architecture_analyzer_output: str = "",
                            intelligent_diagnoser_output: str = "",
                            quality_gate_output: str = "",
                            git_summary: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """聚合所有代理的审查数据"""

        # 解析各代理输出
        code_review_data = self.parse_code_reviewer_output(code_reviewer_output)
        architecture_data = self.parse_architecture_analyzer_output(architecture_analyzer_output)
        diagnoser_data = self.parse_intelligent_diagnoser_output(intelligent_diagnoser_output)

        # 聚合问题数据
        all_issues = self._aggregate_issues(code_review_data, architecture_data, diagnoser_data)

        # 计算质量指标
        quality_metrics = self._calculate_quality_metrics(all_issues, code_review_data, architecture_data)

        # 构建综合数据
        aggregated_data = {
            "timestamp": datetime.now().isoformat(),
            "review_summary": {
                "total_issues": len(all_issues),
                "high_priority_count": len([i for i in all_issues if i.priority == "high"]),
                "medium_priority_count": len([i for i in all_issues if i.priority == "medium"]),
                "low_priority_count": len([i for i in all_issues if i.priority == "low"]),
                "files_analyzed": self._count_analyzed_files(code_reviewer_output),
                "duration": self._extract_duration(code_reviewer_output)
            },
            "quality_metrics": quality_metrics,
            "issues": all_issues,
            "architecture_analysis": {
                "service_boundaries": architecture_data.get("service_boundaries", {}),
                "architecture_patterns": architecture_data.get("architecture_patterns", []),
                "optimization_suggestions": architecture_data.get("optimization_suggestions", [])
            },
            "intelligent_insights": {
                "code_smells": diagnoser_data.get("code_smells", []),
                "performance_bottlenecks": diagnoser_data.get("performance_bottlenecks", []),
                "risk_assessment": self._assess_risks(all_issues, quality_metrics)
            },
            "recommendations": code_review_data.get("recommendations", []),
            "git_summary": git_summary or {},  # 添加Git摘要数据
            "agent_outputs": {
                "code_reviewer": code_reviewer_output,
                "architecture_analyzer": architecture_analyzer_output,
                "intelligent_diagnoser": intelligent_diagnoser_output
            }
        }

        return aggregated_data

    def _extract_issues_by_priority(self, output: str, priority_emoji: str) -> List[Dict[str, Any]]:
        """根据优先级表情符号提取问题"""
        issues = []
        pattern = (f'{priority_emoji}\\s*([^\\n]+)\\n(?:.*?位置[：:]*\\s*([^\\n]+)\\n)?'
                 f'(?:.*?影响[：:]*\\s*([^\\n]+)\\n)?(?:.*?建议[：:]*\\s*([^\\n]+)\\n)?')

        matches = re.findall(pattern, output, re.MULTILINE | re.DOTALL)

        for match in matches:
            description = match[0].strip()
            location = match[1].strip() if match[1] else "未指定"
            impact = match[2].strip() if match[2] else "待评估"
            suggestion = match[3].strip() if match[3] else "需要进一步分析"

            issues.append({
                "description": description,
                "location": location,
                "impact": impact,
                "fix_suggestion": suggestion,
                "priority": self._emoji_to_priority(priority_emoji)
            })

        return issues

    def _extract_recommendations(self, output: str) -> List[str]:
        """提取建议列表"""
        recommendations = []

        # 查找建议部分
        rec_section_match = re.search(r'(?:建议|推荐)[：:]*\\n((?:[•\\-]\\s*.*\\n?)*)', output)
        if rec_section_match:
            rec_text = rec_section_match.group(1)
            recommendations = re.findall(r'[•\\-]\\s*(.+)', rec_text)

        return [r.strip() for r in recommendations if r.strip()]

    def _extract_optimization_suggestions(self, output: str) -> List[Dict[str, str]]:
        """提取架构优化建议"""
        suggestions = []

        # 解析优化建议模式
        pattern = r'(\\w+(?:优化|改进|建议))[：:]*\\s*([^\\n]+)'
        matches = re.findall(pattern, output)

        for category, suggestion in matches:
            suggestions.append({
                "category": category,
                "suggestion": suggestion.strip()
            })

        return suggestions

    def _extract_code_smells(self, output: str) -> List[str]:
        """提取代码异味"""
        code_smells = []

        # 查找代码异味相关内容
        smell_patterns = [
            r'代码异味[：:]*\\s*([^\\n]+)',
            r'坏味道[：:]*\\s*([^\\n]+)',
            r'可疑代码[：:]*\\s*([^\\n]+)'
        ]

        for pattern in smell_patterns:
            matches = re.findall(pattern, output)
            code_smells.extend(matches)

        return list(set(code_smells))

    def _extract_performance_bottlenecks(self, output: str) -> List[str]:
        """提取性能瓶颈"""
        bottlenecks = []

        # 查找性能瓶颈相关内容
        bottleneck_patterns = [
            r'性能瓶颈[：:]*\\s*([^\\n]+)',
            r'性能问题[：:]*\\s*([^\\n]+)',
            r'性能风险[：:]*\\s*([^\\n]+)'
        ]

        for pattern in bottleneck_patterns:
            matches = re.findall(pattern, output)
            bottlenecks.extend(matches)

        return list(set(bottlenecks))

    def _aggregate_issues(self, code_review_data: Dict, architecture_data: Dict, diagnoser_data: Dict) -> List[Dict[str, Any]]:
        """聚合所有问题数据"""
        all_issues = []

        # 从 code-reviewer 数据添加问题
        for issue in code_review_data.get("issues", []):
            all_issues.append({
                **issue,
                "category": "general",
                "source": "code-reviewer"
            })

        # 从 architecture-analyzer 数据添加问题
        for suggestion in architecture_data.get("optimization_suggestions", []):
            all_issues.append({
                "description": f"架构优化: {suggestion['suggestion']}",
                "location": "架构层面",
                "impact": "影响系统可维护性和扩展性",
                "fix_suggestion": suggestion['suggestion'],
                "priority": "medium",
                "category": "architecture",
                "source": "architecture-analyzer"
            })

        # 从 intelligent-diagnoser 数据添加问题
        for smell in diagnoser_data.get("code_smells", []):
            all_issues.append({
                "description": f"代码异味: {smell}",
                "location": "代码层面",
                "impact": "影响代码质量和可读性",
                "fix_suggestion": "重构相关代码，应用最佳实践",
                "priority": "medium",
                "category": "code-quality",
                "source": "intelligent-diagnoser"
            })

        return all_issues

    def _calculate_quality_metrics(self, issues: List[Dict], code_review_data: Dict, architecture_data: Dict) -> Dict[str, Any]:
        """计算质量指标"""

        # 统计问题数量
        high_count = len([i for i in issues if i.get("priority") == "high"])
        medium_count = len([i for i in issues if i.get("priority") == "medium"])
        low_count = len([i for i in issues if i.get("priority") == "low"])
        total_count = len(issues)

        # 基础评分（从 code-reviewer 数据获取）
        health_score = code_review_data.get("quality_assessment", {}).get("health_score", 70)
        overall_grade = code_review_data.get("quality_assessment", {}).get("overall_grade", "C")

        # 根据问题数量调整评分
        penalty = high_count * 10 + medium_count * 5 + low_count * 2
        adjusted_score = max(0, health_score - penalty)

        # 计算综合评分
        architecture_score = 80 if architecture_data.get("architecture_patterns") else 60
        complexity_level = "medium"  # 可以根据实际代码复杂度计算

        # 综合评分算法
        weights = {"architecture": 0.3, "quality": 0.25, "complexity": 0.25, "performance": 0.2}
        complexity_score = 70 if complexity_level == "low" else (50 if complexity_level == "medium" else 30)
        performance_score = max(0, 100 - high_count * 15 - medium_count * 8)

        overall_score = (
            architecture_score * weights["architecture"] +
            adjusted_score * weights["quality"] +
            complexity_score * weights["complexity"] +
            performance_score * weights["performance"]
        )

        # 确定等级
        if overall_score >= 90:
            grade = "A"
        elif overall_score >= 80:
            grade = "B"
        elif overall_score >= 70:
            grade = "C"
        elif overall_score >= 60:
            grade = "D"
        else:
            grade = "F"

        return {
            "overall_score": round(overall_score, 1),
            "overall_grade": grade,
            "health_score": round(adjusted_score, 1),
            "architecture_score": architecture_score,
            "complexity_level": complexity_level,
            "performance_risk": "high" if high_count > 3 else ("medium" if high_count > 0 else "low")
        }

    def _assess_risks(self, issues: List[Dict], quality_metrics: Dict) -> Dict[str, Any]:
        """评估风险"""
        high_count = len([i for i in issues if i["priority"] == "high"])
        overall_score = quality_metrics.get("overall_score", 70)

        if high_count > 5 or overall_score < 50:
            risk_level = "high"
            risk_description = "发现多个严重问题，建议立即处理"
        elif high_count > 2 or overall_score < 70:
            risk_level = "medium"
            risk_description = "存在一些需要关注的问题"
        else:
            risk_level = "low"
            risk_description = "整体质量良好，风险较低"

        return {
            "risk_level": risk_level,
            "risk_description": risk_description,
            "technical_debt": self._assess_technical_debt(issues, quality_metrics)
        }

    def _assess_technical_debt(self, issues: List[Dict], quality_metrics: Dict) -> Dict[str, Any]:
        """评估技术债务"""
        # 简化的技术债务评估
        high_count = len([i for i in issues if i.get("priority") == "high"])
        medium_count = len([i for i in issues if i.get("priority") == "medium"])

        estimated_days = high_count * 3 + medium_count * 1.5  # 粗略估算

        if estimated_days > 20:
            debt_level = "high"
        elif estimated_days > 10:
            debt_level = "medium"
        else:
            debt_level = "low"

        return {
            "debt_level": debt_level,
            "estimated_fix_days": round(estimated_days, 1),
            "most_critical_categories": self._get_top_issue_categories(issues)
        }

    def _get_top_issue_categories(self, issues: List[Dict]) -> List[str]:
        """获取最主要的问题类别"""
        category_count = {}
        for issue in issues:
            category = issue.get("category", "general")
            category_count[category] = category_count.get(category, 0) + 1

        return sorted(category_count.keys(), key=lambda x: category_count[x], reverse=True)[:3]

    def _emoji_to_priority(self, emoji: str) -> str:
        """将表情符号转换为优先级"""
        emoji_to_priority_map = {
            "🔴": "high",
            "🟡": "medium",
            "🟢": "low"
        }
        return emoji_to_priority_map.get(emoji, "medium")

    def _count_analyzed_files(self, output: str) -> int:
        """统计分析的文件数量"""
        # 尝试从输出中提取文件数量
        file_count_match = re.search(r'(\\d+)\\s*个文件', output)
        if file_count_match:
            return int(file_count_match.group(1))
        return 0

    def _extract_duration(self, output: str) -> str:
        """提取执行时长"""
        # 尝试从输出中提取时长信息
        duration_match = re.search(r'(\\d+(?:\\.\\d+)?)\\s*(?:秒|分钟|小时)', output)
        if duration_match:
            return duration_match.group(0)
        return "未记录"