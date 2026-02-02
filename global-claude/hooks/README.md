# 技能评估钩子 (Skill Evaluation Hook)

自动评估用户输入，智能推荐相关技能。

## 功能概述

每次用户输入时，Hook 会自动：
1. 分析用户请求的意图
2. 与白名单中的技能进行匹配
3. 返回最相关的技能供用户选择

## 文件结构

```
global-claude/
├── hooks/
│   ├── hooks.json           # Hook 配置文件
│   └── README.md            # 本文档
└── scripts/
    ├── evaluate_skills.py   # Hook 入口脚本
    └── lib/
        ├── skill_evaluator.py      # 核心评估引擎
        └── whitelist.json          # 白名单配置 ⭐
```

## 快速开始

### 配置白名单

编辑 `scripts/lib/whitelist.json`：

```json
{
  "whitelist": [
    "en2zh",
    "video-downloader",
    "to-mp4"
  ],
  "settings": {
    "confidence_threshold": 0.15,
    "max_results": 3
  }
}
```

### 启用/禁用

- **启用白名单**：在 `whitelist` 中添加技能名
- **评估所有技能**：设为空数组 `"whitelist": []`

## 配置说明

### whitelist.json 参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `whitelist` | 允许评估的技能列表 | 8 个常用技能 |
| `confidence_threshold` | 最低置信度 (0-1) | 0.15 |
| `max_results` | 最多返回几个技能 | 3 |

### 置信度等级

| 图标 | 等级 | 置信度 | 说明 |
|------|------|--------|------|
| 🔥 | 高 | ≥50% | 很确定 |
| ⚡ | 中 | 30-50% | 比较匹配 |
| 💡 | 低 | 15-30% | 可能相关 |

## 所有可用技能

```
en2zh                 # 英中翻译
repeatable-sql        # 可重复执行 SQL
theme-factory         # 主题样式工具
video-downloader      # YouTube 下载
mermaid-visualizer    # Mermaid 图表
excalidraw-diagram    # Excalidraw 图表
create-plan           # 创建计划
markitdown            # 文档转 Markdown
obsidian-canvas-creator  # Obsidian Canvas
agy-impl              # Antigravity 计划实现
excalidraw            # 代码库架构图
json-canvas           # JSON Canvas 文件
obsidian-bases        # Obsidian Bases
obsidian-markdown     # Obsidian Markdown
ob-fm                 # Apple 风格格式化
api-analyzer          # API 分析
to-mp4                # 视频转 MP4
```

## 使用示例

### 单个技能推荐

```
用户: 请帮我翻译这段英文

💡 技能建议: en2zh (置信度 27%)
```

### 多个技能推荐

```
用户: 把这个文档转换

🔍 检测到可能相关的技能:
  1. 🔥 **markitdown** (置信度: 53%)
     将文件和 Office 文档转换为 Markdown
  2. ⚡ **obsidian-markdown** (置信度: 34%)
     创建和编辑 Obsidian Flavored Markdown
```

### 白名单过滤

```
用户: 创建流程图
(如果 mermaid-visualizer 不在白名单中)

→ 无推荐
```

## 工作原理

### Hook 评估流程

```
用户输入
   ↓
1. 读取 stdin JSON
   ↓
2. 加载白名单配置
   ↓
3. 过滤技能（白名单）
   ↓
4. 关键词匹配 (70%)
   ↓
5. 语义相似度 (30%)
   ↓
6. 组合评分
   ↓
7. 过滤低分
   ↓
8. 排序并返回 Top N
   ↓
输出到 stdout (注入 AI 上下文)
```

### 两种匹配模式

#### 模式 1: Hook 匹配

**特征：** 看到技能推荐提示

```
🔍 检测到可能相关的技能:
  1. create-plan (34%)
  2. agy-impl (27%)
  3. json-canvas (26%)
```

**说明：**
- Hook 评估引擎分析用户输入
- 从白名单中匹配合适的技能
- 输出推荐到 AI 上下文中
- AI 基于推荐结果选择技能

**条件：**
- 技能在白名单中
- 评分 ≥ 阈值（默认 0.15）

#### 模式 2: AI 自然匹配

**特征：** 没有技能推荐提示，AI 直接调用技能

```
用户: 创建计划
AI: 我来帮你创建计划...
（直接使用 create-plan 技能）
```

**说明：**
- Hook 没有输出或输出被忽略
- AI 根据自己的理解选择技能
- 可能使用白名单外的技能

**条件：**
- 技能不在白名单中
- 或评分低于阈值
- 或 AI 认为其他技能更合适

### 对比表

| 特征 | Hook 匹配 | AI 自然匹配 |
|------|----------|------------|
| 提示信息 | ✅ 显示推荐 | ❌ 无提示 |
| 技能来源 | 白名单内 | 所有技能 |
| 选择依据 | 算法评分 | AI 理解 |
| 置信度 | 显示百分比 | 不显示 |

### 示例对比

**预设白名单（8 个技能）：**
```
用户: 创建计划
Hook: (无输出，create-plan 不在白名单)
结果: AI 自然匹配调用 create-plan
```

**空白名单：**
```
用户: 创建计划
Hook: create-plan (34%), agy-impl (27%), json-canvas (26%)
结果: AI 基于 Hook 推荐选择
```

## 常见问题

### Q: 如何添加新技能到白名单？

编辑 `scripts/lib/whitelist.json`，在 `whitelist` 数组中添加：

```json
"whitelist": [
  "en2zh",
  "your-new-skill"
]
```

### Q: 如何让所有技能都被评估？

将白名单设为空：

```json
"whitelist": []
```

### Q: 为什么有些请求没有推荐？

可能原因：
1. 匹配的技能不在白名单中
2. 所有技能的评分都低于阈值
3. 请求以 `/` 开头（命令会被跳过）

### Q: 如何调整推荐数量？

修改 `max_results`：

```json
"settings": {
  "max_results": 5
}
```

### Q: 置信度阈值怎么设置？

- `0.10` - 宽松，更多推荐
- `0.15` - 默认，平衡
- `0.25` - 严格，只推荐高匹配

## 性能

| 指标 | 数值 |
|------|------|
| 评估速度 | < 5ms (17 个技能) |
| 内存占用 | < 5MB |
| 支持 | macOS / Linux / Windows |

## 技术实现

- **语言**: Python 3.6+
- **匹配算法**: 关键词匹配 (70%) + 语义相似度 (30%)
- **中文支持**: 双字符短语提取
- **配置格式**: JSON

## 更新日志

- **v1.0** - 初始版本
  - 白名单配置
  - 多技能返回
  - JSON 配置文件
