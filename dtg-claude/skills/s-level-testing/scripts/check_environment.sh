#!/bin/bash

################################################################################
# S 級測試環境檢查腳本
#
# 功能：
#   - 檢查 Java 版本 ≥ 8
#   - 檢查 Maven 版本 ≥ 3.6
#   - 檢查項目目錄存在性
#   - 檢查測試依賴配置
#
# 使用方法：
#   bash .agent/skills/s-level-testing/scripts/check_environment.sh
################################################################################

set -e  # 遇到錯誤立即退出

# 顏色定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 腳本所在目錄
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"
RBGI_POM="$PROJECT_ROOT/rbgi/pom.xml"

echo "=========================================="
echo "S 級測試環境檢查"
echo "=========================================="
echo ""

# 檢查 Java 版本
echo "[1/4] 檢查 Java 版本..."
if command -v java &> /dev/null; then
    JAVA_VERSION=$(java -version 2>&1 | awk -F '"' '/version/ {print $2}' | awk -F '.' '{print $1}')
    # 處理 Java 9+ 的版本格式
    if [[ "$JAVA_VERSION" == "1" ]]; then
        JAVA_VERSION=$(java -version 2>&1 | awk -F '"' '/version/ {print $2}' | awk -F '.' '{print $2}')
    fi

    if [[ $JAVA_VERSION -ge 8 ]]; then
        FULL_VERSION=$(java -version 2>&1 | head -n 1)
        echo -e "${GREEN}✓${NC} Java 版本: $FULL_VERSION"
    else
        echo -e "${RED}✗${NC} Java 版本過低: $JAVA_VERSION (需要 ≥ 8)"
        exit 1
    fi
else
    echo -e "${RED}✗${NC} 未找到 Java 安裝"
    echo "請訪問 https://www.oracle.com/java/technologies/downloads/ 安裝 Java 8 或更高版本"
    exit 1
fi
echo ""

# 檢查 Maven 版本
echo "[2/4] 檢查 Maven 版本..."
if command -v mvn &> /dev/null; then
    MAVEN_VERSION=$(mvn -version 2>&1 | head -n 1 | awk '{print $3}')
    # 提取主版本號
    MAVEN_MAJOR=$(echo "$MAVEN_VERSION" | awk -F '.' '{print $1}')
    MAVEN_MINOR=$(echo "$MAVEN_VERSION" | awk -F '.' '{print $2}')

    if [[ $MAVEN_MAJOR -gt 3 ]] || [[ $MAVEN_MAJOR -eq 3 && $MAVEN_MINOR -ge 6 ]]; then
        echo -e "${GREEN}✓${NC} Maven 版本: $MAVEN_VERSION"
    else
        echo -e "${RED}✗${NC} Maven 版本過低: $MAVEN_VERSION (需要 ≥ 3.6)"
        echo "請訪問 https://maven.apache.org/download.cgi 安裝 Maven 3.6 或更高版本"
        exit 1
    fi
else
    echo -e "${RED}✗${NC} 未找到 Maven 安裝"
    echo "請訪問 https://maven.apache.org/download.cgi 安裝 Maven 3.6 或更高版本"
    exit 1
fi
echo ""

# 檢查項目目錄
echo "[3/4] 檢查項目目錄..."
if [[ -f "$RBGI_POM" ]]; then
    echo -e "${GREEN}✓${NC} 項目目錄: $RBGI_POM"
else
    echo -e "${RED}✗${NC} 項目目錄不存在: $RBGI_POM"
    echo "請確保在 dtg-pay 項目根目錄下運行此腳本"
    exit 1
fi
echo ""

# 檢查測試依賴
echo "[4/4] 檢查測試依賴..."
MISSING_DEPS=0

# 檢查 spring-boot-starter-test
if grep -q "spring-boot-starter-test" "$RBGI_POM"; then
    echo -e "${GREEN}✓${NC} spring-boot-starter-test 依賴存在"
else
    echo -e "${RED}✗${NC} 缺少 spring-boot-starter-test 依賴"
    MISSING_DEPS=$((MISSING_DEPS + 1))
fi

# 檢查 mockito-junit-jupiter
if grep -q "mockito-junit-jupiter" "$RBGI_POM"; then
    echo -e "${GREEN}✓${NC} mockito-junit-jupiter 依賴存在"
else
    echo -e "${YELLOW}⚠${NC} 建議添加 mockito-junit-jupiter 依賴（JUnit 5 支援）"
fi

# 檢查 JUnit 5
if grep -q "junit-jupiter" "$RBGI_POM" || grep -q "spring-boot-starter-test" "$RBGI_POM"; then
    echo -e "${GREEN}✓${NC} JUnit 5 支援存在（通過 spring-boot-starter-test）"
else
    echo -e "${YELLOW}⚠${NC} 未檢測到 JUnit 5 依賴"
fi
echo ""

# 檢查 JaCoCo 插件（可選）
echo "[可選] 檢查覆蓋率工具..."
if grep -q "jacoco-maven-plugin" "$RBGI_POM"; then
    echo -e "${GREEN}✓${NC} JaCoCo Maven 插件已配置"
else
    echo -e "${YELLOW}⚠${NC} 未配置 JaCoCo 插件，無法生成覆蓋率報告"
    echo "  建議在 pom.xml 中添加 JaCoCo 插件配置"
fi
echo ""

# 總結
echo "=========================================="
if [[ $MISSING_DEPS -eq 0 ]]; then
    echo -e "${GREEN}環境檢查通過 ✓${NC}"
    echo ""
    echo "下一步："
    echo "  1. 編譯測試代碼：mvn clean test-compile -pl rbgi -am"
    echo "  2. 運行測試：bash .agent/skills/s-level-testing/scripts/run_tests.sh"
    exit 0
else
    echo -e "${RED}環境檢查失敗 ✗${NC}"
    echo ""
    echo "請修復上述問題後重新運行此腳本"
    exit 1
fi
