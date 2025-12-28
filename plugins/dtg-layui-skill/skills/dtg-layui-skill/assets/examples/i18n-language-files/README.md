# 国际化 (i18n) 支持更新说明

## 版本更新

- **版本**: 3.1.0
- **更新日期**: 2025-12-28
- **更新内容**: 添加完整的国际化 (i18n) 支持

## 新增文件

### 文档
- `references/26-i18n-guide.md` - 国际化完整指南

### 模板
- `assets/templates/i18n-page-template.html` - 带 i18n 的完整页面模板
- `assets/templates/enterprise-list-page-with-i18n.html` - 带 i18n 的企业列表页模板

### 语言文件示例
- `assets/examples/i18n-language-files/en/module.json` - 英文模块翻译示例
- `assets/examples/i18n-language-files/en/common.json` - 英文通用翻译示例
- `assets/examples/i18n-language-files/zh/module.json` - 中文模块翻译示例
- `assets/examples/i18n-language-files/zh/common.json` - 中文通用翻译示例

## 国际化功能概述

### 核心函数

1. **initializeI18n(modules)** - 初始化国际化系统
```javascript
initializeI18n(['merchant', 'common', 'index', 'layout']);
```

2. **translateMessageByPath(path, defaultMsg)** - 获取翻译文本
```javascript
var title = translateMessageByPath("merchant:list.mch_view.basic", "基本信息");
```

3. **updateI18nfortable()** - 更新页面 i18ndata 元素
```javascript
updateI18nfortable();
```

### HTML 使用方式

使用 `i18ndata` 属性标记需要翻译的元素：

```html
<!-- 文本翻译 -->
<label i18ndata="merchant:list.mch_view.merID">商户ID</label>

<!-- 按钮翻译 -->
<button class="layui-btn" i18ndata="merchant:button.save">保存</button>

<!-- 表格标题 -->
{field: 'name', title: '<span i18ndata="merchant:table.name">名称</span>'}
```

### JavaScript 使用方式

```javascript
// 弹窗提示
layer.confirm(
    translateMessageByPath("merchant:prompt.deleteConfirm", '确定要删除吗？'),
    {icon: 3, title: translateMessageByPath("common:prompt.warning", '提示')},
    function(index) {
        // 确认操作
    }
);

// 动态属性
$('input[name="status"][value="1"]').attr('title',
    translateMessageByPath("merchant:status.enabled", "启用")
);
```

## 语言文件结构

```
x_mgr/start/json/language/
├── en/                    # 英文
│   ├── merchant.json
│   ├── common.json
│   └── ...
└── zh/                    # 中文
    ├── merchant.json
    ├── common.json
    └── ...
```

## 快速开始

### 1. 创建语言文件

在 `start/json/language/` 目录下创建对应语言的 JSON 文件。

### 2. 在页面中初始化

```html
<script>
initializeI18n(['yourModule', 'common']);
layui.use(['admin', 'form'], function () {
    // 代码...
});
</script>
```

### 3. 添加 i18ndata 属性

```html
<label i18ndata="yourModule:page.fieldName">字段名</label>
```

### 4. 数据加载后更新

```javascript
table.render({
    // ...
    done: function(res) {
        setTimeout(updateI18nfortable, 100);
    }
});
```

## 触发短语

| 触发短语 | 功能 |
|----------|------|
| "add i18n" | 添加国际化支持 |
| "internationalization" | 国际化 |
| "multi-language" | 多语言 |
| "i18ndata attribute" | HTML 翻译属性 |
| "translateMessageByPath" | JS 翻译函数 |
| "language file" | 语言文件配置 |

## 文档参考

详细文档请查看: `references/26-i18n-guide.md`
