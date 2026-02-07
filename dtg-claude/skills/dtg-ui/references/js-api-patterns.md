# JS API 调用模式参考

DTG 项目中与后端 API 交互的标准模式。

---

## 1. 基础配置

### API Base URL
```javascript
var baseUrl = layui.setter.baseUrl;  // 如: http://localhost:8080
```

### Token 获取
```javascript
var token = layui.data(layui.setter.tableName).access_token;
```

---

## 2. 标准 AJAX 请求

### GET 请求
```javascript
$.ajax({
    url: layui.setter.baseUrl + '/api/merchant/list',
    method: 'GET',
    data: { page: 1, limit: 10, keyword: 'xxx' },
    headers: {
        access_token: layui.data(layui.setter.tableName).access_token
    },
    success: function(res) {
        if(res.code === 0) {
            console.log(res.data);
        } else {
            layer.msg(res.msg || '请求失败');
        }
    },
    error: function(xhr, status, error) {
        layer.msg('网络错误');
    }
});
```

### POST 请求 (Form Data)
```javascript
$.ajax({
    url: layui.setter.baseUrl + '/api/merchant/add',
    method: 'POST',
    data: {
        name: 'xxx',
        email: 'xxx@example.com'
    },
    headers: {
        access_token: layui.data(layui.setter.tableName).access_token
    },
    success: function(res) {
        if(res.code === 0) {
            layer.msg('添加成功');
        } else {
            layer.msg(res.msg);
        }
    }
});
```

### POST 请求 (JSON Body)
```javascript
$.ajax({
    url: layui.setter.baseUrl + '/api/merchant/batchUpdate',
    method: 'POST',
    data: JSON.stringify({
        ids: [1, 2, 3],
        status: 1
    }),
    contentType: 'application/json',
    headers: {
        access_token: layui.data(layui.setter.tableName).access_token
    },
    success: function(res) {
        // ...
    }
});
```

---

## 3. API 响应格式

### 标准响应结构
```json
{
    "code": 0,
    "msg": "success",
    "data": { ... }
}
```

### 分页响应结构
```json
{
    "code": 0,
    "msg": "success",
    "count": 100,
    "data": [ ... ]
}
```

### 错误码约定
| Code | 说明 |
|------|------|
| 0 | 成功 |
| 1 | 通用错误 |
| 401 | 未登录/Token 过期 |
| 403 | 无权限 |
| 500 | 服务器错误 |

---

## 4. 统一请求封装

### 封装工具
```javascript
var api = {
    request: function(options) {
        var defaults = {
            headers: {
                access_token: layui.data(layui.setter.tableName).access_token
            }
        };
        
        options.url = layui.setter.baseUrl + options.url;
        
        $.ajax($.extend(true, defaults, options, {
            success: function(res) {
                if(res.code === 401) {
                    // Token 过期，跳转登录
                    layer.msg('登录已过期', function(){
                        top.location.href = '/login.html';
                    });
                    return;
                }
                options.success && options.success(res);
            },
            error: function(xhr, status, error) {
                layer.msg('网络错误');
                options.error && options.error(xhr, status, error);
            }
        }));
    },
    
    get: function(url, params, success) {
        this.request({
            url: url,
            method: 'GET',
            data: params,
            success: success
        });
    },
    
    post: function(url, data, success) {
        this.request({
            url: url,
            method: 'POST',
            data: data,
            success: success
        });
    },
    
    postJson: function(url, data, success) {
        this.request({
            url: url,
            method: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: success
        });
    }
};
```

### 使用示例
```javascript
api.get('/api/merchant/detail', { id: 123 }, function(res) {
    if(res.code === 0) {
        // 处理数据
    }
});

api.post('/api/merchant/add', formData, function(res) {
    if(res.code === 0) {
        layer.msg('添加成功');
    }
});
```

---

## 5. Table 表格数据接口

### 接口要求
Table 组件要求接口返回特定格式：
```json
{
    "code": 0,
    "msg": "",
    "count": 100,        // 总数据条数
    "data": [...]        // 当前页数据
}
```

### 请求参数
Table 会自动发送以下参数：
- `page`: 当前页码
- `limit`: 每页条数

### 自定义请求参数
```javascript
table.render({
    elem: '#dataTable',
    url: layui.setter.baseUrl + '/api/list',
    headers: { access_token: token },
    where: {
        keyword: 'xxx',
        status: 1
    },
    request: {
        pageName: 'pageNum',    // 自定义页码参数名
        limitName: 'pageSize'   // 自定义条数参数名
    },
    response: {
        statusCode: 0           // 成功状态码
    }
});
```

---

## 6. 文件上传接口

### 上传接口
```
POST /upload/image
Content-Type: multipart/form-data
Header: access_token

Response:
{
    "code": 0,
    "data": {
        "src": "/upload/images/xxx.jpg"
    }
}
```

### 前端代码
```javascript
upload.render({
    elem: '#btnUpload',
    url: layui.setter.baseUrl + '/upload/image',
    headers: { access_token: token },
    accept: 'images',
    size: 5120,  // KB
    done: function(res) {
        if(res.code === 0) {
            $('#preview').attr('src', res.data.src);
            $('#imgUrl').val(res.data.src);
        } else {
            layer.msg(res.msg);
        }
    }
});
```

---

## 7. 导出接口

### 方式1: 直接下载
```javascript
function exportData() {
    var params = $.param({
        keyword: $('input[name="keyword"]').val(),
        status: $('select[name="status"]').val()
    });
    
    window.open(layui.setter.baseUrl + '/api/export?' + params + '&access_token=' + token);
}
```

### 方式2: 异步请求 + Blob
```javascript
function exportData() {
    layer.load();
    $.ajax({
        url: layui.setter.baseUrl + '/api/export',
        method: 'POST',
        data: { /* 筛选条件 */ },
        headers: { access_token: token },
        xhrFields: { responseType: 'blob' },
        success: function(blob) {
            layer.closeAll('loading');
            var link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'export_' + new Date().getTime() + '.xlsx';
            link.click();
        },
        error: function() {
            layer.closeAll('loading');
            layer.msg('导出失败');
        }
    });
}
```

---

## 8. 错误处理最佳实践

```javascript
function handleApiError(res) {
    switch(res.code) {
        case 401:
            layer.confirm('登录已过期，是否重新登录？', function(){
                top.location.href = '/login.html';
            });
            break;
        case 403:
            layer.msg('您没有权限执行此操作');
            break;
        case 500:
            layer.msg('服务器错误，请稍后重试');
            break;
        default:
            layer.msg(res.msg || '操作失败');
    }
}

// 使用
$.ajax({
    // ...
    success: function(res) {
        if(res.code === 0) {
            // 成功处理
        } else {
            handleApiError(res);
        }
    }
});
```

---

## 9. 常用 API 路径约定

| 操作 | Method | Path |
|------|--------|------|
| 列表 | GET | `/api/{module}/list` |
| 详情 | GET | `/api/{module}/detail?id=xxx` |
| 新增 | POST | `/api/{module}/add` |
| 编辑 | POST | `/api/{module}/update` |
| 删除 | POST | `/api/{module}/delete` |
| 批量删除 | POST | `/api/{module}/batchDelete` |
| 状态更新 | POST | `/api/{module}/updateStatus` |
| 导出 | GET/POST | `/api/{module}/export` |
| 下拉选项 | GET | `/api/{module}/options` |
