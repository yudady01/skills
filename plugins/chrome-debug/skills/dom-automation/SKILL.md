---
name: dom-automation
description: This skill should be used when the user asks to "automate login", "fill forms", "click buttons", "select elements", "take screenshots", "wait for elements", or needs to perform DOM manipulation and page automation. Provides comprehensive guidance for web page automation using Chrome DevTools.
version: 1.0.0
---

# DOM Automation Skill

This skill provides comprehensive guidance for automating web page interactions, DOM manipulation, and user interface testing using Chrome DevTools MCP integration.

## Core Automation Patterns

### Element Selection Strategies

Use robust selector strategies for reliable element identification:

#### Priority Order (Most Reliable to Least)
1. **ID Selectors**: `#username`, `#login-button`
2. **Test IDs**: `[data-testid="login-form"]`, `[data-cy="submit"]`
3. **Semantic Classes**: `.btn-primary`, `.form-input`
4. **Attribute Selectors**: `[name="password"]`, `[type="submit"]`
5. **CSS Combinations**: `.container .btn:first-child`
6. **XPath**: `//button[contains(text(), "Submit")]`

```javascript
// Example: Robust element selection
const selectors = [
  '#login-button',           // Primary ID
  '[data-testid="login"]',   // Test ID fallback
  '.btn[type="submit"]',     // Semantic class
  'button[type="submit"]'    // Generic fallback
];
```

### Wait Strategies

Implement proper waiting to handle dynamic content:

#### Wait Types
- **Wait for Load**: Page completely loaded
- **Wait for Element**: Specific element appears
- **Wait for Visible**: Element becomes visible
- **Wait for Clickable**: Element can be clicked
- **Wait for Text**: Element contains specific text

```javascript
// Example: Wait patterns
await mcp.call("wait_for_load");                    // Page load
await mcp.call("wait_for_selector", {               // Element appears
  selector: ".dashboard",
  timeout: 10000
});
await mcp.call("wait_for_text", {                   // Text appears
  selector: ".status",
  text: "Success"
});
```

## Form Automation

### Login Automation Pattern

Complete login workflow with error handling:

```javascript
// Automated login function
async function performLogin(mcp, config) {
  try {
    // Navigate to login page
    await mcp.call("navigate", { url: config.target_url });

    // Wait for login form
    await mcp.call("wait_for_selector", {
      selector: "#username, [name='username'], input[type='text']",
      timeout: 5000
    });

    // Fill username field
    await mcp.call("type", {
      selector: "#username, [name='username']",
      text: config.username
    });

    // Fill password field
    await mcp.call("type", {
      selector: "#password, [name='password']",
      text: config.password
    });

    // Submit form (try multiple selectors)
    const submitSelectors = [
      "#login-button",
      "#submit",
      ".btn-primary",
      "button[type='submit']"
    ];

    for (const selector of submitSelectors) {
      try {
        await mcp.call("click", { selector });
        break; // Success, exit loop
      } catch (e) {
        continue; // Try next selector
      }
    }

    // Wait for successful login
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

### Form Data Patterns

Handle various form input types:

```javascript
// Form filling strategies
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

// Generic form filler
async function fillForm(mcp, formData) {
  for (const [selector, value] of Object.entries(formData)) {
    const inputType = await mcp.call("get_element_type", { selector });
    const action = formActions[inputType];

    if (action) {
      await action(selector, value);
    } else {
      throw new Error(`Unsupported input type: ${inputType}`);
    }
  }
}
```

## Interactive Actions

### Click and Navigation

Handle various click scenarios:

```javascript
// Click strategies
async function smartClick(mcp, selector) {
  // Wait for element to be clickable
  await mcp.call("wait_for_clickable", { selector });

  // Get element position for debugging
  const position = await mcp.call("get_element_position", { selector });

  // Scroll element into view if needed
  if (position.y > window.innerHeight) {
    await mcp.call("scroll_to", { selector });
  }

  // Perform click
  await mcp.call("click", { selector });

  // Wait for any navigation
  await mcp.call("wait_for_navigation_or_timeout", { timeout: 3000 });
}
```

### Keyboard Actions

Handle keyboard interactions:

```javascript
// Keyboard automation
const keyboardActions = {
  tab: () => mcp.call("press_key", { key: "Tab" }),
  enter: () => mcp.call("press_key", { key: "Enter" }),
  escape: () => mcp.call("press_key", { key: "Escape" }),
  arrowDown: () => mcp.call("press_key", { key: "ArrowDown" }),
  ctrlA: () => mcp.call("hotkey", { keys: ["Ctrl", "A"] })
};

// Example: Form navigation with keyboard
async function navigateFormWithKeyboard(mcp) {
  await keyboardActions.tab(); // Move to next field
  await mcp.call("type", { text: "username" });
  await keyboardActions.tab(); // Move to password field
  await mcp.call("type", { text: "password" });
  await keyboardActions.enter(); // Submit form
}
```

## Visual Debugging

### Screenshot Strategies

Capture screenshots for debugging:

```javascript
// Comprehensive screenshot capture
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

### Element Inspection

Inspect DOM elements for debugging:

```javascript
// Element debugging information
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

## Error Handling and Recovery

### Robust Error Handling

Implement comprehensive error handling:

```javascript
// Retry mechanism with exponential backoff
async function retryOperation(operation, maxRetries = 3, baseDelay = 1000) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      return await operation();
    } catch (error) {
      if (attempt === maxRetries) {
        throw error;
      }

      const delay = baseDelay * Math.pow(2, attempt - 1);
      console.log(`Attempt ${attempt} failed, retrying in ${delay}ms...`);
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }
}

// Usage example
await retryOperation(() => mcp.call("click", { selector: "#button" }));
```

### State Validation

Verify page state before and after actions:

```javascript
// State validation
async function validatePageState(mcp, expectedState) {
  const actualState = {
    url: await mcp.call("get_current_url"),
    title: await mcp.call("get_page_title"),
    elements: {}
  };

  // Check expected elements
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

## Performance Considerations

### Efficient Automation

Optimize automation scripts for performance:

```javascript
// Batch operations for better performance
async function batchOperations(mcp, operations) {
  const results = [];

  // Group similar operations
  const clicks = operations.filter(op => op.type === 'click');
  const types = operations.filter(op => op.type === 'type');

  // Execute batched operations
  for (const click of clicks) {
    await mcp.call("click", { selector: click.selector });
  }

  for (const type of types) {
    await mcp.call("type", { selector: type.selector, text: type.text });
  }

  return results;
}

// Parallel waits when possible
async function parallelWaits(mcp, selectors) {
  const waitPromises = selectors.map(selector =>
    mcp.call("wait_for_selector", { selector, timeout: 5000 })
  );

  return Promise.allSettled(waitPromises);
}
```

## Testing Patterns

### Test Workflow Automation

Create automated test workflows:

```javascript
// Complete test workflow
async function runTestSuite(mcp, tests) {
  const results = [];

  for (const test of tests) {
    console.log(`Running test: ${test.name}`);

    try {
      // Setup
      await mcp.call("navigate", { url: test.setup.url });

      // Execute test steps
      for (const step of test.steps) {
        await executeStep(mcp, step);
      }

      // Validation
      const result = await validateTest(mcp, test.expected);
      results.push({ name: test.name, passed: result.success, details: result });

      // Screenshot on failure
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

## Additional Resources

### Reference Files

For detailed automation patterns and best practices:
- **`references/automation-patterns.md`** - Comprehensive automation patterns
- **`references/selector-strategies.md`** - Element selection best practices
- **`references/error-handling.md`** - Advanced error handling techniques

### Example Scripts

Working automation examples in `examples/`:
- **`examples/login-automation.js`** - Complete login flow with error handling
- **`examples/form-filling.js`** - Various form input automation
- **`examples/dynamic-content.js`** - Handling AJAX and dynamic content
- **`examples/multi-page-workflow.js`** - Complex multi-page automation

### Test Data

Sample test configurations:
- **`examples/test-configs/`** - Test data and configuration files
- **`examples/page-objects/`** - Page object model implementations

## Best Practices

### Reliable Automation
1. **Use explicit waits** instead of fixed delays
2. **Implement retry mechanisms** for flaky operations
3. **Validate element state** before interactions
4. **Use multiple selector strategies** for robustness
5. **Capture screenshots** for debugging failures

### Maintainable Code
1. **Separate test data** from test logic
2. **Use page object model** for complex applications
3. **Implement reusable functions** for common operations
4. **Add comprehensive logging** for debugging
5. **Use descriptive names** for selectors and functions

### Performance Optimization
1. **Batch operations** when possible
2. **Minimize unnecessary waits**
3. **Reuse browser sessions** across tests
4. **Optimize selector queries**
5. **Clean up resources** after each test