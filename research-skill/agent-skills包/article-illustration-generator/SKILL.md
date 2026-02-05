---
name: "article-illustration-generator"
description: "为文章生成插图"
---

# 文章插图生成器

此技能使用 Gemini 图像 API 自动为文本文章生成相关插图，并将其转换为视觉美观的 HTML 文件。

## 工作流程

1.  **API 密钥检查**：
    *   首先，检查是否设置了 GOOGLE_API_KEY 环境变量。
    *   如果未设置，使用 AskUserQuestion 工具询问用户是否已配置其 API 密钥。
    *   如果用户尚未配置，请他们提供 Google API 密钥。
    *   存储 API 密钥供脚本执行使用。

2.  **输入分析**：
    *   阅读用户的文章文本。
    *   将文本拆分为逻辑部分（段落）。
    *   识别插图的关键场景（目标是每 2-3 段生成 1 张图片）。

3.  **图像生成**：
    *   对于每个识别的场景，基于文本上下文生成描述性提示。
    *   使用 `google.genai` SDK 生成图像。
    *   **模型**：`gemini-2.5-flash-image`（默认或用户指定）。
    *   **配置**：对文章图像使用 `aspect_ratio="16:9"` 或 `4:3`。

4.  **HTML 构建**：
    *   使用 `assets/template.html` 中提供的 HTML 模板（"故都的秋"风格）。
    *   将文本和生成的图像（本地保存）插入到 HTML 结构中。

## 资源

此技能在 `references/` 目录中包含参考文件：

*   **`references/template.html`**：带有衬线字体和简洁布局的 HTML/CSS 模板。将此作为输出文件的基础。
*   **`references/api_guide.md`**：Nano Banana Pro（Gemini 3 Pro Image）API 的详细文档，可用于高级图像生成需求。
*   **`references/script_template.py`**：包含 API 调用逻辑的 Python 脚本模板。

## 使用指南

当被调用时，代理应该：
1.  **检查 API 密钥配置**：
    *   使用 Bash 检查是否设置了 GOOGLE_API_KEY 环境变量：`echo $GOOGLE_API_KEY`（Linux/Mac）或 `echo %GOOGLE_API_KEY%`（Windows）。
    *   如果为空或未设置，使用 AskUserQuestion 询问："您是否已经配置了 Google API Key？"
        *   选项 1："是，已配置为环境变量" - 继续执行脚本。
        *   选项 2："否，我需要提供 API Key" - 询问 API 密钥并将其作为命令行参数传递给脚本。
    *   如果用户提供了 API 密钥，为此执行临时存储它。

2.  阅读用户提供的目标文章。
3.  计划图像插入点。
4.  使用适当的参数执行 Python 脚本（`scripts/article_to_html.py`）：
    *   如果用户提供了 API 密钥：`python scripts/article_to_html.py <article_file> <api_key>`
    *   如果使用环境变量：`python scripts/article_to_html.py <article_file>`
    *   可选参数：`--images N`、`--model MODEL`、`--ratio RATIO`、`--size SIZE`
5.  验证结果并通知用户输出位置。
