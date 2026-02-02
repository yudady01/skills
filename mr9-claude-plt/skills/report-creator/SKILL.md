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

**重要**：讀取 `references/module-config.yaml` 獲取該模組的配置，特別注意：
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
| 單一 VO、無子單、無隱碼需求 | `assets/simple-handler.java` |
| 有子單 OR 需要隱碼處理 | `assets/complex-handler.java` |
| 使用游標分頁 (reportagg 模組) | 需要使用 `ExportBatchVo` 模式 |

### Step 5: 生成代碼

1. 從 `references/module-config.yaml` 獲取目標模組配置
2. 從 `assets/` 選擇適合的模板
3. 生成 Handler 類別代碼
4. 生成 `ReportType` 枚舉新增項
5. 提供完整代碼供用戶審核

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

- 簡單報表：查看 `references/RechargeProxyReport.java`
- 複雜報表：查看 `references/WithdrawSummaryReport.java`
- 用戶模組報表：查看 `references/UserQueryReport.java`

---

## 完整實作步驟

### Step 1: 分析 API

根據用戶提供的 cURL 命令或 API 路徑，分析：
1. 請求方法和路徑
2. 查詢參數（Query DTO）
3. 響應資料結構（Response VO）
4. 目標模組

### Step 2: 查找相關代碼

使用 Task tool 或 Explore agent 查找：
- Controller 層：確認 API 入口
- DTO/VO 類別：分析資料結構
- DomainService/FeignClient：確認資料來源方法

### Step 3: 向用戶確認需求

通過 AskUserQuestion 確認：
1. **子單處理方式**：
   - 只導出主訂單
   - 展開子訂單（每個子訂單一行）
   - 合併顯示
2. **是否需要隱碼處理**
3. **資料來源類型**：DomainService 或 FeignClient
4. **CSV 欄位列表**：確認需要導出的欄位

### Step 4: 創建 Handler 類別

1. 根據需求選擇模板（`simple-handler.java` 或 `complex-handler.java`）
2. 讀取 `references/module-config.yaml` 獲取模組配置
3. 替換模板參數生成代碼
4. 寫入到 `${MODULE}/src/main/java/com/galaxy/handler/downloadReportHanlder/impl/`

**注意事項**：
- `plt-fund-aggregation` 的枚舉 import：
  - `WithdrawStatus`: `com.galaxy.enumeration.fund.WithdrawStatus`
  - `WithdrawMode`: `com.galaxy.enumeration.WithdrawMode`
  - `OsType`: `com.galaxy.enumeration.OsType`
- 子單展開時，主單顯示 `--`，子單顯示實際值

### Step 5: 同步更新 ReportType 枚舉

**必須同步三個模組的 ReportType**：

| 模組 | 路徑 | 格式 |
|------|------|------|
| plt-fund-aggregation | `enumeration/basics/ReportType.java` | `ENUM_NAME("描述")` |
| plt-basics | `enumeration/ReportType.java` | `ENUM_NAME("routing-key", "描述", "csv")` |
| plt-gateway | `enumeration/basics/ReportType.java` | `ENUM_NAME("權限代碼")` |

**命名規則**：
- 枚舉名稱：`PLT_REPORT_{FEATURE}_DOWNLOAD`
- 權限代碼：`module:feature:action:export`
- 例如：`PLT_REPORT_WITHDRAW_APPROVE_OVERVIEW_DOWNLOAD` → `fund:withdraw:approveOverview:export`

### Step 6: 創建 Migration 權限文件

1. 查找最新的 migration 文件版本號
2. 創建新文件：`V{yyyyMMddHHmmss}__add_auth_{feature}.sql`
3. 路徑：`plt-account/src/main/resources/migration/pg/common/`

**SQL 模板**：
```sql
-- 新增父權限
INSERT INTO ${tenant}_authority (name, authority, pid, type, creator_id, creator)
VALUES ('功能名稱', 'module:feature:action',
        (SELECT id FROM ${tenant}_authority WHERE authority = 'module:feature'), 0, 1, 'superAdmin')
ON CONFLICT (authority) DO NOTHING;

-- 新增導出子權限
INSERT INTO ${tenant}_authority (name, authority, pid, type, creator_id, creator)
VALUES ('导出', 'module:feature:action:export',
        (SELECT id FROM ${tenant}_authority WHERE authority = 'module:feature:action'), 1, 1, 'superAdmin')
ON CONFLICT (authority) DO NOTHING;
```

### Step 7: 驗證編譯

```bash
cd ${MODULE}
mvn compile -DskipTests
```

確保沒有編譯錯誤。

---

## 實作範例：提現審批概觀報表

### 輸入
```
curl 'https://admin-ot888-sit.mr9.site/api/v1/fund/withdraw/manage/approve-overview/list?page=1&size=100...'
```

### 輸出文件
1. **Handler**: `WithdrawApproveOverviewReport.java`
2. **ReportType** (3個模組同步)
3. **Migration**: `V20260202120000__add_auth_withdraw_approve_overview.sql`

### 關鍵代碼片段

#### Handler 類別結構
```java
@Component
@RequiredArgsConstructor
public class WithdrawApproveOverviewReport implements DownloadReportHandler {
    private final WithdrawManageDomainService withdrawManageDomainService;
    private final BasicFeignClient basicFeignClient;
    private final ObjectMapper mapper;

    @Override
    public ReportType type() {
        return ReportType.PLT_REPORT_WITHDRAW_APPROVE_OVERVIEW_DOWNLOAD;
    }

    @Override
    public void handle(ReportQryVo qryVo) {
        // 分頁查詢 + 隱碼處理 + CSV 生成
    }
}
```

#### 子單展開邏輯
```java
// 主單行：託售子單號 顯示 "--"
row.add("--");

// 子單行：展開 subList，每個子單一行
for (WithdrawChildPayOverviewVo child : record.getSubList()) {
    row.add(child.getOrderSubId()); // 實際子單號
}
```
