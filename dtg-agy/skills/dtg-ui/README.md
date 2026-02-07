# DTG UI & i18n Skill 使用说明

## 概述
`dtg-ui` 是一个专门为 `dtg-pay` 项目定制的 AI 开发助手技能。它结合了项目特有的 Layui UI 规范与多皮肤国际化 (i18n) 处理流程。

## 适用模块

| 模块 | 路径 | 国际化 |
|------|------|--------|
| **xxpay-manage** | `/xxpay-manage/.../x_mgr/` | ✅ 需要 |
| **xxpay-merchant** | `/xxpay-merchant/.../[skin]/x_mch/` | ✅ 需要 |
| **xxpay-agent** | `/xxpay-agent/.../[skin]/x_agent/` | ❌ 不需要 |

## 核心功能

### 1. UI 标准化
- **Layui 深度适配**：自动处理 `layui-fluid`, `layui-card`, `layui-tab` 的标准嵌套
- **样式修正自动注入**：针对 `layui-form-pane` 模式下标签宽度问题，自动提供 CSS 修复
- **布局模板**：列表页、新增页、查看页的完整骨架模板

### 2. i18n 自动化流程
> ⚠️ **强制要求**：处理国际化时，**必须同时更新翻译文件**

- **提取与同步**：自动从 HTML 的 `i18ndata` 和 JS 的 `translateMessageByPath` 中提取翻译键
- **翻译文件路径**：
  - `xxpay-manage`: `.../x_mgr/start/json/language/{zh,en}/`
  - `xxpay-merchant`: `.../[skin]/x_mch/start/json/language/{zh,en}/` (ezpay/724pay/lupay)
- **多皮肤一致性**：一键同步更新所有皮肤目录的翻译文件

### 3. 组件模板
- 数据表格 (`layui-table`)
- 弹窗组件 (`layer.open`)
- 表单验证 (`lay-verify`)
- 动态下拉选择器
- 批量操作

## Quick Reference

| 指令 | 用途 |
|------|------|
| `/generate-page [type]` | 生成页面骨架 (list/add/view) |
| `/generate-table [api]` | 生成数据表格代码 |
| `/generate-form [fields]` | 生成表单 HTML |
| `/add-i18n [path]` | **添加国际化 (含 JSON 更新)** |
| `/extract-i18n [path]` | 提取并同步翻译 |
| `/scan-hardcoded [path]` | 扫描硬编码中文 |
| `/validate-i18n [path]` | 检查翻译完整性 |
| `/sync-skins` | 同步所有皮肤翻译 |
| `/fix-alignment` | 注入 CSS 对齐修复 |
| `/refactor-ui [code]` | 提供重构方案 |

## 目录结构
```
dtg-ui/
├── SKILL.md                    # 核心技能定义
├── README.md                   # 本说明文件
├── scripts/
│   ├── extract-i18n.py         # i18n 提取脚本
│   ├── scan-hardcoded.py       # 硬编码扫描脚本
│   └── update-translations.py  # 翻译批量更新脚本
├── references/
│   ├── common-translations.md  # 常用词库
│   ├── layui-cheatsheet.md     # Layui API 速查
│   ├── css-fixes.md            # CSS 常见问题修复
│   └── js-api-patterns.md      # API 调用模式
└── examples/
    ├── list-page-example.html  # 列表页示例
    ├── add-page-example.html   # 新增页示例
    ├── view-page-example.html  # 查看页示例
    └── common-js-patterns.js   # 通用 JS 模式
```

## 如何使用
1. **开发新页面**：`/generate-page list` 生成标准骨架
2. **添加国际化**：`/add-i18n ./edit.html` 自动处理 HTML/JS + JSON 翻译文件
3. **修复样式**：`/fix-alignment` 注入 CSS 对齐修复
4. **验证翻译**：`/validate-i18n ./views/` 检查翻译完整性

## 维护建议
当项目的 UI 库或皮肤目录发生变化时，请同步更新 `SKILL.md` 中的路径定义。
