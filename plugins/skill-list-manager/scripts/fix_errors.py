#!/usr/bin/env python3
"""
技能错误修复工具

自动检测和修复技能生态系统中的常见错误
"""

import json
import os
import sys
import shutil
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
import logging

class SkillFixer:
    """技能错误修复器"""

    def __init__(self, marketplace_path: str = ".claude-plugin/marketplace.json"):
        self.marketplace_path = Path(marketplace_path)
        self.base_path = self.marketplace_path.parent.parent
        self.backup_dir = self.base_path / ".claude-plugin" / "backups"
        self.errors = []
        self.fixes = []
        self.dry_run = False

        # 设置日志
        logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
        self.logger = logging.getLogger(__name__)

    def detect_all_errors(self) -> List[Dict]:
        """检测所有错误"""
        errors = []

        # 检测 marketplace.json 本身的错误
        errors.extend(self.detect_marketplace_errors())

        # 检测插件相关错误
        if self.marketplace_path.exists():
            try:
                with open(self.marketplace_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                for plugin in data.get("plugins", []):
                    plugin_errors = self.detect_plugin_errors(plugin)
                    errors.extend(plugin_errors)

            except json.JSONDecodeError as e:
                errors.append({
                    "type": "config-error",
                    "severity": "critical",
                    "target": "marketplace.json",
                    "issue": f"JSON 语法错误: {str(e)}",
                    "fixable": True,
                    "fix_method": "fix_json_syntax"
                })

        return errors

    def detect_marketplace_errors(self) -> List[Dict]:
        """检测 marketplace.json 配置错误"""
        errors = []

        if not self.marketplace_path.exists():
            errors.append({
                "type": "config-error",
                "severity": "critical",
                "target": "marketplace.json",
                "issue": "marketplace.json 文件不存在",
                "fixable": False,
                "fix_method": None
            })
            return errors

        try:
            with open(self.marketplace_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 检查必需字段
            required_fields = ["name", "plugins"]
            for field in required_fields:
                if field not in data:
                    errors.append({
                        "type": "config-error",
                        "severity": "error",
                        "target": "marketplace.json",
                        "issue": f"缺少必需字段: {field}",
                        "fixable": True,
                        "fix_method": "add_missing_field",
                        "field": field,
                        "default_value": "plugins" if field == "plugins" else "unnamed-marketplace"
                    })

            # 检查 metadata 字段
            if "metadata" not in data:
                errors.append({
                    "type": "config-error",
                    "severity": "warning",
                    "target": "marketplace.json",
                    "issue": "缺少 metadata 字段",
                    "fixable": True,
                    "fix_method": "add_metadata"
                })

        except json.JSONDecodeError as e:
            errors.append({
                "type": "config-error",
                "severity": "critical",
                "target": "marketplace.json",
                "issue": f"JSON 语法错误: {str(e)}",
                "fixable": True,
                "fix_method": "fix_json_syntax"
            })

        return errors

    def detect_plugin_errors(self, plugin: Dict) -> List[Dict]:
        """检测单个插件的错误"""
        errors = []
        plugin_name = plugin.get("name", "unknown")

        # 检查必需字段
        required_fields = ["name", "description", "source"]
        for field in required_fields:
            if field not in plugin:
                errors.append({
                    "type": "config-error",
                    "severity": "error",
                    "target": f"plugin:{plugin_name}",
                    "issue": f"插件缺少必需字段: {field}",
                    "fixable": True,
                    "fix_method": "add_plugin_field",
                    "plugin_name": plugin_name,
                    "field": field,
                    "default_value": self.get_default_field_value(field, plugin_name)
                })

        # 检查路径错误
        source = plugin.get("source", "")
        if source:
            if not source.startswith("./") and not source.startswith("../"):
                errors.append({
                    "type": "path-error",
                    "severity": "warning",
                    "target": f"plugin:{plugin_name}",
                    "issue": f"source 路径格式不正确: {source}",
                    "fixable": True,
                    "fix_method": "fix_source_path",
                    "plugin_name": plugin_name,
                    "current_path": source,
                    "suggested_path": f"./plugins/{plugin_name}"
                })
            else:
                # 检查路径是否存在
                if source.startswith("./"):
                    plugin_path = self.base_path / source
                else:
                    plugin_path = self.base_path / source

                if not plugin_path.exists():
                    # 尝试查找实际的插件目录
                    actual_path = self.find_actual_plugin_path(plugin_name)
                    if actual_path:
                        errors.append({
                            "type": "path-error",
                            "severity": "error",
                            "target": f"plugin:{plugin_name}",
                            "issue": f"插件路径不存在: {source}",
                            "fixable": True,
                            "fix_method": "update_source_path",
                            "plugin_name": plugin_name,
                            "current_path": source,
                            "actual_path": f"./{actual_path.relative_to(self.base_path)}"
                        })
                    else:
                        errors.append({
                            "type": "path-error",
                            "severity": "error",
                            "target": f"plugin:{plugin_name}",
                            "issue": f"插件路径不存在: {source}，且未找到实际目录",
                            "fixable": False,
                            "fix_method": None,
                            "plugin_name": plugin_name,
                            "current_path": source
                        })

        # 检查命名规范
        if plugin_name:
            if not self.is_kebab_case(plugin_name):
                suggested_name = self.to_kebab_case(plugin_name)
                if self.plugin_exists_with_name(suggested_name):
                    errors.append({
                        "type": "name-mismatch",
                        "severity": "error",
                        "target": f"plugin:{plugin_name}",
                        "issue": f"插件名称不符合 kebab-case 规范: {plugin_name}",
                        "fixable": True,
                        "fix_method": "fix_plugin_name",
                        "plugin_name": plugin_name,
                        "suggested_name": suggested_name
                    })

        return errors

    def find_actual_plugin_path(self, plugin_name: str) -> Optional[Path]:
        """查找插件的实际路径"""
        plugins_dir = self.base_path / "plugins"
        if not plugins_dir.exists():
            return None

        # 尝试不同的命名变体
        variants = [
            plugin_name,
            self.to_kebab_case(plugin_name),
            self.to_camel_case(plugin_name),
            self.to_snake_case(plugin_name)
        ]

        for variant in set(variants):
            path = plugins_dir / variant
            if path.exists() and path.is_dir():
                return path

        # 模糊搜索
        for item in plugins_dir.iterdir():
            if item.is_dir() and self.normalize_name(item.name) == self.normalize_name(plugin_name):
                return item

        return None

    def plugin_exists_with_name(self, name: str) -> bool:
        """检查指定名称的插件是否存在"""
        plugins_dir = self.base_path / "plugins"
        if not plugins_dir.exists():
            return False
        return (plugins_dir / name).exists() and (plugins_dir / name).is_dir()

    def fix_all_errors(self, errors: List[Dict], auto_fix: bool = False) -> List[Dict]:
        """修复所有错误"""
        fixes = []

        # 按严重程度排序，优先修复关键错误
        sorted_errors = sorted(errors, key=lambda x: self.severity_priority(x.get("severity", "info")))

        for error in sorted_errors:
            if error.get("fixable", False):
                if auto_fix:
                    fix_result = self.apply_fix(error)
                    fixes.append(fix_result)
                else:
                    fixes.append({
                        "error": error,
                        "status": "pending",
                        "message": f"需要修复: {error['issue']}"
                    })
            else:
                fixes.append({
                    "error": error,
                    "status": "manual",
                    "message": f"需要手动修复: {error['issue']}"
                })

        return fixes

    def apply_fix(self, error: Dict) -> Dict:
        """应用单个修复"""
        fix_method = error.get("fix_method")

        if self.dry_run:
            return {
                "error": error,
                "status": "dry_run",
                "message": f"[预览] 将修复: {error['issue']}"
            }

        try:
            if fix_method == "fix_json_syntax":
                return self.fix_json_syntax(error)
            elif fix_method == "add_missing_field":
                return self.add_missing_field(error)
            elif fix_method == "add_metadata":
                return self.add_metadata(error)
            elif fix_method == "add_plugin_field":
                return self.add_plugin_field(error)
            elif fix_method == "fix_source_path":
                return self.fix_source_path(error)
            elif fix_method == "update_source_path":
                return self.update_source_path(error)
            elif fix_method == "fix_plugin_name":
                return self.fix_plugin_name(error)
            else:
                return {
                    "error": error,
                    "status": "failed",
                    "message": f"未知的修复方法: {fix_method}"
                }
        except Exception as e:
            return {
                "error": error,
                "status": "failed",
                "message": f"修复失败: {str(e)}"
            }

    def fix_json_syntax(self, error: Dict) -> Dict:
        """修复 JSON 语法错误"""
        self.create_backup()

        try:
            # 重新格式化 JSON
            with open(self.marketplace_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 尝试解析并重新格式化
            data = json.loads(content)
            with open(self.marketplace_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            return {
                "error": error,
                "status": "success",
                "message": "JSON 语法已修复并重新格式化"
            }
        except Exception as e:
            return {
                "error": error,
                "status": "failed",
                "message": f"无法修复 JSON 语法: {str(e)}"
            }

    def add_missing_field(self, error: Dict) -> Dict:
        """添加缺失的字段"""
        self.create_backup()

        field = error["field"]
        default_value = error["default_value"]

        try:
            with open(self.marketplace_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            data[field] = default_value

            with open(self.marketplace_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            return {
                "error": error,
                "status": "success",
                "message": f"已添加缺失字段 {field}: {default_value}"
            }
        except Exception as e:
            return {
                "error": error,
                "status": "failed",
                "message": f"无法添加字段 {field}: {str(e)}"
            }

    def add_metadata(self, error: Dict) -> Dict:
        """添加 metadata 字段"""
        self.create_backup()

        try:
            with open(self.marketplace_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            data["metadata"] = {
                "description": "Claude Code 技能集合",
                "version": "1.0.0"
            }

            with open(self.marketplace_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            return {
                "error": error,
                "status": "success",
                "message": "已添加 metadata 字段"
            }
        except Exception as e:
            return {
                "error": error,
                "status": "failed",
                "message": f"无法添加 metadata: {str(e)}"
            }

    def add_plugin_field(self, error: Dict) -> Dict:
        """为插件添加缺失字段"""
        self.create_backup()

        plugin_name = error["plugin_name"]
        field = error["field"]
        default_value = error["default_value"]

        try:
            with open(self.marketplace_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 查找插件
            for plugin in data.get("plugins", []):
                if plugin.get("name") == plugin_name:
                    plugin[field] = default_value
                    break

            with open(self.marketplace_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            return {
                "error": error,
                "status": "success",
                "message": f"已为插件 {plugin_name} 添加字段 {field}: {default_value}"
            }
        except Exception as e:
            return {
                "error": error,
                "status": "failed",
                "message": f"无法为插件 {plugin_name} 添加字段 {field}: {str(e)}"
            }

    def fix_source_path(self, error: Dict) -> Dict:
        """修复插件源路径格式"""
        self.create_backup()

        plugin_name = error["plugin_name"]
        suggested_path = error["suggested_path"]

        try:
            with open(self.marketplace_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 更新路径
            for plugin in data.get("plugins", []):
                if plugin.get("name") == plugin_name:
                    plugin["source"] = suggested_path
                    break

            with open(self.marketplace_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            return {
                "error": error,
                "status": "success",
                "message": f"已修复插件 {plugin_name} 的路径: {suggested_path}"
            }
        except Exception as e:
            return {
                "error": error,
                "status": "failed",
                "message": f"无法修复插件 {plugin_name} 的路径: {str(e)}"
            }

    def update_source_path(self, error: Dict) -> Dict:
        """更新插件源路径为实际路径"""
        self.create_backup()

        plugin_name = error["plugin_name"]
        actual_path = error["actual_path"]

        try:
            with open(self.marketplace_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 更新路径
            for plugin in data.get("plugins", []):
                if plugin.get("name") == plugin_name:
                    plugin["source"] = actual_path
                    break

            with open(self.marketplace_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            return {
                "error": error,
                "status": "success",
                "message": f"已更新插件 {plugin_name} 的路径为: {actual_path}"
            }
        except Exception as e:
            return {
                "error": error,
                "status": "failed",
                "message": f"无法更新插件 {plugin_name} 的路径: {str(e)}"
            }

    def fix_plugin_name(self, error: Dict) -> Dict:
        """修复插件名称"""
        self.create_backup()

        plugin_name = error["plugin_name"]
        suggested_name = error["suggested_name"]

        try:
            with open(self.marketplace_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 更新插件名称
            for plugin in data.get("plugins", []):
                if plugin.get("name") == plugin_name:
                    plugin["name"] = suggested_name
                    break

            with open(self.marketplace_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            return {
                "error": error,
                "status": "success",
                "message": f"已修复插件名称: {plugin_name} → {suggested_name}"
            }
        except Exception as e:
            return {
                "error": error,
                "status": "failed",
                "message": f"无法修复插件名称: {str(e)}"
            }

    def create_backup(self):
        """创建备份"""
        if not self.backup_dir.exists():
            self.backup_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = self.backup_dir / f"marketplace_{timestamp}.json"

        if self.marketplace_path.exists():
            shutil.copy2(self.marketplace_path, backup_file)
            self.logger.info(f"已创建备份: {backup_file}")

    def format_error_report(self, errors: List[Dict]) -> str:
        """格式化错误报告"""
        if not errors:
            return "✅ 未发现错误"

        # 按类型分组
        by_type = {}
        for error in errors:
            error_type = error.get("type", "unknown")
            if error_type not in by_type:
                by_type[error_type] = []
            by_type[error_type].append(error)

        lines = [f"🔍 错误检测完成 - 发现 {len(errors)} 个问题\n"]

        # 按严重程度顺序显示
        type_order = ["config-error", "name-mismatch", "path-error"]

        for error_type in type_order:
            if error_type in by_type:
                type_errors = by_type[error_type]
                type_name = self.get_type_display_name(error_type)
                icon = self.get_type_icon(error_type)

                lines.append(f"{icon} {type_name} ({len(type_errors)}):")

                for error in type_errors:
                    severity = error.get("severity", "info")
                    target = error.get("target", "unknown")
                    issue = error.get("issue", "unknown issue")
                    fixable = error.get("fixable", False)

                    if fixable:
                        lines.append(f"   - {target}")
                        lines.append(f"     问题: {issue}")
                        lines.append(f"     状态: 可自动修复")
                    else:
                        lines.append(f"   - {target}")
                        lines.append(f"     问题: {issue}")
                        lines.append(f"     状态: 需要手动修复")

                lines.append("")

        return "\n".join(lines)

    def format_fix_report(self, fixes: List[Dict]) -> str:
        """格式化修复报告"""
        if not fixes:
            return "✅ 无需修复"

        successful = sum(1 for fix in fixes if fix.get("status") == "success")
        failed = sum(1 for fix in fixes if fix.get("status") == "failed")
        pending = sum(1 for fix in fixes if fix.get("status") in ["pending", "manual"])

        lines = [f"🔧 修复操作完成 - 共处理 {len(fixes)} 个问题"]
        lines.append(f"   ✅ 成功: {successful}")
        lines.append(f"   ❌ 失败: {failed}")
        lines.append(f"   ⏳ 待处理: {pending}")
        lines.append("")

        # 显示详细结果
        for fix in fixes:
            status = fix.get("status", "unknown")
            message = fix.get("message", "no message")
            error = fix.get("error", {})

            status_icon = {
                "success": "✅",
                "failed": "❌",
                "pending": "⏳",
                "manual": "🔧",
                "dry_run": "[预览]"
            }.get(status, "❓")

            lines.append(f"{status_icon} {message}")

        if successful > 0:
            lines.append("")
            lines.append("📋 建议:")
            lines.append("   - 重启 Claude Code 以重新加载插件")
            lines.append("   - 运行 /plugin 命令验证修复结果")

        return "\n".join(lines)

    @staticmethod
    def severity_priority(severity: str) -> int:
        """获取严重程度优先级"""
        priority_map = {
            "critical": 1,
            "error": 2,
            "warning": 3,
            "info": 4
        }
        return priority_map.get(severity, 99)

    @staticmethod
    def get_type_display_name(error_type: str) -> str:
        """获取错误类型显示名称"""
        display_names = {
            "config-error": "配置错误",
            "name-mismatch": "名称不匹配",
            "path-error": "路径错误"
        }
        return display_names.get(error_type, error_type)

    @staticmethod
    def get_type_icon(error_type: str) -> str:
        """获取错误类型图标"""
        icons = {
            "config-error": "❌",
            "name-mismatch": "❌",
            "path-error": "⚠️"
        }
        return icons.get(error_type, "❓")

    @staticmethod
    def get_default_field_value(field: str, plugin_name: str) -> str:
        """获取字段默认值"""
        defaults = {
            "name": plugin_name or "unnamed-plugin",
            "description": "未提供描述",
            "source": f"./plugins/{plugin_name}",
            "category": "uncategorized"
        }
        return defaults.get(field, "")

    @staticmethod
    def normalize_name(name: str) -> str:
        """标准化名称用于比较"""
        return name.lower().replace("-", "").replace("_", "")

    @staticmethod
    def is_kebab_case(name: str) -> bool:
        """检查是否为 kebab-case"""
        return bool(name) and all(c.islower() or c == '-' or c.isdigit() for c in name)

    @staticmethod
    def to_kebab_case(name: str) -> str:
        """转换为 kebab-case"""
        # 将驼峰式和下划线式转换为连字符式
        import re

        # 处理驼峰式：camelCase → camel-case
        s1 = re.sub('([a-z0-9])([A-Z])', r'\1-\2', name)

        # 处理下划线：snake_case → snake-case
        s2 = s1.replace('_', '-')

        # 转换为小写并移除多余的连字符
        result = re.sub('-+', '-', s2.lower())

        return result.strip('-')

    @staticmethod
    def to_camel_case(name: str) -> str:
        """转换为 camelCase"""
        parts = name.replace('_', '-').split('-')
        return parts[0].lower() + ''.join(p.capitalize() for p in parts[1:])

    @staticmethod
    def to_snake_case(name: str) -> str:
        """转换为 snake_case"""
        import re

        # 处理驼峰式：camelCase → snake_case
        s1 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)

        # 处理连字符：kebab-case → snake_case
        s2 = s1.replace('-', '_')

        return s2.lower()

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="修复技能错误")
    parser.add_argument("--marketplace", default=".claude-plugin/marketplace.json", help="Marketplace 文件路径")
    parser.add_argument("--auto-fix", action="store_true", help="自动修复错误")
    parser.add_argument("--dry-run", action="store_true", help="预览修复操作")
    parser.add_argument("--error-type", help="只修复指定类型的错误")
    parser.add_argument("--plugin-name", help="只修复指定插件的问题")

    args = parser.parse_args()

    try:
        fixer = SkillFixer(args.marketplace)
        fixer.dry_run = args.dry_run

        # 检测错误
        errors = fixer.detect_all_errors()

        # 过滤错误
        if args.error_type:
            errors = [e for e in errors if e.get("type") == args.error_type]

        if args.plugin_name:
            errors = [e for e in errors if e.get("plugin_name") == args.plugin_name]

        # 显示错误报告
        print(fixer.format_error_report(errors))

        if not errors:
            print("✅ 所有配置都正确！")
            return

        # 修复错误
        fixes = fixer.fix_all_errors(errors, args.auto_fix)

        # 显示修复报告
        if args.auto_fix or args.dry_run:
            print(fixer.format_fix_report(fixes))
        else:
            print(f"\n🔧 发现 {len(errors)} 个可修复的问题")
            print("使用 --auto-fix 参数执行自动修复")
            print("使用 --dry-run 参数预览修复操作")

    except Exception as e:
        print(f"❌ 错误: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()