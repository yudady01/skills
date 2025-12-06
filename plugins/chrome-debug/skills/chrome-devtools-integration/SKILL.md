---
name: chrome-devtools-integration
description: This skill should be used when the user asks to "configure Chrome DevTools MCP", "set up chrome debugging", "fix chrome connection issues", "install chrome devtools", or mentions Chrome DevTools MCP server configuration. Provides comprehensive guidance for Chrome DevTools Model Context Protocol integration.
version: 1.0.0
---

# Chrome DevTools Integration Skill

This skill provides comprehensive guidance for integrating Chrome DevTools MCP (Model Context Protocol) with Claude Code, enabling powerful browser automation and debugging capabilities.

## Core Concepts

Chrome DevTools MCP is a Model Context Protocol server that allows AI agents to control and inspect live Chrome browsers. It provides programmatic access to Chrome's powerful debugging capabilities through a standardized interface.

### Key Capabilities

- **Performance Analysis**: Record and analyze browser performance traces
- **Network Monitoring**: Inspect HTTP requests, responses, and timing
- **Console Management**: Execute JavaScript and capture console output
- **Visual Debugging**: Take screenshots and page snapshots
- **DOM Manipulation**: Inspect and modify page elements
- **Automation**: Click, type, navigate, and wait for elements

## MCP Server Configuration

### Standard Installation

Install Chrome DevTools MCP globally:

```bash
npm install -g chrome-devtools-mcp@latest
```

### Claude Code Integration

Configure MCP server in `.mcp.json`:

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"],
      "env": {
        "CHROME_PATH": "${CHROME_PATH:-}",
        "HEADLESS": "${HEADLESS:-false}"
      }
    }
  }
}
```

### Environment Variables

Set these environment variables to customize behavior:

- `CHROME_PATH`: Custom Chrome executable path
- `HEADLESS`: Run Chrome in headless mode (true/false)
- `DEBUG_TIMEOUT`: Default timeout for operations (seconds)

## Prerequisites and Setup

### System Requirements

- **Node.js**: v20.19 or higher
- **Chrome**: Stable version or newer
- **npm**: For package management

### Chrome Installation Validation

Verify Chrome installation and version:

```bash
# Check Chrome version
google-chrome --version  # Linux
chrome --version        # macOS

# Verify Chrome accepts remote debugging
chrome --remote-debugging-port=9222 --no-sandbox
```

### Network and Port Configuration

Chrome DevTools MCP uses these default configurations:

- **Debugging Port**: 9222 (default)
- **WebSocket**: For real-time communication
- **HTTP Endpoint**: For DevTools protocol access

## Connection and Troubleshooting

### Common Connection Issues

#### Chrome Not Responding
```
Error: Failed to connect to Chrome DevTools Protocol
```

**Solutions:**
1. Verify Chrome is running with remote debugging enabled
2. Check if port 9222 is available
3. Ensure Chrome version compatibility

#### MCP Server Startup Failure
```
Error: chrome-devtools-mcp package not found
```

**Solutions:**
1. Run `npm install -g chrome-devtools-mcp@latest`
2. Check Node.js version compatibility
3. Verify npm registry access

### Diagnostic Commands

Use the validation script to diagnose issues:

```bash
# Run comprehensive diagnostics
python3 ./plugins/chrome-debug/skills/chrome-devtools-integration/scripts/setup-mcp.py

# Quick validation check
./plugins/chrome-debug/scripts/validate-chrome.sh
```

## Performance Analysis Setup

### Trace Recording

Start performance trace recording:

```bash
# Begin trace collection
mcp call performance_start_trace

# Execute user interactions
# ... user performs actions ...

# Stop and analyze trace
mcp call performance_stop_trace
mcp call performance_analyze_insight
```

### Performance Metrics

Chrome DevTools MCP provides these performance metrics:

- **Loading Metrics**: First Contentful Paint, Largest Contentful Paint
- **Runtime Metrics**: JavaScript execution time, memory usage
- **Network Metrics**: Request timing, response sizes
- **Rendering Metrics**: Frame rate, layout shifts

## Security Considerations

### Remote Debugging Security

Chrome's remote debugging exposes powerful capabilities:

1. **Network Exposure**: Remote debugging port should be firewalled
2. **Code Execution**: Arbitrary JavaScript execution is possible
3. **Data Access**: Full page content and cookies are accessible

### Best Practices

- Use local connections only (localhost)
- Disable remote debugging in production
- Implement authentication for remote access
- Regular Chrome security updates

## Integration Patterns

### Automated Testing Workflow

```python
# Example: Automated login testing
async def test_login_flow(mcp_client):
    # Navigate to login page
    await mcp_client.call("navigate", {"url": "http://localhost:8193/login"})

    # Wait for page load
    await mcp_client.call("wait_for_load")

    # Fill credentials
    await mcp_client.call("type", {"selector": "#username", "text": "superadmin"})
    await mcp_client.call("type", {"selector": "#password", "text": "abc123456"})

    # Submit form
    await mcp_client.call("click", {"selector": "#login-button"})

    # Verify success
    await mcp_client.call("wait_for_selector", {"selector": ".dashboard"})
    screenshot = await mcp_client.call("take_screenshot")
    return screenshot
```

### Performance Monitoring

```python
# Example: Performance monitoring setup
async def setup_performance_monitoring(mcp_client):
    # Start performance trace
    await mcp_client.call("performance_start_trace")

    # Monitor network requests
    await mcp_client.call("list_network_requests")

    # Set up console logging
    await mcp_client.call("list_console_messages")
```

## Error Handling and Recovery

### Common Error Scenarios

#### Chrome Crashes
```javascript
// Restart Chrome and restore session
{
  "action": "restart_chrome",
  "restore_session": true,
  "timeout": 30000
}
```

#### Page Load Failures
```javascript
// Handle page load timeouts
{
  "action": "handle_load_timeout",
  "retry_count": 3,
  "fallback_url": "about:blank"
}
```

#### Element Not Found
```javascript
// Robust element selection
{
  "action": "wait_for_element",
  "selectors": ["#primary-id", ".fallback-class", "[data-testid]"],
  "timeout": 10000
}
```

## Advanced Configuration

### Custom Chrome Flags

Configure Chrome with specific flags for debugging:

```bash
chrome \
  --remote-debugging-port=9222 \
  --no-sandbox \
  --disable-dev-shm-usage \
  --disable-gpu \
  --user-data-dir=/tmp/chrome-debug
```

### Multi-Instance Management

Run multiple Chrome instances for parallel debugging:

```json
{
  "chrome-devtools-1": {
    "command": "npx",
    "args": ["-y", "chrome-devtools-mcp@latest"],
    "env": {
      "CHROME_PORT": "9222"
    }
  },
  "chrome-devtools-2": {
    "command": "npx",
    "args": ["-y", "chrome-devtools-mcp@latest"],
    "env": {
      "CHROME_PORT": "9223"
    }
  }
}
```

## Additional Resources

### Reference Files

For detailed technical specifications and troubleshooting guides:
- **`references/api-reference.md`** - Complete MCP API documentation
- **`references/troubleshooting.md`** - Common issues and solutions
- **`references/performance-patterns.md`** - Performance analysis patterns

### Example Scripts

Working automation examples in `examples/`:
- **`examples/login-automation.js`** - Complete login flow automation
- **`examples/performance-analysis.js`** - Performance monitoring setup
- **`examples/network-monitoring.js`** - Network request analysis

### Utility Scripts

Helper scripts in `scripts/`:
- **`scripts/setup-mcp.py`** - Automated MCP server setup
- **`scripts/validate-chrome.sh`** - Chrome installation validation
- **`scripts/diagnose-mcp.py`** - Comprehensive diagnostic tool

## Best Practices

### Development Workflow

1. **Start Chrome**: Launch with remote debugging enabled
2. **Connect MCP**: Verify MCP server connection
3. **Navigate**: Load target application
4. **Debug**: Use DevTools capabilities for analysis
5. **Automate**: Implement repeatable testing patterns
6. **Monitor**: Track performance and errors continuously

### Code Organization

- Separate configuration from automation logic
- Use descriptive selector strategies
- Implement robust error handling
- Log actions for debugging and audit trails
- Clean up resources after each session