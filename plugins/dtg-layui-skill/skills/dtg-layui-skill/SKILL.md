---
name: dtg-layui-skill
description: This skill should be used when the user asks to "create enterprise admin page", "build data table with API", "design payment system UI", "implement reconciliation page", "add data statistics dashboard", "integrate admin.req API", "create CRUD operations", or similar LayuiAdmin enterprise-level frontend development tasks. Provides enterprise-level code generation templates based on 716+ real project HTML files analysis, including API integration, permission control, data visualization, and payment system patterns.
version: 3.0.0
---

# dtg-layui-skill

企业级 LayuiAdmin 代码生成助手，基于 716+ 个实际支付系统项目 HTML 文件分析，帮助快速构建企业级 LayuiAdmin 应用。

## 关于 Layui

Layui 是一款采用自身模块规范编写的经典模块化前端 UI 框架，遵循原生 HTML/CSS/JS 的书写与组织形式，门槛极低，拿来即用。外在极简，却又不失饱满的内在，体积轻盈，组件丰盈。

## 关于 LayuiAdmin

LayuiAdmin 是基于 Layui 框架的企业级后台管理模板，提供单页面应用（SPA）架构、完善的路由系统、模块化开发支持和内置权限控制。

## 核心能力

### 1. 快速生成页面结构

- 基础 HTML 页面模板
- 后台管理布局（头部/侧边栏/主体/底部）
- 响应式栅格布局系统

### 2. 表单组件生成

- 输入框、下拉框、复选框、单选框
- 开关按钮、文本域
- 表单验证规则配置
- 表单事件监听

### 3. 数据表格生成

- 静态表格与数据表格
- 分页、排序、筛选功能
- CRUD 操作模板
- 工具栏与行操作

### 4. 交互组件生成

- 弹层（alert/confirm/msg/tips）
- 日期时间选择器
- 文件上传组件
- 导航菜单、选项卡、折叠面板

### 5. 其他组件

- 轮播图、树形结构
- 评分、进度条、徽章
- 代码修饰器、流加载

### 6. LayuiAdmin 企业级支持

- LayuiAdmin 后台管理页面模板
- 订单管理页面（复杂搜索、数据统计、导出功能）
- 配置管理页面（权限控制、状态切换）
- 对账管理页面（简洁布局、数据表格）
- 数据统计仪表板（ECharts 图表、轮播组件）
- ECharts 数据可视化集成
- 企业级工具函数库

## 触发短语

### 企业级页面模板（基于 716+ 实际项目）

| 触发短语 | 功能模块 |
|----------|----------|
| "create enterprise list page", "admin list page" | 企业级列表页面 |
| "create detail page", "view page" | 详情页面模板 |
| "create edit page", "update form" | 编辑页面模板 |
| "data summary card", "statistics card" | 数据统计卡片 |
| "batch operation", "bulk action" | 批量操作工具栏 |
| "admin.req API", "API integration" | API 集成模板 |

### 标准 Layui 模块

| 触发短语 | 功能模块 |
|----------|----------|
| "create a form", "layui form" | 表单模块 |
| "build a table", "data table" | 表格模块 |
| "admin layout", "backend layout" | 布局系统 |
| "date picker", "time selector" | 日期选择器 |
| "modal dialog", "popup layer" | 弹层组件 |
| "file upload", "image upload" | 上传组件 |
| "navigation menu", "nav bar" | 导航组件 |

### LayuiAdmin 企业级模块

| 触发短语 | 功能模块 |
|----------|----------|
| "create admin page", "layuiadmin page" | LayuiAdmin 后台页面 |
| "order management page", "order list", "trade page" | 订单管理页面 |
| "config management page", "payment config" | 配置管理页面 |
| "reconciliation page", "bill check page" | 对账管理页面 |
| "data dashboard", "statistics dashboard" | 数据统计仪表板 |
| "echarts chart", "data visualization" | ECharts 图表 |
| "permission control", "auth check" | 权限控制 |

## 17 个核心模块速查

| 模块 | 说明 | 文档 |
|------|------|------|
| layer | 弹层组件 | `references/06-layer-module.md` |
| form | 表单组件 | `references/04-form-module.md` |
| table | 数据表格 | `references/05-table-module.md` |
| laydate | 日期选择器 | `references/09-other-components.md` |
| element | 常用元素 | `references/09-other-components.md` |
| upload | 文件上传 | `references/09-other-components.md` |
| laypage | 分页组件 | `references/09-other-components.md` |
| tree | 树形结构 | `references/08-data-components.md` |
| carousel | 轮播图 | `references/08-data-components.md` |
| flow | 流加载 | `references/08-data-components.md` |
| rate | 评分组件 | `references/09-other-components.md` |
| layedit | 富文本编辑器 | `references/09-other-components.md` |
| code | 代码修饰器 | `references/09-other-components.md` |
| util | 工具函数 | `references/10-api-reference.md` |
| laytpl | 模板引擎 | `references/10-api-reference.md` |

## 使用方式

当用户请求创建企业级 LayuiAdmin 功能时：

1. **分析具体需求**
   - 页面类型（列表/详情/编辑）
   - API 集成需求
   - 功能要求（搜索、统计、导出、权限等）

2. **选择合适模板**
   - `assets/templates/enterprise-list-page.html` - 企业级列表页面
   - `assets/templates/enterprise-detail-page.html` - 详情页面模板
   - `assets/templates/enterprise-edit-page.html` - 编辑页面模板
   - `assets/templates/api-integration-template.html` - API 集成模板
   - `assets/templates/data-summary-card.html` - 数据统计卡片

3. **查询详细文档**
   - 从 `references/` 获取完整 API 文档
   - 查看 API 集成指南和权限控制文档
   - 参考实际项目最佳实践

4. **生成完整代码**
   - 基于 Layui 2.3.0 规范
   - 包含标准 admin.req API 调用
   - 支持完整的 CRUD 操作

5. **提供使用说明**
   - 配置步骤
   - API 接口规范
   - 注意事项

## 代码生成工作流程

```
用户需求 → 匹配模块 → 选择模板 → 查询文档 → 生成代码 → 使用说明
```

## 相关文件

### 模板文件 (assets/templates/)

#### 企业级页面模板（基于 716+ 实际项目）

| 文件 | 用途 |
|------|------|
| enterprise-list-page.html | 企业级列表页面（导航、搜索、统计、表格） |
| enterprise-detail-page.html | 详情页面模板（表单展示、只读字段） |
| enterprise-edit-page.html | 编辑页面模板（表单验证、API 提交） |
| enterprise-search-form.html | 标准搜索表单 |
| api-integration-template.html | API 集成模板（admin.req 模式） |
| data-summary-card.html | 数据统计卡片组件 |
| batch-operation-toolbar.html | 批量操作工具栏 |

#### LayuiAdmin 企业级模板

| 文件 | 用途 |
|------|------|
| admin-layout.html | LayuiAdmin 标准后台布局 |
| layui-admin-page.html | LayuiAdmin 后台管理页面 |
| layui-order-page.html | 订单管理页面（含搜索、统计、导出） |
| layui-config-page.html | 配置管理页面（含权限控制） |
| layui-reconciliation-page.html | 对账管理页面 |
| layui-dashboard.html | 数据统计仪表板（含 ECharts） |

### 参考文档 (references/)

#### 标准 Layui 文档

| 文件 | 内容 |
|------|------|
| 01-getting-started.md | 快速入门指南 |
| 02-module-overview.md | 模块总览与分类 |
| 03-layout-system.md | 布局系统详解 |
| 04-form-module.md | 表单模块详解 |
| 05-table-module.md | 表格模块详解 |
| 06-layer-module.md | 弹层模块详解 |
| 07-navigation.md | 导航组件详解 |
| 08-data-components.md | 数据展示组件 |
| 09-other-components.md | 其他组件详解 |
| 10-api-reference.md | API 速查手册 |
| 11-best-practices.md | 最佳实践 |
| 12-troubleshooting.md | 常见问题解答 |

#### LayuiAdmin 企业级文档

| 文件 | 内容 |
|------|------|
| 13-layuiadmin-guide.md | LayuiAdmin 开发指南 |
| 14-echarts-integration.md | ECharts 集成指南 |
| 15-enterprise-table.md | 企业级表格开发 |
| 16-payment-system-patterns.md | 支付系统页面模式 |
| 17-utility-functions.md | 工具函数库 |

#### 企业级开发文档（新增）

| 文件 | 内容 |
|------|------|
| 18-api-integration-guide.md | API 集成完整指南 |
| 22-permission-system.md | 权限控制系统 |
| 23-data-visualization.md | 数据可视化组件 |
| 24-performance-optimization.md | 性能优化建议 |
| 25-security-best-practices.md | 安全最佳实践 |

### 示例代码 (examples/)

#### 企业级页面示例（基于 716+ 实际项目）

| 目录 | 内容 |
|------|------|
| enterprise-order-management/ | 企业级订单管理完整示例 |
| payment-config-management/ | 支付配置管理示例 |
| reconciliation-management/ | 对账管理示例 |
| user-management/ | 用户管理示例 |

#### LayuiAdmin 企业级示例

| 目录 | 内容 |
|------|------|
| admin-dashboard/ | 企业级仪表板示例 |
| order-management/ | 订单管理完整示例 |
| payment-config/ | 支付配置完整示例 |
| dashboard/ | 数据统计仪表板完整示例 |

## 快速开始

### 模块化方式（推荐）

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Layui 示例</title>
  <link rel="stylesheet" href="./layui/css/layui.css">
</head>
<body>
  <!-- 页面内容 -->

  <script src="./layui/layui.js"></script>
  <script>
  layui.use(['layer', 'form'], function(){
    var layer = layui.layer;
    var form = layui.form;

    layer.msg('Hello World');
  });
  </script>
</body>
</html>
```

### 非模块化方式

```html
<script src="./layui/layui.all.js"></script>
<script>
var layer = layui.layer;
layer.msg('Hello World');
</script>
```

## 注意事项

1. 确保正确引入 Layui 的 CSS 和 JS 文件
2. 数据接口返回格式需符合 Layui 规范
3. 动态插入的表单元素需要重新渲染：`form.render()`
4. 表格数据格式：`{code: 0, msg: "", count: 100, data: []}`
5. 注意模块依赖关系（如 table 依赖 laytpl、laypage、layer、form）

## 最佳实践

- 按需加载模块，避免一次性加载所有模块
- 使用事件委托处理动态元素事件
- 为表格设置合理的高度和每页数量
- 合理使用弹层的 zIndex 层级管理
- 使用响应式类名实现移动端适配
