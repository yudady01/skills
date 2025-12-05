---
name: chrome-config
description: Configure Chrome DevTools MCP server, check status, and manage plugin settings
argument-hint: [--install] [--status] [--reset] [--verify]
allowed-tools: [Read, Write, Bash, mcp__ide__*]
---

# Chrome Config Command

This command manages Chrome DevTools MCP server configuration, verifies installation status, and handles plugin settings.

## Parameters

- `--install`: Install Chrome DevTools MCP server and dependencies
- `--status`: Check current configuration and server status
- `--reset`: Reset configuration to default values
- `--verify`: Verify all components are working correctly

## Execution Steps

### --install Mode
1. **Check System Requirements**
   - Verify Node.js version (requires v20.19+)
   - Check Chrome browser installation
   - Validate npm package manager availability

2. **Install MCP Server**
   - Install chrome-devtools-mcp globally via npm
   - Verify installation success
   - Test basic functionality

3. **Create Configuration Files**
   - Generate .mcp.json with server configuration
   - Create local configuration template
   - Set up default settings

4. **Validate Setup**
   - Test MCP server connection
   - Verify Chrome DevTools protocol access
   - Run basic functionality tests

### --status Mode
1. **Check System Status**
   - Node.js version check
   - Chrome browser detection
   - MCP server installation verification

2. **Configuration Analysis**
   - Validate .mcp.json format
   - Check local configuration settings
   - Verify environment variables

3. **Connectivity Test**
   - Test MCP server startup
   - Verify Chrome remote debugging
   - Check port accessibility

4. **Report Generation**
   - Generate comprehensive status report
   - Identify potential issues
   - Provide recommendations

### --reset Mode
1. **Backup Current Settings**
   - Save existing configuration files
   - Document current settings
   - Create rollback capability

2. **Reset Configuration**
   - Remove corrupted configuration files
   - Reset to default settings
   - Clean up temporary files

3. **Recreate Defaults**
   - Generate fresh .mcp.json
   - Create new local config template
   - Set standard defaults

4. **Validate Reset**
   - Test new configuration
   - Verify basic functionality
   - Confirm reset success

### --verify Mode
1. **Component Verification**
   - Test all plugin components
   - Validate skill configurations
   - Check command integration

2. **Integration Testing**
   - Test MCP server communication
   - Verify Chrome DevTools access
   - Validate automation workflows

3. **Performance Check**
   - Measure response times
   - Check resource usage
   - Validate stability

4. **Generate Report**
   - Comprehensive verification report
   - Performance metrics
   - Recommendations for optimization

## Error Handling

### Installation Errors
- Node.js version incompatible: Provide upgrade instructions
- Chrome not found: Suggest installation paths
- npm permissions: Guide permission fixes
- Network issues: Provide offline installation options

### Configuration Errors
- Invalid JSON: Fix syntax errors
- Missing fields: Add required configuration
- Path issues: Correct file paths
- Permission problems: Resolve access rights

### Connection Errors
- Port conflicts: Suggest alternative ports
- Chrome launch failures: Provide troubleshooting
- MCP server errors: Restart services
- Protocol mismatches: Update configurations

## Usage Examples

### Install MCP Server
```bash
/chrome-config --install
```
Complete installation of Chrome DevTools MCP server with all dependencies.

### Check Status
```bash
/chrome-config --status
```
Display comprehensive status of all components and configurations.

### Reset Configuration
```bash
/chrome-config --reset
```
Reset all configuration files to default values.

### Verify Installation
```bash
/chrome-config --verify
```
Run comprehensive verification of all plugin components.

## Output Format

### Installation Output
```
🚀 Chrome DevTools MCP Installation
✅ Node.js version: v20.19.0 (compatible)
✅ Chrome browser found: Google Chrome 120.0.6099.129
📦 Installing chrome-devtools-mcp@latest...
✅ MCP server installed successfully
📄 Creating .mcp.json configuration...
✅ Configuration created
🔍 Testing MCP server connection...
✅ Installation completed successfully
```

### Status Output
```
📊 Chrome Debug Plugin Status
✅ System Requirements Met
  Node.js: v20.19.0 (✓)
  Chrome: 120.0.6099.129 (✓)
  npm: 10.2.3 (✓)

✅ MCP Server Status
  Installation: Complete (✓)
  Version: chrome-devtools-mcp@1.2.0 (✓)
  Configuration: Valid (✓)

✅ Configuration Files
  .mcp.json: Found and valid (✓)
  chrome-debug.local.md: Found (✓)
  Environment variables: Set (✓)

🔗 Connectivity
  MCP Server: Reachable (✓)
  Chrome Debug Port: 9222 (✓)
  DevTools Protocol: Accessible (✓)
```

### Reset Output
```
🔄 Chrome Debug Configuration Reset
💾 Backing up current configuration...
✅ Backup created: .claude/chrome-debug-backup-20241205.json
🗑️  Removing old configuration files...
📄 Creating new default configuration...
✅ Configuration reset to defaults
🔍 Validating new configuration...
✅ Reset completed successfully
```

## Configuration Files

### .mcp.json Structure
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

### chrome-debug.local.md Template
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

## Troubleshooting

### Common Issues

**MCP Server Not Found**
```bash
# Reinstall MCP server
/chrome-config --install

# Check npm global packages
npm list -g chrome-devtools-mcp
```

**Chrome Path Issues**
```bash
# Set Chrome path environment variable
export CHROME_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Update configuration
/chrome-config --reset
```

**Port Conflicts**
```bash
# Kill existing Chrome processes
pkill -f "chrome.*remote-debugging"

# Use different port
export CHROME_DEBUG_PORT=9223
```

### Manual Verification

Test MCP server manually:
```bash
npx -y chrome-devtools-mcp@latest --help
```

Test Chrome remote debugging:
```bash
chrome --remote-debugging-port=9222 --no-sandbox
```

## Best Practices

### Maintenance
- Regular status checks with `--status`
- Keep MCP server updated
- Monitor Chrome version compatibility
- Backup configurations before changes

### Security
- Use HTTPS URLs when possible
- Secure local configuration files
- Avoid hardcoded credentials
- Regular security updates

### Performance
- Monitor resource usage
- Optimize Chrome startup flags
- Use appropriate timeout values
- Clean up temporary files

## Integration

This command integrates with:
- chrome-debug command: Uses configuration for debugging sessions
- chrome-diagnose command: Leverages status information for diagnostics
- chrome-devtools-integration skill: Provides MCP server expertise
- dom-automation skill: Uses configuration for automation workflows

## Related Commands

- `/chrome-debug`: Main debugging command using this configuration
- `/chrome-diagnose`: Diagnose issues using configuration data
- `/skill chrome-devtools-integration`: Get MCP configuration help
- `/skill dom-automation`: Get automation setup guidance