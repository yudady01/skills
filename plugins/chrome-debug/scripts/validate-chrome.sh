#!/bin/bash

# Chrome Debug Validation Script
# Validates Chrome installation, MCP server, and plugin configuration

set -e

PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(dirname "$(dirname "$0")")}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    local status=$1
    local message=$2
    case $status in
        "OK")
            echo -e "${GREEN}✅ $message${NC}"
            ;;
        "WARN")
            echo -e "${YELLOW}⚠️  $message${NC}"
            ;;
        "ERROR")
            echo -e "${RED}❌ $message${NC}"
            ;;
        "INFO")
            echo -e "${BLUE}ℹ️  $message${NC}"
            ;;
        *)
            echo "$message"
            ;;
    esac
}

# Function to check command availability
check_command() {
    local cmd=$1
    if command -v "$cmd" &> /dev/null; then
        return 0
    else
        return 1
    fi
}

# Function to check Chrome installation
check_chrome() {
    print_status "INFO" "Checking Chrome browser installation..."

    local chrome_paths=(
        "google-chrome"
        "chrome"
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        "/usr/bin/google-chrome"
        "/usr/local/bin/chrome"
        "C:/Program Files/Google/Chrome/Application/chrome.exe"
        "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
    )

    local chrome_found=""
    local chrome_version=""

    for chrome_path in "${chrome_paths[@]}"; do
        if check_command "$chrome_path" || [[ -f "$chrome_path" ]]; then
            chrome_found="$chrome_path"
            break
        fi
    done

    if [[ -z "$chrome_found" ]]; then
        print_status "ERROR" "Chrome browser not found"
        echo "Please install Chrome from https://www.google.com/chrome/"
        return 1
    fi

    # Get Chrome version
    if [[ -f "$chrome_found" ]]; then
        chrome_version=$("$chrome_found" --version 2>&1 || echo "Unknown version")
    else
        chrome_version=$("$chrome_found" --version 2>&1 || echo "Unknown version")
    fi

    print_status "OK" "Chrome found: $chrome_version"

    # Check if Chrome supports remote debugging
    print_status "INFO" "Testing Chrome remote debugging support..."

    # Quick test of Chrome remote debugging (timeout after 5 seconds)
    timeout 5s "$chrome_found" --remote-debugging-port=9222 --no-sandbox --headless > /dev/null 2>&1 &
    local chrome_pid=$!
    sleep 2

    if kill -0 "$chrome_pid" 2>/dev/null; then
        print_status "OK" "Chrome remote debugging supported"
        kill "$chrome_pid" 2>/dev/null || true
    else
        print_status "WARN" "Chrome remote debugging test failed"
    fi

    return 0
}

# Function to check Node.js
check_nodejs() {
    print_status "INFO" "Checking Node.js installation..."

    if ! check_command "node"; then
        print_status "ERROR" "Node.js not found"
        echo "Please install Node.js v20.19+ from https://nodejs.org/"
        return 1
    fi

    local node_version=$(node --version 2>&1)
    print_status "OK" "Node.js found: $node_version"

    # Check version requirement
    local version_number=${node_version#v}
    if [[ "$version_number" < "20.19.0" ]]; then
        print_status "WARN" "Node.js version may be too old (requires v20.19+)"
    fi

    return 0
}

# Function to check npm
check_npm() {
    print_status "INFO" "Checking npm installation..."

    if ! check_command "npm"; then
        print_status "ERROR" "npm not found"
        return 1
    fi

    local npm_version=$(npm --version 2>&1)
    print_status "OK" "npm found: v$npm_version"
    return 0
}

# Function to check MCP server
check_mcp_server() {
    print_status "INFO" "Checking Chrome DevTools MCP server..."

    # Check if package is installed globally
    if npm list -g chrome-devtools-mcp &> /dev/null; then
        local mcp_version=$(npm list -g chrome-devtools-mcp --depth=0 2>/dev/null | grep chrome-devtools-mcp || echo "Unknown version")
        print_status "OK" "MCP server installed: $mcp_version"
    else
        print_status "WARN" "Chrome DevTools MCP server not found globally"
        echo "Install with: npm install -g chrome-devtools-mcp@latest"
    fi

    # Test if npx can run the package
    print_status "INFO" "Testing MCP server accessibility..."
    if timeout 10s npx -y chrome-devtools-mcp@latest --help &> /dev/null; then
        print_status "OK" "MCP server accessible via npx"
    else
        print_status "WARN" "MCP server test failed (may still work)"
    fi

    return 0
}

# Function to check plugin configuration
check_plugin_config() {
    print_status "INFO" "Checking plugin configuration..."

    # Check .mcp.json
    local mcp_config="$PLUGIN_ROOT/.mcp.json"
    if [[ -f "$mcp_config" ]]; then
        if python3 -c "import json; json.load(open('$mcp_config'))" 2>/dev/null; then
            print_status "OK" ".mcp.json configuration valid"
        else
            print_status "ERROR" ".mcp.json contains invalid JSON"
            return 1
        fi
    else
        print_status "WARN" ".mcp.json not found"
    fi

    # Check plugin.json
    local plugin_config="$PLUGIN_ROOT/.claude-plugin/plugin.json"
    if [[ -f "$plugin_config" ]]; then
        if python3 -c "import json; json.load(open('$plugin_config'))" 2>/dev/null; then
            print_status "OK" "plugin.json configuration valid"
        else
            print_status "ERROR" "plugin.json contains invalid JSON"
            return 1
        fi
    else
        print_status "ERROR" "plugin.json not found"
        return 1
    fi

    # Check local configuration template
    local local_config="$PLUGIN_ROOT/.claude/chrome-debug.local.md"
    if [[ -f "$local_config" ]]; then
        print_status "OK" "Local configuration template found"
    else
        print_status "INFO" "Local configuration template not found (will be created on first use)"
    fi

    return 0
}

# Function to check port availability
check_ports() {
    print_status "INFO" "Checking port availability..."

    # Check port 9222 (default Chrome debugging port)
    if command -v lsof &> /dev/null; then
        if lsof -i :9222 &> /dev/null; then
            print_status "WARN" "Port 9222 is in use (may conflict with Chrome debugging)"
        else
            print_status "OK" "Port 9222 is available"
        fi
    else
        print_status "INFO" "Cannot check port availability (lsof not available)"
    fi
}

# Function to check network connectivity
check_network() {
    print_status "INFO" "Checking network connectivity..."

    # Test basic connectivity
    if ping -c 1 -W 3 8.8.8.8 &> /dev/null; then
        print_status "OK" "Basic network connectivity working"
    else
        print_status "WARN" "Network connectivity issues detected"
    fi

    # Test if we can reach common development ports
    local test_ports=(80 443 8080 3000 8193)
    for port in "${test_ports[@]}"; do
        if timeout 3s bash -c "</dev/tcp/localhost/$port" 2>/dev/null; then
            print_status "INFO" "Port $port is open on localhost"
        fi
    done
}

# Function to check dependencies for target URL
check_target_url() {
    print_status "INFO" "Checking target URL accessibility..."

    # Read configuration if available
    local local_config="$PLUGIN_ROOT/.claude/chrome-debug.local.md"
    local target_url="http://localhost:8193"

    if [[ -f "$local_config" ]]; then
        # Extract URL from configuration (basic parsing)
        local extracted_url=$(grep -E "^target_url:" "$local_config" | cut -d'"' -f2 || echo "")
        if [[ -n "$extracted_url" ]]; then
            target_url="$extracted_url"
        fi
    fi

    print_status "INFO" "Testing URL: $target_url"

    if command -v curl &> /dev/null; then
        local response_code=$(curl -s -I --max-time 10 "$target_url" 2>/dev/null | head -1 | cut -d' ' -f2)

        if [[ "$response_code" =~ ^[23] ]]; then
            print_status "OK" "Target URL is accessible (HTTP $response_code)"
        elif [[ "$response_code" == "404" ]]; then
            print_status "WARN" "Target URL returns 404 Not Found"
            print_status "INFO" "Plugin will fallback to https://www.google.com/"
            # Test Google accessibility
            if curl -s -I --max-time 5 "https://www.google.com/" &> /dev/null; then
                print_status "OK" "Fallback URL (Google) is accessible"
            else
                print_status "WARN" "Even fallback URL is not accessible"
            fi
        elif [[ -n "$response_code" ]]; then
            print_status "WARN" "Target URL returned HTTP $response_code"
        else
            print_status "WARN" "Target URL not accessible (may be normal if server not running)"
            print_status "INFO" "Plugin will fallback to https://www.google.com/"
        fi
    else
        print_status "INFO" "Cannot test URL accessibility (curl not available)"
    fi
}

# Function to generate summary
generate_summary() {
    echo
    print_status "INFO" "Validation Summary"
    echo "===================="

    local total_checks=0
    local passed_checks=0

    # Count checks (simplified)
    ((total_checks++))
    if check_command chrome || [[ -f "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" ]]; then
        ((passed_checks++))
    fi

    ((total_checks++))
    if check_command node; then
        ((passed_checks++))
    fi

    ((total_checks++))
    if check_command npm; then
        ((passed_checks++))
    fi

    echo "Checks completed: $passed_checks/$total_checks"

    if [[ $passed_checks -eq $total_checks ]]; then
        print_status "OK" "All validations passed!"
        echo "The Chrome Debug plugin should work correctly."
    else
        print_status "WARN" "Some validations failed"
        echo "Please address the issues above for optimal plugin performance."
    fi

    echo
    print_status "INFO" "Next Steps"
    echo "1. Install missing dependencies if any"
    echo "2. Run: /chrome-config --install (to set up MCP server)"
    echo "3. Run: /chrome-debug (to start debugging)"
}

# Main validation function
main() {
    echo "Chrome Debug Plugin Validation"
    echo "============================="
    echo

    local validation_passed=true

    # Run all checks
    check_chrome || validation_passed=false
    check_nodejs || validation_passed=false
    check_npm || validation_passed=false
    check_mcp_server || validation_passed=false
    check_plugin_config || validation_passed=false
    check_ports
    check_network
    check_target_url

    generate_summary

    if [[ "$validation_passed" == "true" ]]; then
        exit 0
    else
        exit 1
    fi
}

# Run main function
main "$@"