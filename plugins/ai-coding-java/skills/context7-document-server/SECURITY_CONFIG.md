# Context7 安全配置指南

本文档详细说明了 Context7 的安全配置方案，确保 API Key 和敏感信息的安全管理。

## 🔒 安全配置原则

### 1. **用户目录优先级**
Context7 采用多层配置策略，优先级从高到低：
1. **环境变量** - 最高优先级，用于临时配置
2. **用户配置文件** - 次优先级，用于持久化配置
3. **API Key 文件** - 专用文件，独立存储敏感信息

### 2. **配置文件位置**
```
~/.claude/
├── context7.json                    # 主配置文件
├── .context7/                       # Context7 配置目录
│   ├── api-key                      # API Key (权限: 600)
│   ├── config.yaml                  # 详细配置
│   ├── documents/                   # 用户文档存储
│   ├── cache/                       # 缓存目录
│   └── logs/                        # 日志目录
```

## 🔐 配置实现

### 配置加载器设计

```python
class Context7ConfigLoader:
    def __init__(self):
        self.home_dir = Path.home()
        self.claude_dir = self.home_dir / ".claude"
        self.context7_config_file = self.claude_dir / "context7.json"
        self.context7_dir = self.claude_dir / ".context7"
        self.api_key_file = self.context7_dir / "api-key"
        self.detailed_config_file = self.context7_dir / "config.yaml"

    def get_api_key(self) -> Optional[str]:
        """获取 API Key - 按优先级多层读取"""
        # 1. 优先级1: 环境变量
        api_key = os.getenv('CONTEXT7_API_KEY')
        if api_key:
            return api_key

        # 2. 优先级2: 主配置文件中的 API Key
        try:
            config = self.load_config()
            if 'api_key' in config:
                return config['api_key']
        except:
            pass

        # 3. 优先级3: 专用 API Key 文件
        if self.api_key_file.exists():
            with open(self.api_key_file, 'r', encoding='utf-8') as f:
                return f.read().strip()

        return None
```

### MCP 服务器配置

```json
{
  "mcpServers": {
    "context7-doc-server": {
      "command": "python",
      "args": [
        "${CLAUDE_PLUGIN_ROOT}/skills/context7-document-server/scripts/context7_server.py"
      ],
      "env": {
        "CONTEXT7_CONFIG_PATH": "${HOME}/.claude/context7.json",
        "CONTEXT7_CACHE_DIR": "${HOME}/.claude/.context7/cache"
        // ❌ 注意：硬编码 API Key 是不安全的
        // "CONTEXT7_API_KEY": "ctx7sk-xxx-xxx-xxx"
      }
    }
  }
}
```

## 🛡️ 安全最佳实践

### 1. 文件权限设置

```bash
# API Key 文件 - 仅所有者可读写
chmod 600 ~/.claude/.context7/api-key

# 配置文件 - 仅所有者可读写
chmod 600 ~/.claude/context7.json
chmod 600 ~/.claude/.context7/config.yaml

# 目录权限 - 所有者完全控制
chmod 700 ~/.claude/.context7/
chmod 755 ~/.claude/
```

### 2. 配置文件内容示例

#### API Key 文件 (~/.claude/.context7/api-key)
```
ctx7sk-521a76f7-6688-49e9-8f37-29cc97036a55
```

#### 主配置文件 (~/.claude/context7.json)
```json
{
  "server_endpoint": "https://api.context7.ai/v1",
  "default_model": "ctx7-search-v1",
  "timeout": 30000,
  "max_results": 10,
  "cache_enabled": true,
  "cache_ttl": 3600,
  "document_sources": [
    "${CLAUDE_PLUGIN_ROOT}/docs",
    "${HOME}/.context7/documents"
  ],
  "retrieval_config": {
    "semantic_weight": 0.7,
    "keyword_weight": 0.3,
    "chunk_size": 512,
    "overlap": 50
  }
}
```

### 3. 环境变量配置

```bash
# 临时 API Key 配置（当前会话有效）
export CONTEXT7_API_KEY="ctx7sk-xxx-xxx-xxx"

# 临时配置文件路径
export CONTEXT7_CONFIG_PATH="/path/to/custom/context7.json"

# 临时缓存目录
export CONTEXT7_CACHE_DIR="/tmp/context7-cache"
```

## 🔍 安全验证

### 配置安全检查脚本

```python
#!/usr/bin/env python3
"""
Context7 安全配置验证脚本
"""

import os
from pathlib import Path
from config_loader import Context7ConfigLoader

def verify_security():
    """验证安全配置"""
    print("🔒 Context7 安全配置验证")
    print("=" * 40)

    config_loader = Context7ConfigLoader()

    # 检查 API Key 安全性
    api_key = config_loader.get_api_key()
    if not api_key:
        print("❌ 未找到 API Key 配置")
        return False

    print(f"✅ API Key 配置成功: {api_key[:8]}...{api_key[-4:]}")

    # 检查文件权限
    api_key_file = config_loader.api_key_file
    if api_key_file.exists():
        stat = api_key_file.stat()
        permissions = oct(stat.st_mode)[-3:]

        if permissions != "600":
            print(f"⚠️  API Key 文件权限过于宽松: {permissions}")
            print("   建议执行: chmod 600 ~/.claude/.context7/api-key")
            return False
        else:
            print("✅ API Key 文件权限正确: 600")

    # 检查配置文件是否包含硬编码密钥
    config_file = config_loader.context7_config_file
    if config_file.exists():
        with open(config_file, 'r', encoding='utf-8') as f:
            content = f.read()

        dangerous_patterns = [
            "ctx7sk-",
            "sk-",
            "api_key",
            "CONTEXT7_API_KEY"
        ]

        # 检查是否在配置文件中硬编码了密钥
        if any(pattern in content for pattern in dangerous_patterns):
            print("❌ 检测到配置文件中可能包含硬编码密钥")
            return False
        else:
            print("✅ 配置文件安全，无硬编码密钥")

    return True

if __name__ == "__main__":
    success = verify_security()
    print("\n" + "=" * 40)
    if success:
        print("🎉 安全配置验证通过！")
    else:
        print("❌ 安全配置验证失败，请按照指南进行修复")
```

## 🔄 配置更新流程

### 1. 添加新 API Key

```bash
# 方法1: 直接写入文件
echo "ctx7sk-xxxxxxxxxxxx" > ~/.claude/.context7/api-key
chmod 600 ~/.claude/.context7/api-key

# 方法2: 使用编辑器
vim ~/.claude/.context7/api-key
# 输入密钥后保存
chmod 600 ~/.claude/.context7/api-key
```

### 2. 更新配置参数

```bash
# 编辑主配置文件
vim ~/.claude/context7.json

# 或编辑详细配置
vim ~/.claude/.context7/config.yaml
```

### 3. 设置环境变量（临时）

```bash
# 当前终端会话
export CONTEXT7_API_KEY="ctx7sk-xxxxxxxxxxxx"

# 永久化（添加到 shell 配置文件）
echo 'export CONTEXT7_API_KEY="ctx7sk-xxxxxxxxxxxx"' >> ~/.bashrc
source ~/.bashrc
```

## 🔐 安全威胁防护

### 1. **配置文件泄露防护**

- ❌ **不要** 将 API Key 提交到版本控制系统
- ✅ **建议** 使用 `.gitignore` 排除敏感文件
- ✅ **建议** 在项目文档中说明配置要求

### 2. **环境变量安全**

- ❌ **不要** 在公共日志中打印环境变量
- ✅ **建议** 使用生产环境专用的环境变量
- ✅ **建议** 定期轮换 API Key

### 3. **文件权限管理**

- ❌ **不要** 设置过于宽松的文件权限
- ✅ **建议** 定期检查文件权限设置
- ✅ **建议** 使用文件系统加密（可选）

## 📝 配置文件模板

### `.gitignore` 配置

```
# Context7 配置文件
.claude/context7.json
.claude/.context7/
.claude/.context7/api-key

# Context7 数据目录
skills/context7-document-server/data/
.skills/context7-document-server/cache/
skills/context7-document-server/logs/
```

### Docker 环境配置示例

```dockerfile
# Dockerfile
FROM python:3.9

# 创建用户目录
RUN mkdir -p /app/.claude/.context7

# 复制配置模板（可选）
COPY context7.json.template /app/.claude/context7.json.template
COPY api-key.template /app/.claude/.context7/api-key.template

# 设置权限
RUN chmod 600 /app/.claude/.context7/api-key.template
RUN chmod 600 /app/.claude/context7.json.template

# 运行时需要挂载实际的配置文件
VOLUME ["/app/.claude/.context7"]
```

### Kubernetes ConfigMap 示例

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: context7-config
data:
  context7.json: |
    {
      "server_endpoint": "https://api.context7.ai/v1",
      "timeout": 30000,
      "max_results": 10,
      "cache_enabled": true
    }
---
apiVersion: v1
kind: Secret
metadata:
  name: context7-secrets
type: Opaque
data:
  api-key: Y3R4c2stLTUyMWE3NzY3ODgtNjk4OC00MDAwNzljNzA2NmU3 <base64编码>
```

## 🎯 总结

Context7 的安全配置方案具有以下特点：

### ✅ 优势
1. **多层配置策略** - 环境变量 > 用户配置 > 专用文件
2. **权限严格控制** - 敏感文件仅所有者可访问
3. **配置文件分离** - 避免在插件中硬编码密钥
4. **环境变量支持** - 支持临时和持久化配置
5. **自动配置加载** - 智能解析和优先级处理

### 🔧 实施要点
1. **移除插件中硬编码的 API Key**
2. **确保用户目录配置文件正确**
3. **设置适当的文件权限**
4. **定期安全验证**

### 🚀 使用效果
- **提升安全性** - 敏感信息不再硬编码
- **增强灵活性** - 支持多种配置方式
- **简化管理** - 统一的配置管理方案
- **降低风险** - 减少密钥泄露可能性

通过这样的安全配置方案，Context7 在保证功能完整性的同时，显著提升了配置的安全性和灵活性。