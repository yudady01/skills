---
name: report-creator
description: 根據資料來源 API 自動生成報表處理器代碼
---

# Report Creator Skill

## 觸發條件

當用戶請求以下任務時使用此 Skill：
- 創建新的報表下載功能
- 為現有 API 添加報表導出
- 生成 CSV 下載處理器

## 執行流程

### Step 1: 確認目標模組

向用戶確認目標模組，可選項：

| 模組 | 說明 |
|------|------|
| `plt-fund-aggregation` | 財務模組 (充值、提現、轉帳) |
| `plt-activity-aggregation` | 活動模組 |
| `plt-proxy-aggregation` | 代理模組 |
| `plt-reportagg` | 報表模組 (遊戲注單) |
| `plt-user-aggregation` | 用戶模組 |

**重要**：讀取 `module-config.yaml` 獲取該模組的配置，特別注意：
- `plt-user-aggregation` 與其他模組差異極大（路徑、類名都不同）
- Handler 路徑拼寫：大多數模組是 `downloadReportHanlder`（拼錯），但 `plt-user-aggregation` 是 `downloadReportHandler`（正確）

### Step 2: 收集資訊

向用戶確認以下資訊：

| 項目 | 說明 | 範例 |
|------|------|------|
| 資料來源類型 | DomainService 或 FeignClient | `FeignClient` |
| 資料來源類別 | 注入的 Service/Client 類名 | `ProxyFeignClient` |
| API 方法 | 調用的方法名稱 | `proxyReplaceList` |
| Query DTO | 查詢參數類別全路徑 | `com.galaxy.model.proxy.dto.ProxyQueryDto` |
| Response VO | 響應資料類別全路徑 | `com.galaxy.model.proxy.vo.ProxyQueryVo` |
| 報表名稱 | 中文描述 | `代理列表報表` |
| ReportType 枚舉值 | 枚舉常量名稱 | `PLT_PROXY_LIST_DOWNLOAD` |
| 是否需要隱碼 | 是否使用 ReportMaskFactory | `否` |
| 是否有子單 | 是否有嵌套資料結構 | `否` |

### Step 3: 分析 VO 結構

1. 讀取 Response VO 類別
2. 識別所有欄位及其類型
3. 向用戶確認 CSV 欄位順序與中文標題
4. 識別需要特殊處理的欄位：
   - 時間欄位：需要 `convertString(record.getXxxTime(), timezone)`
   - 數字欄位：需要 `convertString(record.getAmount())`
   - Enum 欄位：需要轉換邏輯如 `record.getStatus().getName()`
   - 可 null 欄位：需要 `convertString(record.getXxx(), "--")`

### Step 4: 識別模式並選擇模板

| 條件 | 使用模板 |
|------|----------|
| 單一 VO、無子單、無隱碼需求 | `templates/simple-handler.java` |
| 有子單 OR 需要隱碼處理 | `templates/complex-handler.java` |
| 使用游標分頁 (reportagg 模組) | 需要使用 `ExportBatchVo` 模式 |

### Step 5: 生成代碼

1. 從 `module-config.yaml` 獲取目標模組配置
2. 生成 Handler 類別代碼
3. 生成 `ReportType` 枚舉新增項
4. 提供完整代碼供用戶審核

### Step 6: 驗證

- [ ] 確認 import 路徑正確（根據模組配置）
- [ ] 確認枚舉值不重複
- [ ] 確認 CSV 欄位與 VO 欄位對應
- [ ] 確認分頁邏輯正確

---

## 代碼模板參數

| 參數 | 說明 |
|------|------|
| `${HANDLER_IMPL_PACKAGE}` | Handler 實現包路徑 |
| `${HANDLER_CLASS}` | Handler 類別名稱 |
| `${REPORT_TYPE_IMPORT}` | ReportType import 路徑 |
| `${REPORT_TYPE_ENUM}` | 枚舉值名稱 |
| `${REPORT_TYPE_DESC}` | 枚舉描述（中文） |
| `${QUERY_DTO_IMPORT}` | Query DTO import 路徑 |
| `${QUERY_DTO_CLASS}` | Query DTO 類別名稱 |
| `${RESPONSE_VO_IMPORT}` | Response VO import 路徑 |
| `${RESPONSE_VO_CLASS}` | Response VO 類別名稱 |
| `${DATA_SOURCE_IMPORT}` | 資料來源（FeignClient/DomainService）import |
| `${DATA_SOURCE_CLASS}` | 資料來源類別名稱 |
| `${DATA_SOURCE_FIELD}` | 資料來源欄位名稱 |
| `${API_METHOD}` | API 方法名稱 |
| `${CSV_TITLES}` | CSV 標題列表 |
| `${CSV_ROWS}` | CSV 欄位映射代碼 |

---

## 檔案目標位置

| 文件類型 | 位置 |
|----------|------|
| Handler | `${MODULE}/src/main/java/com/galaxy/handler/downloadReportHanlder/impl/${HANDLER_CLASS}.java` |
| ReportType | `${MODULE}/src/main/java/com/galaxy/enumeration/.../ReportType.java` (新增枚舉項) |

**注意**：`plt-user-aggregation` 的 Handler 路徑是 `downloadReportHandler`（正確拼寫）

---

## 範例參考

- 簡單報表：查看 `examples/RechargeProxyReport.java`
- 複雜報表：查看 `examples/WithdrawSummaryReport.java`
- 用戶模組報表：查看 `examples/UserQueryReport.java`
