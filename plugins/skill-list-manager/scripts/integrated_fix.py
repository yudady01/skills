#!/usr/bin/env python3
"""
集成错误检测和修复工具

结合基础错误修复和系统兼容性检查的完整解决方案
"""

import json
import sys
import os
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

# 导入现有的修复器
from fix_errors import SkillFixer
from system_compatibility import SystemCompatibilityChecker
from settings_fix import SettingsFixer

class IntegratedSkillFixer:
    """集成技能错误修复器"""

    def __init__(self, marketplace_path: str = ".claude-plugin/marketplace.json"):
        self.marketplace_path = Path(marketplace_path)
        self.base_path = self.marketplace_path.parent.parent

        # 初始化子修复器
        self.basic_fixer = SkillFixer(marketplace_path)
        self.compatibility_checker = SystemCompatibilityChecker(marketplace_path)
        self.settings_fixer = SettingsFixer(marketplace_path=marketplace_path)

        self.all_errors = []
        self.all_fixes = []

    def detect_all_errors(self) -> List[Dict]:
        """检测所有类型的错误"""
        all_errors = []

        # 1. 基础配置错误检测
        print("🔍 检测基础配置错误...")
        basic_errors = self.basic_fixer.detect_all_errors()
        all_errors.extend(basic_errors)

        # 2. 系统兼容性错误检测
        print("🔍 检测系统兼容性错误...")
        compatibility_analysis = self.compatibility_checker.analyze_system()

        # 转换兼容性问题为标准错误格式
        for issue in compatibility_analysis["issues_by_type"].get("warning", []):
            if issue.get("category") == "configuration":
                # 配置文件命名错误
                all_errors.append({
                    "type": issue.get("type", "warning"),
                    "severity": "warning",
                    "target": issue.get("target", "unknown"),
                    "issue": issue.get("message", ""),
                    "fixable": issue.get("fixable", False),
                    "fix_method": issue.get("fix_method"),
                    "plugin_name": issue.get("plugin_name"),
                    "suggested_fix": issue.get("suggested_fix", "")
                })

        # 3. Settings.json 错误检测
        print("🔍 检测系统设置错误...")
        settings_errors = self.settings_fixer.detect_plugin_name_mismatches()
        all_errors.extend(settings_errors)

        return all_errors

    def fix_all_errors(self, auto_fix: bool = False, dry_run: bool = False) -> Dict:
        """修复所有错误"""
        # 设置 dry-run 模式
        if dry_run:
            self.basic_fixer.dry_run = True

        # 检测所有错误
        errors = self.detect_all_errors()

        if not errors:
            return {
                "status": "success",
                "message": "✅ 未发现任何错误",
                "errors_detected": 0,
                "fixes_applied": 0,
                "errors": [],
                "fixes": []
            }

        # 修复基础错误
        basic_fixes = self.basic_fixer.fix_all_errors(errors, auto_fix)

        # 修复兼容性错误
        compatibility_fixes = self._fix_compatibility_errors(errors, auto_fix, dry_run)

        # 修复 settings.json 错误
        settings_fixes = self._fix_settings_errors(errors, auto_fix, dry_run)

        all_fixes = basic_fixes + compatibility_fixes + settings_fixes

        return {
            "status": "completed",
            "message": f"🔧 处理完成 - 共发现 {len(errors)} 个问题",
            "errors_detected": len(errors),
            "fixes_applied": len([f for f in all_fixes if f.get("status") == "success"]),
            "errors": errors,
            "fixes": all_fixes
        }

    def _fix_compatibility_errors(self, errors: List[Dict], auto_fix: bool, dry_run: bool) -> List[Dict]:
        """修复兼容性错误"""
        fixes = []

        for error in errors:
            if error.get("fix_method") == "fix_config_filename":
                if auto_fix or dry_run:
                    fix_result = self.basic_fixer.fix_config_filename(error)
                    fixes.append(fix_result)
                else:
                    fixes.append({
                        "error": error,
                        "status": "pending",
                        "message": f"需要修复: {error['issue']}"
                    })

        return fixes

    def _fix_settings_errors(self, errors: List[Dict], auto_fix: bool, dry_run: bool) -> List[Dict]:
        """修复 settings.json 错误"""
        fixes = []

        # 收集 settings.json 相关的错误
        settings_errors = [error for error in errors if error.get("target", "").startswith("settings.json")]

        if settings_errors:
            if auto_fix or dry_run:
                # 使用 settings_fixer 修复所有 settings 错误
                settings_fixes = self.settings_fixer.apply_fixes(settings_errors, auto_fix, dry_run)
                fixes.extend(settings_fixes)
            else:
                for error in settings_errors:
                    fixes.append({
                        "error": error,
                        "status": "pending",
                        "message": f"需要修复: {error['issue']}"
                    })

        return fixes

    def format_comprehensive_report(self, result: Dict) -> str:
        """格式化综合报告"""
        lines = []

        # 状态概览
        lines.append("🔧 技能错误修复 - 综合报告")
        lines.append(f"📊 检测到错误: {result['errors_detected']} 个")
        lines.append(f"✅ 修复成功: {result['fixes_applied']} 个")
        lines.append("")

        # 错误分类统计
        errors_by_type = {}
        for error in result.get("errors", []):
            error_type = error.get("type", "unknown")
            errors_by_type[error_type] = errors_by_type.get(error_type, 0) + 1

        if errors_by_type:
            lines.append("📋 错误类型统计:")
            for error_type, count in errors_by_type.items():
                lines.append(f"   - {error_type}: {count} 个")
            lines.append("")

        # 修复结果
        fixes_by_status = {}
        for fix in result.get("fixes", []):
            status = fix.get("status", "unknown")
            fixes_by_status[status] = fixes_by_status.get(status, 0) + 1

        if fixes_by_status:
            lines.append("🔧 修复结果统计:")
            for status, count in fixes_by_status.items():
                status_icon = {
                    "success": "✅",
                    "failed": "❌",
                    "pending": "⏳",
                    "dry_run": "[预览]",
                    "manual": "🔧"
                }.get(status, "❓")
                status_name = {
                    "success": "成功",
                    "failed": "失败",
                    "pending": "待处理",
                    "dry_run": "预览",
                    "manual": "需手动"
                }.get(status, status)
                lines.append(f"   {status_icon} {status_name}: {count} 个")
            lines.append("")

        # 详细修复结果
        if result.get("fixes"):
            lines.append("📝 详细修复结果:")
            for fix in result.get("fixes", []):
                status = fix.get("status", "unknown")
                message = fix.get("message", "no message")

                status_icon = {
                    "success": "✅",
                    "failed": "❌",
                    "pending": "⏳",
                    "dry_run": "[预览]",
                    "manual": "🔧"
                }.get(status, "❓")

                lines.append(f"   {status_icon} {message}")

        # 建议
        if result.get("fixes_applied", 0) > 0:
            lines.append("")
            lines.append("📋 后续建议:")
            lines.append("   - 重启 Claude Code 以重新加载插件")
            lines.append("   - 运行 /plugin 命令验证修复结果")
            lines.append("   - 运行 /skill-fix 命令再次检查")

        return "\n".join(lines)

def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="集成错误检测和修复工具")
    parser.add_argument("--marketplace", default=".claude-plugin/marketplace.json", help="Marketplace 文件路径")
    parser.add_argument("--auto-fix", action="store_true", help="自动修复错误")
    parser.add_argument("--dry-run", action="store_true", help="预览修复操作")
    parser.add_argument("--error-type", help="只修复指定类型的错误")
    parser.add_argument("--plugin-name", help="只修复指定插件的问题")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="输出格式")

    args = parser.parse_args()

    try:
        fixer = IntegratedSkillFixer(args.marketplace)

        # 执行修复
        result = fixer.fix_all_errors(args.auto_fix, args.dry_run)

        # 输出结果
        if args.format == "json":
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(fixer.format_comprehensive_report(result))

    except Exception as e:
        print(f"❌ 错误: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()