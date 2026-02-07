# Layui 常用 API 速查表

快速查找 Layui 常用组件和方法。

## 模块加载

```javascript
layui.use(['table', 'form', 'layer', 'laydate', 'upload'], function(){
    var table = layui.table;
    var form = layui.form;
    var layer = layui.layer;
    var laydate = layui.laydate;
    var upload = layui.upload;
});
```

---

## Table 数据表格

### 基础渲染
```javascript
table.render({
    elem: '#dataTable',
    url: '/api/list',
    page: true,
    limit: 10,
    cols: [[
        { type: 'checkbox' },
        { field: 'id', title: 'ID', width: 80, sort: true },
        { field: 'name', title: '名称', minWidth: 150 },
        { title: '操作', toolbar: '#actionBar', fixed: 'right' }
    ]]
});
```

### 表格重载
```javascript
table.reload('dataTable', {
    where: { keyword: 'xxx' },
    page: { curr: 1 }
});
```

### 获取选中行
```javascript
var checkStatus = table.checkStatus('dataTable');
var data = checkStatus.data;  // 选中的数据数组
```

### 行事件监听
```javascript
table.on('tool(dataTable)', function(obj){
    var data = obj.data;
    if(obj.event === 'edit') { /* 编辑 */ }
    if(obj.event === 'del') { /* 删除 */ }
});
```

---

## Form 表单

### 表单渲染
```javascript
form.render();           // 渲染所有
form.render('select');   // 只渲染下拉
form.render('checkbox'); // 只渲染复选框
```

### 表单提交
```javascript
form.on('submit(submitBtn)', function(data){
    console.log(data.field);  // 表单数据
    return false;  // 阻止默认提交
});
```

### 选择事件
```javascript
form.on('select(filterName)', function(data){
    console.log(data.value);  // 选中值
    console.log(data.elem);   // select 元素
});
```

### 自定义验证
```javascript
form.verify({
    customRule: function(value, item){
        if(value.length < 5){
            return '最少5个字符';
        }
    }
});
```

---

## Layer 弹窗

### 普通信息框
```javascript
layer.msg('操作成功');
layer.msg('操作成功', { icon: 1 });  // 带图标
layer.msg('错误', { icon: 2 });
```

### 确认框
```javascript
layer.confirm('确定删除？', { icon: 3, title: '提示' }, function(index){
    // 确定回调
    layer.close(index);
});
```

### iframe 弹窗
```javascript
layer.open({
    type: 2,
    title: '标题',
    area: ['800px', '600px'],
    content: 'page.html',
    end: function() { /* 关闭回调 */ }
});
```

### 内容层弹窗
```javascript
layer.open({
    type: 1,
    title: '标题',
    area: ['500px', 'auto'],
    content: '<div>内容</div>'
});
```

### 加载层
```javascript
var loadIndex = layer.load();
// 请求完成后
layer.close(loadIndex);
// 或
layer.closeAll('loading');
```

### 获取父页面
```javascript
// 子页面中
var index = parent.layer.getFrameIndex(window.name);
parent.layer.close(index);

// 刷新父页面表格
parent.layui.table.reload('dataTable');
```

---

## Laydate 日期

### 基础日期选择
```javascript
laydate.render({
    elem: '#date',
    type: 'date'  // date|datetime|year|month|time
});
```

### 日期范围
```javascript
laydate.render({
    elem: '#dateRange',
    type: 'datetime',
    range: true
});
```

### 限制范围
```javascript
laydate.render({
    elem: '#date',
    min: '2020-01-01',
    max: 0  // 0 表示今天
});
```

---

## Upload 上传

### 图片上传
```javascript
upload.render({
    elem: '#btnUpload',
    url: '/upload/image',
    accept: 'images',  // file|images|video|audio
    done: function(res){
        if(res.code === 0){
            $('#preview').attr('src', res.data.src);
            $('#imgUrl').val(res.data.src);
        }
    },
    error: function(){
        layer.msg('上传失败');
    }
});
```

### 多文件上传
```javascript
upload.render({
    elem: '#btnUpload',
    url: '/upload/files',
    multiple: true,
    allDone: function(obj){
        console.log(obj.total);      // 总数
        console.log(obj.successful); // 成功数
        console.log(obj.aborted);    // 失败数
    }
});
```

---

## 数据存储

### 设置/获取数据
```javascript
// 设置
layui.data('myTable', { key: 'token', value: 'xxx' });

// 获取
var token = layui.data('myTable').token;

// 删除
layui.data('myTable', { key: 'token', remove: true });
```

### 项目中常用
```javascript
// 获取 token
var token = layui.data(layui.setter.tableName).access_token;

// 获取权限列表
var permissions = layui.data(layui.setter.tableName).permissions;
```

---

## 常用 CSS 类

| 类名 | 说明 |
|------|------|
| `layui-btn` | 按钮 |
| `layui-btn-sm` | 小按钮 |
| `layui-btn-xs` | 超小按钮 |
| `layui-btn-primary` | 原始按钮 |
| `layui-btn-normal` | 百搭按钮 |
| `layui-btn-warm` | 暖色按钮 |
| `layui-btn-danger` | 警告按钮 |
| `layui-badge` | 徽章 |
| `layui-bg-green` | 绿色背景 |
| `layui-bg-orange` | 橙色背景 |
| `layui-bg-red` | 红色背景 |
| `layui-bg-gray` | 灰色背景 |
| `layui-hide` | 隐藏元素 |
| `layui-show` | 显示元素 |

---

## 图标

```html
<i class="layui-icon layui-icon-add-1"></i>    <!-- 添加 -->
<i class="layui-icon layui-icon-edit"></i>     <!-- 编辑 -->
<i class="layui-icon layui-icon-delete"></i>   <!-- 删除 -->
<i class="layui-icon layui-icon-search"></i>   <!-- 搜索 -->
<i class="layui-icon layui-icon-export"></i>   <!-- 导出 -->
<i class="layui-icon layui-icon-refresh"></i>  <!-- 刷新 -->
<i class="layui-icon layui-icon-ok"></i>       <!-- 确定 -->
<i class="layui-icon layui-icon-close"></i>    <!-- 关闭 -->
```

完整图标库: https://layui.dev/docs/2/icon/
