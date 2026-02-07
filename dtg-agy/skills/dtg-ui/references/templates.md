# 参考模板 (Reference Templates)

## 目录

- [统计汇总块](#统计汇总块-summary-block)
- [详情展示模式](#详情展示模式-read-only-detail)

---

## 统计汇总块 (Summary Block)

用于订单或资金流水列表的顶部汇总：

```html
<div class="layui-form-item" id="summaryBlock" style="display: none">
    <blockquote class="layui-elem-quote">
        提交笔数:<span id="totalCount" style="color: blue; margin-right: 10px;"></span>
        总金额:<span id="totalAmount" style="color: green; margin-right: 10px;"></span>
    </blockquote>
</div>
```

---

## 详情展示模式 (Read-only Detail)

使用 `disabled` 状态的输入框和 `layui-form-pane` 进行结构化展示：

```html
<form class="layui-form layui-form-pane">
    <div class="layui-form-item">
        <label class="layui-form-label">商户名称</label>
        <div class="layui-input-block">
            <input type="text" class="layui-input" value="示例商户" disabled>
        </div>
    </div>
    <div class="layui-form-item">
        <label class="layui-form-label">状态</label>
        <div class="layui-input-block">
            <input type="text" class="layui-input" value="正常" disabled>
        </div>
    </div>
</form>
```
