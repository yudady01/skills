#!/bin/bash

# AI Coding Boilerplate - Quality Gate Script
# 执行代码质量检查的自动化脚本

set -e

PLUGIN_ROOT="/Users/tommy/.claude/plugins/marketplace/claude-code-plugins/plugins/ai-coding-boilerplate"

echo "🔍 Starting quality gate checks..."

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 检查函数
check_command() {
    if command -v "$1" >/dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

# 1. TypeScript 类型检查
echo "📝 TypeScript type checking..."
if check_command npm; then
    if npm run type-check >/dev/null 2>&1; then
        echo -e "${GREEN}✓ TypeScript type check passed${NC}"
    else
        echo -e "${RED}✗ TypeScript type check failed${NC}"
        npm run type-check
        exit 1
    fi
else
    echo -e "${YELLOW}⚠ npm not found, skipping type check${NC}"
fi

# 2. 代码格式检查
echo "🎨 Code format checking..."
if [ -f "biome.json" ] || [ -f ".biomerc.json" ] || grep -q "biome" package.json; then
    if npm run format:check >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Code format check passed${NC}"
    else
        echo -e "${RED}✗ Code format check failed${NC}"
        echo "Run 'npm run format:fix' to fix formatting issues"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠ Biome not configured, skipping format check${NC}"
fi

# 3. Lint 检查
echo "🔧 Code linting..."
if [ -f "biome.json" ] || [ -f ".biomerc.json" ] || grep -q "lint" package.json; then
    if npm run lint >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Lint check passed${NC}"
    else
        echo -e "${RED}✗ Lint check failed${NC}"
        echo "Run 'npm run lint:fix' to fix linting issues"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠ Linting not configured, skipping lint check${NC}"
fi

# 4. 测试检查
echo "🧪 Test execution..."
if grep -q "test" package.json; then
    if npm test >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Tests passed${NC}"
    else
        echo -e "${RED}✗ Tests failed${NC}"
        echo "Run 'npm test' to see test failures"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠ No tests configured, skipping test check${NC}"
fi

# 5. 构建检查
echo "🏗️ Build verification..."
if grep -q "build" package.json; then
    if npm run build >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Build successful${NC}"
    else
        echo -e "${RED}✗ Build failed${NC}"
        echo "Run 'npm run build' to see build errors"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠ No build script configured, skipping build check${NC}"
fi

echo -e "${GREEN}🎉 All quality gate checks passed!${NC}"