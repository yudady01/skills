# UI 重构与组件化 (Refactoring)

当代码出现重复或可以抽象时，请提供以下三级重构策略：

## 目录

- [三级重构策略](#三级重构策略)
  - [方案 A：最小化抽取](#方案-a最小化抽取-low-coupling)
  - [方案 B：中等封装](#方案-b中等封装-medium-coupling---推荐)
  - [方案 C：完全封装](#方案-c完全封装-high-coupling)
- [组件开发规范](#组件开发规范)

---

## 三级重构策略

### 方案 A：最小化抽取 (Low Coupling)

- **封装内容**：只封装 HTML 模板和 UI 渲染逻辑。
- **适用场景**：代码逻辑差异较大，只有模板结构相同。
- **代码示例**：
  ```javascript
  Component.render({
      containerId: 'xxx',
      onSelect: function(value) { /* 调用方自己处理业务 */ }
  });
  ```

---

### 方案 B：中等封装 (Medium Coupling) - *推荐*

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

---

### 方案 C：完全封装 (High Coupling)

- **封装内容**：模板 + API + 完整业务逻辑（自闭环）。
- **适用场景**：业务逻辑高度一致，只有参数不同（如"删除按钮"的逻辑）。
- **代码示例**：
  ```javascript
  Component.bind({
      containerId: 'xxx',
      idValue: mchId
  });
  ```

---

## 组件开发规范

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
