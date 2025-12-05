#!/usr/bin/env python3
"""
技能验证工具

用于验证 Claude Code 技能的结构和内容质量
"""

import json
import os
import re
import sys
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class SkillValidator:
    """技能验证器"""

    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.results = []
        self.total_skills = 0
        self.valid_skills = 0
        self.warning_skills = 0
        self.error_skills = 0

    def validate_frontmatter(self, content: str) -> Dict:
        """验证 YAML frontmatter"""
        result = {"valid": True, "errors": [], "warnings": [], "score": 0}

        # 检查 frontmatter 存在
        if not content.startswith('---'):
            result["valid"] = False
            result["errors"].append("缺少 YAML frontmatter")
            return result

        # 提取 frontmatter
        try:
            end_index = content.find('---', 3)
            if end_index == -1:
                result["valid"] = False
                result["errors"].append("YAML frontmatter 结束标记缺失")
                return result

            frontmatter_text = content[3:end_index].strip()
            frontmatter_data = yaml.safe_load(frontmatter_text)

            if not isinstance(frontmatter_data, dict):
                result["valid"] = False
                result["errors"].append("Frontmatter 不是有效的字典格式")
                return result

            # 检查必需字段
            required_fields = ["name", "description"]
            for field in required_fields:
                if field not in frontmatter_data:
                    result["valid"] = False
                    result["errors"].append(f"缺少必需字段: {field}")
                elif not frontmatter_data[field]:
                    result["valid"] = False
                    result["errors"].append(f"字段 {field} 不能为空")

            # 检查 name 字段格式
            if "name" in frontmatter_data:
                name = frontmatter_data["name"]
                if not isinstance(name, str) or len(name.strip()) == 0:
                    result["valid"] = False
                    result["errors"].append("name 字段必须是非空字符串")

            # 检查 description 字段质量
            if "description" in frontmatter_data:
                desc = frontmatter_data["description"]
                if not isinstance(desc, str):
                    result["valid"] = False
                    result["errors"].append("description 字段必须是字符串")
                else:
                    # 检查是否使用第三人称
                    if not desc.startswith("This skill should be used when") and \
                       not any(phrase in desc for phrase in ["当用户", "当使用者", "用于", "适用"]):
                        result["warnings"].append("description 应该使用第三人称或包含具体触发条件")

                    # 检查是否包含具体触发短语
                    if len(desc.strip()) < 20:
                        result["warnings"].append("description 过于简单，建议添加更多细节和触发条件")

            result["score"] = min(20, 20 - len(result["errors"]) * 5 - len(result["warnings"]) * 2)

        except yaml.YAMLError as e:
            result["valid"] = False
            result["errors"].append(f"YAML 语法错误: {str(e)}")
        except Exception as e:
            result["valid"] = False
            result["errors"].append(f"解析 frontmatter 时出错: {str(e)}")

        return result

    def validate_content_quality(self, content: str, frontmatter_end: int) -> Dict:
        """验证内容质量"""
        result = {"valid": True, "errors": [], "warnings": [], "score": 0}

        # 提取正文内容
        body_content = content[frontmatter_end:].strip()

        if not body_content:
            result["valid"] = False
            result["errors"].append("技能内容为空")
            return result

        # 检查内容长度
        word_count = len(body_content.split())
        if word_count < 100:
            result["valid"] = False
            result["errors"].append("内容过短，建议至少 100 词")
        elif word_count > 5000:
            result["warnings"].append("内容过长，建议控制在 5000 词以内，详细内容可移至 references/")
        elif 1500 <= word_count <= 2000:
            result["score"] += 5  # 理想长度

        # 检查标题结构
        if not re.search(r'^#+ ', body_content, re.MULTILINE):
            result["warnings"].append("建议使用标题组织内容结构")

        # 检查是否使用祈使/不定式形式
        first_person_patterns = [r'\b我\b', r'\b我们\b', r'\byou\b', r'\byour\b']
        for pattern in first_person_patterns:
            if re.search(pattern, body_content, re.IGNORECASE):
                result["warnings"].append("建议使用祈使/不定式形式，避免第一人称")
                break

        # 检查是否引用了其他文件
        if not re.search(r'references/|examples/|scripts/', body_content):
            result["warnings"].append("建议引用 supporting 文件（references/, examples/, scripts/）")

        result["score"] = min(25, result["score"] + max(0, 20 - len(result["warnings"]) * 3))

        return result

    def validate_file_structure(self, skill_path: Path) -> Dict:
        """验证文件结构"""
        result = {"valid": True, "errors": [], "warnings": [], "score": 0}

        # 检查技能目录命名
        if not re.match(r'^[a-z0-9-]+$', skill_path.name):
            result["valid"] = False
            result["errors"].append("技能目录名称应符合 kebab-case 格式（小写字母、数字、连字符）")

        # 检查必需文件
        skill_md = skill_path / "SKILL.md"
        if not skill_md.exists():
            result["valid"] = False
            result["errors"].append("缺少必需的 SKILL.md 文件")
            return result

        # 检查子目录
        subdirs = ["scripts", "references", "examples"]
        existing_dirs = [d for d in subdirs if (skill_path / d).exists()]

        if not existing_dirs:
            result["warnings"].append("建议创建 scripts/、references/ 或 examples/ 目录来组织资源")
        else:
            result["score"] = min(10, len(existing_dirs) * 3)

        # 检查文件权限
        try:
            with open(skill_md, 'r', encoding='utf-8') as f:
                f.read()
        except PermissionError:
            result["valid"] = False
            result["errors"].append("SKILL.md 文件无法读取（权限问题）")
        except UnicodeDecodeError:
            result["valid"] = False
            result["errors"].append("SKILL.md 文件编码错误，应使用 UTF-8")

        result["score"] += 10  # 基础结构分数

        return result

    def validate_best_practices(self, skill_path: Path, content: str) -> Dict:
        """验证最佳实践"""
        result = {"valid": True, "errors": [], "warnings": [], "score": 0}

        # 检查是否使用了绝对路径
        absolute_path_patterns = [
            r'/Users/[^/\s]+/',
            r'/home/[^/\s]+/',
            r'C:\\',
            r'/opt/',
        ]

        for pattern in absolute_path_patterns:
            if re.search(pattern, content):
                result["warnings"].append("发现绝对路径，建议使用 CLAUDE_PLUGIN_ROOT 环境变量")
                result["score"] -= 5

        # 检查是否包含敏感信息
        sensitive_patterns = [
            r'password\s*[:=]\s*["\']?[^"\'\s]+',
            r'api[_-]?key\s*[:=]\s*["\']?[^"\'\s]+',
            r'token\s*[:=]\s*["\']?[^"\'\s]+',
        ]

        for pattern in sensitive_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                result["valid"] = False
                result["errors"].append("发现可能的敏感信息，请移除硬编码的密码、API密钥等")

        # 检查引用文件是否存在
        references = re.findall(r'references/([^/\s\]]+)', content)
        examples = re.findall(r'examples/([^/\s\]]+)', content)
        scripts = re.findall(r'scripts/([^/\s\]]+)', content)

        for ref in references:
            if not (skill_path / "references" / ref).exists():
                result["warnings"].append(f"引用的 references/{ref} 文件不存在")

        for example in examples:
            if not (skill_path / "examples" / example).exists():
                result["warnings"].append(f"引用的 examples/{example} 文件不存在")

        for script in scripts:
            if not (skill_path / "scripts" / script).exists():
                result["warnings"].append(f"引用的 scripts/{script} 文件不存在")

        result["score"] = max(0, 20 - len(result["warnings"]) * 2 - len(result["errors"]) * 5)

        return result

    def validate_skill(self, skill_path: Path) -> Dict:
        """验证单个技能"""
        skill_result = {
            "name": skill_path.name,
            "path": str(skill_path),
            "valid": True,
            "errors": [],
            "warnings": [],
            "score": 0,
            "details": {}
        }

        # 验证文件结构
        structure_result = self.validate_file_structure(skill_path)
        skill_result["details"]["structure"] = structure_result
        skill_result["errors"].extend(structure_result["errors"])
        skill_result["warnings"].extend(structure_result["warnings"])

        if not structure_result["valid"]:
            skill_result["valid"] = False

        # 读取技能文件内容
        skill_md = skill_path / "SKILL.md"
        if skill_md.exists():
            try:
                with open(skill_md, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 查找 frontmatter 结束位置
                frontmatter_end = content.find('---', 3)
                if frontmatter_end == -1:
                    frontmatter_end = 0
                else:
                    frontmatter_end += 3

                # 验证 frontmatter
                frontmatter_result = self.validate_frontmatter(content)
                skill_result["details"]["frontmatter"] = frontmatter_result
                skill_result["errors"].extend(frontmatter_result["errors"])
                skill_result["warnings"].extend(frontmatter_result["warnings"])

                if not frontmatter_result["valid"]:
                    skill_result["valid"] = False

                # 验证内容质量
                content_result = self.validate_content_quality(content, frontmatter_end)
                skill_result["details"]["content"] = content_result
                skill_result["errors"].extend(content_result["errors"])
                skill_result["warnings"].extend(content_result["warnings"])

                if not content_result["valid"]:
                    skill_result["valid"] = False

                # 验证最佳实践
                practices_result = self.validate_best_practices(skill_path, content)
                skill_result["details"]["practices"] = practices_result
                skill_result["errors"].extend(practices_result["errors"])
                skill_result["warnings"].extend(practices_result["warnings"])

                # 计算总分
                skill_result["score"] = (
                    structure_result["score"] +
                    frontmatter_result["score"] +
                    content_result["score"] +
                    practices_result["score"]
                )

                if not practices_result["valid"]:
                    skill_result["valid"] = False

            except Exception as e:
                skill_result["valid"] = False
                skill_result["errors"].append(f"读取技能文件时出错: {str(e)}")

        return skill_result

    def scan_skills(self) -> List[Path]:
        """扫描技能目录"""
        skills = []

        # 扫描当前目录下的 skills/
        skills_dir = self.base_path / "skills"
        if skills_dir.exists():
            # 检查 skills 目录本身是否包含 SKILL.md
            if (skills_dir / "SKILL.md").exists():
                skills.append(skills_dir)
            # 检查子目录中的技能
            for item in skills_dir.iterdir():
                if item.is_dir() and (item / "SKILL.md").exists():
                    skills.append(item)

        # 扫描 plugins/ 下的技能
        plugins_dir = self.base_path / "plugins"
        if plugins_dir.exists():
            for plugin_dir in plugins_dir.iterdir():
                if plugin_dir.is_dir():
                    plugin_skills_dir = plugin_dir / "skills"
                    if plugin_skills_dir.exists():
                        # 检查 skills 目录本身是否包含 SKILL.md
                        if (plugin_skills_dir / "SKILL.md").exists():
                            skills.append(plugin_skills_dir)
                        # 检查子目录中的技能
                        for skill_dir in plugin_skills_dir.iterdir():
                            if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                                skills.append(skill_dir)

        return skills

    def validate_all(self) -> Dict:
        """验证所有技能"""
        skills = self.scan_skills()
        self.total_skills = len(skills)

        results = []
        for skill_path in skills:
            result = self.validate_skill(skill_path)
            results.append(result)

            if result["valid"] and not result["warnings"]:
                self.valid_skills += 1
            elif result["valid"] and result["warnings"]:
                self.warning_skills += 1
            else:
                self.error_skills += 1

        self.results = results
        return self.generate_report()

    def generate_report(self) -> Dict:
        """生成验证报告"""
        return {
            "summary": {
                "total_skills": self.total_skills,
                "valid_skills": self.valid_skills,
                "warning_skills": self.warning_skills,
                "error_skills": self.error_skills,
                "health_status": self.get_health_status()
            },
            "skills": self.results
        }

    def get_health_status(self) -> str:
        """获取整体健康状态"""
        if self.total_skills == 0:
            return "无技能"

        valid_ratio = self.valid_skills / self.total_skills

        if valid_ratio >= 0.9:
            return "优秀"
        elif valid_ratio >= 0.7:
            return "良好"
        elif valid_ratio >= 0.5:
            return "一般"
        else:
            return "需要改进"

    def print_report(self, report: Dict):
        """打印验证报告"""
        print("🔍 技能验证报告")
        print("=" * 50)

        # 确保包含所有必需的字段
        summary = report.get("summary", {})
        if "total_skills" not in summary:
            summary["total_skills"] = 0
        if "valid_skills" not in summary:
            summary["valid_skills"] = 0
        if "warning_skills" not in summary:
            summary["warning_skills"] = 0
        if "error_skills" not in summary:
            summary["error_skills"] = 0
        if "health_status" not in summary:
            summary["health_status"] = "未知"

        print(f"📊 扫描统计:")
        print(f"   - 总技能数: {summary['total_skills']} 个")
        print(f"   - 完全有效: {summary['valid_skills']} 个")
        print(f"   - 存在警告: {summary['warning_skills']} 个")
        print(f"   - 需要修复: {summary['error_skills']} 个")
        print(f"   - 健康状态: {summary['health_status']}")
        print()

        for skill in report["skills"]:
            status_icon = "✅" if skill["valid"] and not skill["warnings"] else \
                         "⚠️" if skill["valid"] and skill["warnings"] else "❌"

            print(f"{status_icon} {skill['name']} ({skill['score']}/100)")

            if skill["errors"]:
                for error in skill["errors"]:
                    print(f"   ❌ {error}")

            if skill["warnings"]:
                for warning in skill["warnings"]:
                    print(f"   ⚠️ {warning}")

            print()

def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="验证 Claude Code 技能")
    parser.add_argument("--path", default=".", help="技能根目录路径")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="输出格式")
    parser.add_argument("--skill", help="验证特定技能")

    args = parser.parse_args()

    validator = SkillValidator(args.path)

    if args.skill:
        # 验证特定技能
        skill_path = Path(args.path) / args.skill
        if not skill_path.exists():
            print(f"❌ 技能目录不存在: {skill_path}")
            sys.exit(1)

        result = validator.validate_skill(skill_path)
        report = {"summary": {"total_skills": 1}, "skills": [result]}
    else:
        # 验证所有技能
        report = validator.validate_all()

    if args.format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        validator.print_report(report)

if __name__ == "__main__":
    main()