---
name: dom-automation
description: 当用户要求"自动登录"、"填写表单"、"点击按钮"、"选择元素"、"截图"、"等待元素"或需要执行 DOM 操作和页面自动化时使用此技能。提供使用 Chrome DevTools 进行网页自动化的全面指导。
version: 1.0.0
---

# DOM 自动化技能

此技能提供使用 Chrome DevTools MCP 集成进行网页交互自动化、DOM 操作和用户界面测试的全面指导。

## 核心自动化模式

### 元素选择策略

使用健壮的选择器策略进行可靠的元素识别：

#### 优先级顺序（从最可靠到最不可靠）
1. **ID 选择器**：`#username`、`#login-button`
2. **测试 ID**：`[data-testid="login-form"]`、`[data-cy="submit"]`
3. **语义化类名**：`.btn-primary`、`.form-input`
4. **属性选择器**：`[name="password"]`、`[type="submit"]`
5. **CSS 组合器**：`.container .btn:first-child`
6. **XPath**：`//button[contains(text(), "Submit")]`

```javascript
// 示例：健壮的元素选择
const selectors = [
  '#login-button',           // 主要 ID
  '[data-testid="login"]',   // 测试 ID 备用方案
  '.btn[type="submit"]',     // 语义化类名
  'button[type="submit"]'    // 通用备用方案
];
```

### 等待策略

实施适当的等待机制以处理动态内容：

#### 等待类型
- **等待加载**：页面完全加载
- **等待元素**：特定元素出现
- **等待可见**：元素变为可见
- **等待可点击**：元素可以被点击
- **等待文本**：元素包含特定文本

```javascript
// 示例：等待模式
await mcp.call("wait_for_load");                    // 页面加载
await mcp.call("wait_for_selector", {               // 元素出现
  selector: ".dashboard",
  timeout: 10000
});
await mcp.call("wait_for_text", {                   // 文本出现
  selector: ".status",
  text: "Success"
});
```

## 表单自动化

### 登录自动化模式

带错误处理的完整登录工作流：

```javascript
// 自动登录函数
async function performLogin(mcp, config) {
  try {
    // 导航到登录页面
    await mcp.call("navigate", { url: config.target_url });

    // 等待登录表单
    await mcp.call("wait_for_selector", {
      selector: "#username, [name='username'], input[type='text']",
      timeout: 5000
    });

    // 填写用户名字段
    await mcp.call("type", {
      selector: "#username, [name='username']",
      text: config.username
    });

    // 填写密码字段
    await mcp.call("type", {
      selector: "#password, [name='password']",
      text: config.password
    });

    // 提交表单（尝试多个选择器）
    const submitSelectors = [
      "#login-button",
      "#submit",
      ".btn-primary",
      "button[type='submit']"
    ];

    for (const selector of submitSelectors) {
      try {
        await mcp.call("click", { selector });
        break; // 成功，退出循环
      } catch (e) {
        continue; // 尝试下一个选择器
      }
    }

    // 等待登录成功
    await mcp.call("wait_for_selector", {
      selector: ".dashboard, .main-content, [data-testid='dashboard']",
      timeout: 10000
    });

    return { success: true };

  } catch (error) {
    return { success: false, error: error.message };
  }
}
```

### 表单数据模式

处理各种表单输入类型：

```javascript
// 表单填写策略
const formActions = {
  text: (selector, value) => mcp.call("type", { selector, text: value }),
  select: (selector, value) => mcp.call("select", { selector, value }),
  checkbox: (selector, checked) => mcp.call("click", {
    selector,
    state: checked ? "check" : "uncheck"
  }),
  radio: (selector, value) => mcp.call("click", {
    selector: `${selector}[value="${value}"]`
  }),
  file: (selector, filepath) => mcp.call("upload_file", { selector, filepath })
};

// 通用表单填写器
async function fillForm(mcp, formData) {
  for (const [selector, value] of Object.entries(formData)) {
    const inputType = await mcp.call("get_element_type", { selector });
    const action = formActions[inputType];

    if (action) {
      await action(selector, value);
    } else {
      throw new Error(`不支持的输入类型: ${inputType}`);
    }
  }
}
```

## 交互操作

### 点击和导航

处理各种点击场景：

```javascript
// 点击策略
async function smartClick(mcp, selector) {
  // 等待元素可点击
  await mcp.call("wait_for_clickable", { selector });

  // 获取元素位置用于调试
  const position = await mcp.call("get_element_position", { selector });

  // 如需要则滚动元素到视图中
  if (position.y > window.innerHeight) {
    await mcp.call("scroll_to", { selector });
  }

  // 执行点击
  await mcp.call("click", { selector });

  // 等待任何导航
  await mcp.call("wait_for_navigation_or_timeout", { timeout: 3000 });
}
```

### 键盘操作

处理键盘交互：

```javascript
// 键盘自动化
const keyboardActions = {
  tab: () => mcp.call("press_key", { key: "Tab" }),
  enter: () => mcp.call("press_key", { key: "Enter" }),
  escape: () => mcp.call("press_key", { key: "Escape" }),
  arrowDown: () => mcp.call("press_key", { key: "ArrowDown" }),
  ctrlA: () => mcp.call("hotkey", { keys: ["Ctrl", "A"] })
};

// 示例：使用键盘导航表单
async function navigateFormWithKeyboard(mcp) {
  await keyboardActions.tab(); // 移动到下一个字段
  await mcp.call("type", { text: "username" });
  await keyboardActions.tab(); // 移动到密码字段
  await mcp.call("type", { text: "password" });
  await keyboardActions.enter(); // 提交表单
}
```

## 可视化调试

### 截图策略

为调试捕获截图：

```javascript
// 全面的截图捕获
async function captureDebugScreenshots(mcp, testName) {
  const screenshots = {
    fullPage: await mcp.call("take_screenshot", {
      full_page: true,
      filename: `${testName}-full.png`
    }),
    viewport: await mcp.call("take_screenshot", {
      filename: `${testName}-viewport.png`
    }),
    element: await mcp.call("take_element_screenshot", {
      selector: ".error-message",
      filename: `${testName}-error.png`
    })
  };

  return screenshots;
}
```

### 元素检查

检查 DOM 元素进行调试：

```javascript
// 元素调试信息
async function inspectElement(mcp, selector) {
  const info = await mcp.call("inspect_element", { selector });

  return {
    visible: info.visible,
    enabled: info.enabled,
    text: info.textContent,
    attributes: info.attributes,
    position: info.boundingClientRect,
    styles: {
      display: info.computedStyles.display,
      visibility: info.computedStyles.visibility,
      opacity: info.computedStyles.opacity
    }
  };
}
```

## 错误处理和恢复

### 健壮的错误处理

实施全面的错误处理：

```javascript
// 带指数退避的重试机制
async function retryOperation(operation, maxRetries = 3, baseDelay = 1000) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      return await operation();
    } catch (error) {
      if (attempt === maxRetries) {
        throw error;
      }

      const delay = baseDelay * Math.pow(2, attempt - 1);
      console.log(`第 ${attempt} 次尝试失败，${delay}ms 后重试...`);
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }
}

// 使用示例
await retryOperation(() => mcp.call("click", { selector: "#button" }));
```

### 状态验证

在操作前后验证页面状态：

```javascript
// 状态验证
async function validatePageState(mcp, expectedState) {
  const actualState = {
    url: await mcp.call("get_current_url"),
    title: await mcp.call("get_page_title"),
    elements: {}
  };

  // 检查预期元素
  for (const [name, selector] of Object.entries(expectedState.elements)) {
    actualState.elements[name] = {
      exists: await mcp.call("element_exists", { selector }),
      visible: await mcp.call("is_element_visible", { selector }),
      enabled: await mcp.call("is_element_enabled", { selector })
    };
  }

  return actualState;
}
```

## 性能考虑

### 高效自动化

优化自动化脚本的性能：

```javascript
// 批量操作以获得更好的性能
async function batchOperations(mcp, operations) {
  const results = [];

  // 分组相似操作
  const clicks = operations.filter(op => op.type === 'click');
  const types = operations.filter(op => op.type === 'type');

  // 执行批量操作
  for (const click of clicks) {
    await mcp.call("click", { selector: click.selector });
  }

  for (const type of types) {
    await mcp.call("type", { selector: type.selector, text: type.text });
  }

  return results;
}

// 可能时并行等待
async function parallelWaits(mcp, selectors) {
  const waitPromises = selectors.map(selector =>
    mcp.call("wait_for_selector", { selector, timeout: 5000 })
  );

  return Promise.allSettled(waitPromises);
}
```

## 测试模式

### 测试工作流自动化

创建自动化测试工作流：

```javascript
// 完整的测试工作流
async function runTestSuite(mcp, tests) {
  const results = [];

  for (const test of tests) {
    console.log(`运行测试: ${test.name}`);

    try {
      // 设置
      await mcp.call("navigate", { url: test.setup.url });

      // 执行测试步骤
      for (const step of test.steps) {
        await executeStep(mcp, step);
      }

      // 验证
      const result = await validateTest(mcp, test.expected);
      results.push({ name: test.name, passed: result.success, details: result });

      // 失败时截图
      if (!result.success) {
        await mcp.call("take_screenshot", {
          filename: `${test.name}-failure.png`
        });
      }

    } catch (error) {
      results.push({ name: test.name, passed: false, error: error.message });
    }
  }

  return results;
}
```

## 其他资源

### 参考文件

详细的自动化模式和最佳实践：
- **`references/automation-patterns.md`** - 全面的自动化模式
- **`references/selector-strategies.md`** - 元素选择最佳实践
- **`references/error-handling.md`** - 高级错误处理技术

### 示例脚本

`examples/` 中的工作自动化示例：
- **`examples/login-automation.js`** - 带错误处理的完整登录流程
- **`examples/form-filling.js`** - 各种表单输入自动化
- **`examples/dynamic-content.js`** - 处理 AJAX 和动态内容
- **`examples/multi-page-workflow.js`** - 复杂的多页面自动化

### 测试数据

示例测试配置：
- **`examples/test-configs/`** - 测试数据和配置文件
- **`examples/page-objects/`** - 页面对象模型实现

## 最佳实践

### 可靠的自动化
1. **使用显式等待** 而不是固定延迟
2. **实施重试机制** 处理不稳定的操作
3. **验证元素状态** 在交互之前
4. **使用多种选择器策略** 提高健壮性
5. **捕获截图** 用于调试失败

### 可维护的代码
1. **分离测试数据** 和测试逻辑
2. **使用页面对象模型** 处理复杂应用程序
3. **实施可重用函数** 用于常见操作
4. **添加全面日志** 用于调试
5. **使用描述性名称** 为选择器和函数命名

### 性能优化
1. **批量操作** 当可能时
2. **最小化不必要的等待**
3. **重用浏览器会话** 跨测试
4. **优化选择器查询**
5. **清理资源** 每次测试后