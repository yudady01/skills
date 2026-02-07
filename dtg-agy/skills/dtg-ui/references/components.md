# 高频组件模板 (Component Library)

## 目录

- [日期范围选择器](#日期范围选择器-daterange)
- [图片上传](#图片上传-image-upload)
- [富文本编辑器](#富文本编辑器-rich-text)
- [数据表格](#数据表格-layui-table)
- [弹窗组件](#弹窗组件-layeropen)
- [表单验证规则](#表单验证规则-lay-verify)
- [动态下拉选择器](#动态下拉选择器)
- [批量操作](#批量操作)

---

## 日期范围选择器 (DateRange)

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

---

## 图片上传 (Image Upload)

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

---

## 富文本编辑器 (Rich Text)

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

## 数据表格 (layui-table)

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

---

## 弹窗组件 (layer.open)

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

---

## 表单验证规则 (lay-verify)

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

---

## 动态下拉选择器

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

---

## 批量操作

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
