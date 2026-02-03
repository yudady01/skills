# Report Creator Skill - 優化後計畫

## 優化重點

### 🔧 問題一：模組獨立處理

建立**模組配置映射表**，讓 Skill 能自動識別各模組的差異：

```yaml
# 模組配置映射表
modules:
  plt-fund-aggregation:
    name: "財務模組"
    report_type_path: "com.galaxy.enumeration.basics.ReportType"
    handler_interface_path: "com.galaxy.handler.downloadReportHanlder.DownloadReportHandler"
    handler_impl_path: "com.galaxy.handler.downloadReportHanlder.impl"
    report_qry_vo_path: "com.galaxy.model.basic.vo.ReportQryVo"
    mq_queue: "plt.basic.report.topic.fund-report-download.q"
    has_mask_factory: true
    mask_factory_path: "com.galaxy.utils.ReportMaskFactory"
    
  plt-activity-aggregation:
    name: "活動模組"
    report_type_path: "com.galaxy.enumeration.ReportType"  # 注意：路徑不同！
    handler_interface_path: "com.galaxy.handler.downloadReportHanlder.DownloadReportHandler"
    handler_impl_path: "com.galaxy.handler.downloadReportHanlder.impl"
    report_qry_vo_path: "com.galaxy.model.basic.vo.ReportQryVo"
    mq_queue: "plt.basic.report.topic.activity-download.q"
    has_mask_factory: false
    
  plt-proxy-aggregation:
    name: "代理模組"
    report_type_path: "com.galaxy.enumeration.basics.ReportType"
    handler_interface_path: "com.galaxy.handler.downloadReportHanlder.DownloadReportHandler"
    handler_impl_path: "com.galaxy.handler.downloadReportHanlder.impl"
    report_qry_vo_path: "com.galaxy.model.basic.vo.ReportQryVo"
    mq_queue: "plt.basic.report.topic.proxy-download.q"
    has_mask_factory: false
    
  plt-reportagg:
    name: "報表模組"
    report_type_path: "com.galaxy.enumeration.basics.ReportType"
    handler_interface_path: "com.galaxy.handler.downloadReportHanlder.DownloadReportHandler"
    handler_impl_path: "com.galaxy.handler.downloadReportHanlder.impl"
    report_qry_vo_path: "com.galaxy.model.basic.vo.ReportQryVo"
    mq_queue: "plt.basic.report.topic.report-download.q"
    has_mask_factory: true

  plt-user-aggregation:
    name: "用戶模組"
    report_type_path: "com.galaxy.enumeration.basics.ReportType"
    handler_interface_path: "com.galaxy.handler.downloadReportHanlder.DownloadReportHandler"
    handler_impl_path: "com.galaxy.handler.downloadReportHanlder.impl"
    report_qry_vo_path: "com.galaxy.model.basic.vo.ReportQryVo"
    mq_queue: "plt.basic.report.topic.user-download.q"
    has_mask_factory: false
    # 注意：utils 路徑不同！
    report_convert_utils_path: "com.galaxy.util.ReportConvertUtils"  # 其他模組是 com.galaxy.utils
```

---

### 🔧 問題三：其他潛在問題

經進一步分析發現以下問題，需要在 Skill 中處理：

#### 3.1 ReportConvertUtils 工具類獨立副本

每個模組都有獨立的 `ReportConvertUtils` 工具類，且 **package 路徑可能不同**：

| 模組 | 路徑 |
|------|------|
| plt-fund-aggregation | `com.galaxy.utils.ReportConvertUtils` |
| plt-activity-aggregation | `com.galaxy.utils.ReportConvertUtils` |
| plt-proxy-aggregation | `com.galaxy.utils.ReportConvertUtils` |
| plt-reportagg | `com.galaxy.utils.ReportConvertUtils` |
| **plt-user-aggregation** | `com.galaxy.util.ReportConvertUtils` ⚠️ 不同！ |

#### 3.2 資料來源可能是 DomainService 或 FeignClient

報表處理器的資料來源不統一：

| 模式 | 說明 | 範例 |
|------|------|------|
| DomainService | 調用本地 Domain 層服務 | `withdrawManageDomainService.findSummaryList()` |
| FeignClient | 調用遠端 Feign 接口 | `proxyFeignClient.proxyReplaceList()` |

Skill 需要讓用戶選擇資料來源類型。

#### 3.3 searchParam 需額外提取參數

從 `qryVo.getSearchParam()` 中需要額外提取的常見參數：

```java
// 常見參數
String language = String.valueOf(qryVo.getSearchParam().get(H_KEY_LANGUAGE));
String currency = String.valueOf(qryVo.getSearchParam().get(H_KEY_CURRENCY));
String defaultLanguage = String.valueOf(qryVo.getSearchParam().get(H_KEY_DEFAULT_LANGUAGE));
Long adminId = Long.parseLong(qryVo.getSearchParam().get(H_KEY_ACCT_ID).toString());
```

Skill 需要分析 Query DTO 來判斷需要哪些額外參數。

#### 3.4 Enum 轉換處理

報表中常見的 Enum 轉名稱處理：

```java
// 需要識別 VO 中的 Enum 欄位並生成轉換代碼
row.add(WithdrawStatus.valueOf(record.getStatus()).getName());
row.add(OsType.valueOf(record.getClientType()).getDesc());
row.add(record.getUserType().equals(UserType.CLIENT.getClientType()) ? "會員" : "代理");
```

#### 3.5 BasicFeignClient 名稱不統一 ⚠️

| 模組 | 類別名稱 | import 路徑 |
|------|----------|-------------|
| plt-fund-aggregation | `BasicFeignClient` | `com.galaxy.feign.client.basic.BasicFeignClient` |
| plt-activity-aggregation | `BasicsFeignClient` | `com.galaxy.feign.client.basics.BasicsFeignClient` |
| plt-proxy-aggregation | `BasicsFeignClient` | `com.galaxy.feign.client.basic.BasicsFeignClient` |
| plt-reportagg | `BasicsFeignClient` | `com.galaxy.feign.client.basic.BasicsFeignClient` |

#### 3.6 plt-reportagg 枚舉路徑特殊

`plt-reportagg` 的 `ReportType` 枚舉路徑是 `com.galaxy.enumeration.ReportType`（與 activity 相同，不是 `enumeration.basics`）

#### 3.7 分頁方式有兩種

| 方式 | 說明 | 範例模組 |
|------|------|----------|
| PageVo 分頁 | 使用 `page`/`size` 參數 | fund, activity, proxy |
| ExportBatchVo 游標分頁 | 使用 `lastSortValues` 游標 | reportagg (GameDailyReport) |

#### 3.8 plt-game-aggregation 無報表架構

`plt-game-aggregation` 沒有 `DownloadReportHandler` 架構，不需要加入配置。

---

### 🔧 完整模組配置映射表 (更新版)

```yaml
modules:
  plt-fund-aggregation:
    name: "財務模組"
    report_type_path: "com.galaxy.enumeration.basics.ReportType"
    handler_impl_path: "com.galaxy.handler.downloadReportHanlder.impl"
    report_qry_vo_path: "com.galaxy.model.basic.vo.ReportQryVo"
    report_update_dto_path: "com.galaxy.model.basic.dto.ReportUpdateDto"
    basic_feign_client: "com.galaxy.feign.client.basic.BasicFeignClient"
    basic_feign_client_name: "BasicFeignClient"
    page_vo_path: "com.galaxy.module.model.vo.PageVo"
    report_convert_utils_path: "com.galaxy.utils.ReportConvertUtils"
    has_mask_factory: true
    mask_factory_path: "com.galaxy.utils.ReportMaskFactory"
    
  plt-activity-aggregation:
    name: "活動模組"
    report_type_path: "com.galaxy.enumeration.ReportType"
    handler_impl_path: "com.galaxy.handler.downloadReportHanlder.impl"
    report_qry_vo_path: "com.galaxy.model.basic.vo.ReportQryVo"
    report_update_dto_path: "com.galaxy.model.basic.dto.ReportUpdateDto"
    basic_feign_client: "com.galaxy.feign.client.basics.BasicsFeignClient"
    basic_feign_client_name: "BasicsFeignClient"
    page_vo_path: "com.galaxy.module.model.vo.PageVo"
    report_convert_utils_path: "com.galaxy.utils.ReportConvertUtils"
    has_mask_factory: false
    
  plt-proxy-aggregation:
    name: "代理模組"
    report_type_path: "com.galaxy.enumeration.basics.ReportType"
    handler_impl_path: "com.galaxy.handler.downloadReportHanlder.impl"
    report_qry_vo_path: "com.galaxy.model.basic.vo.ReportQryVo"
    report_update_dto_path: "com.galaxy.model.basic.dto.ReportUpdateDto"
    basic_feign_client: "com.galaxy.feign.client.basic.BasicsFeignClient"
    basic_feign_client_name: "BasicsFeignClient"
    page_vo_path: "com.galaxy.module.model.vo.PageVo"
    report_convert_utils_path: "com.galaxy.utils.ReportConvertUtils"
    has_mask_factory: false
    
  plt-reportagg:
    name: "報表模組"
    report_type_path: "com.galaxy.enumeration.ReportType"
    handler_impl_path: "com.galaxy.handler.downloadReportHanlder.impl"
    report_qry_vo_path: "com.galaxy.model.basic.vo.ReportQryVo"
    report_update_dto_path: "com.galaxy.model.basic.dto.ReportUpdateDto"
    basic_feign_client: "com.galaxy.feign.client.basic.BasicsFeignClient"
    basic_feign_client_name: "BasicsFeignClient"
    page_vo_path: "com.galaxy.module.model.vo.PageVo"
    report_convert_utils_path: "com.galaxy.utils.ReportConvertUtils"
    has_mask_factory: false  # 修正：此模組沒有 ReportMaskFactory
    supports_cursor_pagination: true  # 支援游標分頁 (ExportBatchVo)

  plt-user-aggregation:
    name: "用戶模組"
    # ⚠️ 此模組與其他模組差異極大，需特別注意！
    report_type_path: "com.galaxy.enumeration.ReportType"  # 其他是 enumeration.basics
    handler_interface_path: "com.galaxy.handler.downloadReportHandler.DownloadReportHandler"  # 注意：沒有 Hanlder 拼寫錯誤！
    handler_impl_path: "com.galaxy.handler.downloadReportHandler.impl"  # 同上
    report_qry_vo_path: "com.galaxy.model.vo.ReportQryVo"  # 其他是 model.basic.vo
    report_update_dto_path: "com.galaxy.model.dto.ReportUpdateDto"  # 其他是 model.basic.dto
    basic_feign_client: "com.galaxy.feign.client.basics.BasicsReportFeignClient"  # 完全不同的類別！
    basic_feign_client_name: "BasicsReportFeignClient"  # 完全不同！
    page_vo_path: "com.galaxy.module.model.vo.PageVo"
    report_convert_utils_path: "com.galaxy.util.ReportConvertUtils"  # util 不是 utils
    has_mask_factory: true
    mask_factory_path: "com.galaxy.util.ReportMaskFactory"  # util 不是 utils
```

---

### 🔧 問題四：Handler 路徑拼寫錯誤問題

| 模組 | Handler 路徑 | 說明 |
|------|--------------|------|
| plt-fund-aggregation | `downloadReportHanlder` | ⚠️ 拼寫錯誤 (Hanlder) |
| plt-activity-aggregation | `downloadReportHanlder` | ⚠️ 拼寫錯誤 |
| plt-proxy-aggregation | `downloadReportHanlder` | ⚠️ 拼寫錯誤 |
| plt-reportagg | `downloadReportHanlder` | ⚠️ 拼寫錯誤 |
| **plt-user-aggregation** | `downloadReportHandler` | ✅ 正確拼寫！ |

不再是獨立 Java 應用，改為 **Gemini Skill 標準格式**：

```
.agent/skills/report-creator/
├── SKILL.md                    # 主要指令文檔 (必須)
├── module-config.yaml          # 模組配置映射表
├── templates/                  # 代碼模板
│   ├── simple-handler.java     # 簡單報表模板
│   └── complex-handler.java    # 複雜報表模板 (含子單、隱碼)
└── examples/                   # 現有報表範例參考
    ├── RechargeProxyReport.java    # 簡單範例
    └── WithdrawSummaryReport.java  # 複雜範例
```

---

## SKILL.md 內容設計

```markdown
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

### Step 1: 收集資訊

向用戶確認以下資訊：

| 項目 | 說明 | 範例 |
|------|------|------|
| 目標模組 | fund/activity/proxy/report | `plt-fund-aggregation` |
| 資料來源 API | 提供資料的 API 路徑 | `/api/v1/fund/withdraw/manage/summary/list` |
| Query DTO | 查詢參數類別 | `QueryWithdrawSummaryDto` |
| Response VO | 響應資料類別 | `WithdrawVo` |
| 報表名稱 | 中文描述 | `出款匯總報表` |
| 權限 | 權限字串 | `fund:withdraw:summary:export` |

### Step 2: 分析 VO 結構

1. 讀取 Response VO 類別
2. 識別所有欄位及其類型
3. 向用戶確認 CSV 欄位順序與標題

### Step 3: 識別模式

根據以下條件選擇模板：

| 條件 | 使用模板 |
|------|----------|
| 單一 VO、無子單、無隱碼需求 | `simple-handler.java` |
| 有子單 OR 需要隱碼處理 | `complex-handler.java` |

### Step 4: 生成代碼

1. 從 `module-config.yaml` 獲取目標模組配置
2. 新增 `ReportType` 枚舉項
3. 生成 Handler 類別
4. 提供完整代碼供用戶審核

### Step 5: 驗證

- 確認 import 路徑正確
- 確認枚舉值不重複
- 確認 CSV 欄位與 VO 欄位對應

## 代碼模板參數

| 參數 | 說明 |
|------|------|
| `${MODULE}` | 目標模組名稱 |
| `${HANDLER_CLASS}` | Handler 類別名稱 |
| `${REPORT_TYPE_ENUM}` | 枚舉值名稱 |
| `${REPORT_TYPE_DESC}` | 枚舉描述 |
| `${QUERY_DTO_CLASS}` | Query DTO 類別 |
| `${RESPONSE_VO_CLASS}` | Response VO 類別 |
| `${DOMAIN_SERVICE}` | DomainService 類別 |
| `${CSV_TITLES}` | CSV 標題列表 |
| `${CSV_ROWS}` | CSV 欄位映射代碼 |
```

---

## 簡單模板設計

```java
// templates/simple-handler.java
package ${HANDLER_IMPL_PACKAGE};

import com.fasterxml.jackson.databind.ObjectMapper;
import ${REPORT_TYPE_IMPORT};
import ${FEIGN_CLIENT_IMPORT};
import ${HANDLER_INTERFACE_IMPORT};
import ${REPORT_UPDATE_DTO_IMPORT};
import ${REPORT_QRY_VO_IMPORT};
import ${QUERY_DTO_IMPORT};
import ${RESPONSE_VO_IMPORT};
import ${PAGE_VO_IMPORT};
import java.util.ArrayList;
import java.util.List;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

import static ${HEADER_KEY_IMPORT}.H_KEY_LANGUAGE;
import static ${REPORT_CONVERT_UTILS_IMPORT}.convertString;

@Slf4j
@Component
@RequiredArgsConstructor
public class ${HANDLER_CLASS} implements DownloadReportHandler {

    private final static long MAX_SIZE = 500L;
    private final static long START_PAGE = 1L;
    
    private final ${FEIGN_CLIENT_CLASS} feignClient;
    private final BasicFeignClient basicFeignClient;
    private final ObjectMapper mapper;

    @Override
    public ReportType type() {
        return ReportType.${REPORT_TYPE_ENUM};
    }

    @Override
    public void handle(ReportQryVo qryVo) {
        log.info("[${REPORT_TYPE_ENUM}], START");
        
        ${QUERY_DTO_CLASS} queryDto = mapper.convertValue(
            qryVo.getSearchParam(), ${QUERY_DTO_CLASS}.class);
        Integer timezone = qryVo.getTimezone();
        String language = String.valueOf(qryVo.getSearchParam().get(H_KEY_LANGUAGE));
        
        queryDto.setPage(START_PAGE);
        queryDto.setSize(MAX_SIZE);

        long current;
        long pages;
        PageVo<${RESPONSE_VO_CLASS}> pageVo;
        
        do {
            pageVo = feignClient.${API_METHOD}(language, queryDto).getData();
            makeReport(qryVo, pageVo, pageVo.getPages(), pageVo.getCurrent(), timezone);

            current = pageVo.getCurrent() + 1;
            queryDto.setPage(current);
            pages = pageVo.getPages();
        } while (!pageVo.getRecords().isEmpty() && current <= pages);

        log.info("[${REPORT_TYPE_ENUM}], END");
    }

    private List<List<String>> createCsvRowsData(List<${RESPONSE_VO_CLASS}> records, Integer timezone) {
        List<List<String>> rows = new ArrayList<>();

        for (${RESPONSE_VO_CLASS} record : records) {
            List<String> row = new ArrayList<>();
            
            ${CSV_ROWS}

            rows.add(row);
        }
        return rows;
    }

    private void makeReport(ReportQryVo qryVo, PageVo<${RESPONSE_VO_CLASS}> pageVo, 
                           Long totalPage, Long currentPage, Integer timezone) {
        ReportUpdateDto dto = new ReportUpdateDto();
        dto.setId(qryVo.getId());
        dto.setReportExportType("CSV");
        dto.setTitles(List.of(${CSV_TITLES}));
        dto.setRows(createCsvRowsData(pageVo.getRecords(), timezone));
        dto.setTotalPage(totalPage.intValue());
        dto.setCurrentPage(currentPage.intValue());
        
        basicFeignClient.makeReportDocument(dto);
        log.info("[${HANDLER_CLASS}], dto:{}", dto);
    }
}
```

---

## 檔案目標位置

生成的文件放置位置：

| 文件類型 | 位置 |
|----------|------|
| Handler | `${MODULE}/src/main/java/${HANDLER_IMPL_PACKAGE}/${HANDLER_CLASS}.java` |
| ReportType | `${MODULE}/src/main/java/${REPORT_TYPE_PACKAGE}/ReportType.java` (修改) |

---

## 成功指標

| 項目 | 狀態 |
|------|------|
| AI 能根據 VO 自動識別 CSV 欄位 | 待實現 |
| 自動選擇正確的模組配置 | 待實現 |
| 生成代碼通過編譯 | 待實現 |
| 枚舉值不重複 | 待實現 |
