/**
 * DTG 常用 JS 模式示例
 * 包含：权限检查、API 请求封装、表格渲染、表单提交等
 */

// ============================================================
// 1. 权限检查模式
// ============================================================

/**
 * 检查当前用户是否有指定权限
 * @param {string} permCode - 权限代码
 * @returns {boolean}
 */
function checkAuth(permCode) {
    var permissions = layui.data(layui.setter.tableName).permissions || [];
    return permissions.indexOf(permCode) !== -1;
}

/**
 * 根据权限控制按钮显示
 */
function initAuthButtons() {
    // 新增按钮
    if(!checkAuth('merchant:add')) {
        $('#btnAdd').hide();
    }
    // 删除按钮
    if(!checkAuth('merchant:delete')) {
        $('#btnDelete').hide();
    }
    // 编辑按钮（表格内）
    if(!checkAuth('merchant:edit')) {
        $('.btn-edit').hide();
    }
}


// ============================================================
// 2. API 请求封装模式
// ============================================================

/**
 * 封装的 AJAX 请求
 * 自动添加 token 和统一错误处理
 */
var api = {
    /**
     * GET 请求
     */
    get: function(url, params, callback) {
        $.ajax({
            url: layui.setter.baseUrl + url,
            method: 'GET',
            data: params,
            headers: {
                access_token: layui.data(layui.setter.tableName).access_token
            },
            success: function(res) {
                if(res.code === 0) {
                    callback && callback(res.data);
                } else {
                    layer.msg(res.msg || '请求失败');
                }
            },
            error: function() {
                layer.msg('网络错误');
            }
        });
    },

    /**
     * POST 请求
     */
    post: function(url, data, callback) {
        $.ajax({
            url: layui.setter.baseUrl + url,
            method: 'POST',
            data: data,
            headers: {
                access_token: layui.data(layui.setter.tableName).access_token
            },
            success: function(res) {
                if(res.code === 0) {
                    callback && callback(res.data);
                } else {
                    layer.msg(res.msg || '请求失败');
                }
            },
            error: function() {
                layer.msg('网络错误');
            }
        });
    },

    /**
     * POST JSON 请求
     */
    postJson: function(url, data, callback) {
        $.ajax({
            url: layui.setter.baseUrl + url,
            method: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json',
            headers: {
                access_token: layui.data(layui.setter.tableName).access_token
            },
            success: function(res) {
                if(res.code === 0) {
                    callback && callback(res.data);
                } else {
                    layer.msg(res.msg || '请求失败');
                }
            },
            error: function() {
                layer.msg('网络错误');
            }
        });
    }
};

// 使用示例
// api.get('/api/merchant/list', { page: 1 }, function(data) { console.log(data); });
// api.post('/api/merchant/add', { name: 'test' }, function(data) { console.log(data); });


// ============================================================
// 3. 表格渲染模式
// ============================================================

/**
 * 通用表格配置生成器
 */
function createTableConfig(options) {
    return {
        elem: options.elem || '#dataTable',
        url: layui.setter.baseUrl + options.url,
        headers: { access_token: layui.data(layui.setter.tableName).access_token },
        page: options.page !== false,
        limit: options.limit || 10,
        limits: options.limits || [10, 20, 50, 100],
        cols: [options.cols],
        where: options.where || {},
        done: options.done || function() {}
    };
}

// 使用示例
/*
table.render(createTableConfig({
    url: '/api/merchant/list',
    cols: [
        { type: 'checkbox', fixed: 'left' },
        { field: 'id', title: 'ID', width: 80 },
        { field: 'name', title: '名称', minWidth: 150 }
    ]
}));
*/


// ============================================================
// 4. 状态模板函数
// ============================================================

/**
 * 生成状态标签 HTML
 */
function statusBadge(status) {
    var config = {
        1: { text: '启用', color: 'green' },
        0: { text: '禁用', color: 'gray' },
        2: { text: '待审核', color: 'orange' },
        3: { text: '已拒绝', color: 'red' }
    };
    var item = config[status] || { text: '未知', color: 'gray' };
    return '<span class="layui-badge layui-bg-' + item.color + '">' + item.text + '</span>';
}

/**
 * 金额格式化
 */
function formatAmount(amount) {
    if(amount === null || amount === undefined) return '-';
    return parseFloat(amount).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

/**
 * 时间格式化（从时间戳）
 */
function formatTime(timestamp) {
    if(!timestamp) return '-';
    var date = new Date(timestamp);
    return date.getFullYear() + '-' +
           String(date.getMonth() + 1).padStart(2, '0') + '-' +
           String(date.getDate()).padStart(2, '0') + ' ' +
           String(date.getHours()).padStart(2, '0') + ':' +
           String(date.getMinutes()).padStart(2, '0') + ':' +
           String(date.getSeconds()).padStart(2, '0');
}


// ============================================================
// 5. 表单提交模式
// ============================================================

/**
 * 通用表单提交处理
 */
function handleFormSubmit(formData, apiUrl, successCallback) {
    layer.load();
    api.post(apiUrl, formData, function(data) {
        layer.closeAll('loading');
        layer.msg('操作成功', { icon: 1 });
        successCallback && successCallback(data);
    });
}

// 使用示例（在 layui.use 中）
/*
form.on('submit(submitForm)', function(data) {
    handleFormSubmit(data.field, '/api/merchant/add', function() {
        // 关闭弹窗
        var index = parent.layer.getFrameIndex(window.name);
        parent.layer.close(index);
    });
    return false;
});
*/


// ============================================================
// 6. 下拉选项动态加载模式
// ============================================================

/**
 * 加载下拉选项
 */
function loadSelectOptions(selectName, apiUrl, valueField, textField, defaultValue) {
    api.get(apiUrl, {}, function(data) {
        var html = '<option value="">请选择</option>';
        data.forEach(function(item) {
            var selected = (defaultValue && item[valueField] == defaultValue) ? ' selected' : '';
            html += '<option value="' + item[valueField] + '"' + selected + '>' + item[textField] + '</option>';
        });
        $('select[name="' + selectName + '"]').html(html);
        layui.form.render('select');
    });
}

// 使用示例
// loadSelectOptions('agentId', '/api/agent/options', 'id', 'name', currentAgentId);


// ============================================================
// 7. URL 参数获取模式
// ============================================================

/**
 * 获取 URL 参数
 */
function getUrlParam(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    return r ? decodeURIComponent(r[2]) : null;
}

// 使用示例
// var id = getUrlParam('id');


// ============================================================
// 8. 弹窗封装模式
// ============================================================

/**
 * 打开 iframe 弹窗
 */
function openIframe(title, url, width, height, endCallback) {
    layer.open({
        type: 2,
        title: title,
        area: [width || '800px', height || '600px'],
        content: url,
        end: endCallback
    });
}

/**
 * 确认弹窗
 */
function confirmAction(message, callback) {
    layer.confirm(message, { icon: 3, title: '提示' }, function(index) {
        callback && callback();
        layer.close(index);
    });
}

// 使用示例
// openIframe('编辑商户', 'mch_edit.html?id=123', '800px', '600px', function() { table.reload('dataTable'); });
// confirmAction('确定删除？', function() { api.post('/api/delete', { id: 1 }); });
