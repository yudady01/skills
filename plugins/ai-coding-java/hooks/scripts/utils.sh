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

# ========== Git 相关辅助函数 ==========

# 检查是否在Git仓库中
is_git_repo() {
    git rev-parse --git-dir >/dev/null 2>&1
}

# 获取Git根目录
get_git_root() {
    git rev-parse --show-toplevel 2>/dev/null || echo "$(pwd)"
}

# 获取当前分支
get_git_branch() {
    git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown"
}

# 获取Git提交哈希（短格式）
get_git_commit_hash() {
    git rev-parse --short HEAD 2>/dev/null || echo "unknown"
}

# 获取远程分支信息
get_git_remote() {
    git rev-parse --abbrev-ref --symbolic-full-name @{upstream} 2>/dev/null || echo "origin/main"
}

# 检查是否有未提交的更改
has_uncommitted_changes() {
    [[ -n $(git status --porcelain 2>/dev/null) ]]
}

# 获取未提交文件数量
get_uncommitted_count() {
    git status --porcelain 2>/dev/null | wc -l || echo "0"
}

# 获取最近的提交数量
get_recent_commit_count() {
    local count="${1:-10}"
    git log --oneline -$count 2>/dev/null | wc -l || echo "0"
}

# 生成Git状态摘要
get_git_status_summary() {
    if ! is_git_repo; then
        echo "非Git仓库"
        return 1
    fi

    local branch=$(get_git_branch)
    local uncommitted=$(get_uncommitted_count)
    local status="干净"

    if [[ "$uncommitted" -gt 0 ]]; then
        status="有${uncommitted}个未提交文件"
    fi

    echo "分支: $branch | 状态: $status"
}

# 获取文件变更统计
get_file_changes_stats() {
    local base_branch="${1:-main}"

    if ! is_git_repo; then
        echo '{"files": 0, "additions": 0, "deletions": 0}'
        return 1
    fi

    # 尝试与基准分支比较
    local diff_output=""
    if git rev-parse --verify "$base_branch" >/dev/null 2>&1; then
        diff_output=$(git diff $base_branch...HEAD --stat 2>/dev/null || echo "")
    else
        # 如果没有基准分支，使用最近10个提交
        diff_output=$(git diff HEAD~10..HEAD --stat 2>/dev/null || echo "")
    fi

    # 解析统计信息
    local files=0
    local additions=0
    local deletions=0

    if [[ -n "$diff_output" ]]; then
        # 从git diff --stat输出中提取数字
        if echo "$diff_output" | grep -q "files changed"; then
            files=$(echo "$diff_output" | grep "files changed" | sed 's/[^0-9]*\([0-9]*\) files changed.*/\1/' 2>/dev/null || echo "0")
            additions=$(echo "$diff_output" | grep "files changed" | sed 's/.*\([0-9]*\) insertions.*/\1/' 2>/dev/null || echo "0")
            deletions=$(echo "$diff_output" | grep "files changed" | sed 's/.*\([0-9]*\) deletions.*/\1/' 2>/dev/null || echo "0")
        fi
    fi

    echo "{\"files\": $files, \"additions\": $additions, \"deletions\": $deletions}"
}

# 检查Git命令是否可用
check_git_command() {
    command -v git >/dev/null 2>&1
}

# 获取Git配置信息
get_git_config() {
    local key="$1"
    git config --get "$key" 2>/dev/null || echo ""
}

# 获取作者信息
get_git_author_info() {
    local name=$(get_git_config "user.name")
    local email=$(get_git_config "user.email")

    if [[ -n "$name" && -n "$email" ]]; then
        echo "$name <$email>"
    elif [[ -n "$name" ]]; then
        echo "$name"
    else
        echo "未知作者"
    fi
}

# 判断Git工作目录状态
get_git_worktree_status() {
    if ! is_git_repo; then
        echo "not_git_repo"
        return
    fi

    local status_output=$(git status --porcelain 2>/dev/null)

    if [[ -z "$status_output" ]]; then
        echo "clean"
    elif echo "$status_output" | grep -q "^ M "; then
        echo "modified"
    elif echo "$status_output" | grep -q "^?? "; then
        echo "untracked"
    elif echo "$status_output" | grep -q "^A "; then
        echo "staged"
    else
        echo "mixed"
    fi
}

# 获取最后一次提交时间
get_last_commit_time() {
    git log -1 --format="%ci" 2>/dev/null || echo "未知"
}

# 生成Git仓库信息摘要（JSON格式）
generate_git_info_json() {
    if ! is_git_repo || ! check_git_command; then
        echo '{"error": "not_git_repository", "message": "非Git环境或Git命令不可用"}'
        return 1
    fi

    local git_root=$(get_git_root)
    local branch=$(get_git_branch)
    local commit_hash=$(get_git_commit_hash)
    local remote=$(get_git_remote)
    local uncommitted=$(get_uncommitted_count)
    local worktree_status=$(get_git_worktree_status)
    local last_commit_time=$(get_last_commit_time)
    local author=$(get_git_author_info)

    local file_stats
    file_stats=$(get_file_changes_stats "main")

    cat <<EOF
{
  "repository": {
    "root_path": "$git_root",
    "current_branch": "$branch",
    "commit_hash": "$commit_hash",
    "remote_branch": "$remote",
    "worktree_status": "$worktree_status",
    "last_commit_time": "$last_commit_time",
    "author": "$author",
    "is_clean": $([ "$worktree_status" = "clean" ] && echo "true" || echo "false")
  },
  "changes": $file_stats,
  "status": {
    "uncommitted_files": $uncommitted,
    "has_changes": $([ "$uncommitted" -gt 0 ] && echo "true" || echo "false")
  },
  "timestamp": "$(get_iso_timestamp)"
}
EOF
}