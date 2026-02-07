---
name: dtg:dtg-ui-refactor
description: 识别重复的 UI 代码并提取为共用组件，提供至少 3 个重构方案
---

# DTG UI Refactor Skill

用户提供一段重复的代码块，识别可提取的共用方法，并提供至少 3 个解决方案。

## 触发条件

- 用户提供重复的 HTML + JavaScript 代码块
- 用户提及 "抽取共用"、"重构"、"提取组件" 等关键词

---

## 工作流程

### 1. 分析阶段

**步骤：**
1. 接收用户提供的代码块
2. 在项目中搜索类似代码（使用 `grep_search`）
3. 统计使用位置数量
4. 识别代码中的差异点（参数、回调、配置等）

**输出：**
- 使用位置清单
- 差异点分析

### 2. 方案生成阶段

**必须提供至少 3 个方案：**

---

#### 方案 A：最小化抽取（Low Coupling）

**封装内容：** 只封装 HTML 模板和 UI 渲染逻辑

**代码示例：**
```javascript
Component.render({
    containerId: 'xxx',
    onSelect: function(value) { /* 调用方自己处理 */ }
});
```

| 优点 | 缺点 |
|------|------|
| ✅ 高度灵活，调用方完全控制业务逻辑 | ❌ 调用方代码仍较多 |
| ✅ 易于测试，组件职责单一 | ❌ 复用程度有限 |
| ✅ 低耦合，不依赖特定后端接口 | |

**代码量减少：** ~30%

**适用场景：** 代码逻辑差异较大，只有模板相同

---

#### 方案 B：中等封装（Medium Coupling）

**封装内容：** HTML 模板 + API 请求（带缓存） + 事件绑定

**代码示例：**
```javascript
Component.init({
    containerId: 'xxx',
    apiPath: '/api/list',
    defaultValue: 'PHP',
    onSelect: function(value) { /* 调用方处理业务 */ }
});
```

| 优点 | 缺点 |
|------|------|
| ✅ 调用方简洁，只需配置和回调 | ❌ 中度耦合，依赖特定 API |
| ✅ API 调用统一，避免重复请求 | ❌ 配置项较多 |
| ✅ 支持缓存，提升性能 | |

**代码量减少：** ~60%

**适用场景：** API 请求相同，业务处理逻辑不同

---

#### 方案 C：完全封装（High Coupling）

**封装内容：** 模板 + API + 完整业务逻辑

**代码示例：**
```javascript
Component.bind({
    containerId: 'xxx',
    tableId: 'tableReload',
    idField: 'mchId',
    idValue: mchId
});
```

| 优点 | 缺点 |
|------|------|
| ✅ 调用极简，一行代码完成 | ❌ 灵活性差，特殊需求需改组件 |
| ✅ 行为统一 | ❌ 高度耦合，依赖特定业务逻辑 |

**代码量减少：** ~80%

**适用场景：** 业务逻辑高度一致，只有参数不同

---

### 3. 决策收集阶段

**必须询问用户以下问题：**

1. **选择封装方案** → A / B / C
2. **是否需要多实例支持** → 同一页面可能有多个组件实例
3. **共享策略** → 单模块放置 / 每模块各放一份
4. **默认参数** → 默认值设定
5. **i18n 处理** → 使用哪个国际化 key

### 4. 执行阶段

1. 创建共用组件文件
2. 重构所有使用位置
3. 复制组件到需要的模块（如果跨模块）
4. 验证功能

---

## 组件命名规范

- 文件名：`{功能名}Util.js`（如 `currencyFilterUtil.js`）
- 模块名：驼峰命名
- 放置于：`src/controller/` 目录

## 组件代码模板

```javascript
layui.define(function (exports) {
    const ComponentName = (() => {
        // 私有变量和函数

        return {
            init: function(options) {
                // 公开 API
            }
        };
    })();

    exports('componentName', { ComponentName });
});
```

---

## 示例：CurrencyFilter 重构

参考已完成的币种过滤器重构：
- 原始代码：12 个页面，每个 ~50 行重复代码
- 采用方案 B
- 最终：1 个共用组件 + 12 个页面各 ~10 行调用代码
- 代码减少：~60%
