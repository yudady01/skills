#!/bin/bash

# Spring Boot Enterprise Quality Gate Script
# 执行 Spring Boot 企业级代码质量检查的自动化脚本

set -e

PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"

echo "🔍 Starting Spring Boot enterprise quality gate checks..."

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 统计变量
TOTAL_CHECKS=0
PASSED_CHECKS=0

# 检查函数
check_command() {
    if command -v "$1" >/dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

# 增加检查计数
increment_counter() {
    TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
    if [ "$1" = "passed" ]; then
        PASSED_CHECKS=$((PASSED_CHECKS + 1))
    fi
}

# 1. Java 编译检查
echo "📝 Java compilation check..."
increment_counter
if check_command mvn; then
    if mvn compile -q >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Java compilation passed${NC}"
        increment_counter "passed"
    else
        echo -e "${RED}✗ Java compilation failed${NC}"
        echo "Run 'mvn compile' to see compilation errors"
        exit 1
    fi
elif check_command gradle; then
    if ./gradlew compileJava -q >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Java compilation passed${NC}"
        increment_counter "passed"
    else
        echo -e "${RED}✗ Java compilation failed${NC}"
        echo "Run './gradlew compileJava' to see compilation errors"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠ No Java build tool found (Maven/Gradle), skipping compilation check${NC}"
fi

# 2. 单元测试检查
echo "🧪 Unit test execution..."
increment_counter
if check_command mvn; then
    if mvn test -q >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Unit tests passed${NC}"
        increment_counter "passed"
    else
        echo -e "${RED}✗ Unit tests failed${NC}"
        echo "Run 'mvn test' to see test failures"
        exit 1
    fi
elif check_command gradle; then
    if ./gradlew test -q >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Unit tests passed${NC}"
        increment_counter "passed"
    else
        echo -e "${RED}✗ Unit tests failed${NC}"
        echo "Run './gradlew test' to see test failures"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠ No build tool found, skipping unit test check${NC}"
fi

# 3. Spring Boot 应用启动检查
echo "🚀 Spring Boot application startup check..."
increment_counter
if [ -f "src/main/java" ] && find src/main/java -name "*Application.java" | grep -q .; then
    if check_command mvn; then
        # 尝试启动应用并快速停止以验证配置
        timeout 30s mvn spring-boot:run -Dspring-boot.run.arguments="--server.port=0" -Dspring.profiles.active=test >/dev/null 2>&1 &
        PID=$!
        sleep 10
        if kill -0 $PID 2>/dev/null; then
            kill $PID 2>/dev/null
            echo -e "${GREEN}✓ Spring Boot application startup check passed${NC}"
            increment_counter "passed"
        else
            echo -e "${RED}✗ Spring Boot application failed to start${NC}"
            echo "Check application logs for startup errors"
            exit 1
        fi
    else
        echo -e "${YELLOW}⚠ Maven not available, skipping Spring Boot startup check${NC}"
    fi
else
    echo -e "${YELLOW}⚠ No Spring Boot application class found, skipping startup check${NC}"
fi

# 4. 构建最终检查
echo "🏗️ Final build verification..."
increment_counter
if check_command mvn; then
    if mvn clean package -DskipTests -q >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Final build successful${NC}"
        increment_counter "passed"
    else
        echo -e "${RED}✗ Final build failed${NC}"
        echo "Run 'mvn clean package' to see build errors"
        exit 1
    fi
elif check_command gradle; then
    if ./gradlew clean build -x test -q >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Final build successful${NC}"
        increment_counter "passed"
    else
        echo -e "${RED}✗ Final build failed${NC}"
        echo "Run './gradlew clean build' to see build errors"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠ No build tool found, skipping final build check${NC}"
fi

# 生成质量报告
echo ""
echo -e "${BLUE}📋 Quality Gate Summary${NC}"
echo "=============================="
echo -e "Total checks: ${BLUE}$TOTAL_CHECKS${NC}"
echo -e "Passed checks: ${GREEN}$PASSED_CHECKS${NC}"
echo -e "Failed checks: ${RED}$((TOTAL_CHECKS - PASSED_CHECKS))${NC}"
echo "=============================="

# 检查是否所有检查都通过
if [ $PASSED_CHECKS -eq $TOTAL_CHECKS ]; then
    echo -e "${GREEN}🎉 All Spring Boot enterprise quality gate checks passed!${NC}"
    echo -e "${GREEN}✨ Code is ready for enterprise deployment${NC}"
    exit 0
else
    echo -e "${RED}❌ Some quality gate checks failed${NC}"
    echo -e "${RED}🚫 Code is not ready for deployment${NC}"
    exit 1
fi