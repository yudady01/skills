#!/bin/bash

# Git 分析器脚本 - 简化版本
set -euo pipefail

# 获取插件根目录
PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"

# 导入工具函数
source "${PLUGIN_ROOT}/hooks/scripts/utils.sh"

# 主函数
main() {
    local output_format="${1:-summary}"

    log_debug "开始Git分析..."

    # 使用utils.sh中的函数生成Git信息
    local git_info
    git_info=$(generate_git_info_json)

    if [[ "$output_format" == "json" ]]; then
        echo "$git_info"
    else
        # 显示摘要信息
        if echo "$git_info" | grep -q '"error"'; then
            echo "📊 Git 状态: 非Git环境或Git命令不可用"
            return 0
        fi

        local current_branch
        current_branch=$(echo "$git_info" | jq -r '.repository.current_branch // "unknown"')

        local total_files
        total_files=$(echo "$git_info" | jq -r '.changes.files // 0')

        local total_additions
        total_additions=$(echo "$git_info" | jq -r '.changes.additions // 0')

        local total_deletions
        total_deletions=$(echo "$git_info" | jq -r '.changes.deletions // 0')

        local uncommitted_files
        uncommitted_files=$(echo "$git_info" | jq -r '.status.uncommitted_files // 0')

        echo
        echo "📊 Git 更改摘要:"
        echo "   🌿 分支: $current_branch"
        echo "   📁 修改文件: $total_files 个"
        echo "   📈 代码变更: +$total_additions 行 / -$total_deletions 行"
        echo "   📋 未提交文件: $uncommitted_files 个"
    fi

    log_debug "Git分析完成"
    return 0
}

# 脚本入口
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi