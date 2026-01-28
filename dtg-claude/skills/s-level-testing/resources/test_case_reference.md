# 測試用例參考文檔

> **Skill 類型**: s-level-testing
> **適用項目**: dtg-pay/rbgi
> **最後更新**: 2025-01-24

---

## 目錄

1. [重試延遲策略表](#重試延遲策略表)
2. [RetryBackoffStrategyTest 用例](#retrybackoffstrategytest-用例)
3. [CallbackServiceTest 用例](#callbackservicetest-用例)
4. [CallbackSenderTest 用例](#callbacksendertest-用例)

---

## 重試延遲策略表

| 重試次數 | 延遲時間(ms) | 延遲時間(秒) | 累計時間(秒) | 說明 |
|---------|-------------|-------------|------------|------|
| 1 | 5,000 | 5秒 | 5秒 | 首次重試，5秒延遲 |
| 2 | 5,000 | 5秒 | 10秒 | 第二次重試，5秒延遲 |
| 3 | 5,000 | 5秒 | 15秒 | 第三次重試，5秒延遲 |
| 4 | 5,000 | 5秒 | 20秒 | 第四次重試，5秒延遲 |
| 5 | 10,000 | 10秒 | 30秒 | 第五次重試，延遲增至 10秒 |
| 6 | 10,000 | 10秒 | 40秒 | 第六次重試，10秒延遲 |
| 7 | 10,000 | 10秒 | 50秒 | 第七次重試，10秒延遲 |
| 8 | 60,000 | 1分鐘 | 1分50秒 | 第八次重試，延遲增至 1分鐘 |
| 9 | 60,000 | 1分鐘 | 2分50秒 | 第九次重試，1分鐘延遲 |
| 10 | 60,000 | 1分鐘 | 3分50秒 | 第十次重試，1分鐘延遲 |
| 11 | 120,000 | 2分鐘 | 5分50秒 | 第十一次重試，延遲增至 2分鐘 |
| 12 | 240,000 | 4分鐘 | 9分50秒 | 最後一次重試，延遲增至 4分鐘 |

**總重試次數**: 12 次
**最大累計時間**: 9分50秒（590秒）

---

## RetryBackoffStrategyTest 用例

### 測試目標

驗證退避策略工具類的所有功能，包括：
- 延遲時間計算
- 最大重試次數
- 邊界值處理
- 異常場景處理

### 用例詳情

| 用例ID | 測試方法 | 測試場景 | 輸入參數 | 預期輸出 | 備註 |
|--------|----------|----------|---------|---------|------|
| RT-001 | `testGetMaxRetryCount` | 獲取最大重試次數 | 無 | `12` | 驗證常量定義 |
| RT-002 | `testCalculateDelay_NormalRetryCount` | 正常重試次數 | `1` ~ `12` | 對應的延遲時間 | 測試所有有效重試次數 |
| RT-003 | `testCalculateDelay_ExceededMaxRetry` | 超過最大重試次數 | `13`, `100` | `240000` | 返回最後一個延遲時間 |
| RT-004 | `testCalculateDelay_MinRetryCount` | 最小重試次數 | `1` | `5000` | 邊界值測試 |
| RT-005 | `testCalculateDelay_MaxRetryCount` | 最大重試次數 | `12` | `240000` | 邊界值測試 |
| RT-006 | `testCalculateDelay_InvalidRetryCount` | 無效重試次數 | `0`, `-1`, `-10` | 拋出 `IllegalArgumentException` | 異常場景 |
| RT-007 | `testIsExceededMaxRetry` | 判斷是否超過最大重試次數 | `1` ~ `12` | `false` | 未超過 |
| RT-008 | `testIsExceededMaxRetry_AtMax` | 重試次數等於最大值 | `12` | `false` | 邊界值測試 |
| RT-009 | `testIsExceededMaxRetry_OneMoreThanMax` | 重試次數=最大值+1 | `13` | `true` | 邊界值測試 |
| RT-010 | `testGetDelayMilliseconds` | 獲取延遲時間數組 | 無 | 完整的延遲數組 | 驗證數組完整性 |
| RT-011 | `testDelayTimeConstants` | 驗證常量定義 | 無 | 常量值正確 | 驗證硬編碼值 |

### 執行命令

```bash
# 運行所有用例
mvn test -pl rbgi -am -Dtest=RetryBackoffStrategyTest

# 運行單個用例
mvn test -pl rbgi -am -Dtest=RetryBackoffStrategyTest#testGetMaxRetryCount
```

### 預期輸出

```
Tests run: 11, Failures: 0, Errors: 0, Skipped: 0
```

### 關鍵測試數據

```java
// 預期的延遲時間數組
private static final int[] DELAY_MILLISECONDS = {
    5000,   // 1次
    5000,   // 2次
    5000,   // 3次
    5000,   // 4次
    10000,  // 5次
    10000,  // 6次
    10000,  // 7次
    60000,  // 8次
    60000,  // 9次
    60000,  // 10次
    120000, // 11次
    240000  // 12次
};

// 最大重試次數
private static final int MAX_RETRY_COUNT = 12;
```

---

## CallbackServiceTest 用例

### 測試目標

驗證回調通知服務的所有業務場景，包括：
- 通知成功處理
- 通知失敗重試
- 重試耗盡處理
- 異常場景處理

### 用例詳情

| 用例ID | 測試方法 | 測試場景 | 初始狀態 | HTTP 響應 | 預期狀態 | 預期操作 |
|--------|----------|----------|---------|-----------|---------|---------|
| CS-001 | `testCallback_Success` | 通知成功 | `count=0` | `SUCCESS` | `SUCCESS` | 不發送重試 |
| CS-002 | `testCallback_Failure_FirstRetry` | 第 1 次失敗重試 | `count=0` | 失敗 | `PROCESS` | 發送延遲 5000ms 重試 |
| CS-003 | `testCallback_Failure_LastRetry` | 第 12 次失敗重試 | `count=11` | 失敗 | `PROCESS` | 發送延遲 240000ms 重試 |
| CS-004 | `testCallback_Failure_RetryExhausted` | 第 13 次失敗（重試耗盡） | `count=12` | 失敗 | `FAILED` | 不發送重試 |
| CS-005 | `testCallback_Failure_HttpSuccessButNotSuccessBody` | HTTP 成功但響應不是 SUCCESS | `count=0` | HTTP 200 但內容非 SUCCESS | `PROCESS` | 發送重試 |
| CS-006 | `testCallback_NotifyNotFound` | 通知記錄不存在 | 無 | N/A | 拋出 `BusinessException` | N/A |
| CS-007 | `testSend` | send 方法委託 | 任意 | N/A | 正確調用 `CallbackSender` | 驗證調用 |

### Mock 對象說明

| Mock 對象 | 用途 | 關鍵方法 |
|----------|------|---------|
| `NotifyDao` | 模擬數據庫操作 | `updateStatus()`, `findById()` |
| `CallbackSender` | 模擬消息發送 | `send()` |
| `OkHttpClientUtil` | 模擬 HTTP 請求 | `postJson()` |

### 執行命令

```bash
# 運行所有用例
mvn test -pl rbgi -am -Dtest=CallbackServiceTest

# 運行單個用例
mvn test -pl rbgi -am -Dtest=CallbackServiceTest#testCallback_Success
```

### 預期輸出

```
Tests run: 7, Failures: 0, Errors: 0, Skipped: 0
```

### 關鍵測試邏輯

```java
// 重試耗盡判斷
if (count >= MAX_RETRY_COUNT) {
    // 更新狀態為 FAILED
    notify.setNotifyStatus(NotifyStatus.FAILED);
    notify.setNotifyTime(new Date());
    notifyDao.updateStatus(notify);
    return;
}

// 計算延遲時間
long delay = RetryBackoffStrategy.calculateDelay(count + 1);

// 發送延遲消息
callbackSender.send(notifyId, delay);
```

---

## CallbackSenderTest 用例

### 測試目標

驗證回調消息發送器的所有功能，包括：
- 正常消息發送
- 參數驗證
- 異常處理
- 消息屬性驗證

### 用例詳情

| 用例ID | 測試方法 | 測試場景 | 輸入參數 | 預期結果 | 備註 |
|--------|----------|----------|---------|---------|------|
| CS-001 | `testSend_Milliseconds_Success` | 正常發送（毫秒級） | `notifyId=1L, delay=5000` | 成功發送，屬性設置正確 | 使用新的毫秒級 API |
| CS-002 | `testSend_Seconds_Deprecated` | 向後兼容（秒級） | `notifyId=1L, delay=5` | 成功發送，延遲轉換為毫秒 | 向後兼容舊 API |
| CS-003 | `testSend_NullNotifyId` | notifyId 為 null | `notifyId=null, delay=5000` | 拋出 `IllegalArgumentException` | 參數驗證 |
| CS-004 | `testSend_NegativeDelay` | 延遲時間為 0 | `notifyId=1L, delay=0` | 允許（邊界值） | 立即發送 |
| CS-005 | `testSend_JMSException` | JMS 設置屬性異常 | `mock JMS 異常` | 拋出 `RuntimeException` | JMS 異常處理 |
| CS-006 | `testSend_ConvertAndSendException` | convertAndSend 異常 | `mock convertAndSend 異常` | 拋出 `DelayMessageSendException` | 自定義異常 |
| CS-007 | `testSend_DelayMismatch` | 延遲時間不匹配 | `mock 延遲不匹配` | 記錄警告但不拋異常 | 寬鬆驗證 |
| CS-008 | `testSend_RepeatMismatch` | 重複次數不匹配 | `mock 重複次數不匹配` | 記錄警告但不拋異常 | 寬鬆驗證 |
| CS-009 | `testSend_DeliveryModeMismatch` | 持久化模式不匹配 | `mock 持久化模式不匹配` | 記錄警告但不拋異常 | 寬鬆驗證 |
| CS-010 | `testSend_NullProperties` | 消息屬性為 null | `mock properties=null` | 正常完成 | 處理 null 屬性 |
| CS-011 | `testDelayMessageSendException` | 異常類測試 | `new DelayMessageSendException("msg")` | 異常信息正確 | 驗證異常類 |

### Mock 對象說明

| Mock 對象 | 用途 | 關鍵方法 |
|----------|------|---------|
| `Queue` | 模擬 JMS 隊列 | `getQueueName()` |
| `JmsTemplate` | 模擬 JMS 模板 | `convertAndSend()`, `getMessageConverter()` |
| `Message` | 模擬 JMS 消息 | `getLongProperty()`, `getIntProperty()` |

### 執行命令

```bash
# 運行所有用例
mvn test -pl rbgi -am -Dtest=CallbackSenderTest

# 運行單個用例
mvn test -pl rbgi -am -Dtest=CallbackSenderTest#testSend_Milliseconds_Success
```

### 預期輸出

```
Tests run: 11, Failures: 0, Errors: 0, Skipped: 0
```

### 關鍵測試邏輯

```java
// 消息屬性驗證
verify(message).getLongProperty("_AMQ_SCHED_DELIVERY");
verify(message).getLongProperty("notifyId");
verify(message).getIntProperty("repeat");
verify(message).getIntProperty("delay");

// JMS 模板調用驗證
verify(jmsTemplate).convertAndSend(eq(queue), any(NotifyMessage.class));
```

---

## 測試用例統計

### 總計

| 測試類 | 用例數 | 成功標準 |
|--------|-------|---------|
| **RetryBackoffStrategyTest** | 11 | 11/11 通過 |
| **CallbackServiceTest** | 7 | 7/7 通過 |
| **CallbackSenderTest** | 11 | 11/11 通過 |
| **總計** | **29** | **29/29 通過** |

### 覆蓋場景統計

| 場景類型 | 用例數 | 測試類 |
|---------|-------|-------|
| 正常場景 | 12 | 所有 |
| 邊界值測試 | 8 | RetryBackoffStrategyTest, CallbackSenderTest |
| 異常場景 | 9 | 所有測試類 |

---

## 預期輸出示例

### 完整測試執行輸出

```bash
$ mvn test -pl rbgi -am

[INFO] Scanning for projects...
[INFO]
[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running org.xxpay.rbgi.common.RetryBackoffStrategyTest
[INFO] Tests run: 11, Failures: 0, Errors: 0, Skipped: 0
[INFO] Running org.xxpay.rbgi.service.CallbackServiceTest
[INFO] Tests run: 7, Failures: 0, Errors: 0, Skipped: 0
[INFO] Running org.xxpay.rbgi.mq.sender.CallbackSenderTest
[INFO] Tests run: 11, Failures: 0, Errors: 0, Skipped: 0
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
```

### 覆蓋率報告輸出

```bash
$ bash .agent/skills/s-level-testing/scripts/check_coverage.sh

==========================================
S 級測試覆蓋率檢查
==========================================

[1/3] 生成覆蓋率報告...
✓ 覆蓋率報告生成成功

[2/3] 解析覆蓋率報告...

[3/3] 驗證覆蓋率是否達到 S 級標準...

覆蓋率報告已生成：/path/to/rbgi/target/site/jacoco/index.html

覆蓋率驗證結果：
┌─────────────────┬──────────┬──────────┬─────────┐
│ 指標            │ 實際值   │ S級標準  │ 狀態    │
├─────────────────┼──────────┼──────────┼─────────┤
│ 語句覆蓋率      │ 100%     │ 100%     │ ✓ PASS  │
│ 分支覆蓋率      │ 100%     │ 100%     │ ✓ PASS  │
│ 方法覆蓋率      │ 100%     │ 100%     │ ✓ PASS  │
│ 類覆蓋率        │ 100%     │ 100%     │ ✓ PASS  │
└─────────────────┴──────────┴──────────┴─────────┘

✓ 所有覆蓋率指標均達到 S 級標準
```

---

## 相關文檔

- [S 級測試執行 Skill](../SKILL.md)
- [EZPAY-768 測試指南](/Users/tommy/Documents/work.nosync/dtg/dtg-pay/doc/EZPAY-768_2025-12-12_测试指南_S级标准.md)

---

**文檔版本**: v1.0
**創建日期**: 2025-01-24
**最後更新**: 2025-01-24
