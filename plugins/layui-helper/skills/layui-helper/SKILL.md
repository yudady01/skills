---
name: layui-helper
description: This skill should be used when the user asks to "create a layui form", "build a data table", "design admin layout", "add date picker", "create modal dialog", "create file upload", "build navigation menu", or similar Layui 2.3.0 frontend development tasks. Provides code generation templates and API reference for Layui framework.
version: 1.0.0
---

# layui-helper

Layui 代码生成助手，帮助快速构建使用 Layui 2.3.0 的网页。

## 关于 Layui

Layui 是一款采用自身模块规范编写的经典模块化前端 UI 框架，遵循原生 HTML/CSS/JS 的书写与组织形式，门槛极低，拿来即用。外在极简，却又不失饱满的内在，体积轻盈，组件丰盈。

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

## 触发短语

| 触发短语 | 功能模块 |
|----------|----------|
| "create a form", "layui form" | 表单模块 |
| "build a table", "data table" | 表格模块 |
| "admin layout", "backend layout" | 布局系统 |
| "date picker", "time selector" | 日期选择器 |
| "modal dialog", "popup layer" | 弹层组件 |
| "file upload", "image upload" | 上传组件 |
| "navigation menu", "nav bar" | 导航组件 |
| "carousel", "slider" | 轮播组件 |
| "tab panel", "accordion" | 选项卡/折叠面板 |
| "tree structure", "tree menu" | 树形组件 |

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

当用户请求创建 Layui 相关功能时：

1. **询问具体需求**
   - 组件类型
   - 样式偏好
   - 功能要求（如分页、验证等）

2. **选择合适模板**
   - `assets/templates/basic-page.html` - 基础页面
   - `assets/templates/admin-layout.html` - 后台布局
   - `assets/templates/form-template.html` - 表单
   - `assets/templates/table-template.html` - 表格
   - `assets/templates/login-page.html` - 登录页

3. **查询详细文档**
   - 从 `references/` 获取完整 API 文档
   - 查看配置选项和参数说明

4. **生成完整代码**
   - 基于 Layui 2.3.0 规范
   - 包含 HTML/CSS/JS
   - 支持模块化和非模块化两种方式

5. **提供使用说明**
   - 配置步骤
   - 数据格式要求
   - 注意事项

## 代码生成工作流程

```
用户需求 → 匹配模块 → 选择模板 → 查询文档 → 生成代码 → 使用说明
```

## 相关文件

### 模板文件 (assets/templates/)

| 文件 | 用途 |
|------|------|
| basic-page.html | 基础 HTML 页面结构 |
| admin-layout.html | 经典后台布局 |
| form-template.html | 表单模板 |
| table-template.html | 数据表格模板 |
| login-page.html | 登录页面模板 |

### 参考文档 (references/)

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

### 示例代码 (examples/)

| 目录 | 内容 |
|------|------|
| simple-page/ | 简单页面示例 |
| admin-dashboard/ | 后台仪表板示例 |

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
