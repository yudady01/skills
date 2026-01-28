#!/bin/bash

################################################################################
# S 級測試執行腳本
#
# 功能：
#   - 運行所有測試或指定測試類
#   - 生成測試報告
#   - 顯示測試結果摘要
#
# 使用方法：
#   # 運行所有測試
#   bash .agent/skills/s-level-testing/scripts/run_tests.sh
#
#   # 運行指定測試類
#   bash .agent/skills/s-level-testing/scripts/run_tests.sh RetryBackoffStrategyTest
#   bash .agent/skills/s-level-testing/scripts/run_tests.sh CallbackServiceTest
#   bash .agent/skills/s-level-testing/scripts/run_tests.sh CallbackSenderTest
#
#   # 運行多個測試類
#   bash .agent/skills/s-level-testing/scripts/run_tests.sh "RetryBackoffStrategyTest,CallbackServiceTest"
################################################################################

set -e  # 遇到錯誤立即退出

# 顏色定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 腳本所在目錄
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"

echo "=========================================="
echo "S 級測試執行"
echo "=========================================="
echo ""

# 解析參數
TEST_CLASS="$1"

if [[ -z "$TEST_CLASS" ]]; then
    echo "運行所有測試..."
    MVN_CMD="mvn test -pl rbgi -am"
else
    echo "運行測試類: $TEST_CLASS"
    MVN_CMD="mvn test -pl rbgi -am -Dtest=$TEST_CLASS"
fi
echo ""

# 執行測試
echo "執行命令: $MVN_CMD"
echo ""

cd "$PROJECT_ROOT"

# 記錄開始時間
START_TIME=$(date +%s)

# 運行測試
if eval "$MVN_CMD"; then
    END_TIME=$(date +%s)
    DURATION=$((END_TIME - START_TIME))

    echo ""
    echo "=========================================="
    echo -e "${GREEN}測試執行成功 ✓${NC}"
    echo "=========================================="
    echo "執行時間: ${DURATION} 秒"
    echo ""

    # 解析測試結果
    echo "測試結果摘要："
    echo "---------------"

    # 查找最新的測試報告
    LATEST_REPORT=$(find "$PROJECT_ROOT/rbgi/target/surefire-reports" -name "TEST-*.xml" -type f -printf '%T@ %p\n' 2>/dev/null | sort -n | tail -1 | cut -d' ' -f2-)

    if [[ -n "$LATEST_REPORT" ]]; then
        # 使用 xmlstarlet 或 grep 解析測試結果
        if command -v xmlstarlet &> /dev/null; then
            TESTS_RUN=$(xmlstarlet sel -t -v "/testsuite/@tests" "$LATEST_REPORT")
            FAILURES=$(xmlstarlet sel -t -v "/testsuite/@failures" "$LATEST_REPORT")
            ERRORS=$(xmlstarlet sel -t -v "/testsuite/@errors" "$LATEST_REPORT")
            SKIPPED=$(xmlstarlet sel -t -v "/testsuite/@skipped" "$LATEST_REPORT")

            echo "Tests run: $TESTS_RUN"
            echo "Failures: $FAILURES"
            echo "Errors: $ERRORS"
            echo "Skipped: $SKIPPED"

            if [[ "$FAILURES" -eq 0 && "$ERRORS" -eq 0 ]]; then
                echo -e "${GREEN}✓ 所有測試通過${NC}"
            else
                echo -e "${RED}✗ 存在測試失敗${NC}"
            fi
        else
            # 備用方案：查找 txt 報告
            TXT_REPORT="${LATEST_REPORT%.xml}.txt"
            if [[ -f "$TXT_REPORT" ]]; then
                # 提取測試統計信息
                grep -o "Tests run: [0-9]*" "$TXT_REPORT" | head -1
                grep -o "Failures: [0-9]*" "$TXT_REPORT" | head -1
                grep -o "Errors: [0-9]*" "$TXT_REPORT" | head -1
                grep -o "Skipped: [0-9]*" "$TXT_REPORT" | head -1 || echo "Skipped: 0"
            else
                echo "無法解析測試結果，請查看詳細報告"
            fi
        fi
    else
        echo "未找到測試報告"
    fi

    echo ""
    echo "測試報告位置:"
    echo "  XML: $PROJECT_ROOT/rbgi/target/surefire-reports/"
    echo "  HTML: $PROJECT_ROOT/rbgi/target/site/surefire-report.html"
    echo ""

    echo "下一步："
    echo "  1. 生成覆蓋率報告：bash .agent/skills/s-level-testing/scripts/check_coverage.sh"
    echo "  2. 查看測試報告：open $PROJECT_ROOT/rbgi/target/site/surefire-report.html"

    exit 0
else
    END_TIME=$(date +%s)
    DURATION=$((END_TIME - START_TIME))

    echo ""
    echo "=========================================="
    echo -e "${RED}測試執行失敗 ✗${NC}"
    echo "=========================================="
    echo "執行時間: ${DURATION} 秒"
    echo ""

    echo "問題排查建議："
    echo "---------------"
    echo ""
    echo "1. 編譯錯誤："
    echo "   mvn clean compile test-compile -pl rbgi -am"
    echo ""
    echo "2. 查看詳細日誌："
    echo "   $MVN_CMD -X"
    echo ""
    echo "3. 查看測試輸出："
    echo "   cat $PROJECT_ROOT/rbgi/target/surefire-reports/*.txt"
    echo ""
    echo "4. 跳過測試執行（僅編譯驗證）："
    echo "   mvn clean compile test-compile -pl rbgi -am -DskipTests"
    echo ""

    echo "常見問題："
    echo "---------"
    echo "- No tests were executed! → 升級 Surefire 插件到 3.0.0-M7+"
    echo "- Mock 驗證失敗 → 使用 ArgumentCaptor 檢查參數"
    echo "- 編譯錯誤 → 清理並重新編譯"
    echo ""

    exit 1
fi
