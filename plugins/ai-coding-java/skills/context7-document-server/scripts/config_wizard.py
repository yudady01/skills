#!/usr/bin/env python3
"""
Context7 智能配置向导
当配置文件缺失或损坏时，自动提示用户创建配置文件
"""

import os
import sys
import json
import yaml
from pathlib import Path
from getpass import getpass
from typing import Optional, Dict, Any

class Context7ConfigWizard:
    def __init__(self):
        self.home_dir = Path.home()
        self.claude_dir = self.home_dir / ".claude"
        self.context7_config_file = self.claude_dir / "context7.json"
        self.context7_dir = self.claude_dir / ".context7"
        self.api_key_file = self.context7_dir / "api-key"
        self.detailed_config_file = self.context7_dir / "config.yaml"

    def check_configuration_status(self) -> Dict[str, Any]:
        """检查配置状态"""
        status = {
            "claude_dir_exists": self.claude_dir.exists(),
            "context7_config_exists": self.context7_config_file.exists(),
            "context7_dir_exists": self.context7_dir.exists(),
            "api_key_file_exists": self.api_key_file.exists(),
            "config_is_valid": False,
            "api_key_is_valid": False,
            "permissions_ok": True,
            "issues": []
        }

        # 检查 Claude 目录
        if not status["claude_dir_exists"]:
            status["issues"].append("Claude 目录不存在")

        # 检查 Context7 目录
        if not status["context7_dir_exists"]:
            status["issues"].append("Context7 配置目录不存在")

        # 检查配置文件
        if status["context7_config_exists"]:
            try:
                with open(self.context7_config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                status["config_is_valid"] = isinstance(config, dict) and len(config) > 0

                if "api_key" in config and config["api_key"]:
                    print("⚠️  警告: 主配置文件中包含 API Key，建议移动到专用文件")
                    status["api_key_in_main_config"] = True

            except Exception as e:
                status["issues"].append(f"配置文件格式错误: {e}")
                status["config_is_valid"] = False

        # 检查 API Key 文件
        if status["api_key_file_exists"]:
            try:
                with open(self.api_key_file, 'r', encoding='utf-8') as f:
                    api_key = f.read().strip()
                status["api_key_is_valid"] = len(api_key) > 20 and api_key.startswith("ctx7sk-")

                # 检查文件权限
                stat = self.api_key_file.stat()
                permissions = oct(stat.st_mode)[-3:]
                if permissions != "600":
                    status["permissions_ok"] = False
                    status["issues"].append(f"API Key 文件权限不安全: {permissions} (应为 600)")

            except Exception as e:
                status["issues"].append(f"API Key 文件读取错误: {e}")
                status["api_key_is_valid"] = False

        return status

    def prompt_for_api_key(self) -> Optional[str]:
        """提示用户输入 API Key"""
        print("\n🔑 Context7 API Key 配置")
        print("=" * 50)
        print("请输入您的 Context7 API Key (格式: ctx7sk-xxxxxxxxxxxx)")
        print("API Key 通常以 'ctx7sk-' 开头")
        print("输入 'skip' 跳过此步骤（稍后可手动配置）")
        print()

        while True:
            try:
                api_key = getpass("🔑 请输入 Context7 API Key: ").strip()

                if api_key.lower() == 'skip':
                    print("⏭️ 跳过 API Key 配置")
                    return None

                if not api_key:
                    print("❌ API Key 不能为空")
                    continue

                if len(api_key) < 20:
                    print("❌ API Key 长度过短，请检查输入")
                    continue

                if not api_key.startswith("ctx7sk-"):
                    print("❌ API Key 格式不正确，应以 'ctx7sk-' 开头")
                    continue

                return api_key

            except KeyboardInterrupt:
                print("\n⚠️  配置被用户中断")
                return None

    def create_default_config(self, api_key: Optional[str] = None) -> bool:
        """创建默认配置"""
        print("\n📝 创建 Context7 默认配置...")
        print("=" * 50)

        try:
            # 创建目录
            self.claude_dir.mkdir(exist_ok=True)
            self.context7_dir.mkdir(exist_ok=True)

            # 创建主配置文件
            main_config = {
                "server_endpoint": "https://api.context7.ai/v1",
                "default_model": "ctx7-search-v1",
                "timeout": 30000,
                "max_results": 10,
                "cache_enabled": True,
                "cache_ttl": 3600,
                "document_sources": [
                    "${CLAUDE_PLUGIN_ROOT}/docs",
                    "${HOME}/.claude/.context7/documents",
                    "${HOME}/Documents/context7"
                ],
                "retrieval_config": {
                    "semantic_weight": 0.7,
                    "keyword_weight": 0.3,
                    "chunk_size": 512,
                    "overlap": 50
                }
            }

            # 如果提供了 API Key，添加到配置中（优先级较低）
            if api_key:
                print(f"🔑 添加 API Key 到配置文件")
                main_config["api_key"] = api_key

            with open(self.context7_config_file, 'w', encoding='utf-8') as f:
                json.dump(main_config, f, indent=2, ensure_ascii=False)

            print(f"✅ 主配置文件已创建: {self.context7_config_file}")

            # 创建 API Key 文件（如果提供）
            if api_key:
                with open(self.api_key_file, 'w', encoding='utf-8') as f:
                    f.write(api_key)
                print(f"✅ API Key 文件已创建: {self.api_key_file}")

                # 设置文件权限
                os.chmod(self.api_key_file, 0o600)
                print(f"🔒 API Key 文件权限已设置为: 600 (仅所有者可读写)")

            # 创建详细配置文件
            detailed_config = {
                "service": {
                    "name": "context7-document-server",
                    "version": "1.0.0",
                    "description": "智能文档检索和知识管理服务"
                },
                "api": {
                    "base_url": "https://api.context7.ai/v1",
                    "timeout": 30,
                    "retry_attempts": 3,
                    "retry_delay": 1000
                },
                "models": {
                    "embedding": {
                        "name": "ctx7-embedding-v1",
                        "dimension": 768,
                        "max_tokens": 8192
                    },
                    "search": {
                        "name": "ctx7-search-v1",
                        "max_context": 4096
                    }
                },
                "document_processing": {
                    "supported_formats": [
                        "markdown",
                        "pdf",
                        "html",
                        "text",
                        "docx"
                    ],
                    "chunking": {
                        "strategy": "semantic",
                        "chunk_size": 512,
                        "overlap": 50,
                        "min_chunk_size": 100
                    },
                    "preprocessing": {
                        "remove_headers_footers": True,
                        "normalize_whitespace": True,
                        "extract_tables": True
                    }
                },
                "retrieval": {
                    "hybrid_search": {
                        "semantic_weight": 0.7,
                        "keyword_weight": 0.3,
                        "rerank": True
                    },
                    "filters": {
                        "enabled": True,
                        "fields": [
                            "category",
                            "source",
                            "format",
                            "created_at"
                        ]
                    }
                },
                "cache": {
                    "enabled": True,
                    "ttl": 3600,
                    "max_size": 1000,
                    "storage_path": "${HOME}/.context7/cache"
                },
                "logging": {
                    "level": "INFO",
                    "file": "${HOME}/.context7/logs/context7.log",
                    "max_size": "10MB",
                    "backup_count": 5
                }
            }

            with open(self.detailed_config_file, 'w', encoding='utf-8') as f:
                yaml.dump(detailed_config, f, default_flow_style=False, allow_unicode=True)

            print(f"✅ 详细配置文件已创建: {self.detailed_config_file}")

            # 创建必要目录
            required_dirs = [
                self.context7_dir / "documents",
                self.context7_dir / "cache",
                self.context7_dir / "logs"
            ]

            for dir_path in required_dirs:
                dir_path.mkdir(exist_ok=True)
                print(f"✅ 目录已创建: {dir_path}")

            return True

        except Exception as e:
            print(f"❌ 创建配置失败: {e}")
            return False

    def fix_permissions(self) -> bool:
        """修复文件权限"""
        print("\n🔒 修复配置文件权限...")
        print("=" * 40)

        try:
            # API Key 文件权限
            if self.api_key_file.exists():
                current_permissions = oct(self.api_key_file.stat().st_mode)[-3:]
                if current_permissions != "600":
                    print(f"🔧 修复 API Key 文件权限: {current_permissions} → 600")
                    os.chmod(self.api_key_file, 0o600)
                    print("✅ API Key 文件权限已修复")
                else:
                    print("✅ API Key 文件权限正确: 600")

            # 主配置文件权限
            if self.context7_config_file.exists():
                current_permissions = oct(self.context7_config_file.stat().st_mode)[-3:]
                if current_permissions != "600":
                    print(f"🔧 修复配置文件权限: {current_permissions} → 600")
                    os.chmod(self.context7_config_file, 0o600)
                    print("✅ 配置文件权限已修复")
                else:
                    print("✅ 配置文件权限正确: 600")

            # 目录权限
            if self.context7_dir.exists():
                current_permissions = oct(self.context7_dir.stat().st_mode)[-3:]
                if current_permissions != "700":
                    print(f"🔧 修复配置目录权限: {current_permissions} → 700")
                    os.chmod(self.context7_dir, 0o700)
                    print("✅ 配置目录权限已修复")
                else:
                    print("✅ 配置目录权限正确: 700")

            # Claude 目录权限
            if self.claude_dir.exists():
                current_permissions = oct(self.claude_dir.stat().st_mode)[-3:]
                if current_permissions != "755":
                    print(f"🔧 修复 Claude 目录权限: {current_permissions} → 755")
                    os.chmod(self.claude_dir, 0o755)
                    print("✅ Claude 目录权限已修复")
                else:
                    print("✅ Claude 目录权限正确: 755")

            return True

        except Exception as e:
            print(f"❌ 权限修复失败: {e}")
            return False

    def show_next_steps(self) -> None:
        """显示后续步骤"""
        print("\n🎯 后续步骤")
        print("=" * 30)
        print("1. ✅ 配置文件已创建完成")
        print("2. 🔍 Context7 现在可以正常使用")
        print("3. 📚 支持文档搜索和索引")
        print("4. 🔧 可以随时修改配置文件")
        print()
        print("📖 配置文件位置:")
        print(f"   主配置: {self.context7_config_file}")
        print(f"   API Key: {self.api_key_file}")
        print(f"   详细配置: {self.detailed_config_file}")
        print()
        print("🚀 常用命令:")
        print("   /docs-search '查询内容'  # 搜索文档")
        print("   /docs-search --scope=builtin '关键词'  # 搜索内置文档")
        print("   /docs-search --limit=5 '查询'       # 限制结果数量")

def main():
    """配置向导主函数"""
    print("🔮 Context7 智能配置向导")
    print("=" * 50)
    print("检测 Context7 配置状态并提供自动配置帮助")
    print()

    wizard = Context7ConfigWizard()

    # 检查当前配置状态
    status = wizard.check_configuration_status()

    print("🔍 配置状态检查:")
    print(f"   ✅ Claude 目录: {'存在' if status['claude_dir_exists'] else '不存在'}")
    print(f"   ✅ Context7 配置文件: {'存在' if status['context7_config_exists'] else '不存在'}")
    print(f"   ✅ Context7 配置目录: {'存在' if status['context7_dir_exists'] else '不存在'}")
    print(f"   ✅ API Key 文件: {'存在' if status['api_key_file_exists'] else '不存在'}")

    # 显示问题
    if status["issues"]:
        print(f"\n⚠️  发现 {len(status['issues'])} 个配置问题:")
        for i, issue in enumerate(status['issues'], 1):
            print(f"   {i}. {issue}")

    # 根据状态采取行动
    needs_configuration = (
        not status['claude_dir_exists'] or
        not status['context7_config_exists'] or
        not status['context7_dir_exists'] or
        not status['api_key_file_exists'] or
        not status['config_is_valid'] or
        not status['api_key_is_valid'] or
        not status['permissions_ok']
    )

    if needs_configuration:
        print(f"\n🚀 需要创建或修复配置")
        print("=" * 30)

        # 询问用户是否要自动创建配置
        try:
            user_input = input("是否要自动创建配置文件？(y/n): ").strip().lower()

            if user_input in ['y', 'yes', '是', '']:
                print("\n🎯 开始自动配置...")

                # 询问 API Key
                print("\n" + "="*50)
                print("需要您的 Context7 API Key 来使用智能文档搜索功能")
                print("如果您没有 API Key，可以选择:")
                print("  1. 立即输入 API Key")
                print(" 2. 跳过配置（稍后手动配置）")
                print()

                api_key_input = input("选择配置方式 (1/2): ").strip()

                api_key = None
                if api_key_input == "1":
                    api_key = wizard.prompt_for_api_key()

                # 创建配置
                success = wizard.create_default_config(api_key)

                if success:
                    # 修复权限
                    wizard.fix_permissions()

                    # 显示后续步骤
                    wizard.show_next_steps()
                else:
                    print("\n❌ 配置创建失败，请手动创建配置文件")

                    print(f"\n📝 手动配置指南:")
                    print(f"1. 创建目录: mkdir -p ~/.claude/.context7")
                    print(f"2. 创建 API Key 文件:")
                    print(f"   echo 'ctx7sk-your-api-key-here' > ~/.claude/.context7/api-key")
                    print(f"   chmod 600 ~/.claude/.context7/api-key")
                    print(f"3. 创建配置文件:")
                    print(f"   vim ~/.claude/context7.json")
                    print(f"4. 设置文件权限:")
                    print(f"   chmod 600 ~/.claude/context7.json")

            else:
                print("\n📝 手动配置指南:")
                print("1. 创建目录: mkdir -p ~/.claude/.context7")
                print("2. 创建 API Key 文件:")
                print("   echo 'ctx7sk-your-api-key-here' > ~/.claude/.context7/api-key")
                print("   chmod 600 ~/.claude/.context7/api-key")
                print("3. 创建配置文件:")
                print("   vim ~/.claude/context7.json")
                print("4. 设置文件权限:")
                print("   chmod 600 ~/.claude/context7.json")

        except KeyboardInterrupt:
            print("\n⚠️  配置被用户中断")

    else:
        print("\n✅ 配置状态良好，无需额外操作")

        # 检查是否有改进空间
        if status.get("api_key_in_main_config"):
            print("\n💡 改进建议:")
            print("   • 考虑将主配置文件中的 API Key 移动到专用文件")
            print("   • 删除主配置文件中的 api_key 字段")
            print("   • 这样可以提高安全性")

        if not status.get("permissions_ok"):
            print("\n💡 权限改进建议:")
            print("   • 运行: chmod 600 ~/.claude/.context7/api-key")
            print("   • 运行: chmod 600 ~/.claude/context7.json")
            print("   • 运行: chmod 700 ~/.claude/.context7/")

if __name__ == "__main__":
    main()