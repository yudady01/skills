# DTG UI & i18n Skill 使用说明

## 概述
`dtg-ui` 是一个专门为 `xxpay-manage` 项目定制的 AI 开发助手技能。它结合了项目特有的 Layui UI 规范与多皮肤国际化 (i18n) 处理流程。

## 核心功能

### 1. UI 标准化 (多模块支持)
- **多模块适配**：原生支持以下三个核心模块的 UI 开发：
  - **Manage**: `xxpay-manage` (管理后台)
  - **Agent**: `xxpay-agent` (代理商系统)
  - **Merchant**: `xxpay-merchant` (商户系统)
- **Layui 深度适配**：自动处理 `layui-fluid`, `layui-card`, `layui-tab` 的标准嵌套。
- **样式修正自动注入**：针对 `layui-form-pane` 模式下标签宽度不一的问题，自动提供 CSS 修复 (`!important` 覆盖)。
- **布局库**：包含列表页（带右侧搜索）、新增/编辑页（方框风格）、查看页（只读风格）的骨架模板。

### 2. i18n 自动化流程
- **提取与同步**：自动从 HTML 的 `i18ndata` 和 JS 的 `translateMessageByPath` 中提取翻译键。
- **多皮肤一致性**：一键同步更新项目内 `ezpay`, `724pay`, `lupay`, `x_mch` 四个皮肤目录下的 `translation.json`。
- **常用翻译对照**：内置金融/支付行业的常用中英对照表，确保翻译语境专业。

### 3. 业务模板
- **汇总块 (Summary Block)**：快速生成带有 `blockquote` 风格的统计展示区域。
- **权限控制**：自动在 JS 中注入基于 `checkAuth` 的权限检查代码模版。

## 目录结构
```
.agent/skills/dtg-ui/
├── SKILL.md                 # 核心技能定义与 AI 指令
├── README.md                # 本说明文件
├── scripts/
│   ├── extract-i18n.py      # i18n 提取脚本
│   └── update-translations.py # 翻译文件批量更新脚本
├── references/
│   └── common-translations.md # 常用词库
└── examples/                # 输出示例
```

## 如何使用
1. **开发新页面**：直接告知 Agent “使用 dtg-ui 技能生成一个商户列表页”，Agent 将应用标准骨架。
2. **修复样式**：如果页面对齐有问题，可以使用 “使用 dtg-ui 修复表单对齐”。
3. **处理翻译**：完成 UI 开发后，指示 Agent “扫描此文件的 i18n 并更新所有皮肤”。

## 维护建议
当项目的 UI 库（如 Layui 版本升级）或 皮肤目录（增加新品牌）发生变化时，请同步更新 `SKILL.md` 中的路径定义和脚本参数。
