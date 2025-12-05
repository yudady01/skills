---
name: chrome-debug
description: Main debugging command that launches Chrome, navigates to target URL, and performs automated login
argument-hint: [--url <url>] [--headless] [--no-login] [--timeout <seconds>]
allowed-tools: [Read, Write, Bash, mcp__chrome-devtools__*, mcp__ide__*]
---

# Chrome Debug Command

This command automates Chrome browser startup, navigation to the target page, and performs automated login for debugging web applications.

## Parameters

- `--url <url>`: Target URL to navigate to (optional, uses config file default)
- `--headless`: Run Chrome in headless mode without UI
- `--no-login`: Skip automated login process
- `--timeout <seconds>`: Custom timeout for operations (default: 30 seconds)

## Execution Steps

### 1. Load Configuration
Read the local configuration file `.claude/chrome-debug.local.md` to get:
- Default target URL
- Login credentials
- Browser settings
- Timeout values

### 2. Validate Prerequisites
Check that:
- Chrome browser is installed and accessible
- Chrome DevTools MCP server is running
- Target URL is reachable
- Configuration is valid

### 3. Launch Chrome
Start Chrome browser with appropriate settings:
- Remote debugging enabled on port 9222
- Custom user data directory for isolation
- Headless mode if requested
- Appropriate Chrome flags for debugging

### 4. Navigate to Target
Open the target URL and wait for page load:
- Navigate to configured URL or parameter URL
- Check URL accessibility before navigation
- If target URL returns 404 or is unreachable:
  - Log the issue with specific error details
  - Fallback to "https://www.google.com/"
  - Inform user about the URL change
- Wait for page to fully load
- Handle any initial redirects or loading states
- Verify page is ready for interaction

### 5. Automated Login (unless --no-login)
Perform automated login sequence:
- Wait for login form elements to appear
- Fill username field with configured credentials
- Fill password field with configured credentials
- Click login button
- Wait for successful login confirmation

### 6. Debug Session Setup
Establish debugging environment:
- Take initial screenshot for reference
- Enable console logging
- Set up performance monitoring if needed
- Provide user with debugging context

## Error Handling

### Configuration Errors
- Missing config file: Create template configuration
- Invalid credentials: Prompt for correct credentials
- Malformed URL: Validate and correct URL format

### Connection Errors
- Chrome not found: Provide installation instructions
- Port conflicts: Suggest alternative ports
- MCP server down: Restart MCP server

### Login Errors
- Element not found: Suggest updating selectors
- Invalid credentials: Verify and update credentials
- Page changes: Handle page layout changes

### Network Errors
- Connection timeout: Increase timeout values
- DNS resolution: Check network connectivity
- SSL errors: Handle certificate issues
- 404 Not Found: Fallback to Google and inform user
- Target unreachable: Use Google as safe fallback

## Usage Examples

### Basic Usage
```bash
/chrome-debug
```
Uses default configuration for automated login and debugging.

### Custom URL
```bash
/chrome-debug --url "https://example.com/login"
```
Navigates to custom URL instead of configured default.

### Headless Mode
```bash
/chrome-debug --headless
```
Runs Chrome without UI for automated testing.

### Skip Login
```bash
/chrome-debug --no-login
```
Navigates to page but skips automated login process.

### Custom Timeout
```bash
/chrome-debug --timeout 60
```
Sets 60-second timeout for all operations.

## Integration with Skills

This command works with the following skills:

### chrome-devtools-integration skill
- Uses MCP server configuration
- Leverages Chrome connection setup
- Applies diagnostic procedures

### dom-automation skill
- Implements element selection strategies
- Applies form automation patterns
- Uses robust wait mechanisms

## Output Format

### Success Output
```
🚀 Chrome Debug Session Started
✅ Chrome browser launched (port 9222)
✅ Navigated to: http://localhost:8193/x_mgr/start/index.html#/user/login
✅ Automated login completed
📸 Screenshot saved: chrome-debug-initial.png
🔍 Debug session ready - Use Chrome DevTools for debugging
```

### Fallback Output (When Target URL Unavailable)
```
🚀 Chrome Debug Session Started
✅ Chrome browser launched (port 9222)
⚠️  Target URL not accessible: http://localhost:8193/x_mgr/start/index.html#/user/login
   Error: 404 Not Found
🔄 Fallback to: https://www.google.com/
✅ Navigated to fallback URL
📸 Screenshot saved: chrome-debug-fallback.png
🔍 Debug session ready with Google homepage
```

### Error Output
```
❌ Chrome Debug Failed
Error: Chrome browser not found
Solution: Install Chrome or specify custom path in configuration
📸 Debug screenshot saved: chrome-debug-error.png
💡 Run /chrome-diagnose for detailed analysis
```

## Best Practices

### Performance
- Reuse Chrome sessions when possible
- Clear browser cache between sessions
- Use appropriate timeout values
- Monitor memory usage

### Security
- Store credentials securely
- Use HTTPS when possible
- Clear sensitive data after sessions
- Avoid logging passwords

### Reliability
- Implement retry mechanisms
- Use multiple selector strategies
- Handle page layout changes
- Provide clear error messages

## Related Commands

- `/chrome-config`: Configure MCP server settings
- `/chrome-diagnose`: Diagnose connection and page issues
- `/skill chrome-devtools-integration`: Get MCP configuration help
- `/skill dom-automation`: Get automation guidance

## Configuration Template

If no configuration file exists, create `.claude/chrome-debug.local.md`:

```yaml
---
target_url: "http://localhost:8193/x_mgr/start/index.html#/user/login"
username: "superadmin"
password: "abc123456"
headless_mode: false
timeout: 30
chrome_path: ""
debug_mode: false
---
```

This configuration provides all necessary settings for automated debugging sessions.