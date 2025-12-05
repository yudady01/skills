#!/usr/bin/env python3
"""
系统兼容性检查工具

检查插件系统内部命名与实际文件命名的一致性问题
"""

import json
import os
import sys
import re
from pathlib import Path
from typing import Dict, List, Optional, Set
from dataclasses import dataclass

@dataclass
class PluginInfo:
    """插件信息"""
    market_name: str  # marketplace.json 中的名称
    directory_name: str  # 实际目录名
    expected_name: str  # 标准化的期望名称
    plugin_config: Dict  # 插件配置
    skills_count: int = 0
    has_skills: bool = False

class SystemCompatibilityChecker:
    """系统兼容性检查器"""

    def __init__(self, marketplace_path: str = ".claude-plugin/marketplace.json"):
        self.marketplace_path = Path(marketplace_path)
        self.base_path = self.marketplace_path.parent.parent
        self.plugins_dir = self.base_path / "plugins"
        self.plugins = []
        self.issues = []

    def analyze_system(self) -> Dict:
        """分析整个系统"""
        # 收集插件信息
        self.collect_plugin_info()

        # 检测兼容性问题
        self.detect_compatibility_issues()

        # 生成分析报告
        return self.generate_analysis_report()

    def collect_plugin_info(self):
        """收集插件信息"""
        self.plugins = []

        # 读取 marketplace.json
        if not self.marketplace_path.exists():
            self.issues.append({
                "type": "critical",
                "category": "system",
                "message": f"marketplace.json 文件不存在: {self.marketplace_path}",
                "fixable": False
            })
            return

        try:
            with open(self.marketplace_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            marketplace_plugins = {p["name"]: p for p in data.get("plugins", [])}

            # 扫描实际插件目录
            if self.plugins_dir.exists():
                actual_plugins = {}
                for item in self.plugins_dir.iterdir():
                    if item.is_dir():
                        # 检查是否有 marketplace.json
                        plugin_config_file = item / ".claude-plugin" / "marketplace.json"
                        plugin_config = {}
                        if plugin_config_file.exists():
                            try:
                                with open(plugin_config_file, 'r', encoding='utf-8') as f:
                                    plugin_config = json.load(f)
                            except:
                                pass

                        # 统计技能数量
                        skills_count = 0
                        has_skills = False
                        skills_dir = item / "skills"
                        if skills_dir.exists():
                            # 检查主 SKILL.md
                            if (skills_dir / "SKILL.md").exists():
                                skills_count += 1
                                has_skills = True

                            # 检查子目录中的技能
                            for subitem in skills_dir.iterdir():
                                if subitem.is_dir() and (subitem / "SKILL.md").exists():
                                    skills_count += 1
                                    has_skills = True

                        actual_plugins[item.name] = {
                            "config": plugin_config,
                            "skills_count": skills_count,
                            "has_skills": has_skills
                        }

                # 对比 marketplace.json 和实际目录
                for market_name, market_plugin in marketplace_plugins.items():
                    source = market_plugin.get("source", "")
                    actual_dir = self.extract_directory_from_source(source)

                    plugin_info = PluginInfo(
                        market_name=market_name,
                        directory_name=actual_dir,
                        expected_name=self.normalize_to_kebab_case(market_name),
                        plugin_config=market_plugin,
                        skills_count=actual_plugins.get(actual_dir, {}).get("skills_count", 0),
                        has_skills=actual_plugins.get(actual_dir, {}).get("has_skills", False)
                    )
                    self.plugins.append(plugin_info)

                # 检查未在 marketplace.json 中注册的插件目录
                registered_dirs = {self.extract_directory_from_source(p.get("source", ""))
                                 for p in marketplace_plugins.values()}
                unregistered = set(actual_plugins.keys()) - registered_dirs
                for dir_name in unregistered:
                    plugin_info = PluginInfo(
                        market_name="",
                        directory_name=dir_name,
                        expected_name=dir_name,
                        plugin_config={},
                        skills_count=actual_plugins[dir_name]["skills_count"],
                        has_skills=actual_plugins[dir_name]["has_skills"]
                    )
                    self.plugins.append(plugin_info)

        except Exception as e:
            self.issues.append({
                "type": "error",
                "category": "system",
                "message": f"分析插件信息失败: {str(e)}",
                "fixable": False
            })

    def detect_compatibility_issues(self):
        """检测兼容性问题"""
        for plugin in self.plugins:
            # 1. 检查命名一致性
            if plugin.market_name:
                if not self.names_compatible(plugin.market_name, plugin.directory_name):
                    self.issues.append({
                        "type": "error",
                        "category": "naming",
                        "message": f"插件名称不匹配: marketplace='{plugin.market_name}' vs 目录='{plugin.directory_name}'",
                        "plugin": plugin,
                        "fixable": True,
                        "suggested_fix": f"统一使用 '{plugin.expected_name}'"
                    })

                # 2. 检查命名规范
                if not self.is_kebab_case(plugin.market_name):
                    self.issues.append({
                        "type": "warning",
                        "category": "naming",
                        "message": f"插件名称不符合 kebab-case 规范: '{plugin.market_name}'",
                        "plugin": plugin,
                        "fixable": True,
                        "suggested_fix": f"建议改为 '{plugin.expected_name}'"
                    })

            # 3. 检查未注册的插件
            if not plugin.market_name and plugin.has_skills:
                self.issues.append({
                    "type": "warning",
                    "category": "registration",
                    "message": f"插件未在 marketplace.json 中注册: '{plugin.directory_name}'",
                    "plugin": plugin,
                    "fixable": True,
                    "suggested_fix": f"添加到 marketplace.json"
                })

            # 4. 检查缺失的技能
            if plugin.market_name and not plugin.has_skills:
                self.issues.append({
                    "type": "info",
                    "category": "skills",
                    "message": f"插件缺少技能定义: '{plugin.market_name}'",
                    "plugin": plugin,
                    "fixable": False
                })

    def extract_directory_from_source(self, source: str) -> str:
        """从 source 字段提取目录名"""
        if not source:
            return ""

        # 移除 "./" 或 "../" 前缀
        clean_source = source.lstrip("./")
        clean_source = source.lstrip("../")

        # 取最后一部分作为目录名
        return clean_source.split("/")[-1]

    def normalize_to_kebab_case(self, name: str) -> str:
        """将名称标准化为 kebab-case"""
        # 转换为小写
        result = name.lower()

        # 替换分隔符为连字符
        result = result.replace('_', '-')
        result = re.sub(r'([a-z])([A-Z])', r'\1-\2', result)

        # 移除多余的连字符
        result = re.sub(r'-+', '-', result)
        result = result.strip('-')

        return result

    def names_compatible(self, name1: str, name2: str) -> bool:
        """检查两个名称是否兼容（忽略大小写、连字符、下划线）"""
        norm1 = self.normalize_name_for_comparison(name1)
        norm2 = self.normalize_name_for_comparison(name2)
        return norm1 == norm2

    def normalize_name_for_comparison(self, name: str) -> str:
        """标准化名称用于比较"""
        # 转小写，移除连字符和下划线
        result = name.lower()
        result = result.replace('-', '')
        result = result.replace('_', '')
        return result

    def is_kebab_case(self, name: str) -> bool:
        """检查是否为 kebab-case"""
        if not name:
            return False
        # 只允许小写字母、数字和连字符
        return bool(re.match(r'^[a-z0-9-]+$', name))

    def generate_analysis_report(self) -> Dict:
        """生成分析报告"""
        total_plugins = len(self.plugins)
        issues_by_type = {}
        critical_issues = []

        for issue in self.issues:
            issue_type = issue["type"]
            if issue_type not in issues_by_type:
                issues_by_type[issue_type] = []
            issues_by_type[issue_type].append(issue)

            if issue_type == "critical":
                critical_issues.append(issue)

        return {
            "total_plugins": total_plugins,
            "total_issues": len(self.issues),
            "issues_by_type": issues_by_type,
            "critical_issues": critical_issues,
            "plugins": self.plugins,
            "system_health": "healthy" if len(critical_issues) == 0 else "needs_attention"
        }

    def format_analysis_report(self, analysis: Dict) -> str:
        """格式化分析报告"""
        lines = []
        lines.append("🔍 系统兼容性分析报告")
        lines.append(f"📊 总插件数: {analysis['total_plugins']}")
        lines.append(f"⚠️ 发现问题: {analysis['total_issues']} 个")
        lines.append(f"🏥 系统状态: {self.get_health_status_display(analysis['system_health'])}")
        lines.append("")

        # 按类型显示问题
        for issue_type, issues in analysis["issues_by_type"].items():
            type_display = self.get_issue_type_display(issue_type)
            icon = self.get_issue_type_icon(issue_type)
            lines.append(f"{icon} {type_display} ({len(issues)} 个):")

            for issue in issues:
                message = issue["message"]
                plugin = issue.get("plugin")
                fixable = issue.get("fixable", False)

                if plugin:
                    lines.append(f"   - {plugin.market_name or plugin.directory_name}")
                    lines.append(f"     {message}")
                else:
                    lines.append(f"   - {message}")

                if fixable:
                    suggested_fix = issue.get("suggested_fix", "")
                    if suggested_fix:
                        lines.append(f"     💡 建议: {suggested_fix}")

                lines.append("")

        # 显示插件详情
        if analysis["plugins"]:
            lines.append("📦 插件详情:")
            for plugin in analysis["plugins"]:
                status = "✅" if plugin.has_skills else "⚠️"
                market_name = plugin.market_name or "未注册"
                directory_name = plugin.directory_name
                skills_count = plugin.skills_count

                lines.append(f"   {status} {market_name} → {directory_name} ({skills_count} 技能)")

        return "\n".join(lines)

    @staticmethod
    def get_health_status_display(status: str) -> str:
        """获取健康状态显示"""
        status_map = {
            "healthy": "🟢 健康",
            "needs_attention": "🟡 需要关注",
            "critical": "🔴 严重问题"
        }
        return status_map.get(status, status)

    @staticmethod
    def get_issue_type_display(issue_type: str) -> str:
        """获取问题类型显示"""
        type_map = {
            "critical": "严重错误",
            "error": "错误",
            "warning": "警告",
            "info": "信息"
        }
        return type_map.get(issue_type, issue_type)

    @staticmethod
    def get_issue_type_icon(issue_type: str) -> str:
        """获取问题类型图标"""
        icon_map = {
            "critical": "🔴",
            "error": "❌",
            "warning": "⚠️",
            "info": "ℹ️"
        }
        return icon_map.get(issue_type, "❓")

def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="检查系统兼容性")
    parser.add_argument("--marketplace", default=".claude-plugin/marketplace.json", help="Marketplace 文件路径")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="输出格式")

    args = parser.parse_args()

    try:
        checker = SystemCompatibilityChecker(args.marketplace)
        analysis = checker.analyze_system()

        if args.format == "json":
            # 转换 dataclass 为字典用于 JSON 序列化
            json_analysis = {
                "total_plugins": analysis["total_plugins"],
                "total_issues": analysis["total_issues"],
                "critical_issues": analysis["critical_issues"],
                "system_health": analysis["system_health"],
                "issues_by_type": {
                    k: [{"type": i["type"], "category": i["category"], "message": i["message"]}
                     for i in v]
                    for k, v in analysis["issues_by_type"].items()
                },
                "plugins": [
                    {
                        "market_name": p.market_name,
                        "directory_name": p.directory_name,
                        "expected_name": p.expected_name,
                        "skills_count": p.skills_count,
                        "has_skills": p.has_skills
                    } for p in analysis["plugins"]
                ]
            }
            print(json.dumps(json_analysis, indent=2, ensure_ascii=False))
        else:
            print(checker.format_analysis_report(analysis))

    except Exception as e:
        print(f"❌ 错误: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()