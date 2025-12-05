#!/usr/bin/env python3
"""
Marketplace 配置解析工具

用于解析和分析 marketplace.json 配置文件
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any
from urllib.parse import urlparse

class MarketplaceParser:
    """Marketplace 解析器"""

    def __init__(self, marketplace_path: str = ".claude-plugin/marketplace.json"):
        self.marketplace_path = Path(marketplace_path)
        self.data = None
        self.plugins = []

    def load_marketplace(self) -> Dict:
        """加载 marketplace 配置"""
        try:
            if not self.marketplace_path.exists():
                raise FileNotFoundError(f"Marketplace 文件不存在: {self.marketplace_path}")

            with open(self.marketplace_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)

            # 验证基本结构
            self.validate_structure()

            # 提取插件列表
            if "plugins" in self.data:
                self.plugins = self.data["plugins"]

            return self.data

        except json.JSONDecodeError as e:
            raise ValueError(f"JSON 语法错误: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"加载 marketplace 失败: {str(e)}")

    def validate_structure(self) -> bool:
        """验证 marketplace 结构"""
        if not isinstance(self.data, dict):
            raise ValueError("Marketplace 必须是对象格式")

        # 检查必需字段
        required_fields = ["name", "plugins"]
        for field in required_fields:
            if field not in self.data:
                raise ValueError(f"缺少必需字段: {field}")

        # 验证 name 字段
        if not isinstance(self.data["name"], str) or not self.data["name"].strip():
            raise ValueError("name 字段必须是非空字符串")

        # 验证 plugins 字段
        if not isinstance(self.data["plugins"], list):
            raise ValueError("plugins 字段必须是数组")

        # 验证每个插件
        for i, plugin in enumerate(self.data["plugins"]):
            self.validate_plugin(plugin, f"plugins[{i}]")

        return True

    def validate_plugin(self, plugin: Dict, path: str) -> bool:
        """验证单个插件配置"""
        if not isinstance(plugin, dict):
            raise ValueError(f"{path}: 插件必须是对象格式")

        # 检查必需字段
        required_fields = ["name", "description", "source"]
        for field in required_fields:
            if field not in plugin:
                raise ValueError(f"{path}: 缺少必需字段 {field}")

        # 验证 name 字段
        if not isinstance(plugin["name"], str) or not plugin["name"].strip():
            raise ValueError(f"{path}: name 字段必须是非空字符串")

        # 验证 description 字段
        if not isinstance(plugin["description"], str) or not plugin["description"].strip():
            raise ValueError(f"{path}: description 字段必须是非空字符串")

        # 验证 source 字段
        if not isinstance(plugin["source"], str) or not plugin["source"].strip():
            raise ValueError(f"{path}: source 字段必须是非空字符串")

        # 验证 category 字段（如果存在）
        if "category" in plugin:
            if not isinstance(plugin["category"], str):
                raise ValueError(f"{path}: category 字段必须是字符串")

        # 验证 source 路径格式
        source = plugin["source"]
        if not source.startswith("./") and not source.startswith("../"):
            raise ValueError(f"{path}: source 应该是相对路径，以 './' 或 '../' 开头")

        return True

    def get_plugins_by_category(self, category: str) -> List[Dict]:
        """按类别获取插件"""
        return [plugin for plugin in self.plugins if plugin.get("category") == category]

    def get_plugin_by_name(self, name: str) -> Optional[Dict]:
        """按名称获取插件"""
        for plugin in self.plugins:
            if plugin.get("name") == name:
                return plugin
        return None

    def search_plugins(self, query: str, fields: List[str] = None) -> List[Dict]:
        """搜索插件"""
        if fields is None:
            fields = ["name", "description", "category"]

        query_lower = query.lower()
        results = []

        for plugin in self.plugins:
            for field in fields:
                if field in plugin and isinstance(plugin[field], str):
                    if query_lower in plugin[field].lower():
                        results.append(plugin)
                        break

        return results

    def validate_plugin_paths(self) -> Dict[str, List[str]]:
        """验证插件路径"""
        results = {
            "valid": [],
            "invalid": [],
            "missing": []
        }

        base_path = self.marketplace_path.parent.parent

        for plugin in self.plugins:
            source = plugin.get("source", "")
            if source.startswith("./"):
                plugin_path = base_path / source
            else:
                plugin_path = base_path / source

            if not plugin_path.exists():
                results["missing"].append({
                    "name": plugin.get("name", "Unknown"),
                    "path": str(plugin_path),
                    "source": source
                })
            elif not plugin_path.is_dir():
                results["invalid"].append({
                    "name": plugin.get("name", "Unknown"),
                    "path": str(plugin_path),
                    "source": source
                })
            else:
                results["valid"].append({
                    "name": plugin.get("name", "Unknown"),
                    "path": str(plugin_path),
                    "source": source
                })

        return results

    def get_skill_status(self) -> Dict[str, Any]:
        """获取技能状态信息"""
        if not self.data:
            self.load_marketplace()

        path_validation = self.validate_plugin_paths()

        skill_status = {
            "total_plugins": len(self.plugins),
            "valid_paths": len(path_validation["valid"]),
            "invalid_paths": len(path_validation["invalid"]),
            "missing_paths": len(path_validation["missing"]),
            "categories": self.get_categories(),
            "plugins_with_skills": 0
        }

        # 检查每个插件是否有技能
        base_path = self.marketplace_path.parent.parent
        for plugin in self.plugins:
            source = plugin.get("source", "")
            if source.startswith("./"):
                plugin_path = base_path / source
            else:
                plugin_path = base_path / source

            if plugin_path.exists():
                skills_dir = plugin_path / "skills"
                if skills_dir.exists():
                    # 检查是否有技能子目录
                    has_skills = any(
                        (skills_dir / item).is_dir() and
                        (skills_dir / item / "SKILL.md").exists()
                        for item in skills_dir.iterdir()
                    )
                    if has_skills:
                        skill_status["plugins_with_skills"] += 1

        return skill_status

    def get_categories(self) -> List[str]:
        """获取所有类别"""
        categories = set()
        for plugin in self.plugins:
            category = plugin.get("category")
            if category:
                categories.add(category)
        return sorted(list(categories))

    def generate_skills_list(self, validate: bool = False) -> List[Dict]:
        """生成技能列表"""
        if not self.data:
            self.load_marketplace()

        skills = []
        base_path = self.marketplace_path.parent.parent

        for plugin in self.plugins:
            source = plugin.get("source", "")
            if source.startswith("./"):
                plugin_path = base_path / source
            else:
                plugin_path = base_path / source

            if not plugin_path.exists():
                continue

            skills_dir = plugin_path / "skills"
            if not skills_dir.exists():
                continue

            # 检查 skills 目录本身是否包含 SKILL.md
            skill_md = skills_dir / "SKILL.md"
            if skill_md.exists():
                skill_info = {
                    "name": f"{plugin.get('name', 'unknown')}:skills",
                    "plugin_name": plugin.get("name", "unknown"),
                    "skill_name": "skills",
                    "category": plugin.get("category", "unknown"),
                    "description": plugin.get("description", ""),
                    "path": str(skills_dir),
                    "status": "unknown"
                }

                # 如果需要验证技能状态
                if validate:
                    # 这里可以集成技能验证逻辑
                    try:
                        # 简单的文件存在性检查
                        if skill_md.exists():
                            skill_info["status"] = "valid"
                        else:
                            skill_info["status"] = "missing"
                    except Exception:
                        skill_info["status"] = "error"
                else:
                    skill_info["status"] = "valid" if skill_md.exists() else "missing"

                skills.append(skill_info)

            # 扫描子目录中的技能
            for item in skills_dir.iterdir():
                if item.is_dir():
                    skill_md = item / "SKILL.md"
                    if skill_md.exists():
                        skill_info = {
                            "name": f"{plugin.get('name', 'unknown')}:{item.name}",
                            "plugin_name": plugin.get("name", "unknown"),
                            "skill_name": item.name,
                            "category": plugin.get("category", "unknown"),
                            "description": plugin.get("description", ""),
                            "path": str(item),
                            "status": "unknown"
                        }

                        # 如果需要验证技能状态
                        if validate:
                            # 这里可以集成技能验证逻辑
                            try:
                                # 简单的文件存在性检查
                                if skill_md.exists():
                                    skill_info["status"] = "valid"
                                else:
                                    skill_info["status"] = "missing"
                            except Exception:
                                skill_info["status"] = "error"
                        else:
                            skill_info["status"] = "valid" if skill_md.exists() else "missing"

                        skills.append(skill_info)

        return skills

    def export_format(self, format_type: str = "table") -> str:
        """导出为指定格式"""
        skills = self.generate_skills_list()

        if format_type == "table":
            return self.format_table(skills)
        elif format_type == "json":
            return json.dumps({
                "marketplace": {
                    "name": self.data.get("name", ""),
                    "version": self.data.get("metadata", {}).get("version", "1.0.0"),
                    "total_skills": len(skills)
                },
                "skills": skills
            }, indent=2, ensure_ascii=False)
        elif format_type == "csv":
            return self.format_csv(skills)
        else:
            raise ValueError(f"不支持的格式: {format_type}")

    def format_table(self, skills: List[Dict]) -> str:
        """格式化为表格"""
        if not skills:
            return "未找到技能"

        # 计算列宽
        name_width = max(25, max(len(skill["name"]) for skill in skills))
        category_width = max(10, max(len(skill["category"]) for skill in skills))
        description_width = max(30, min(50, max(len(skill["description"]) for skill in skills)))
        status_width = 8

        # 构建表格
        lines = []

        # 标题行
        header = f"┌─{'─' * name_width}─┬─{'─' * category_width}─┬─{'─' * description_width}─┬─{'─' * status_width}─┐"
        lines.append(header)

        title_row = f"│ {'技能名称':<{name_width}} │ {'类别':<{category_width}} │ {'描述':<{description_width}} │ {'状态':<{status_width}} │"
        lines.append(title_row)

        separator = f"├─{'─' * name_width}─┼─{'─' * category_width}─┼─{'─' * description_width}─┼─{'─' * status_width}─┤"
        lines.append(separator)

        # 数据行
        for skill in skills:
            name = skill["name"][:name_width-3] + "..." if len(skill["name"]) > name_width else skill["name"]
            category = skill["category"][:category_width-3] + "..." if len(skill["category"]) > category_width else skill["category"]
            description = skill["description"][:description_width-3] + "..." if len(skill["description"]) > description_width else skill["description"]
            status = "✅ 有效" if skill["status"] == "valid" else "❌ 缺失"

            data_row = f"│ {name:<{name_width}} │ {category:<{category_width}} │ {description:<{description_width}} │ {status:<{status_width}} │"
            lines.append(data_row)

        # 底部行
        footer = f"└─{'─' * name_width}─┴─{'─' * category_width}─┴─{'─' * description_width}─┴─{'─' * status_width}─┘"
        lines.append(footer)

        return "\n".join(lines)

    def format_csv(self, skills: List[Dict]) -> str:
        """格式化为 CSV"""
        lines = ["name,category,description,status,path"]

        for skill in skills:
            name = f'"{skill["name"]}"'
            category = f'"{skill["category"]}"'
            description = f'"{skill["description"].replace(chr(34), chr(34)+chr(34))}"'
            status = skill["status"]
            path = f'"{skill["path"]}"'

            lines.append(f"{name},{category},{description},{status},{path}")

        return "\n".join(lines)

def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="解析 marketplace 配置")
    parser.add_argument("--marketplace", default=".claude-plugin/marketplace.json", help="Marketplace 文件路径")
    parser.add_argument("--format", choices=["table", "json", "csv"], default="table", help="输出格式")
    parser.add_argument("--category", help="按类别过滤")
    parser.add_argument("--search", help="搜索关键词")
    parser.add_argument("--validate", action="store_true", help="验证技能状态")
    parser.add_argument("--validate-paths", action="store_true", help="验证插件路径")
    parser.add_argument("--stats", action="store_true", help="显示统计信息")

    args = parser.parse_args()

    try:
        parser = MarketplaceParser(args.marketplace)
        parser.load_marketplace()

        if args.stats:
            status = parser.get_skill_status()
            print("📊 技能统计信息:")
            print(f"   - 总插件数: {status['total_plugins']}")
            print(f"   - 有效路径: {status['valid_paths']}")
            print(f"   - 无效路径: {status['invalid_paths']}")
            print(f"   - 缺失路径: {status['missing_paths']}")
            print(f"   - 有技能插件: {status['plugins_with_skills']}")
            print(f"   - 类别: {', '.join(status['categories'])}")
            return

        if args.validate_paths:
            path_validation = parser.validate_plugin_paths()
            print("🔍 路径验证结果:")
            print(f"   - 有效路径: {len(path_validation['valid'])}")
            print(f"   - 无效路径: {len(path_validation['invalid'])}")
            print(f"   - 缺失路径: {len(path_validation['missing'])}")

            if path_validation["invalid"]:
                print("\n❌ 无效路径:")
                for item in path_validation["invalid"]:
                    print(f"   - {item['name']}: {item['path']}")

            if path_validation["missing"]:
                print("\n⚠️ 缺失路径:")
                for item in path_validation["missing"]:
                    print(f"   - {item['name']}: {item['path']}")
            return

        skills = parser.generate_skills_list(args.validate)

        if args.category:
            skills = [skill for skill in skills if skill["category"] == args.category]

        if args.search:
            skills = parser.search_plugins(args.search)
            skills = [
                {
                    "name": plugin.get("name", "") + ":skills",
                    "plugin_name": plugin.get("name", ""),
                    "skill_name": "",
                    "category": plugin.get("category", ""),
                    "description": plugin.get("description", ""),
                    "path": plugin.get("source", ""),
                    "status": "unknown"
                }
                for plugin in skills
            ]

        if args.format == "table":
            # 临时创建实例来格式化表格
            temp_parser = MarketplaceParser(args.marketplace)
            temp_parser.data = parser.data
            temp_parser.plugins = parser.plugins
            print(temp_parser.format_table(skills))
        else:
            print(json.dumps(skills, indent=2, ensure_ascii=False))

    except Exception as e:
        print(f"❌ 错误: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()