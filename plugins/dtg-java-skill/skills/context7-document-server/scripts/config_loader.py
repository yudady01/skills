import os
import json
import yaml
from pathlib import Path
from typing import Dict, Any, Optional

class Context7ConfigLoader:
    def __init__(self):
        self.home_dir = Path.home()
        self.claude_dir = self.home_dir / ".claude"
        self.context7_config_file = self.claude_dir / "context7.json"
        self.context7_dir = self.claude_dir / ".context7"
        self.api_key_file = self.context7_dir / "api-key"
        self.detailed_config_file = self.context7_dir / "config.yaml"

    def load_config(self) -> Dict[str, Any]:
        """加载完整的 Context7 配置"""
        config = {}

        # 1. 加载主配置文件
        if self.context7_config_file.exists():
            with open(self.context7_config_file, 'r', encoding='utf-8') as f:
                main_config = json.load(f)
                config.update(main_config)

        # 2. 从环境变量或文件加载 API Key
        api_key = os.getenv('CONTEXT7_API_KEY')
        if not api_key and self.api_key_file.exists():
            with open(self.api_key_file, 'r', encoding='utf-8') as f:
                api_key = f.read().strip()
        if api_key:
            config['api_key'] = api_key

        # 3. 加载详细配置文件
        if self.detailed_config_file.exists():
            with open(self.detailed_config_file, 'r', encoding='utf-8') as f:
                detailed_config = yaml.safe_load(f)
                config.update(detailed_config)

        # 4. 处理环境变量替换
        config = self._resolve_env_vars(config)

        return config

    def _resolve_env_vars(self, obj: Any) -> Any:
        """递归解析配置中的环境变量"""
        if isinstance(obj, str):
            import re
            # 使用正则表达式找到所有 ${VAR} 格式的环境变量
            def replace_env_var(match):
                env_expr = match.group(1)
                # 检查是否有默认值
                if ':' in env_expr:
                    env_var, default_value = env_expr.split(':', 1)
                else:
                    env_var = env_expr
                    default_value = None
                result = os.getenv(env_var.strip(), default_value)
                return result if result is not None else match.group(0)

            # 匹配 ${VAR} 或 ${VAR:default} 格式
            pattern = r'\$\{([^}]+)\}'
            return re.sub(pattern, replace_env_var, obj)
        elif isinstance(obj, dict):
            return {k: self._resolve_env_vars(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._resolve_env_vars(item) for item in obj]
        else:
            return obj

    def get_api_key(self) -> Optional[str]:
        """获取 API Key"""
        # 优先级: 环境变量 > 配置文件 > API Key 文件
        api_key = os.getenv('CONTEXT7_API_KEY')
        if api_key:
            return api_key

        config = self.load_config()
        if 'api_key' in config:
            return config['api_key']

        if self.api_key_file.exists():
            with open(self.api_key_file, 'r', encoding='utf-8') as f:
                return f.read().strip()

        return None

    def get_document_sources(self) -> list:
        """获取文档源路径列表"""
        config = self.load_config()
        sources = config.get('document_sources', [])

        # 添加默认路径
        default_sources = [
            str(self.context7_dir / "documents"),
            str(self.home_dir / "Documents" / "context7")
        ]

        # 去重并返回存在的路径
        all_sources = list(set(sources + default_sources))
        return [Path(source).expanduser().resolve() for source in all_sources if Path(source).expanduser().exists()]

    def get_retrieval_config(self) -> Dict[str, Any]:
        """获取检索配置"""
        config = self.load_config()
        return config.get('retrieval_config', {
            'semantic_weight': 0.7,
            'keyword_weight': 0.3,
            'chunk_size': 512,
            'overlap': 50
        })

# 使用示例
config_loader = Context7ConfigLoader()
config = config_loader.load_config()