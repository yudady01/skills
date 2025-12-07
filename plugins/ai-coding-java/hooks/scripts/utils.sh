#!/bin/bash

# 钩子系统通用工具函数

# 获取插件根目录
get_plugin_root() {
    echo "${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
}

# 日志函数
log_info() {
    echo "ℹ️  $*"
}

log_error() {
    echo "❌ $*" >&2
}

log_success() {
    echo "✅ $*"
}

log_warning() {
    echo "⚠️  $*"
}

log_debug() {
    if [[ "${DEBUG:-false}" == "true" ]]; then
        echo "🐛 DEBUG: $*"
    fi
}

# 检查命令是否存在
command_exists() {
    command -v "$1" &> /dev/null
}

# 检查文件是否存在且可读
file_readable() {
    [[ -f "$1" && -r "$1" ]]
}

# 确保目录存在
ensure_directory() {
    local dir="$1"
    if [[ ! -d "$dir" ]]; then
        mkdir -p "$dir"
        log_debug "创建目录: $dir"
    fi
}

# 获取文件大小（字节）
get_file_size() {
    local file="$1"
    if [[ -f "$file" ]]; then
        if command_exists stat; then
            # macOS和Linux的stat命令参数不同
            if [[ "$(uname)" == "Darwin" ]]; then
                stat -f%z "$file" 2>/dev/null || echo "0"
            else
                stat -c%s "$file" 2>/dev/null || echo "0"
            fi
        else
            echo "0"
        fi
    else
        echo "0"
    fi
}

# 格式化文件大小
format_file_size() {
    local size="$1"
    if [[ $size -lt 1024 ]]; then
        echo "${size} B"
    elif [[ $size -lt 1048576 ]]; then
        echo "$(( size / 1024 )) KB"
    else
        echo "$(( size / 1048576 )) MB"
    fi
}

# 获取当前时间戳
get_timestamp() {
    date '+%Y-%m-%d %H:%M:%S'
}

# 获取ISO格式时间戳
get_iso_timestamp() {
    date -Iseconds
}

# 清理临时文件
cleanup_temp_files() {
    local pattern="${1:-/tmp/claude_*}"
    if ls $pattern 1> /dev/null 2>&1; then
        rm -f $pattern
        log_debug "清理临时文件: $pattern"
    fi
}

# 检查Python依赖
check_python_deps() {
    local deps=("jinja2>=3.1.0" "pyyaml>=6.0")
    local missing_deps=()

    for dep in "${deps[@]}"; do
        local package=$(echo "$dep" | cut -d'=' -f1)
        if ! python3 -c "import $package" 2>/dev/null; then
            missing_deps+=("$dep")
        fi
    done

    if [[ ${#missing_deps[@]} -gt 0 ]]; then
        log_error "缺少Python依赖:"
        for dep in "${missing_deps[@]}"; do
            echo "  - $dep"
        done
        echo "请运行: pip install ${missing_deps[*]}"
        return 1
    fi

    return 0
}

# 生成随机字符串
generate_random_string() {
    local length="${1:-8}"
    if command_exists openssl; then
        openssl rand -hex $((length/2)) 2>/dev/null || head -c $length /dev/urandom | base64
    else
        head -c $length /dev/urandom | base64
    fi
}

# 检查网络连接
check_network() {
    local url="${1:-https://www.google.com}"
    if command_exists curl; then
        curl -s --head "$url" > /dev/null 2>&1
    elif command_exists wget; then
        wget -q --spider "$url" 2>/dev/null
    else
        return 1
    fi
}

# 颜色输出
color_echo() {
    local color="$1"
    shift
    local text="$*"

    case "$color" in
        "red") echo -e "\033[31m$text\033[0m" ;;
        "green") echo -e "\033[32m$text\033[0m" ;;
        "yellow") echo -e "\033[33m$text\033[0m" ;;
        "blue") echo -e "\033[34m$text\033[0m" ;;
        "purple") echo -e "\033[35m$text\033[0m" ;;
        "cyan") echo -e "\033[36m$text\033[0m" ;;
        "white") echo -e "\033[37m$text\033[0m" ;;
        *) echo "$text" ;;
    esac
}

# 进度条
show_progress() {
    local current="$1"
    local total="$2"
    local width="${3:-50}"
    local percent=$(( current * 100 / total ))
    local filled=$(( current * width / total ))
    local empty=$(( width - filled ))

    printf "\r["
    printf "%*s" $filled | tr ' ' '='
    printf "%*s" $empty | tr ' ' '-'
    printf "] %d%% (%d/%d)" $percent $current $total

    if [[ $current -eq $total ]]; then
        echo
    fi
}