# CSS 常见问题修复集

DTG 项目中常见的 CSS 问题及解决方案。

---

## 1. 表单标签对齐问题

### 问题描述
`layui-form-pane` 模式下，标签宽度不一致导致表单错位。

### 解决方案
```css
<style>
    .layui-form-label {
        width: 120px !important;
    }
    .layui-input-inline {
        width: calc(100% - 140px) !important;
    }
    .layui-form-item .layui-input-block {
        margin-left: 140px;
    }
</style>
```

---

## 2. 表格操作列按钮挤压

### 问题描述
操作列按钮过多时换行或被截断。

### 解决方案
```css
/* 方案1: 固定列宽 */
{ title: '操作', width: 200, toolbar: '#actionBar', fixed: 'right' }

/* 方案2: 使用下拉菜单 */
<script type="text/html" id="actionBar">
    <div class="layui-btn-group">
        <a class="layui-btn layui-btn-xs" lay-event="view">查看</a>
        <a class="layui-btn layui-btn-xs layui-btn-primary" lay-event="more">
            更多<i class="layui-icon layui-icon-down"></i>
        </a>
    </div>
</script>
```

---

## 3. 弹窗内容溢出

### 问题描述
iframe 弹窗内容超出可视区域。

### 解决方案
```css
/* 在弹窗页面中 */
body {
    overflow-y: auto;
    padding: 15px;
}

.layui-fluid {
    padding: 0;
}
```

---

## 4. 下拉选择器宽度不一致

### 问题描述
select 渲染后宽度与 input 不一致。

### 解决方案
```css
.layui-form-select {
    width: 100%;
}
.layui-form-select .layui-input {
    width: 100%;
}
```

---

## 5. 日期选择器被遮挡

### 问题描述
弹窗内的日期选择器被遮挡。

### 解决方案
```javascript
laydate.render({
    elem: '#date',
    type: 'datetime',
    trigger: 'click',  // 改为 click 触发
    zIndex: 99999999   // 提高层级
});
```

---

## 6. 移动端表格适配

### 问题描述
表格在移动端显示不全。

### 解决方案
```css
/* 启用表格横向滚动 */
.layui-table-view {
    overflow-x: auto;
}

/* 或使用媒体查询隐藏非必要列 */
@media screen and (max-width: 768px) {
    .hide-on-mobile {
        display: none !important;
    }
}
```

在 cols 配置中：
```javascript
{ field: 'createTime', title: '创建时间', hide: true }  // 移动端隐藏
```

---

## 7. 必填项标记样式

### 问题描述
需要统一显示必填项红色星号。

### 解决方案
```css
.required {
    color: #ff5722;
    margin-right: 3px;
}
```

```html
<label class="layui-form-label">
    <span class="required">*</span>商户名称
</label>
```

---

## 8. 按钮组间距

### 问题描述
按钮组内按钮间距过大或无间距。

### 解决方案
```css
/* 按钮间距 */
.layui-btn + .layui-btn {
    margin-left: 10px;
}

/* 或使用按钮组 */
.layui-btn-group .layui-btn {
    margin: 0;
}
```

---

## 9. 只读输入框样式

### 问题描述
disabled 输入框样式不明显。

### 解决方案
```css
.layui-input[disabled],
.layui-input[readonly] {
    background-color: #f5f5f5;
    color: #666;
    cursor: not-allowed;
}
```

---

## 10. 表格状态标签样式

### 问题描述
需要统一的状态展示样式。

### 解决方案
```html
<script type="text/html" id="statusTpl">
    {{# if(d.status === 1){ }}
        <span class="layui-badge layui-bg-green">启用</span>
    {{# } else if(d.status === 0){ }}
        <span class="layui-badge layui-bg-gray">禁用</span>
    {{# } else if(d.status === 2){ }}
        <span class="layui-badge layui-bg-orange">待审核</span>
    {{# } else if(d.status === 3){ }}
        <span class="layui-badge layui-bg-red">已拒绝</span>
    {{# } }}
</script>
```

---

## 11. 搜索区域右对齐

```css
.search-box {
    float: right;
    margin-bottom: 10px;
}
.search-box .layui-form-item {
    margin: 0;
}
```

---

## 12. 汇总区域样式

```css
.summary-block {
    margin-bottom: 15px;
}
.summary-block .layui-elem-quote {
    padding: 10px 15px;
    border-left-color: #1e9fff;
}
.summary-block span {
    margin-right: 15px;
}
.summary-block .value {
    font-weight: bold;
    color: #1e9fff;
}
```

---

## 13. 卡片阴影效果

```css
.layui-card {
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    transition: box-shadow 0.3s;
}
.layui-card:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
```

---

## 14. 打印样式

```css
@media print {
    .no-print,
    .layui-breadcrumb,
    .layui-btn-group,
    .search-box {
        display: none !important;
    }
    .layui-table {
        font-size: 12px;
    }
}
```
