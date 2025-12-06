#!/bin/bash

# AI Coding Boilerplate - Documentation Validator Script
# 验证项目文档完整性和一致性

set -e

PLUGIN_ROOT="/Users/tommy/.claude/plugins/marketplace/claude-code-plugins/plugins/ai-coding-boilerplate"

echo "📚 Starting documentation validation..."

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 检查函数
check_file_exists() {
    if [ -f "$1" ]; then
        echo -e "${GREEN}✓ $1 exists${NC}"
        return 0
    else
        echo -e "${YELLOW}⚠ $1 not found${NC}"
        return 1
    fi
}

# 检查文档质量
check_documentation_quality() {
    local file="$1"
    local min_lines="${2:-10}"

    if [ -f "$file" ]; then
        local lines=$(wc -l < "$file")
        if [ "$lines" -ge "$min_lines" ]; then
            echo -e "${GREEN}✓ $1 has sufficient content ($lines lines)${NC}"
            return 0
        else
            echo -e "${YELLOW}⚠ $1 has insufficient content ($lines lines, expected at least $min_lines)${NC}"
            return 1
        fi
    fi
    return 1
}

# 1. 检查核心文档文件
echo "📄 Checking core documentation files..."
missing_docs=0

# 基础文档检查
check_file_exists "README.md" || ((missing_docs++))
check_file_exists "CHANGELOG.md" || ((missing_docs++))

# API 文档检查
if [ -d "src" ] && find src -name "*.ts" | grep -q "api\|route\|controller"; then
    check_file_exists "docs/api/README.md" || ((missing_docs++))
fi

# 配置文档检查
if [ -f "package.json" ] && grep -q "scripts" package.json; then
    check_file_exists "docs/development.md" || ((missing_docs++))
fi

# 2. 检查文档内容质量
echo "📖 Checking documentation content quality..."
if check_file_exists "README.md"; then
    check_documentation_quality "README.md" 50
fi

# 3. 检查代码注释
echo "💬 Checking code documentation..."
if [ -d "src" ]; then
    ts_files=$(find src -name "*.ts" | wc -l)
    if [ "$ts_files" -gt 0 ]; then
        echo "Found $ts_files TypeScript files"
        # 简单检查是否有 JSDoc 注释
        documented_files=$(grep -r "/\*\*" src --include="*.ts" | wc -l)
        if [ "$documented_files" -gt 0 ]; then
            echo -e "${GREEN}✓ Found JSDoc comments in code${NC}"
        else
            echo -e "${YELLOW}⚠ No JSDoc comments found in TypeScript files${NC}"
        fi
    fi
fi

# 4. 检查 API 文档
echo "🔌 Checking API documentation..."
if [ -d "src/routes" ] || [ -d "src/controllers" ] || [ -d "src/api" ]; then
    api_files=$(find src -name "*.ts" | grep -E "(route|controller|api)" | wc -l)
    if [ "$api_files" -gt 0 ]; then
        echo "Found $api_files API-related files"
        if check_file_exists "docs/api/README.md"; then
            check_documentation_quality "docs/api/README.md" 20
        fi
    fi
fi

# 5. 检查文档一致性
echo "🔄 Checking documentation consistency..."
if check_file_exists "README.md" && check_file_exists "package.json"; then
    # 检查 README 中的脚本名称是否与 package.json 一致
    if grep -q "npm run" README.md; then
        echo -e "${GREEN}✓ README contains npm script references${NC}"
    else
        echo -e "${YELLOW}⚠ README doesn't contain npm script usage examples${NC}"
    fi
fi

# 总结报告
echo ""
echo "📊 Documentation validation summary:"
if [ "$missing_docs" -eq 0 ]; then
    echo -e "${GREEN}✅ All core documentation files exist${NC}"
else
    echo -e "${YELLOW}⚠ $missing_docs core documentation files missing${NC}"
fi

echo -e "${GREEN}🎉 Documentation validation completed!${NC}"

# 返回缺失文档数量
exit $missing_docs