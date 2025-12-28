# dtg-layui-skill

> Layui 2.3.0 + LayuiAdmin 企业级代码生成助手 - Claude Code 插件

一个强大的 Claude Code 技能插件，专门用于快速生成 Layui 2.3.0 和 LayuiAdmin 前端代码。提供完整的组件模板、API 参考文档和企业级示例代码，帮助开发者高效构建现代化的 Web 界面。

## 功能特性

### 标准 Layui 支持

#### 页面结构生成
- 基础 HTML 页面模板
- 后台管理布局（头部/侧边栏/主体/底部）
- 响应式栅格布局系统

#### 表单组件
- 输入框、下拉框、复选框、单选框
- 开关按钮、文本域
- 表单验证规则配置
- 表单事件监听

#### 数据表格
- 静态表格与数据表格
- 分页、排序、筛选功能
- CRUD 操作模板
- 工具栏与行操作

#### 交互组件
- 弹层（alert/confirm/msg/tips）
- 日期时间选择器
- 文件上传组件
- 导航菜单、选项卡、折叠面板

### LayuiAdmin 企业级支持

#### 企业级页面模板
- **后台管理页面**: 标准的 LayuiAdmin 页面布局
- **订单管理页面**: 复杂搜索、数据统计、导出功能
- **配置管理页面**: 权限控制、状态切换、表单验证
- **对账管理页面**: 简洁布局、数据表格
- **数据统计仪表板**: ECharts 图表、轮播组件、实时数据

#### 数据可视化
- ECharts 图表集成（折线图、饼图、柱状图）
- 轮播数据展示
- 实时数据更新
- 响应式图表

#### 企业功能
- 权限控制系统
- 数据导出功能
- 工具函数库
- 并发请求优化

## 使用方法

当使用 Claude Code 时，可以通过以下短语触发此技能：

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
| "order management page", "order list" | 订单管理页面 |
| "config management page", "payment config" | 配置管理页面 |
| "reconciliation page" | 对账管理页面 |
| "data dashboard", "statistics dashboard" | 数据统计仪表板 |
| "echarts chart", "data visualization" | ECharts 图表 |

## 目录结构

```
dtg-layui-skill/
├── .claude-plugin/
│   └── marketplace.json        # 插件配置
├── skills/
│   └── dtg-layui-skill/
│       ├── SKILL.md            # 技能定义
│       ├── assets/
│       │   └── templates/      # HTML 模板
│       │       ├── [标准 Layui 模板...]
│       │       ├── layui-admin-page.html       # LayuiAdmin 后台页面
│       │       ├── layui-order-page.html        # 订单管理页面
│       │       ├── layui-config-page.html       # 配置管理页面
│       │       ├── layui-reconciliation-page.html # 对账管理页面
│       │       └── layui-dashboard.html         # 数据统计仪表板
│       ├── examples/
│       │   ├── simple-page/                    # 简单页面示例
│       │   ├── admin-dashboard/                # 后台仪表板示例
│       │   ├── order-management/               # 订单管理示例
│       │   ├── payment-config/                 # 支付配置示例
│       │   └── dashboard/                      # 数据统计示例
│       └── references/         # API 参考文档
│           ├── [标准 Layui 文档 01-12...]
│           ├── 13-layuiadmin-guide.md          # LayuiAdmin 开发指南
│           ├── 14-echarts-integration.md       # ECharts 集成指南
│           ├── 15-enterprise-table.md          # 企业级表格开发
│           ├── 16-payment-system-patterns.md   # 支付系统页面模式
│           └── 17-utility-functions.md         # 工具函数库
└── README.md                   # 本文件
```

## 支持的 Layui 模块

| 模块 | 说明 |
|------|------|
| layer | 弹层组件 |
| form | 表单组件 |
| table | 数据表格 |
| laydate | 日期选择器 |
| element | 常用元素 |
| upload | 文件上传 |
| laypage | 分页组件 |
| tree | 树形结构 |
| carousel | 轮播图 |
| flow | 流加载 |
| rate | 评分组件 |
| layedit | 富文本编辑器 |

## 新增功能 (v2.0.0)

### LayuiAdmin 支持
- LayuiAdmin 后台管理页面模板
- 企业级页面开发模式
- 路由系统和权限控制

### ECharts 集成
- ECharts 图表模板
- 轮播图组件集成
- 数据可视化最佳实践

### 企业级示例
- 订单管理完整示例
- 支付配置完整示例
- 数据统计仪表板完整示例

## 代码示例

### 标准 Layui 模块化方式

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

### LayuiAdmin 数据统计仪表板

```html
<div class="layui-fluid">
  <!-- 数据概览轮播 -->
  <div class="layui-carousel layadmin-carousel">
    <div carousel-item>
      <ul class="layui-row layui-col-space10" id="dataCards">
        <li class="layui-col-xs6 layui-col-sm3">
          <div class="layadmin-backlog-body">
            <h3>今日订单</h3>
            <p><cite id="todayOrderCount">0</cite></p>
          </div>
        </li>
      </ul>
    </div>
  </div>

  <!-- ECharts 图表 -->
  <div id="trendChart" style="height: 300px;"></div>
</div>

<script>
layui.use(['admin', 'carousel', 'echarts'], function(){
  var echarts = layui.echarts;
  var myChart = echarts.init(document.getElementById('trendChart'), layui.echartsTheme);
  myChart.setOption({
    title: {text: '交易趋势'},
    xAxis: {type: 'category', data: ['Mon', 'Tue', 'Wed']},
    yAxis: {type: 'value'},
    series: [{type: 'line', data: [120, 200, 150]}]
  });
});
</script>
```

## 注意事项

1. 确保正确引入 Layui 的 CSS 和 JS 文件
2. 数据接口返回格式需符合 Layui 规范
3. 动态插入的表单元素需要重新渲染：`form.render()`
4. 表格数据格式：`{code: 0, msg: "", count: 100, data: []}`
5. 注意模块依赖关系（如 table 依赖 laytpl、laypage、layer、form）
6. LayuiAdmin 需要正确配置 config.js 和路由系统
7. ECharts 需要在 config.js 中配置扩展模块

## 版本历史

### v2.0.0 (2025-12-28)
- 新增 LayuiAdmin 企业级支持
- 新增 5 个 LayuiAdmin 页面模板
- 新增 3 个企业级完整示例
- 新增 5 个企业级参考文档
- 新增 ECharts 集成指南
- 新增工具函数库

### v1.0.0
- 初始版本
- 标准 Layui 2.3.0 支持
- 基础模板和文档

## 版本

- **当前版本**: 2.0.0
- **Layui 版本**: 2.3.0
- **作者**: tommy

## 许可证

MIT License
