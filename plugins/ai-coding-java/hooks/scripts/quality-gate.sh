#!/bin/bash

# Spring Boot Enterprise Quality Gate Script
# 执行 Spring Boot 企业级代码质量检查的自动化脚本

set -e

PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-/Users/tommy/.claude/plugins/marketplace/claude-code-plugins/plugins/ai-coding-java}"

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

# 2. Checkstyle 代码规范检查
echo "🎨 Checkstyle code standards check..."
increment_counter
if check_command mvn; then
    if [ -f "checkstyle.xml" ] || mvn checkstyle:check -q >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Checkstyle check passed${NC}"
        increment_counter "passed"
    else
        echo -e "${RED}✗ Checkstyle check failed${NC}"
        echo "Run 'mvn checkstyle:check' to see style violations"
        exit 1
    fi
elif check_command gradle && [ -f "build.gradle" ] && grep -q "checkstyle" build.gradle; then
    if ./gradlew checkstyleMain -q >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Checkstyle check passed${NC}"
        increment_counter "passed"
    else
        echo -e "${RED}✗ Checkstyle check failed${NC}"
        echo "Run './gradlew checkstyleMain' to see style violations"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠ Checkstyle not configured, skipping style check${NC}"
fi

# 3. PMD 代码质量检查
echo "🔧 PMD code quality check..."
increment_counter
if check_command mvn && [ -f "pom.xml" ] && grep -q "maven-pmd-plugin" pom.xml; then
    if mvn pmd:check -q >/dev/null 2>&1; then
        echo -e "${GREEN}✓ PMD check passed${NC}"
        increment_counter "passed"
    else
        echo -e "${RED}✗ PMD check failed${NC}"
        echo "Run 'mvn pmd:check' to see quality violations"
        exit 1
    fi
elif check_command gradle && [ -f "build.gradle" ] && grep -q "pmd" build.gradle; then
    if ./gradlew pmdMain -q >/dev/null 2>&1; then
        echo -e "${GREEN}✓ PMD check passed${NC}"
        increment_counter "passed"
    else
        echo -e "${RED}✗ PMD check failed${NC}"
        echo "Run './gradlew pmdMain' to see quality violations"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠ PMD not configured, skipping quality check${NC}"
fi

# 4. SpotBugs Bug 检测
echo "🐛 SpotBugs bug detection..."
increment_counter
if check_command mvn && [ -f "pom.xml" ] && grep -q "spotbugs-maven-plugin" pom.xml; then
    if mvn spotbugs:check -q >/dev/null 2>&1; then
        echo -e "${GREEN}✓ SpotBugs check passed${NC}"
        increment_counter "passed"
    else
        echo -e "${RED}✗ SpotBugs check failed${NC}"
        echo "Run 'mvn spotbugs:check' to see bug violations"
        exit 1
    fi
elif check_command gradle && [ -f "build.gradle" ] && grep -q "spotbugs" build.gradle; then
    if ./gradlew spotbugsMain -q >/dev/null 2>&1; then
        echo -e "${GREEN}✓ SpotBugs check passed${NC}"
        increment_counter "passed"
    else
        echo -e "${RED}✗ SpotBugs check failed${NC}"
        echo "Run './gradlew spotbugsMain' to see bug violations"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠ SpotBugs not configured, skipping bug check${NC}"
fi

# 5. 单元测试检查
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

# 6. 测试覆盖率检查
echo "📊 Test coverage check..."
increment_counter
if check_command mvn && [ -f "pom.xml" ] && grep -q "jacoco-maven-plugin" pom.xml; then
    if mvn jacoco:check -q >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Test coverage check passed${NC}"
        increment_counter "passed"
    else
        echo -e "${RED}✗ Test coverage check failed${NC}"
        echo "Run 'mvn jacoco:check' to see coverage violations"
        echo "View coverage report: target/site/jacoco/index.html"
        exit 1
    fi
elif check_command gradle && [ -f "build.gradle" ] && grep -q "jacoco" build.gradle; then
    if ./gradlew jacocoTestCoverageVerification -q >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Test coverage check passed${NC}"
        increment_counter "passed"
    else
        echo -e "${RED}✗ Test coverage check failed${NC}"
        echo "Run './gradlew jacocoTestCoverageVerification' to see coverage violations"
        echo "View coverage report: build/reports/jacoco/test/html/index.html"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠ JaCoCo not configured, skipping coverage check${NC}"
fi

# 7. 集成测试检查（如果存在）
echo "🔗 Integration test check..."
increment_counter
if [ -d "src/test/java" ] && find src/test/java -name "*IntegrationTest*" -o -name "*IT*" | grep -q .; then
    if check_command mvn; then
        if mvn verify -Pintegration-tests -q >/dev/null 2>&1; then
            echo -e "${GREEN}✓ Integration tests passed${NC}"
            increment_counter "passed"
        else
            echo -e "${RED}✗ Integration tests failed${NC}"
            echo "Run 'mvn verify -Pintegration-tests' to see integration test failures"
            exit 1
        fi
    elif check_command gradle; then
        if ./gradlew integrationTest -q >/dev/null 2>&1; then
            echo -e "${GREEN}✓ Integration tests passed${NC}"
            increment_counter "passed"
        else
            echo -e "${RED}✗ Integration tests failed${NC}"
            echo "Run './gradlew integrationTest' to see integration test failures"
            exit 1
        fi
    else
        echo -e "${YELLOW}⚠ Integration tests found but no build tool available${NC}"
    fi
else
    echo -e "${YELLOW}⚠ No integration tests found, skipping integration test check${NC}"
fi

# 8. Spring Boot 应用启动检查
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

# 9. 代码格式化检查（Spotless）
echo "✨ Code formatting check..."
increment_counter
if check_command mvn && [ -f "pom.xml" ] && grep -q "spotless-maven-plugin" pom.xml; then
    if mvn spotless:check -q >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Code formatting check passed${NC}"
        increment_counter "passed"
    else
        echo -e "${RED}✗ Code formatting check failed${NC}"
        echo "Run 'mvn spotless:apply' to fix formatting issues"
        exit 1
    fi
elif check_command gradle && [ -f "build.gradle" ] && grep -q "spotless" build.gradle; then
    if ./gradlew spotlessCheck -q >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Code formatting check passed${NC}"
        increment_counter "passed"
    else
        echo -e "${RED}✗ Code formatting check failed${NC}"
        echo "Run './gradlew spotlessApply' to fix formatting issues"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠ Spotless not configured, skipping format check${NC}"
fi

# 10. 安全漏洞扫描
echo "🔒 Security vulnerability scan..."
increment_counter
if check_command mvn && [ -f "pom.xml" ] && grep -q "dependency-check-maven" pom.xml; then
    if mvn dependency-check:check -q >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Security vulnerability scan passed${NC}"
        increment_counter "passed"
    else
        echo -e "${RED}✗ Security vulnerability scan failed${NC}"
        echo "Run 'mvn dependency-check:check' to see security vulnerabilities"
        exit 1
    fi
elif check_command gradle && [ -f "build.gradle" ] && grep -q "dependency-check" build.gradle; then
    if ./gradlew dependencyCheckAnalyze -q >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Security vulnerability scan passed${NC}"
        increment_counter "passed"
    else
        echo -e "${RED}✗ Security vulnerability scan failed${NC}"
        echo "Run './gradlew dependencyCheckAnalyze' to see security vulnerabilities"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠ OWASP Dependency Check not configured, skipping security scan${NC}"
fi

# 11. 构建最终检查
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