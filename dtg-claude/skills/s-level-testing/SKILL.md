---
name: s-level-testing
description: 執行 S 級標準的單元測試，包括環境檢查、測試執行、覆蓋率驗證和問題排查
---

# S 級測試執行 Skill

## 概述

本 Skill 幫助 AI Agent 自動執行和管理 S 級標準的測試流程，適用於 DTG-Pay 項目中的 `rbgi` 模組。

**適用場景**：
- 執行自動退避模組的單元測試
- 驗證測試覆蓋率是否達到 S 級標準（語句 100%，分支 100%）
- 診斷並解決常見測試問題
- 生成測試報告

## 核心能力

| 能力 | 描述 | 支援工具 |
|------|------|---------|
| **環境檢查** | 驗證 Java、Maven、Spring Boot 等前置條件 | `check_environment.sh` |
| **依賴檢查** | 確認 `pom.xml` 包含必要的測試依賴 | Maven |
| **測試執行** | 運行單元測試、指定測試類、生成報告 | `run_tests.sh` |
| **覆蓋率驗證** | 檢查語句/分支覆蓋率是否達到 100% | `check_coverage.sh` |
| **問題排查** | 自動診斷常見測試問題並提供解決方案 | 內置決策樹 |

## S 級測試標準

| 維度 | S 級標準 |
|------|---------|
| **質量等級** | 🛩️ S級 - 航空級 (DO-178C) |
| **測試覆蓋** | 語句 100%, 分支 100% |
| **測試類型** | 單元測試 + 集成測試 + 性能測試 |
| **審查要求** | 雙人審查 |

---

## 執行流程

### 步驟 1：環境檢查

檢測開發環境是否滿足測試要求：

```bash
bash .agent/skills/s-level-testing/scripts/check_environment.sh
```

**檢查項目**：
- ✅ Java 版本 ≥ 8
- ✅ Maven 版本 ≥ 3.6
- ✅ `rbgi/pom.xml` 文件存在
- ✅ 測試依賴是否正確配置

**預期輸出**：
```
✓ Java 版本: 11.0.18
✓ Maven 版本: 3.8.6
✓ 項目目錄: /path/to/rbgi/pom.xml
✓ 測試依賴檢查通過
環境檢查通過 ✓
```

---

### 步驟 2：編譯測試代碼

確保測試代碼可以正常編譯：

```bash
mvn clean test-compile -pl rbgi -am
```

**預期結果**：`BUILD SUCCESS`

**常見問題**：
- 如果編譯失敗，運行 `mvn clean` 清理後重試
- 檢查是否有導入語句缺失或類型不兼容錯誤

---

### 步驟 3：執行測試

根據需求執行測試：

#### 3.1 運行所有測試

```bash
bash .agent/skills/s-level-testing/scripts/run_tests.sh
```

或直接使用 Maven：

```bash
mvn test -pl rbgi -am
```

#### 3.2 運行指定測試類

```bash
# 使用腳本
bash .agent/skills/s-level-testing/scripts/run_tests.sh RetryBackoffStrategyTest

# 使用 Maven
mvn test -pl rbgi -am -Dtest=RetryBackoffStrategyTest
mvn test -pl rbgi -am -Dtest=CallbackServiceTest
mvn test -pl rbgi -am -Dtest=CallbackSenderTest
```

#### 3.3 運行多個測試類

```bash
mvn test -pl rbgi -am -Dtest="*RetryBackoffStrategyTest,*CallbackServiceTest,*CallbackSenderTest"
```

#### 3.4 生成測試報告

```bash
mvn surefire-report:report -pl rbgi
```

報告位置：`rbgi/target/site/surefire-report.html`

---

### 步驟 4：生成覆蓋率報告

```bash
bash .agent/skills/s-level-testing/scripts/check_coverage.sh
```

或使用 Maven：

```bash
mvn clean test jacoco:report -pl rbgi
```

覆蓋率報告位置：`rbgi/target/site/jacoco/index.html`

---

### 步驟 5：驗證覆蓋率

檢查覆蓋率是否達到 S 級標準：

| 指標 | S 級要求 | 驗證命令 |
|------|---------|---------|
| **語句覆蓋率** | 100% | `check_coverage.sh` 輸出 |
| **分支覆蓋率** | 100% | `check_coverage.sh` 輸出 |
| **函數覆蓋率** | 100% | `check_coverage.sh` 輸出 |
| **類覆蓋率** | 100% | `check_coverage.sh` 輸出 |

**預期輸出**：
```
覆蓋率報告已生成：rbgi/target/site/jacoco/index.html

覆蓋率驗證結果：
┌─────────────────┬──────────┬──────────┬─────────┐
│ 指標            │ 實際值   │ S級標準  │ 狀態    │
├─────────────────┼──────────┼──────────┼─────────┤
│ 語句覆蓋率      │ 100%     │ 100%     │ ✓ PASS  │
│ 分支覆蓋率      │ 100%     │ 100%     │ ✓ PASS  │
│ 函數覆蓋率      │ 100%     │ 100%     │ ✓ PASS  │
│ 類覆蓋率        │ 100%     │ 100%     │ ✓ PASS  │
└─────────────────┴──────────┴──────────┴─────────┘
✓ 所有覆蓋率指標均達到 S 級標準
```

---

## 測試用例檢查表

### RetryBackoffStrategyTest（11 個用例）

| 用例ID | 測試方法 | 測試場景 | 預期結果 |
|--------|----------|----------|----------|
| RT-001 | `testGetMaxRetryCount` | 獲取最大重試次數 | 返回 12 |
| RT-002 | `testCalculateDelay_NormalRetryCount` | 正常重試次數（1-12） | 返回對應延遲時間 |
| RT-003 | `testCalculateDelay_ExceededMaxRetry` | 超過最大重試次數（13+） | 返回最後一個延遲時間（240000ms） |
| RT-004 | `testCalculateDelay_MinRetryCount` | 最小重試次數（1） | 返回 5000ms |
| RT-005 | `testCalculateDelay_MaxRetryCount` | 最大重試次數（12） | 返回 240000ms |
| RT-006 | `testCalculateDelay_InvalidRetryCount` | 無效重試次數（0, -1） | 拋出 IllegalArgumentException |
| RT-007 | `testIsExceededMaxRetry` | 判斷是否超過最大重試次數 | 返回 true/false |
| RT-008 | `testIsExceededMaxRetry_AtMax` | 重試次數等於最大值 | 返回 false |
| RT-009 | `testIsExceededMaxRetry_OneMoreThanMax` | 重試次數=最大值+1 | 返回 true |
| RT-010 | `testGetDelayMilliseconds` | 獲取延遲時間數組 | 返回完整數組 |
| RT-011 | `testDelayTimeConstants` | 驗證常量定義 | 常量值正確 |

**執行示例**：
```bash
mvn test -pl rbgi -am -Dtest=RetryBackoffStrategyTest
```

**預期輸出**：
```
Tests run: 11, Failures: 0, Errors: 0, Skipped: 0
```

---

### CallbackServiceTest（7 個用例）

| 用例ID | 測試方法 | 測試場景 | 預期結果 |
|--------|----------|----------|----------|
| CS-001 | `testCallback_Success` | 通知成功 | 更新狀態為 SUCCESS，不發送重試 |
| CS-002 | `testCallback_Failure_FirstRetry` | 第 1 次失敗重試 | 更新狀態為 PROCESS，發送延遲 5000ms 重試 |
| CS-003 | `testCallback_Failure_LastRetry` | 第 12 次失敗重試 | 更新狀態為 PROCESS，發送延遲 240000ms 重試 |
| CS-004 | `testCallback_Failure_RetryExhausted` | 第 13 次失敗（重試耗盡） | 更新狀態為 FAILED，不發送重試 |
| CS-005 | `testCallback_Failure_HttpSuccessButNotSuccessBody` | HTTP 成功但響應不是 SUCCESS | 更新狀態為 PROCESS，發送重試 |
| CS-006 | `testCallback_NotifyNotFound` | 通知記錄不存在 | 拋出 BusinessException |
| CS-007 | `testSend` | send 方法委託 | 正確調用 CallbackSender |

**執行示例**：
```bash
mvn test -pl rbgi -am -Dtest=CallbackServiceTest
```

**預期輸出**：
```
Tests run: 7, Failures: 0, Errors: 0, Skipped: 0
```

---

### CallbackSenderTest（11 個用例）

| 用例ID | 測試方法 | 測試場景 | 預期結果 |
|--------|----------|----------|----------|
| CS-001 | `testSend_Milliseconds_Success` | 正常發送（毫秒級） | 成功發送，屬性設置正確 |
| CS-002 | `testSend_Seconds_Deprecated` | 向後兼容（秒級） | 成功發送，延遲轉換為毫秒 |
| CS-003 | `testSend_NullNotifyId` | notifyId 為 null | 拋出 IllegalArgumentException |
| CS-004 | `testSend_NegativeDelay` | 延遲時間為 0 | 允許（邊界值） |
| CS-005 | `testSend_JMSException` | JMS 設置屬性異常 | 拋出 RuntimeException |
| CS-006 | `testSend_ConvertAndSendException` | convertAndSend 異常 | 拋出 DelayMessageSendException |
| CS-007 | `testSend_DelayMismatch` | 延遲時間不匹配 | 記錄警告但不拋異常 |
| CS-008 | `testSend_RepeatMismatch` | 重複次數不匹配 | 記錄警告但不拋異常 |
| CS-009 | `testSend_DeliveryModeMismatch` | 持久化模式不匹配 | 記錄警告但不拋異常 |
| CS-010 | `testSend_NullProperties` | 消息屬性為 null | 正常完成 |
| CS-011 | `testDelayMessageSendException` | 異常類測試 | 異常信息正確 |

**執行示例**：
```bash
mvn test -pl rbgi -am -Dtest=CallbackSenderTest
```

**預期輸出**：
```
Tests run: 11, Failures: 0, Errors: 0, Skipped: 0
```

---

## 問題排查決策樹

### 問題 1：測試無法運行

**症狀**：`No tests were executed!`

**診斷流程**：
```
開始
  ├─ 檢查 Surefire 插件版本
  │   ├─ 版本 < 3.0.0-M7 → 升級到 3.0.0-M7 或更高
  │   └─ 版本正常 → 檢查測試類命名
  │       ├─ 不符合規範 → 修正類名（Test 結尾）
  │       └─ 符合規範 → 檢查包路徑
  │           ├─ 路徑錯誤 → 移動到正確目錄
  │           └─ 路徑正確 → 跳過測試執行，僅編譯驗證
```

**解決方案**：

**方案 1：升級 Surefire 插件（推薦）**

在 `rbgi/pom.xml` 中添加或更新：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0-M7</version>
        </plugin>
    </plugins>
</build>
```

**方案 2：跳過測試執行（僅編譯驗證）**

```bash
mvn clean compile test-compile -pl rbgi -am -DskipTests
```

---

### 問題 2：Mock 對象驗證失敗

**症狀**：`Wanted but not invoked` 或 `Unnecessary stubbing`

**診斷流程**：
```
開始
  ├─ 檢查 Mock 對象配置
  │   ├─ 配置不正確 → 修正 Mock 配置
  │   └─ 配置正確 → 檢查方法調用順序
  │       ├─ 順序不匹配 → 使用 InOrder 驗證
  │       └─ 順序正確 → 檢查參數匹配
  │           ├─ 參數不精確 → 使用 ArgumentCaptor
  │           └─ 參數正確 → 使用寬鬆驗證
```

**解決方案**：

**使用 ArgumentCaptor 捕獲參數**：

```java
ArgumentCaptor<Long> captor = ArgumentCaptor.forClass(Long.class);
Mockito.verify(mock).method(captor.capture());
Assertions.assertEquals(expected, captor.getValue());
```

**使用寬鬆的驗證**：

```java
Mockito.verify(mock, Mockito.atLeastOnce()).method(Mockito.any());
```

**使用 InOrder 驗證調用順序**：

```java
InOrder inOrder = Mockito.inOrder(mock1, mock2);
inOrder.verify(mock1).method1();
inOrder.verify(mock2).method2();
```

---

### 問題 3：編譯錯誤

**症狀**：`cannot find symbol` 或 `incompatible types`

**診斷流程**：
```
開始
  ├─ 檢查導入語句
  │   ├─ 導入缺失 → 添加必要的 import
  │   └─ 導入正確 → 檢查方法簽名
  │       ├─ 簽名不匹配 → 修正方法調用
  │       └─ 簽名正確 → 檢查類型兼容性
  │           ├─ 類型不兼容 → 進行類型轉換
  │           └─ 類型正確 → 清理並重新編譯
```

**解決方案**：

**清理並重新編譯**：

```bash
mvn clean compile test-compile -pl rbgi -am
```

**檢查導入語句**：

確保所有必要的 import 都已添加：

```java
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import org.junit.jupiter.api.Assertions;
```

---

### 問題 4：覆蓋率不達標

**症狀**：語句或分支覆蓋率 < 100%

**診斷流程**：
```
開始
  ├─ 查看覆蓋率報告
  │   ├─ 找出未覆蓋的代碼行
  │   └─ 分析未覆蓋的原因
  │       ├─ 死代碼 → 刪除或標記為 @Deprecated
  │       ├─ 條件分支未測試 → 添加測試用例
  │       └─ 異常場景未測試 → 添加異常測試
  │           ├─ 添加邊界值測試
  │           └─ 添加異常處理測試
  │               └─ 重新運行測試並驗證
```

**解決方案**：

**1. 查看覆蓋率報告**：

打開 `rbgi/target/site/jacoco/index.html`，查找紅色標記的未覆蓋代碼。

**2. 添加測試用例**：

根據未覆蓋的代碼路徑，添加相應的測試用例：

```java
@Test
void testBoundaryCase() {
    // 測試邊界值
    // ...
}

@Test
void testExceptionCase() {
    // 測試異常場景
    // ...
}
```

**3. 重新運行測試**：

```bash
mvn clean test jacoco:report -pl rbgi
```

---

### 問題 5：測試超時

**症狀**：測試執行時間過長或超時

**診斷流程**：
```
開始
  ├─ 檢查測試執行時間
  │   ├─ 單個測試超時 → 使用 @Timeout 設置超時
  │   └─ 全部測試慢 → 檢查資源消耗
  │       ├─ 資源洩漏 → 修復洩漏問題
  │       └─ 等待時間過長 → 使用 Mockito.when 代替實際等待
```

**解決方案**：

**設置測試超時**：

```java
@Test
@Timeout(value = 5, unit = TimeUnit.SECONDS)
void testShouldCompleteWithin5Seconds() {
    // 測試代碼
}
```

**使用 Mockito 模擬等待**：

```java
// 避免 Thread.sleep(5000)
Mockito.when(service.delay()).thenReturn(true);
```

---

## 調試技巧

### 1. 啟用詳細日誌

```bash
mvn test -pl rbgi -am -Dtest=CallbackServiceTest -X
```

### 2. 單步調試

在 IDE 中設置斷點，使用調試模式運行測試：
- IntelliJ IDEA：右鍵測試方法 → Debug
- Eclipse：右鍵測試方法 → Debug As → JUnit Test

### 3. 查看測試輸出

```bash
cat rbgi/target/surefire-reports/*.txt
```

---

## 驗證清單

在測試完成後，使用以下清單進行驗證：

- [ ] 所有測試類編譯通過
- [ ] 所有測試用例執行通過（Failures: 0, Errors: 0）
- [ ] 測試覆蓋率 ≥ 100%（語句、分支）
- [ ] 所有邊界值測試通過
- [ ] 所有異常場景測試通過
- [ ] Mock 對象驗證正確
- [ ] 無關鍵警告（允許 deprecation 警告）

---

## 參考資料

- [EZPAY-768 測試指南](/Users/tommy/Documents/work.nosync/dtg/dtg-pay/doc/EZPAY-768_2025-12-12_测试指南_S级标准.md)
- [測試用例參考](/Users/tommy/Documents/work.nosync/dtg/dtg-pay/.agent/skills/s-level-testing/resources/test_case_reference.md)
- [JaCoCo 官方文檔](https://www.jacoco.org/jacoco/trunk/doc/)
- [Maven Surefire 插件文檔](https://maven.apache.org/surefire/maven-surefire-plugin/)

---

**Skill 版本**: v1.0
**創建日期**: 2025-01-24
**最後更新**: 2025-01-24
**適用項目**: dtg-pay/rbgi
