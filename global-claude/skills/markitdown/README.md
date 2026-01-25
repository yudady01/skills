# MarkItDown 技能

此技能提供使用 Microsoft MarkItDown 工具将各种文件格式转换为 Markdown 的全面支持。

## 概述

MarkItDown 是一个将文件和办公文档转换为 Markdown 格式的 Python 工具。此技能包括：

- 完整的 API 文档
- 针对特定格式的转换指南
- 批处理实用脚本
- AI 增强型转换示例
- 与科学工作流的集成

## 内容

### 主技能文件
- **SKILL.md** - 使用 MarkItDown 的完整指南，包含快速入门、示例和最佳实践

### 参考资料
- **api_reference.md** - 详细的 API 文档、类参考和方法签名
- **file_formats.md** - 所有支持文件类型的特定格式详情

### 脚本
- **batch_convert.py** - 支持并行处理的批量文件转换
- **convert_with_ai.py** - 支持自定义提示词的 AI 增强型转换
- **convert_literature.py** - 带元数据提取的科学文献转换

### 资源
- **example_usage.md** - 常见用例的实用示例

## 安装

```bash
# 安装所有功能
pip install 'markitdown[all]'

# 或安装特定功能
pip install 'markitdown[pdf,docx,pptx,xlsx]'
```

## 快速开始

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("document.pdf")
print(result.text_content)
```

## 支持的格式

- **文档**: PDF, DOCX, PPTX, XLSX, EPUB
- **图片**: JPEG, PNG, GIF, WebP (支持 OCR)
- **音频**: WAV, MP3 (支持转录)
- **网页**: HTML, YouTube URL
- **数据**: CSV, JSON, XML
- **压缩包**: ZIP 文件

## 核心功能

### 1. AI 增强型转换
通过 OpenRouter 使用 AI 模型生成详细的图片描述：

```python
from openai import OpenAI

# OpenRouter 提供对 100+ AI 模型的访问
client = OpenAI(
    api_key="your-openrouter-api-key",
    base_url="https://openrouter.ai/api/v1"
)

md = MarkItDown(
    llm_client=client,
    llm_model="anthropic/claude-sonnet-4.5"  # 视觉任务推荐
)
result = md.convert("presentation.pptx")
```

### 2. 批量处理
高效转换多个文件：

```bash
python scripts/batch_convert.py papers/ output/ --extensions .pdf .docx
```

### 3. 科学文献
转换和组织研究论文：

```bash
python scripts/convert_literature.py papers/ output/ --organize-by-year --create-index
```

### 4. Azure 文档智能
使用 Microsoft Document Intelligence 增强 PDF 转换：

```python
md = MarkItDown(docintel_endpoint="https://YOUR-ENDPOINT.cognitiveservices.azure.com/")
result = md.convert("complex_document.pdf")
```

## 使用场景

### 文献综述
将研究论文转换为 Markdown 以便于分析和做笔记。

### 数据提取
将 Excel 文件中的表格提取为 Markdown 格式。

### 演示文稿处理
转换 PowerPoint 幻灯片并生成 AI 描述。

### 文档分析
处理文档供 LLM 使用，使用 token 高效的 Markdown 格式。

### YouTube 字幕
获取并转换 YouTube 视频转录。

## 脚本使用

### 批量转换
```bash
# 转换目录中的所有 PDF
python scripts/batch_convert.py input_dir/ output_dir/ --extensions .pdf

# 递归处理多种格式
python scripts/batch_convert.py docs/ markdown/ --extensions .pdf .docx .pptx -r
```

### AI 增强型转换
```bash
# 通过 OpenRouter 使用 AI 描述进行转换
export OPENROUTER_API_KEY="sk-or-v1-..."
python scripts/convert_with_ai.py paper.pdf output.md --prompt-type scientific

# 使用不同模型
python scripts/convert_with_ai.py image.png output.md --model anthropic/claude-sonnet-4.5

# 使用自定义提示词
python scripts/convert_with_ai.py image.png output.md --custom-prompt "描述此图表"
```

### 文献转换
```bash
# 转换论文并提取元数据
python scripts/convert_literature.py papers/ markdown/ --organize-by-year --create-index
```

## 与 Scientific Writer 集成

此技能与 Scientific Writer CLI 无缝集成，用于：
- 转换论文写作的源材料
- 处理综述文献
- 从各种文档格式提取数据
- 准备文档供 LLM 分析

## 资源

- **MarkItDown GitHub**: https://github.com/microsoft/markitdown
- **PyPI**: https://pypi.org/project/markitdown/
- **OpenRouter**: https://openrouter.ai (AI 模型访问)
- **OpenRouter API 密钥**: https://openrouter.ai/keys
- **OpenRouter 模型**: https://openrouter.ai/models
- **许可证**: MIT

## 系统要求

- Python 3.10+
- 基于所需格式的可选依赖项
- OpenRouter API 密钥（用于 AI 增强型转换）- 在 https://openrouter.ai/keys 获取
- Azure 订阅（可选，用于文档智能）

## 示例

详见 `assets/example_usage.md` 获取全面示例，涵盖：
- 基础转换
- 科学工作流
- AI 增强型处理
- 批量操作
- 错误处理
- 集成模式
