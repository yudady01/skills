#!/usr/bin/env python3
"""
Claude Code settings.json 修复工具

检测和修复 ~/.claude/settings.json 中的插件名称不一致问题
"""

import json
import os
import sys
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime

class SettingsFixer:
    """settings.json 修复器"""

    def __init__(self, settings_path: str = None, marketplace_path: str = ".claude-plugin/marketplace.json"):
        self.settings_path = Path(settings_path) if settings_path else Path.home() / ".claude" / "settings.json"
        self.marketplace_path = Path(marketplace_path)
        self.base_path = self.marketplace_path.parent.parent
        self.backup_dir = self.base_path / ".claude-plugin" / "backups"

        self.errors = []
        self.fixes = []

    def detect_plugin_name_mismatches(self) -> List[Dict]:
        """检测插件名称不匹配"""
        errors = []

        # 读取 settings.json
        if not self.settings_path.exists():
            errors.append({
                "type": "critical",
                "target": "settings.json",
                "issue": f"settings.json 文件不存在: {self.settings_path}",
                "fixable": False
            })
            return errors

        try:
            with open(self.settings_path, 'r', encoding='utf-8') as f:
                settings_data = json.load(f)
        except json.JSONDecodeError as e:
            errors.append({
                "type": "critical",
                "target": "settings.json",
                "issue": f"settings.json JSON 语法错误: {str(e)}",
                "fixable": True,
                "fix_method": "fix_json_syntax"
            })
            return errors

        # 获取启用的插件列表
        enabled_plugins = settings_data.get("enabledPlugins", {})
        if not isinstance(enabled_plugins, dict):
            errors.append({
                "type": "error",
                "target": "settings.json",
                "issue": "enabledPlugins 字段不是对象格式",
                "fixable": True,
                "fix_method": "fix_enabled_plugins_structure"
            })
            return errors

        # 读取 marketplace 配置获取正确的插件名称
        marketplace_plugins = self.get_marketplace_plugins()

        # 检查每个启用的插件
        for plugin_key, enabled in enabled_plugins.items():
            if not isinstance(enabled, bool):
                errors.append({
                    "type": "warning",
                    "target": f"settings.json:{plugin_key}",
                    "issue": f"插件状态不是布尔值: {enabled}",
                    "fixable": True,
                    "fix_method": "fix_plugin_status",
                    "plugin_key": plugin_key,
                    "correct_value": True
                })
                continue

            # 解析插件键名
            parts = plugin_key.split("@")
            if len(parts) != 2:
                errors.append({
                    "type": "warning",
                    "target": f"settings.json:{plugin_key}",
                    "issue": f"插件键名格式不正确: {plugin_key}",
                    "fixable": False
                })
                continue

            plugin_name, marketplace = parts

            # 检查插件名称是否在 marketplace 中存在
            correct_name = self.find_correct_plugin_name(plugin_name, marketplace_plugins)
            if correct_name and correct_name != plugin_name:
                errors.append({
                    "type": "error",
                    "target": f"settings.json:{plugin_key}",
                    "issue": f"插件名称不匹配: {plugin_name} → {correct_name}",
                    "fixable": True,
                    "fix_method": "fix_plugin_name",
                    "plugin_key": plugin_key,
                    "correct_plugin_key": f"{correct_name}@{marketplace}",
                    "current_name": plugin_name,
                    "correct_name": correct_name,
                    "marketplace": marketplace
                })

            # 检查插件是否实际存在
            if correct_name:
                plugin_path = self.base_path / "plugins" / correct_name
                if not plugin_path.exists():
                    errors.append({
                        "type": "warning",
                        "target": f"settings.json:{plugin_key}",
                        "issue": f"插件目录不存在: {plugin_path}",
                        "fixable": True,
                        "fix_method": "disable_missing_plugin",
                        "plugin_key": plugin_key
                    })

        return errors

    def get_marketplace_plugins(self) -> Dict[str, Dict]:
        """获取 marketplace 中的插件列表"""
        plugins = {}

        if not self.marketplace_path.exists():
            return plugins

        try:
            with open(self.marketplace_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            for plugin in data.get("plugins", []):
                plugin_name = plugin.get("name", "")
                if plugin_name:
                    plugins[plugin_name] = plugin

        except Exception as e:
            print(f"警告: 读取 marketplace.json 失败: {str(e)}")

        return plugins

    def find_correct_plugin_name(self, current_name: str, marketplace_plugins: Dict[str, Dict]) -> Optional[str]:
        """查找正确的插件名称"""
        # 直接匹配
        if current_name in marketplace_plugins:
            return current_name

        # 尝试标准化比较
        current_normalized = self.normalize_name_for_comparison(current_name)

        for plugin_name in marketplace_plugins.keys():
            plugin_normalized = self.normalize_name_for_comparison(plugin_name)
            if current_normalized == plugin_normalized:
                return plugin_name

        # 尝试常见的命名转换
        variants = [
            self.to_kebab_case(current_name),
            self.to_camel_case(current_name),
            self.to_snake_case(current_name)
        ]

        for variant in set(variants):
            if variant in marketplace_plugins:
                return variant

        return None

    def fix_plugin_name(self, error: Dict) -> Dict:
        """修复插件名称"""
        current_key = error["plugin_key"]
        correct_key = error["correct_plugin_key"]

        try:
            # 备份文件
            self.create_settings_backup()

            # 读取当前设置
            with open(self.settings_path, 'r', encoding='utf-8') as f:
                settings_data = json.load(f)

            # 更新插件键名
            enabled_plugins = settings_data.get("enabledPlugins", {})
            current_value = enabled_plugins.get(current_key, False)

            # 删除旧键名，添加新键名
            if current_key in enabled_plugins:
                del enabled_plugins[current_key]
            enabled_plugins[correct_key] = current_value

            # 保存设置
            with open(self.settings_path, 'w', encoding='utf-8') as f:
                json.dump(settings_data, f, indent=2, ensure_ascii=False)

            return {
                "error": error,
                "status": "success",
                "message": f"已修复插件名称: {current_key} → {correct_key}"
            }

        except Exception as e:
            return {
                "error": error,
                "status": "failed",
                "message": f"修复插件名称失败: {str(e)}"
            }

    def fix_plugin_status(self, error: Dict) -> Dict:
        """修复插件状态"""
        plugin_key = error["plugin_key"]
        correct_value = error["correct_value"]

        try:
            # 备份文件
            self.create_settings_backup()

            # 读取当前设置
            with open(self.settings_path, 'r', encoding='utf-8') as f:
                settings_data = json.load(f)

            # 更新插件状态
            enabled_plugins = settings_data.get("enabledPlugins", {})
            enabled_plugins[plugin_key] = correct_value

            # 保存设置
            with open(self.settings_path, 'w', encoding='utf-8') as f:
                json.dump(settings_data, f, indent=2, ensure_ascii=False)

            return {
                "error": error,
                "status": "success",
                "message": f"已修复插件状态: {plugin_key} = {correct_value}"
            }

        except Exception as e:
            return {
                "error": error,
                "status": "failed",
                "message": f"修复插件状态失败: {str(e)}"
            }

    def fix_enabled_plugins_structure(self, error: Dict) -> Dict:
        """修复 enabledPlugins 结构"""
        try:
            # 备份文件
            self.create_settings_backup()

            # 读取当前设置
            with open(self.settings_path, 'r', encoding='utf-8') as f:
                settings_data = json.load(f)

            # 重置为正确的对象格式
            settings_data["enabledPlugins"] = {}

            # 保存设置
            with open(self.settings_path, 'w', encoding='utf-8') as f:
                json.dump(settings_data, f, indent=2, ensure_ascii=False)

            return {
                "error": error,
                "status": "success",
                "message": "已修复 enabledPlugins 结构"
            }

        except Exception as e:
            return {
                "error": error,
                "status": "failed",
                "message": f"修复 enabledPlugins 结构失败: {str(e)}"
            }

    def fix_json_syntax(self, error: Dict) -> Dict:
        """修复 JSON 语法错误"""
        try:
            # 备份文件
            self.create_settings_backup()

            # 读取并重新格式化 JSON
            with open(self.settings_path, 'r', encoding='utf-8') as f:
                content = f.read()

            data = json.loads(content)
            with open(self.settings_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            return {
                "error": error,
                "status": "success",
                "message": "已修复 settings.json JSON 语法"
            }

        except Exception as e:
            return {
                "error": error,
                "status": "failed",
                "message": f"修复 JSON 语法失败: {str(e)}"
            }

    def disable_missing_plugin(self, error: Dict) -> Dict:
        """禁用缺失的插件"""
        plugin_key = error["plugin_key"]

        try:
            # 备份文件
            self.create_settings_backup()

            # 读取当前设置
            with open(self.settings_path, 'r', encoding='utf-8') as f:
                settings_data = json.load(f)

            # 禁用插件
            enabled_plugins = settings_data.get("enabledPlugins", {})
            enabled_plugins[plugin_key] = False

            # 保存设置
            with open(self.settings_path, 'w', encoding='utf-8') as f:
                json.dump(settings_data, f, indent=2, ensure_ascii=False)

            return {
                "error": error,
                "status": "success",
                "message": f"已禁用缺失的插件: {plugin_key}"
            }

        except Exception as e:
            return {
                "error": error,
                "status": "failed",
                "message": f"禁用插件失败: {str(e)}"
            }

    def create_settings_backup(self):
        """创建 settings.json 备份"""
        if not self.backup_dir.exists():
            self.backup_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = self.backup_dir / f"settings_{timestamp}.json"

        if self.settings_path.exists():
            shutil.copy2(self.settings_path, backup_file)
            print(f"已创建设置备份: {backup_file}")

    def apply_fixes(self, errors: List[Dict], auto_fix: bool = False, dry_run: bool = False) -> List[Dict]:
        """应用修复"""
        fixes = []

        for error in errors:
            fix_method = error.get("fix_method")
            if not fix_method:
                fixes.append({
                    "error": error,
                    "status": "manual",
                    "message": f"需要手动修复: {error['issue']}"
                })
                continue

            if dry_run:
                fixes.append({
                    "error": error,
                    "status": "dry_run",
                    "message": f"[预览] 将修复: {error['issue']}"
                })
                continue

            if auto_fix:
                if fix_method == "fix_plugin_name":
                    fix_result = self.fix_plugin_name(error)
                elif fix_method == "fix_plugin_status":
                    fix_result = self.fix_plugin_status(error)
                elif fix_method == "fix_enabled_plugins_structure":
                    fix_result = self.fix_enabled_plugins_structure(error)
                elif fix_method == "fix_json_syntax":
                    fix_result = self.fix_json_syntax(error)
                elif fix_method == "disable_missing_plugin":
                    fix_result = self.disable_missing_plugin(error)
                else:
                    fix_result = {
                        "error": error,
                        "status": "failed",
                        "message": f"未知的修复方法: {fix_method}"
                    }
            else:
                fix_result = {
                    "error": error,
                    "status": "pending",
                    "message": f"需要修复: {error['issue']}"
                }

            fixes.append(fix_result)

        return fixes

    def format_report(self, errors: List[Dict], fixes: List[Dict] = None) -> str:
        """格式化报告"""
        lines = []

        if not errors:
            lines.append("✅ settings.json 未发现问题")
            return "\n".join(lines)

        lines.append(f"🔍 settings.json 检测完成 - 发现 {len(errors)} 个问题\n")

        # 按严重程度分组
        by_type = {}
        for error in errors:
            error_type = error.get("type", "unknown")
            if error_type not in by_type:
                by_type[error_type] = []
            by_type[error_type].append(error)

        type_order = ["critical", "error", "warning", "info"]
        type_icons = {"critical": "🔴", "error": "❌", "warning": "⚠️", "info": "ℹ️"}

        for error_type in type_order:
            if error_type in by_type:
                type_errors = by_type[error_type]
                icon = type_icons[error_type]
                type_name = {"critical": "严重错误", "error": "错误", "warning": "警告", "info": "信息"}.get(error_type, error_type)

                lines.append(f"{icon} {type_name} ({len(type_errors)} 个):")

                for error in type_errors:
                    target = error.get("target", "unknown")
                    issue = error.get("issue", "unknown issue")
                    fixable = error.get("fixable", False)

                    lines.append(f"   - {target}")
                    lines.append(f"     问题: {issue}")

                    if error.get("current_name") and error.get("correct_name"):
                        lines.append(f"     修复: {error['current_name']} → {error['correct_name']}")

                    if fixable:
                        lines.append(f"     状态: 可自动修复")
                    else:
                        lines.append(f"     状态: 需要手动处理")

                lines.append("")

        # 显示修复结果
        if fixes:
            successful = sum(1 for fix in fixes if fix.get("status") == "success")
            failed = sum(1 for fix in fixes if fix.get("status") == "failed")
            pending = sum(1 for fix in fixes if fix.get("status") in ["pending", "manual"])

            lines.append("🔧 修复结果:")
            lines.append(f"   ✅ 成功: {successful}")
            lines.append(f"   ❌ 失败: {failed}")
            lines.append(f"   ⏳ 待处理: {pending}")

            if successful > 0:
                lines.append("")
                lines.append("📋 建议:")
                lines.append("   - 重启 Claude Code 以重新加载插件")
                lines.append("   - 运行 /plugin 命令验证修复结果")

        return "\n".join(lines)

    @staticmethod
    def normalize_name_for_comparison(name: str) -> str:
        """标准化名称用于比较"""
        return name.lower().replace("-", "").replace("_", "")

    @staticmethod
    def to_kebab_case(name: str) -> str:
        """转换为 kebab-case"""
        import re
        s1 = re.sub('([a-z0-9])([A-Z])', r'\1-\2', name)
        s2 = s1.replace('_', '-')
        return re.sub('-+', '-', s2.lower()).strip('-')

    @staticmethod
    def to_camel_case(name: str) -> str:
        """转换为 camelCase"""
        parts = name.replace('_', '-').split('-')
        return parts[0].lower() + ''.join(p.capitalize() for p in parts[1:])

    @staticmethod
    def to_snake_case(name: str) -> str:
        """转换为 snake_case"""
        import re
        s1 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
        return s1.replace('-', '_').lower()

def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="修复 settings.json 中的插件名称问题")
    parser.add_argument("--settings", help="settings.json 文件路径 (默认: ~/.claude/settings.json)")
    parser.add_argument("--marketplace", default=".claude-plugin/marketplace.json", help="marketplace.json 文件路径")
    parser.add_argument("--auto-fix", action="store_true", help="自动修复错误")
    parser.add_argument("--dry-run", action="store_true", help="预览修复操作")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="输出格式")

    args = parser.parse_args()

    try:
        fixer = SettingsFixer(args.settings, args.marketplace)

        # 检测错误
        errors = fixer.detect_plugin_name_mismatches()

        # 应用修复
        fixes = None
        if args.auto_fix or args.dry_run:
            fixes = fixer.apply_fixes(errors, args.auto_fix, args.dry_run)

        # 输出结果
        if args.format == "json":
            result = {
                "errors_detected": len(errors),
                "fixes_applied": len([f for f in fixes or [] if f.get("status") == "success"]) if fixes else 0,
                "errors": errors,
                "fixes": fixes
            }
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(fixer.format_report(errors, fixes))

    except Exception as e:
        print(f"❌ 错误: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()