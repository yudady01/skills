#!/usr/bin/env python3
"""
Chrome DevTools MCP Setup Script
Automates the installation and configuration of Chrome DevTools MCP server
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def check_node_version():
    """Check if Node.js version meets requirements"""
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        version_str = result.stdout.strip().lstrip('v')
        major, minor, patch = map(int, version_str.split('.'))

        if major > 20 or (major == 20 and minor >= 19):
            print(f"✅ Node.js version {version_str} meets requirements")
            return True
        else:
            print(f"❌ Node.js version {version_str} is too old. Requires v20.19+")
            return False
    except FileNotFoundError:
        print("❌ Node.js not found. Please install Node.js v20.19+")
        return False

def check_chrome_installation():
    """Check if Chrome browser is installed"""
    chrome_commands = [
        'google-chrome',
        'chrome',
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    ]

    for cmd in chrome_commands:
        try:
            result = subprocess.run([cmd, '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                version = result.stdout.strip()
                print(f"✅ Chrome found: {version}")
                return True
        except FileNotFoundError:
            continue

    print("❌ Chrome browser not found")
    return False

def install_mcp_server():
    """Install Chrome DevTools MCP server globally"""
    print("📦 Installing Chrome DevTools MCP server...")

    try:
        result = subprocess.run([
            'npm', 'install', '-g', 'chrome-devtools-mcp@latest'
        ], capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ MCP server installed successfully")
            return True
        else:
            print(f"❌ Installation failed: {result.stderr}")
            return False
    except subprocess.SubprocessError as e:
        print(f"❌ Installation error: {e}")
        return False

def create_mcp_config():
    """Create MCP configuration file"""
    config_path = Path('.mcp.json')

    if config_path.exists():
        print("ℹ️  .mcp.json already exists, updating...")
        with open(config_path, 'r') as f:
            config = json.load(f)
    else:
        print("📄 Creating new .mcp.json configuration...")
        config = {}

    if 'mcpServers' not in config:
        config['mcpServers'] = {}

    config['mcpServers']['chrome-devtools'] = {
        "command": "npx",
        "args": ["-y", "chrome-devtools-mcp@latest"],
        "env": {
            "CHROME_PATH": "${CHROME_PATH:-}",
            "HEADLESS": "${HEADLESS:-false}"
        }
    }

    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)

    print("✅ MCP configuration updated")
    return True

def test_mcp_connection():
    """Test MCP server connection"""
    print("🔍 Testing MCP server connection...")

    try:
        # Test if npx can find the package
        result = subprocess.run([
            'npx', '-y', 'chrome-devtools-mcp@latest', '--help'
        ], capture_output=True, text=True, timeout=10)

        if result.returncode == 0:
            print("✅ MCP server is accessible")
            return True
        else:
            print(f"❌ MCP server test failed: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("❌ MCP server test timed out")
        return False
    except subprocess.SubprocessError as e:
        print(f"❌ MCP server test error: {e}")
        return False

def create_local_config():
    """Create local configuration template"""
    config_dir = Path('.claude')
    config_dir.mkdir(exist_ok=True)

    config_file = config_dir / 'chrome-debug.local.md'

    if config_file.exists():
        print(f"ℹ️  Local config already exists: {config_file}")
        return True

    template = """---
# Chrome Debug Plugin Configuration
target_url: "http://localhost:8193/x_mgr/start/index.html#/user/login"
username: "superadmin"
password: "abc123456"
headless_mode: false
timeout: 30
chrome_path: ""
debug_mode: false
---

# Chrome Debug Settings

## Target Configuration
- **URL**: Target application URL for debugging
- **Username**: Login username for automatic authentication
- **Password**: Login password for automatic authentication

## Browser Settings
- **Headless Mode**: Run Chrome without visible UI
- **Timeout**: Default timeout for operations (seconds)
- **Chrome Path**: Custom Chrome executable path (optional)

## Debug Options
- **Debug Mode**: Enable verbose logging and debugging output
"""

    with open(config_file, 'w') as f:
        f.write(template)

    print(f"✅ Local configuration template created: {config_file}")
    return True

def main():
    """Main setup function"""
    print("🚀 Chrome DevTools MCP Setup")
    print("=" * 40)

    # Check prerequisites
    if not check_node_version():
        sys.exit(1)

    if not check_chrome_installation():
        print("⚠️  Chrome not found. Please install Chrome browser and retry.")
        sys.exit(1)

    # Install MCP server
    if not install_mcp_server():
        sys.exit(1)

    # Create configuration
    if not create_mcp_config():
        sys.exit(1)

    # Test connection
    if not test_mcp_connection():
        print("⚠️  MCP server test failed, but installation may still work")

    # Create local config
    create_local_config()

    print("\n🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Update .claude/chrome-debug.local.md with your settings")
    print("2. Restart Claude Code to load the MCP server")
    print("3. Use /chrome-debug commands to start debugging")

if __name__ == "__main__":
    main()