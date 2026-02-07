---
name: dtg-ui
description: dtg-pay 项目 UI 开发助手。支持 Layui 页面生成、组件模板、i18n 国际化自动处理（含翻译文件更新）、CSS 修复、代码重构。适用 xxpay-manage xxpay-merchant xxpay-agent 模块。
---

# DTG UI & i18n 综合助理 (多模块增强版)

本技能为 dtg-pay 项目（`manage`, `agent`, `merchant` 模块）提供标准化 UI 开发指导和 i18n 处理能力。

## 🚀 Quick Reference

| 指令 | 用途 | 示例 |
|------|------|------|
| `/generate-page [type]` | 生成页面骨架 | `/generate-page list` |
| `/generate-table [api]` | 生成数据表格 | `/generate-table /api/mch/list` |
| `/generate-form [fields]` | 生成表单 | `/generate-form name,email,phone` |
| `/add-i18n [path]` | **添加国际化(含JSON更新)** | `/add-i18n ./edit.html` |
| `/extract-i18n [path]` | 提取并同步翻译 | `/extract-i18n ./mch_add.html` |
| `/scan-hardcoded [path]` | 扫描硬编码中文 | `/scan-hardcoded ./views/` |
| `/fix-alignment` | 注入 CSS 对齐修复 | - |
| `/refactor-ui [code]` | 提供重构方案 | - |
| `/validate-i18n [path]` | 检查翻译完整性 | `/validate-i18n ./views/` |
| `/sync-skins` | 同步所有皮肤翻译 | - |

---

## 目标模块路径

在处理任务前，请先确认所属模块及其对应的资源路径：

- **xxpay-manage**: `/xxpay-manage/src/main/resources/static/x_mgr/src/views/`
- **xxpay-agent**: `/xxpay-agent/src/main/resources/static/[skin]/x_agent/src/views/`
- **xxpay-merchant**: `/xxpay-merchant/src/main/resources/static/[skin]/x_mch/src/views/`

*注：[skin] 通常包含 ezpay, 724pay, lupay 等品牌，修改 UI 时应注意是否需要跨皮肤同步。*

## 核心任务

1. **UI 布局生成与重构**：复刻 Layui 特定风格的页面结构和样式微调。
2. **i18n 自动化处理**：从视图中提取键值并同步更新所有皮肤的翻译文件。
3. **标准化 JS 注入**：自动包含权限校验、数据请求和渲染逻辑。

---

## 模式 1：UI 布局规范 (Standard Layouts)

### 1.1 页面标准结构

所有二级页面应遵循以下层次：

```html
<div class="layui-card layadmin-header">
    <div class="layui-breadcrumb" lay-filter="breadcrumb">
        <a lay-href="" i18ndata="common:home">主页</a>
        <a><cite i18ndata="module:feature.title">功能标题</cite></a>
    </div>
</div>

<div class="layui-fluid">
    <div class="layui-card">
        <div class="layui-tab layui-tab-brief">
            <ul class="layui-tab-title">
                <li class="layui-this" i18ndata="module:feature.tab">选项卡名称</li>
            </ul>
            <div class="layui-tab-content">
                <!-- 内容区域 -->
            </div>
        </div>
    </div>
</div>
```

### 1.2 搜索区域 (Right-aligned Search)

列表页面的搜索表单通常右浮动：

```html
<div class="layui-row">
    <div class="layui-form" style="float:right; margin-bottom: 10px;">
        <div class="layui-form-item" style="margin:0;">
            <div class="layui-input-inline">
                <input type="text" name="key" placeholder="占位符" class="layui-input">
            </div>
            <button id="search" class="layui-btn" data-type="reload" i18ndata="common:search">搜索</button>
        </div>
    </div>
</div>
```

### 1.3 样式修正习惯 (CSS Overrides)

在 `layui-form-pane`（方框模式）中，必须包含以下样式覆盖以确保对齐：

```html
<style>
    .layui-form-label {
        width: 15% !important; /* 或固定宽度如 120px */
        margin-left: 1%;
    }
    .layui-input-inline {
        width: 33% !important; /* 确保一行多列时的平衡 */
    }
</style>
<form class="layui-form layui-form-pane">
    <!-- Form items... -->
</form>
```

### 1.4 高频组件模板

👉 **详细组件代码参见** [components.md](references/components.md)

包含：日期选择器、图片上传、富文本、数据表格、弹窗、表单验证、下拉选择器、批量操作等。

---

## 模式 2：i18n 自动化处理 (i18n Processor)

> ⚠️ **强制要求**：处理国际化时，**必须同时更新翻译文件**，不得只修改 HTML/JS 而不更新 JSON。

### 2.1 翻译文件路径

**xxpay-manage** 翻译文件位置：
```
/xxpay-manage/src/main/resources/static/x_mgr/start/json/language/
├── zh/
│   ├── agent.json      # 代理商模块
│   ├── merchant.json   # 商户模块
│   ├── common.json     # 通用翻译
│   └── ...
└── en/
    ├── agent.json
    ├── merchant.json
    ├── common.json
    └── ...
```

**xxpay-merchant** 翻译文件位置（多皮肤）：
```
/xxpay-merchant/src/main/resources/static/[skin]/x_mch/start/json/language/
├── ezpay/x_mch/start/json/language/{zh,en}/
├── 724pay/x_mch/start/json/language/{zh,en}/
└── lupay/x_mch/start/json/language/{zh,en}/
```

> 📌 **注意**：`xxpay-agent` 模块不需要国际化处理。

### 2.2 处理模式

技能在扫描 HTML/JS 时会自动识别以下两种模式：
1. **HTML 属性**：`i18ndata="module:key.name"`
2. **JS 函数**：`translateMessageByPath("module:key.name", "默认中文")`

### 2.3 完整工作流程 (必须全部执行)

1. **扫描确认**：检查目标文件中的硬编码中文
2. **添加 i18n 属性**：为 HTML 元素添加 `i18ndata` 属性
3. **添加 JS 翻译**：为 JS 消息添加 `translateMessageByPath()` 调用
4. **添加初始化**：在 `<script>` 开头添加 `initializeI18n(['module1', 'module2'])`
5. **更新动态内容**：在 `table.render` 或动态生成内容后调用 `updateI18nfortable()`
6. **❗ 更新中文 JSON**：在 `zh/` 目录下的对应文件中添加所有新键
7. **❗ 更新英文 JSON**：在 `en/` 目录下的对应文件中添加所有新键（英文翻译）

### 2.4 键命名规范

- 嵌套结构：`module:feature.sub_feature.property`
- 常用前缀：`merchant:`, `agent:`, `common:`, `order:`
- 通用键（存放在 common.json）：`save`, `back`, `saveSuccess`, `saveFailed`, `search`, `export`

### 2.5 翻译文件格式示例

```json
// agent.json
{
  "rate": {
    "edit": {
      "home": "首页",
      "agentManagement": "代理商管理",
      "updateAgentRate": "修改代理商费率",
      "basicInfo": "基本信息"
    }
  }
}
```

对应的 i18n 键：`agent:rate.edit.home`, `agent:rate.edit.agentManagement` 等

---

## 模式 3：参考模板

👉 **详细模板参见** [templates.md](references/templates.md)

包含：统计汇总块、详情展示模式等。

---

## 模式 4：UI 重构与组件化

👉 **详细重构策略参见** [refactoring.md](references/refactoring.md)

包含：三级重构策略（Low/Medium/High Coupling）、组件开发规范等。

---

## 指令集 (Commands)

### 核心指令
- **/extract-i18n [path]**: 扫描指定文件并生成翻译更新请求。**必须同时更新 zh/ 和 en/ 下的 JSON 文件。**
- **/scan-hardcoded [path]**: 扫描指定路径下未国际化的硬编码中文。
- **/generate-page [type]**: 生成指定类型的页面骨架（list, add, view），**包含 i18n 支持和对应 JSON 更新**。
- **/fix-alignment**: 自动注入针对 Layui Form Pane 的 CSS 宽度修复代码。
- **/refactor-ui [code_block]**: 分析提供的代码块，识别重复模式并提供三级重构方案。

### 生成指令
- **/generate-table [api_path]**: 根据 API 路径生成完整的数据表格代码。
- **/generate-form [field1,field2,...]**: 根据字段列表生成表单 HTML。

### 验证与同步指令
- **/validate-i18n [path]**: 双向检查 i18n 键完整性，找出缺失的翻译或未使用的键。
- **/sync-skins**: 同步所有皮肤目录的翻译文件，确保 ezpay/724pay/lupay 一致。
- **/add-i18n [path]**: 为指定文件添加国际化支持，**强制同时更新 HTML/JS + zh/JSON + en/JSON**。

---

## 辅助工具与参考资源

| 类型 | 路径 |
|------|------|
| 提取脚本 | `scripts/extract-i18n.py` |
| 扫描脚本 | `scripts/scan-hardcoded.py` |
| 更新脚本 | `scripts/update-translations.py` |
| 常用翻译 | [common-translations.md](references/common-translations.md) |
| Layui 速查 | [layui-cheatsheet.md](references/layui-cheatsheet.md) |
| CSS 修复集 | [css-fixes.md](references/css-fixes.md) |
| JS API 模式 | [js-api-patterns.md](references/js-api-patterns.md) |
| 组件模板 | [components.md](references/components.md) |
| 参考模板 | [templates.md](references/templates.md) |
| 重构策略 | [refactoring.md](references/refactoring.md) |
