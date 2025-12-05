---
name: chrome-diagnose
description: Diagnose Chrome DevTools MCP connection issues, page accessibility problems, and provide detailed error analysis
argument-hint: [--url <url>] [--verbose] [--test-login] [--check-dependencies]
allowed-tools: [Read, Write, Bash, mcp__ide__*, WebFetch]
---

# Chrome Diagnose Command

This command performs comprehensive diagnostics to identify and troubleshoot Chrome DevTools MCP connection issues, page accessibility problems, and configuration errors.

## Parameters

- `--url <url>`: Specific URL to test (optional, uses config default)
- `--verbose`: Enable detailed output with step-by-step analysis
- `--test-login`: Test automated login functionality
- `--check-dependencies`: Verify all system dependencies

## Diagnostic Categories

### 1. System Environment Check
- **Operating System**: Verify OS compatibility
- **Node.js Version**: Check v20.19+ requirement
- **Chrome Installation**: Verify Chrome browser presence and version
- **Network Connectivity**: Test internet and local network access
- **Port Availability**: Check for port conflicts and availability

### 2. MCP Server Status
- **Installation Verification**: Confirm chrome-devtools-mcp is installed
- **Version Compatibility**: Check MCP server version compatibility
- **Configuration Validation**: Verify .mcp.json format and content
- **Startup Testing**: Test MCP server initialization
- **Protocol Access**: Verify DevTools protocol accessibility

### 3. Chrome Browser Analysis
- **Installation Path**: Detect Chrome executable location
- **Version Check**: Verify Chrome version compatibility
- **Remote Debugging**: Test Chrome remote debugging capabilities
- **Permission Issues**: Check Chrome startup permissions
- **Resource Availability**: Verify memory and disk space

### 4. Network and URL Testing
- **DNS Resolution**: Test domain name resolution
- **HTTP/HTTPS Access**: Test URL accessibility
- **404 Not Found Detection**: Check for missing pages and suggest fallbacks
- **SSL Certificate**: Verify certificate validity for HTTPS
- **Response Time**: Measure page load times
- **Content Analysis**: Analyze page structure and elements
- **Fallback URL Testing**: Verify Google accessibility as fallback option

### 5. Login Functionality Testing
- **Form Detection**: Identify login form elements
- **Selector Analysis**: Test element selector strategies
- **Credential Validation**: Verify login credential format
- **Submit Testing**: Test form submission process
- **Success Detection**: Verify login success indicators

## Diagnostic Procedures

### System Environment Diagnostics
```bash
# Operating System Information
uname -a
sw_vers  # macOS
cat /etc/os-release  # Linux

# Node.js Version Check
node --version
npm --version

# Chrome Detection
which google-chrome || which chrome
chrome --version
ls -la "/Applications/Google Chrome.app/Contents/MacOS/"
```

### Network Diagnostics
```bash
# Local Network Test
ping -c 3 localhost
netstat -an | grep 9222

# URL Accessibility Test
curl -I "http://localhost:8193"
curl -I "https://www.google.com"

# DNS Resolution
nslookup localhost
dig localhost
```

### MCP Server Diagnostics
```bash
# Package Installation Check
npm list -g chrome-devtools-mcp
npx -y chrome-devtools-mcp@latest --version

# Configuration Validation
python3 -c "import json; print(json.load(open('.mcp.json')))"

# Server Startup Test
timeout 10s npx -y chrome-devtools-mcp@latest
```

### Chrome Functionality Test
```bash
# Chrome Remote Debugging Test
chrome --remote-debugging-port=9222 --no-sandbox --headless &
sleep 3
curl http://localhost:9222/json/version
pkill -f chrome

# Chrome Path Detection
find /Applications -name "Google Chrome.app" 2>/dev/null
mdfind "kMDItemDisplayName == 'Google Chrome'" 2>/dev/null
```

## Error Analysis and Solutions

### System Requirement Errors

**Node.js Version Incompatible**
```
Error: Node.js v18.17.0 detected. Requires v20.19+
Solution:
1. Install Node.js v20+ from https://nodejs.org
2. Use nvm: nvm install 20 && nvm use 20
3. Update package manager: brew install node@20
```

**Chrome Browser Not Found**
```
Error: Chrome browser installation not detected
Solution:
1. Install Chrome from https://www.google.com/chrome/
2. Set CHROME_PATH environment variable
3. Update configuration with custom Chrome path
```

### MCP Server Errors

**Package Not Installed**
```
Error: chrome-devtools-mcp package not found
Solution:
1. Run: npm install -g chrome-devtools-mcp@latest
2. Check npm global path: npm config get prefix
3. Verify npm permissions: npm list -g
```

**Configuration File Invalid**
```
Error: Invalid .mcp.json format
Solution:
1. Validate JSON syntax: python3 -m json.tool .mcp.json
2. Reset configuration: /chrome-config --reset
3. Check file permissions: ls -la .mcp.json
```

### Network and Connection Errors

**Port Already in Use**
```
Error: Port 9222 already in use
Solution:
1. Kill existing processes: lsof -ti:9222 | xargs kill
2. Use different port: export CHROME_DEBUG_PORT=9223
3. Update configuration for custom port
```

**URL Not Accessible**
```
Error: Target URL not reachable: http://localhost:8193
Solution:
1. Check server status: curl -I http://localhost:8193
2. Verify port is open: netstat -an | grep 8193
3. Test different URL or check server logs
4. Auto-fallback: Plugin will automatically fallback to https://www.google.com/
   - Debug session will continue with Google homepage
   - Update .claude/chrome-debug.local.md with correct URL for next time
```

### Chrome Startup Errors

**Permission Denied**
```
Error: Chrome startup permission denied
Solution:
1. Check file permissions: ls -la $(which chrome)
2. Run with appropriate user: sudo -u user chrome
3. Update Chrome to latest version
```

**Sandbox Issues**
```
Error: Chrome sandbox initialization failed
Solution:
1. Disable sandbox: chrome --no-sandbox
2. Check kernel compatibility: uname -r
3. Update system packages
```

## Usage Examples

### Basic Diagnostics
```bash
/chrome-diagnose
```
Run comprehensive diagnostic tests on default configuration.

### URL-Specific Testing
```bash
/chrome-diagnose --url "https://example.com/login"
```
Test specific URL accessibility and functionality.

### Verbose Analysis
```bash
/chrome-diagnose --verbose
```
Enable detailed step-by-step diagnostic output.

### Login Functionality Test
```bash
/chrome-diagnose --test-login --verbose
```
Test automated login process with detailed output.

### Complete System Check
```bash
/chrome-diagnose --check-dependencies --test-login --verbose
```
Run comprehensive system and functionality tests.

## Output Format

### Success Report
```
🔍 Chrome Debug Plugin Diagnostics
✅ System Environment
  Operating System: macOS 14.2.1 (✓)
  Node.js: v20.19.0 (✓)
  Chrome: 120.0.6099.129 (✓)
  Memory: 16GB available (✓)

✅ MCP Server Status
  Installation: Complete (✓)
  Version: chrome-devtools-mcp@1.2.0 (✓)
  Configuration: Valid (✓)
  Startup: Successful (✓)

✅ Chrome Browser
  Path: /Applications/Google Chrome.app (✓)
  Version: Compatible (✓)
  Remote Debugging: Working (✓)
  Permissions: Sufficient (✓)

✅ Network Connectivity
  Local Network: Connected (✓)
  DNS Resolution: Working (✓)
  Target URL: Accessible (✓)
  Response Time: 245ms (✓)

🎯 Summary: All systems operational
```

### Error Report with Solutions
```
❌ Chrome Debug Plugin Diagnostics
❌ System Environment
  Operating System: macOS 14.2.1 (✓)
  Node.js: v18.17.0 (❌)
  Chrome: Not found (❌)
  Memory: 16GB available (✓)

🔧 Recommended Actions:
1. Update Node.js:
   nvm install 20 && nvm use 20

2. Install Chrome:
   brew install --cask google-chrome

3. Update configuration:
   /chrome-config --reset

💡 Run after fixes: /chrome-diagnose --check-dependencies
```

### Verbose Technical Details
```
🔬 Detailed Analysis (Verbose Mode)

[1/15] Checking Node.js version...
  Command: node --version
  Output: v20.19.0
  Status: ✓ Compatible (>= v20.19)

[2/15] Locating Chrome executable...
  Search paths:
    - /usr/bin/google-chrome
    - /usr/local/bin/chrome
    - /Applications/Google Chrome.app/Contents/MacOS/Google Chrome ✓
  Found: /Applications/Google Chrome.app/Contents/MacOS/Google Chrome

[3/15] Testing Chrome version...
  Command: /Applications/Google Chrome.app/Contents/MacOS/Google Chrome --version
  Output: Google Chrome 120.0.6099.129
  Status: ✓ Compatible

[4/15] Checking port 9222 availability...
  Command: lsof -i :9222
  Output: (no processes)
  Status: ✓ Port available

[5/15] Testing MCP server installation...
  Command: npm list -g chrome-devtools-mcp
  Output: /usr/local/lib/node_modules/chrome-devtools-mcp@1.2.0
  Status: ✓ Installed

... (continues with detailed step-by-step analysis)
```

## Integration with Other Components

### Chrome Debug Command
- Uses diagnostic results to guide debugging sessions
- Applies configuration fixes automatically
- Provides error context for failed sessions

### Chrome Config Command
- Leverages diagnostic data for configuration updates
- Validates configuration changes
- Monitors configuration health over time

### Skills Integration
- chrome-devtools-integration: Provides MCP expertise
- dom-automation: Helps troubleshoot automation issues
- Error analysis guides skill selection and usage

## Automated Fixes

The diagnose command can automatically fix common issues:

- **Reset Configuration**: `--auto-fix` flag
- **Reinstall Dependencies**: `--reinstall` flag
- **Update Chrome Path**: `--update-paths` flag
- **Clear Cache**: `--clean` flag

## Best Practices

### Regular Maintenance
- Run diagnostics weekly to catch issues early
- Use verbose mode for detailed troubleshooting
- Document custom configurations for team reference
- Keep Chrome and Node.js versions updated

### Troubleshooting Workflow
1. Run basic diagnostics: `/chrome-diagnose`
2. Analyze error patterns and categorize
3. Apply targeted fixes based on recommendations
4. Verify fixes with: `/chrome-diagnose --verify`
5. Document solutions for future reference

### Performance Monitoring
- Monitor diagnostic execution times
- Track error patterns over time
- Optimize diagnostic test sequences
- Cache results for repeated tests

## Related Commands

- `/chrome-debug`: Main debugging command
- `/chrome-config`: Configuration management
- `/skill chrome-devtools-integration`: MCP expertise
- `/skill dom-automation`: Automation troubleshooting