---
name: dtg-ui
description: 专门用于处理 dtg-pay 项目（xxpay-manage）的 UI 相关任务。包含 Layui 布局规范、CSS 宽度修正习惯、统计汇总块模版、多皮肤 i18n 自动化处理逻辑以及标准的 JS 常规操作（权限、请求、渲染）。
version: 1.0.0
---

# DTG UI & i18n 综合助理 (多模块增强版)

本技能旨在为 dtg-pay 项目（包含 `manage`, `agent`, `merchant` 三个核心模块）提供标准化的 UI 开发指导和国际化 (i18n) 处理能力。

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

#### 1.4.4 数据表格 (layui-table)
完整的分页表格配置：
```javascript
layui.use(['table'], function(){
    var table = layui.table;
    
    table.render({
        elem: '#dataTable',
        url: layui.setter.baseUrl + '/api/list',
        headers: { access_token: layui.data(layui.setter.tableName).access_token },
        page: true,
        limit: 10,
        limits: [10, 20, 50, 100],
        cols: [[
            { type: 'checkbox', fixed: 'left' },
            { field: 'id', title: 'ID', width: 80, sort: true },
            { field: 'name', title: '名称', minWidth: 150 },
            { field: 'status', title: '状态', width: 100, templet: '#statusTpl' },
            { field: 'createTime', title: '创建时间', width: 180 },
            { title: '操作', width: 150, toolbar: '#actionBar', fixed: 'right' }
        ]],
        done: function(res, curr, count) {
            // 表格渲染完成回调
        }
    });
    
    // 工具栏事件
    table.on('tool(dataTable)', function(obj){
        var data = obj.data;
        if(obj.event === 'edit') {
            layer.open({ /* 编辑弹窗 */ });
        } else if(obj.event === 'del') {
            layer.confirm('确定删除？', function(index){
                // 调用删除 API
            });
        }
    });
});
```

#### 1.4.5 弹窗组件 (layer.open)
```javascript
// iframe 弹窗（加载子页面）
layer.open({
    type: 2,
    title: '编辑信息',
    area: ['800px', '600px'],
    content: 'edit.html?id=' + id,
    end: function() {
        table.reload('dataTable'); // 关闭后刷新表格
    }
});

// 确认弹窗
layer.confirm('确定执行此操作？', {icon: 3, title: '提示'}, function(index){
    // 确认回调
    layer.close(index);
}, function(){
    // 取消回调
});

// 表单弹窗
layer.open({
    type: 1,
    title: '快速添加',
    area: ['500px', 'auto'],
    content: $('#formTemplate').html(),
    success: function(layero, index) {
        layui.form.render();
    }
});
```

#### 1.4.6 表单验证规则 (lay-verify)
```html
<form class="layui-form">
    <!-- 必填 -->
    <input type="text" name="name" lay-verify="required" placeholder="必填项">
    
    <!-- 手机号 -->
    <input type="text" name="phone" lay-verify="required|phone" placeholder="手机号">
    
    <!-- 邮箱 -->
    <input type="text" name="email" lay-verify="email" placeholder="邮箱">
    
    <!-- 数字 -->
    <input type="text" name="amount" lay-verify="required|number" placeholder="金额">
    
    <!-- 自定义验证 -->
    <input type="text" name="rate" lay-verify="rate" placeholder="费率">
</form>
<script>
layui.use('form', function(){
    var form = layui.form;
    
    // 自定义验证规则
    form.verify({
        rate: function(value){
            if(!/^\d+(\.\d{1,4})?$/.test(value)){
                return '费率格式不正确，最多4位小数';
            }
            if(parseFloat(value) > 100){
                return '费率不能超过100%';
            }
        }
    });
});
</script>
```

#### 1.4.7 动态下拉选择器
从 API 加载选项并绑定事件：
```javascript
layui.use(['form'], function(){
    var form = layui.form;
    
    // 动态加载下拉选项
    $.ajax({
        url: layui.setter.baseUrl + '/api/options',
        headers: { access_token: layui.data(layui.setter.tableName).access_token },
        success: function(res) {
            if(res.code === 0) {
                var html = '<option value="">请选择</option>';
                res.data.forEach(function(item){
                    html += '<option value="' + item.id + '">' + item.name + '</option>';
                });
                $('select[name="category"]').html(html);
                form.render('select'); // 重新渲染
            }
        }
    });
    
    // 选择事件监听
    form.on('select(category)', function(data){
        console.log('选择值：', data.value);
        // 联动逻辑
    });
});
```

#### 1.4.8 批量操作
表格全选 + 批量处理：
```javascript
// 批量删除按钮
$('#batchDelete').on('click', function(){
    var checkStatus = table.checkStatus('dataTable');
    var data = checkStatus.data;
    
    if(data.length === 0) {
        layer.msg('请选择要删除的数据');
        return;
    }
    
    var ids = data.map(function(item){ return item.id; });
    
    layer.confirm('确定删除选中的 ' + ids.length + ' 条数据？', function(index){
        $.ajax({
            url: layui.setter.baseUrl + '/api/batchDelete',
            method: 'POST',
            data: JSON.stringify({ ids: ids }),
            contentType: 'application/json',
            headers: { access_token: layui.data(layui.setter.tableName).access_token },
            success: function(res) {
                if(res.code === 0) {
                    layer.msg('删除成功');
                    table.reload('dataTable');
                }
            }
        });
        layer.close(index);
    });
});
```

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
1.  **HTML 属性**：`i18ndata="module:key.name"`
2.  **JS 函数**：`translateMessageByPath("module:key.name", "默认中文")`

### 2.3 完整工作流程 (必须全部执行)

1.  **扫描确认**：检查目标文件中的硬编码中文
2.  **添加 i18n 属性**：为 HTML 元素添加 `i18ndata` 属性
3.  **添加 JS 翻译**：为 JS 消息添加 `translateMessageByPath()` 调用
4.  **添加初始化**：在 `<script>` 开头添加 `initializeI18n(['module1', 'module2'])`
5.  **更新动态内容**：在 `table.render` 或动态生成内容后调用 `updateI18nfortable()`
6.  **❗ 更新中文 JSON**：在 `zh/` 目录下的对应文件中添加所有新键
7.  **❗ 更新英文 JSON**：在 `en/` 目录下的对应文件中添加所有新键（英文翻译）

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

## 模式 4：UI 重构与组件化 (Refactoring)

当代码出现重复或可以抽象时，请提供以下三级重构策略：

### 4.1 三级重构策略

#### 方案 A：最小化抽取 (Low Coupling)
- **封装内容**：只封装 HTML 模板和 UI 渲染逻辑。
- **适用场景**：代码逻辑差异较大，只有模板结构相同。
- **代码示例**：
  ```javascript
  Component.render({
      containerId: 'xxx',
      onSelect: function(value) { /* 调用方自己处理业务 */ }
  });
  ```

#### 方案 B：中等封装 (Medium Coupling) - *推荐*
- **封装内容**：HTML 模板 + API 请求（带缓存） + 基础事件绑定。
- **适用场景**：API 请求相同，但业务后续处理逻辑不同（如通过 API 获取列表）。
- **代码示例**：
  ```javascript
  Component.init({
      containerId: 'xxx',
      apiPath: '/api/list', // 可选覆盖
      defaultValue: 'PHP',
      onSelect: function(value) { /* 仅处理选择后的回调 */ }
  });
  ```

#### 方案 C：完全封装 (High Coupling)
- **封装内容**：模板 + API + 完整业务逻辑（自闭环）。
- **适用场景**：业务逻辑高度一致，只有参数不同（如“删除按钮”的逻辑）。
- **代码示例**：
  ```javascript
  Component.bind({
      containerId: 'xxx',
      idValue: mchId
  });
  ```

### 4.2 组件开发规范
- **文件位置**：`src/controller/{功能名}Util.js` (如 `currencyFilterUtil.js`)
- **定义模版**：
  ```javascript
  layui.define(function (exports) {
      const ComponentName = (() => {
          // 私有变量
          return {
              init: function(options) { /* 公开 API */ }
          };
      })();
      exports('componentName', { ComponentName });
  });
  ```

---

## 指令集 (Commands)

### 核心指令
- **/extract-i18n [path]**: 扫描指定文件并生成翻译更新请求。**必须同时更新 zh/ 和 en/ 下的 JSON 文件。**
- **/scan-hardcoded [path]**: 扫描指定路径下未国际化的硬编码中文。
- **/generate-page [type]**: 生成指定类型的页面骨架（list, add, view），**包含 i18n 支持和对应 JSON 更新**。
- **/fix-alignment**: 自动注入针对 Layui Form Pane 的 CSS 宽度修复代码。
- **/refactor-ui [code_block]**: 分析提供的代码块，识别重复模式并提供三级重构方案。

### 生成指令
- **/generate-table [api_path]**: 根据 API 路径生成完整的数据表格代码，包含列配置、分页、工具栏事件。
  - 示例：`/generate-table /api/merchant/list`
- **/generate-form [field1,field2,...]**: 根据字段列表生成表单 HTML，自动添加验证规则和布局。
  - 示例：`/generate-form name,email,phone,status`

### 验证与同步指令
- **/validate-i18n [path]**: 双向检查 i18n 键完整性，找出缺失的翻译或未使用的键。
- **/sync-skins**: 同步所有皮肤目录的翻译文件，确保 ezpay/724pay/lupay 一致。
- **/add-i18n [path]**: 为指定文件添加国际化支持，**强制同时更新 HTML/JS + zh/JSON + en/JSON**。

---

## 辅助工具位置

- 提取脚本：`scripts/extract-i18n.py`
- 扫描脚本：`scripts/scan-hardcoded.py`
- 更新脚本：`scripts/update-translations.py`
- 翻译参考：`references/common-translations.md`
- 常用翻译：`references/common-translations.md`
- Layui 速查：`references/layui-cheatsheet.md`
- CSS 修复集：`references/css-fixes.md`
