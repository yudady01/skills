---
name: dtg-ui
description: 专门用于处理 dtg-pay 项目（xxpay-manage）的 UI 相关任务。包含 Layui 布局规范、CSS 宽度修正习惯、统计汇总块模版、多皮肤 i18n 自动化处理逻辑以及标准的 JS 常规操作（权限、请求、渲染）。
version: 1.0.0
---

# DTG UI & i18n 综合助理 (多模块增强版)

本技能旨在为 dtg-pay 项目（包含 `manage`, `agent`, `merchant` 三个核心模块）提供标准化的 UI 开发指导和国际化 (i18n) 处理能力。

## 目标模块路径
在处理任务前，请先确认所属模块及其对应的资源路径：

- **xxpay-manage**: `/xxpay-manage/src/main/resources/static/x_mgr/src/views/`
- **xxpay-agent**: `/xxpay-agent/src/main/resources/static/[skin]/x_agent/src/views/`
- **xxpay-merchant**: `/xxpay-merchant/src/main/resources/static/[skin]/x_mch/src/views/`

*注：[skin] 通常包含 ezpay, 724pay, lupay 等品牌，修改 UI 时应注意是否需要跨皮肤同步。*

## 核心任务

1.  **UI 布局生成与重构**：复刻 Layui 特定风格的页面结构和样式微调。
2.  **i18n 自动化处理**：从视图中提取键值并同步更新所有皮肤的翻译文件。
3.  **标准化 JS 注入**：自动包含权限校验、数据请求和渲染逻辑。

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

### 1.4 高频组件模板 (Component Library)

#### 1.4.1 日期范围选择器 (DateRange)
标准的搜索栏时间筛选组件：
```html
<div class="layui-input-inline">
    <input type="text" class="layui-input" id="createTimeStart" name="createTimeStart" placeholder="开始时间">
</div>
<div class="layui-input-inline">
    <input type="text" class="layui-input" id="createTimeEnd" name="createTimeEnd" placeholder="结束时间">
</div>
<script>
    layui.use(['laydate'], function(){
        var laydate = layui.laydate;
        laydate.render({ elem: '#createTimeStart', type: 'datetime' });
        laydate.render({ elem: '#createTimeEnd', type: 'datetime' });
    });
</script>
```

#### 1.4.2 图片上传 (Image Upload)
用于商户证件或Logo上传：
```html
<div class="layui-form-item">
    <label class="layui-form-label">证件图片</label>
    <div class="layui-input-inline">
        <input type="hidden" name="imgUrl" id="imgUrl">
        <img class="layui-upload-img" id="imgPreview" style="width: 150px;">
        <button type="button" class="layui-btn" id="btnUpload">上传图片</button>
    </div>
</div>
<script>
    layui.use('upload', function(){
        var upload = layui.upload;
        upload.render({
            elem: '#btnUpload',
            url: layui.setter.baseUrl + '/upload/image',
            headers: {access_token: layui.data(layui.setter.tableName).access_token},
            done: function(res){
                if(res.code === 0){
                    $('#imgPreview').attr('src', res.data.src);
                    $('#imgUrl').val(res.data.src);
                }
            }
        });
    });
</script>
```

#### 1.4.3 富文本编辑器 (Rich Text)
```html
<textarea id="content" name="content" style="display: none;"></textarea>
<script>
    layui.use('layedit', function(){
        var layedit = layui.layedit;
        layedit.set({
            uploadImage: { url: layui.setter.baseUrl + '/upload/image', type: 'post' }
        });
        var index = layedit.build('content'); // build editor
    });
</script>
```

---

## 模式 2：i18n 自动化处理 (i18n Processor)

### 2.1 处理模式
技能在扫描 HTML/JS 时会自动识别以下两种模式：
1.  **HTML 属性**：`i18ndata="module:key.name"`
2.  **JS 函数**：`translateMessageByPath("module:key.name", "默认中文")`

### 2.2 工作流程
1.  **提取**：扫描目标文件，识别所有 `i18ndata` 键。
2.  **对比**：检查各皮肤（ezpay, 724pay, lupay, x_mch）的 `translation.json`。
3.  **生成**：提示 Agent 使用 Python 脚本或直接执行 JSON 更新。
4.  **同步**：确保所有皮肤文件同步受更。

### 2.3 键命名规范
- 嵌套结构：`module:feature.sub_feature.property`
- 常用前缀：`merchant:`, `agent:`, `common:`, `order:`

---

## 模式 3：参考模板 (Reference Templates)

### 3.1 统计汇总块 (Summary Block)
用于订单或资金流水列表的顶部汇总：
```html
<div class="layui-form-item" id="summaryBlock" style="display: none">
    <blockquote class="layui-elem-quote">
        提交笔数:<span id="totalCount" style="color: blue; margin-right: 10px;"></span>
        总金额:<span id="totalAmount" style="color: green; margin-right: 10px;"></span>
    </blockquote>
</div>
```

### 3.2 详情展示模式 (Read-only Detail)
使用 `disabled` 状态的输入框和 `layui-form-pane` 进行结构化展示。

---

## 指令集 (Commands)

- **/extract-i18n [path]**: 扫描指定文件并生成翻译更新请求。脚本会自动复用现有翻译记忆 (Shared TMs)。
- **/scan-hardcoded [path]**: 扫描指定路径下未国际化的硬编码中文。
- **/generate-page [type]**: 生成指定类型的页面骨架（list, add, view）。
- **/fix-alignment**: 自动注入针对 Layui Form Pane 的 CSS 宽度修复代码。

---

## 辅助工具位置

- 提取脚本：`.agent/skills/dtg-ui/scripts/extract-i18n.py`
- 扫描脚本：`.agent/skills/dtg-ui/scripts/scan-hardcoded.py`
- 更新脚本：`.agent/skills/dtg-ui/scripts/update-translations.py`
- 翻译参考：`.agent/skills/dtg-ui/references/common-translations.md`
