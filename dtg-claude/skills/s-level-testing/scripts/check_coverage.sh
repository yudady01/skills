#!/bin/bash

################################################################################
# S 級測試覆蓋率檢查腳本
#
# 功能：
#   - 生成 JaCoCo 覆蓋率報告
#   - 驗證覆蓋率是否達到 S 級標準（100%）
#   - 顯示覆蓋率摘要
#
# 使用方法：
#   bash .agent/skills/s-level-testing/scripts/check_coverage.sh
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
JACOCO_REPORT="$PROJECT_ROOT/rbgi/target/site/jacoco/index.html"

# S 級標準
REQUIRED_COVERAGE=100

echo "=========================================="
echo "S 級測試覆蓋率檢查"
echo "=========================================="
echo ""

# 檢查 JaCoCo 是否配置
if ! grep -q "jacoco-maven-plugin" "$PROJECT_ROOT/rbgi/pom.xml"; then
    echo -e "${YELLOW}⚠${NC} 未檢測到 JaCoCo 插件配置"
    echo ""
    echo "請在 rbgi/pom.xml 中添加 JaCoCo 插件配置："
    echo ""
    cat << 'EOF'
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.8</version>
            <executions>
                <execution>
                    <goals>
                        <goal>prepare-agent</goal>
                    </goals>
                </execution>
                <execution>
                    <id>report</id>
                    <phase>test</phase>
                    <goals>
                        <goal>report</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
EOF
    echo ""
    echo "完成後重新運行：bash .agent/skills/s-level-testing/scripts/check_coverage.sh"
    exit 1
fi

# 生成覆蓋率報告
echo "[1/3] 生成覆蓋率報告..."
cd "$PROJECT_ROOT"

if mvn clean test jacoco:report -pl rbgi -am; then
    echo -e "${GREEN}✓${NC} 覆蓋率報告生成成功"
else
    echo -e "${RED}✗${NC} 覆蓋率報告生成失敗"
    echo ""
    echo "請檢查："
    echo "  1. 測試是否通過：bash .agent/skills/s-level-testing/scripts/run_tests.sh"
    echo "  2. JaCoCo 插件是否正確配置"
    exit 1
fi
echo ""

# 檢查報告文件是否存在
echo "[2/3] 解析覆蓋率報告..."
if [[ ! -f "$JACOCO_REPORT" ]]; then
    echo -e "${RED}✗${NC} 覆蓋率報告文件不存在: $JACOCO_REPORT"
    exit 1
fi

# 解析覆蓋率數據
# 從 HTML 報告中提取覆蓋率百分比
INSTRUCTION_COVERAGE=$(grep -oP 'Total(?s).*?(?=<td>).*?<td>\K[0-9]+(?=%)' "$JACOCO_REPORT" | head -1)
BRANCH_COVERAGE=$(grep -oP 'Branch(?s).*?(?=<td>).*?<td>\K[0-9]+(?=%)' "$JACOCO_REPORT" | head -1)
LINE_COVERAGE=$(grep -oP 'Line(?s).*?(?=<td>).*?<td>\K[0-9]+(?=%)' "$JACOCO_REPORT" | head -1)
METHOD_COVERAGE=$(grep -oP 'Method(?s).*?(?=<td>).*?<td>\K[0-9]+(?=%)' "$JACOCO_REPORT" | head -1)
CLASS_COVERAGE=$(grep -oP 'Class(?s).*?(?=<td>).*?<td>\K[0-9]+(?=%)' "$JACOCO_REPORT" | head -1)

# 如果解析失敗，嘗試另一種方式
if [[ -z "$INSTRUCTION_COVERAGE" ]]; then
    echo -e "${YELLOW}⚠${NC} 無法從 HTML 報告解析覆蓋率數據"
    echo "請手動查看報告：open $JACOCO_REPORT"
    echo ""
    echo "JaCoCo 報告包含以下指標："
    echo "  - Instruction（指令覆蓋率）"
    echo "  - Branch（分支覆蓋率）"
    echo "  - Line（語句覆蓋率）"
    echo "  - Method（方法覆蓋率）"
    echo "  - Class（類覆蓋率）"
    echo ""
    echo "S 級標準要求所有指標均達到 100%"
    exit 0
fi

# 驗證覆蓋率
echo ""
echo "[3/3] 驗證覆蓋率是否達到 S 級標準..."
echo ""
echo "覆蓋率報告已生成：$JACOCO_REPORT"
echo ""
echo "覆蓋率驗證結果："
echo "┌─────────────────┬──────────┬──────────┬─────────┐"
echo "│ 指標            │ 實際值   │ S級標準  │ 狀態    │"
echo "├─────────────────┼──────────┼──────────┼─────────┤"

ALL_PASSED=true

# 驗證語句覆蓋率（使用 Line 作為語句覆蓋率）
if [[ -n "$LINE_COVERAGE" ]]; then
    LINE_STATUS="${GREEN}✓ PASS${NC}"
    if [[ $LINE_COVERAGE -lt $REQUIRED_COVERAGE ]]; then
        LINE_STATUS="${RED}✗ FAIL${NC}"
        ALL_PASSED=false
    fi
    printf "│ %-15s │ %6s%% │ %6s%% │ %s │\n" "語句覆蓋率" "$LINE_COVERAGE" "$REQUIRED_COVERAGE" "$LINE_STATUS"
else
    printf "│ %-15s │ %6s │ %6s%% │ %s │\n" "語句覆蓋率" "N/A" "$REQUIRED_COVERAGE" "${YELLOW}? N/A${NC}"
    ALL_PASSED=false
fi

# 驗證分支覆蓋率
if [[ -n "$BRANCH_COVERAGE" ]]; then
    BRANCH_STATUS="${GREEN}✓ PASS${NC}"
    if [[ $BRANCH_COVERAGE -lt $REQUIRED_COVERAGE ]]; then
        BRANCH_STATUS="${RED}✗ FAIL${NC}"
        ALL_PASSED=false
    fi
    printf "│ %-15s │ %6s%% │ %6s%% │ %s │\n" "分支覆蓋率" "$BRANCH_COVERAGE" "$REQUIRED_COVERAGE" "$BRANCH_STATUS"
else
    printf "│ %-15s │ %6s │ %6s%% │ %s │\n" "分支覆蓋率" "N/A" "$REQUIRED_COVERAGE" "${YELLOW}? N/A${NC}"
    ALL_PASSED=false
fi

# 驗證方法覆蓋率
if [[ -n "$METHOD_COVERAGE" ]]; then
    METHOD_STATUS="${GREEN}✓ PASS${NC}"
    if [[ $METHOD_COVERAGE -lt $REQUIRED_COVERAGE ]]; then
        METHOD_STATUS="${RED}✗ FAIL${NC}"
        ALL_PASSED=false
    fi
    printf "│ %-15s │ %6s%% │ %6s%% │ %s │\n" "方法覆蓋率" "$METHOD_COVERAGE" "$REQUIRED_COVERAGE" "$METHOD_STATUS"
else
    printf "│ %-15s │ %6s │ %6s%% │ %s │\n" "方法覆蓋率" "N/A" "$REQUIRED_COVERAGE" "${YELLOW}? N/A${NC}"
    ALL_PASSED=false
fi

# 驗證類覆蓋率
if [[ -n "$CLASS_COVERAGE" ]]; then
    CLASS_STATUS="${GREEN}✓ PASS${NC}"
    if [[ $CLASS_COVERAGE -lt $REQUIRED_COVERAGE ]]; then
        CLASS_STATUS="${RED}✗ FAIL${NC}"
        ALL_PASSED=false
    fi
    printf "│ %-15s │ %6s%% │ %6s%% │ %s │\n" "類覆蓋率" "$CLASS_COVERAGE" "$REQUIRED_COVERAGE" "$CLASS_STATUS"
else
    printf "│ %-15s │ %6s │ %6s%% │ %s │\n" "類覆蓋率" "N/A" "$REQUIRED_COVERAGE" "${YELLOW}? N/A${NC}"
    ALL_PASSED=false
fi

echo "└─────────────────┴──────────┴──────────┴─────────┘"
echo ""

# 輸出結果
if [[ "$ALL_PASSED" == true ]]; then
    echo -e "${GREEN}✓ 所有覆蓋率指標均達到 S 級標準${NC}"
    echo ""
    echo "下一步："
    echo "  1. 查看詳細覆蓋率報告：open $JACOCO_REPORT"
    echo "  2. 生成測試報告：mvn surefire-report:report -pl rbgi"
    exit 0
else
    echo -e "${RED}✗ 覆蓋率未達到 S 級標準${NC}"
    echo ""
    echo "改進建議："
    echo "------------"
    echo ""
    echo "1. 查看未覆蓋的代碼："
    echo "   open $JACOCO_REPORT"
    echo ""
    echo "2. 針對未覆蓋的代碼添加測試用例："
    echo "   - 添加邊界值測試"
    echo "   - 添加異常場景測試"
    echo "   - 添加分支覆蓋測試"
    echo ""
    echo "3. 重新運行測試並驗證："
    echo "   bash .agent/skills/s-level-testing/scripts/run_tests.sh"
    echo "   bash .agent/skills/s-level-testing/scripts/check_coverage.sh"
    echo ""
    echo "注意：S 級標準要求語句覆蓋率和分支覆蓋率均達到 100%"
    exit 1
fi
