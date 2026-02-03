# 功能開發文檔 #2275：黑名單新增USDT錢包地址

## 需求概述

在風控管理系統的黑名單功能中新增 USDT 錢包地址作為監控維度，允許管理員將特定的 USDT 錢包地址加入黑名單，防止該地址用戶進行交易或註冊。

## 變更模組總覽

| 模組 | Commit | 說明 |
|------|--------|------|
| plt-gateway | d8a30116 | 新增 USDT 錢包地址維度到黑名單 |
| plt-gateway | 8cdd905a | 修復查詢參數維度最大值 |
| plt-basics | 5f5d85d1 | 新增錯誤碼定義 |
| plt-user | b24cf743 | 新增 USDT_ADDRESS 枚舉值 |
| plt-user | acd00301 | 修復查詢參數維度最大值 |

---

## 各模組詳細變更

### plt-gateway

#### Commit d8a30116 (2025-08-21)

**作者**: dexter <dexter@mr9.online>

**變更說明**: 新增 USDT 錢包地址維度到黑名單

**變更文件**:
| 文件 | 變更類型 |
|------|----------|
| `.../model/risk/dto/BlackListAddDto.java` | 修改 |

**變更詳情**:

**文件**: `src/main/java/com/galaxy/pltgateway/model/risk/dto/BlackListAddDto.java`
```diff
- @Schema(description = "監控維度0:IP, 1:device_id, 2:身分證字號, 3:手機號碼, 4:銀行卡卡號")
+ @Schema(description = "監控維度0:IP, 1:device_id, 2:身分證字號, 3:手機號碼, 4:銀行卡卡號, 5:USDT錢包地址")
- @Max(value = 4, message = "監控維度最大值為1")
+ @Max(value = 5, message = "監控維度最大值為5")
```

**說明**: 更新 `BlackListAddDto` 的監控維度最大值從 4 改為 5，新增 USDT 錢包地址維度。

---

#### Commit 8cdd905a (2025-08-28)

**作者**: dexter <dexter@mr9.online>

**變更說明**: 修復查詢參數維度最大值

**變更文件**:
| 文件 | 變更類型 |
|------|----------|
| `.../model/report/dto/BlackListQueryDto.java` | 修改 |

**變更詳情**:

**文件**: `src/main/java/com/galaxy/pltgateway/model/report/dto/BlackListQueryDto.java`
```diff
- @Parameter(description = "監控維度0:IP, 1:device_id, 2:身分證字號, 3:手機號碼, 4:銀行卡卡號")
+ @Parameter(description = "監控維度0:IP, 1:device_id, 2:身分證字號, 3:手機號碼, 4:銀行卡卡號, 5:USDT錢包地址")
- @Max(value = 4, message = "監控維度最大值為4")
+ @Max(value = 5, message = "監控維度最大值為5")
```

**說明**: 更新 `BlackListQueryDto` 的查詢參數，支持按 USDT 錢包地址維度查詢黑名單。

---

### plt-basics

#### Commit 5f5d85d1 (2025-08-22)

**作者**: dexter <dexter@mr9.online>

**變更說明**: 新增錯誤碼定義

**變更文件**:
| 文件 | 變更類型 |
|------|----------|
| `.../migration/pg/common/V20250827110133__add_error_code_risk.sql` | 新增 |

**變更詳情**:

**文件**: `src/main/resources/migration/pg/common/V20250827110133__add_error_code_risk.sql`
```sql
UPDATE ${tenant}_error_code_version
SET version = version + 1
WHERE language IN ('TW', 'ZH', 'EN');

INSERT INTO host_error_code (language, type, show_type, http_status, error_code, description) VALUES
('EN', 'CLIENT_SIDE_RISK_ERROR', 'TOAST', 400, '017009', 'Please enter a valid wallet address. If you have any questions, please contact customer support.') ON CONFLICT (language, error_code) DO NOTHING,
('TW', 'CLIENT_SIDE_RISK_ERROR', 'TOAST', 400, '017009', '請輸入有效的錢包地址資訊，如有疑問，請聯繫客服') ON CONFLICT (language, error_code) DO NOTHING,
('ZH', 'CLIENT_SIDE_RISK_ERROR', 'TOAST', 400, '017009', '请输入有效的钱包地址资讯，如有疑问，请联繫客服') ON CONFLICT (language, error_code) DO NOTHING;
```

**說明**: 新增錯誤碼 `017009`，用於 USDT 錢包地址格式驗證失敗時的提示訊息。

---

### plt-user

#### Commit b24cf743 (2025-08-28)

**作者**: dexter <dexter@mr9.online>

**變更說明**: 新增 USDT_ADDRESS 枚舉值

**變更文件**:
| 文件 | 變更類型 |
|------|----------|
| `.../enumeration/black/DimensionType.java` | 修改 |

**變更詳情**:

**文件**: `src/main/java/com/galaxy/enumeration/black/DimensionType.java`
```diff
 public enum DimensionType {
     IP(0, "IP"),
     DEVICE_ID(1, "DEVICE_ID"),
     ID_NUMBER(2, "ID_NUMBER"),
     MOBILE_NUMBER(3, "MOBILE_NUMBER"),
     BANK_CARD_NUMBER(4, "BANK_CARD_NUMBER"),
+    USDT_ADDRESS(5, "USDT_ADDRESS"),
     ;
```

**說明**: 在 `DimensionType` 枚舉中新增 `USDT_ADDRESS` 類型，code 值為 5。

---

#### Commit acd00301 (2025-08-28)

**作者**: dexter <dexter@mr9.online>

**變更說明**: 修復查詢參數維度最大值

**變更文件**:
| 文件 | 變更類型 |
|------|----------|
| `.../model/user/dto/BlackListQueryDto.java` | 修改 |

**變更詳情**:

**文件**: `src/main/java/com/galaxy/model/user/dto/BlackListQueryDto.java`
```diff
- @Max(value = 4, message = "監控維度最小值為1")
+ @Max(value = 5, message = "監控維度最大值為5")
```

**說明**: 更新 `BlackListQueryDto` 的維度最大值限制。

---

## 數據模型變更

### 枚舉變更

**文件**: `plt-user/src/main/java/com/galaxy/enumeration/black/DimensionType.java`

```java
// 變更後
public enum DimensionType {
    IP(0, "IP"),
    DEVICE_ID(1, "DEVICE_ID"),
    ID_NUMBER(2, "ID_NUMBER"),
    MOBILE_NUMBER(3, "MOBILE_NUMBER"),
    BANK_CARD_NUMBER(4, "BANK_CARD_NUMBER"),
    USDT_ADDRESS(5, "USDT_ADDRESS"),  // 新增
    ;
}
```

| Code | 列舉值 | 描述 |
|------|--------|------|
| 0 | IP | IP 地址 |
| 1 | DEVICE_ID | 設備 ID |
| 2 | ID_NUMBER | 身分證字號 |
| 3 | MOBILE_NUMBER | 手機號碼 |
| 4 | BANK_CARD_NUMBER | 銀行卡卡號 |
| 5 | **USDT_ADDRESS** | **USDT 錢包地址（新增）** |

---

## API 變更

### 新增黑名單 API

**路徑**: `POST /api/v1/blackList`

**請求參數** (`BlackListAddDto`):
```json
{
    "dimension": 5,          // 監控維度：5 = USDT 錢包地址
    "type": 0,              // 類型：0 = 黑名單
    "value": "TXyz...abc",  // USDT 錢包地址
    "remark": "備註說明"    // 可選，最多 500 字符
}
```

**驗證規則**:
- `dimension`: 必填，範圍 0-5
- `type`: 必填，值為 0
- `value`: 必填，最多 120 字符

### 查詢黑名單列表 API

**路徑**: `GET /api/v1/blackList/list`

**查詢參數** (`BlackListQueryDto`):
| 參數 | 類型 | 說明 |
|------|------|------|
| from | OffsetDateTime | 監控時間開始（必填） |
| to | OffsetDateTime | 監控時間結束（必填） |
| dimension | Integer | 監控維度 0-5（可選） |
| type | Integer | 類型 0:黑名單（可選） |
| value | String | 監控內容（可選） |
| remark | String | 備註（可選，模糊搜索） |
| page | Integer | 頁碼（必填） |
| size | Integer | 每頁數量（必填） |

---

## 數據庫變更

### Migration 文件

**文件**: `plt-basics/src/main/resources/migration/pg/common/V20250827110133__add_error_code_risk.sql`

```sql
UPDATE ${tenant}_error_code_version
SET version = version + 1
WHERE language IN ('TW', 'ZH', 'EN');

INSERT INTO host_error_code (language, type, show_type, http_status, error_code, description) VALUES
('EN', 'CLIENT_SIDE_RISK_ERROR', 'TOAST', 400, '017009', 'Please enter a valid wallet address. If you have any questions, please contact customer support.') ON CONFLICT (language, error_code) DO NOTHING,
('TW', 'CLIENT_SIDE_RISK_ERROR', 'TOAST', 400, '017009', '請輸入有效的錢包地址資訊，如有疑問，請聯繫客服') ON CONFLICT (language, error_code) DO NOTHING,
('ZH', 'CLIENT_SIDE_RISK_ERROR', 'TOAST', 400, '017009', '请输入有效的钱包地址资讯，如有疑问，请联繫客服') ON CONFLICT (language, error_code) DO NOTHING;
```

**說明**: 新增錯誤碼定義，支持三語言。

---

## 錯誤碼變更

### 017009 - 錢包地址格式無效

| 語言 | 錯誤訊息 |
|------|----------|
| EN | Please enter a valid wallet address. If you have any questions, please contact customer support. |
| TW | 請輸入有效的錢包地址資訊，如有疑問，請聯繫客服 |
| ZH | 请输入有效的钱包地址资讯，如有疑问，请联繫客服 |

**屬性**:
- Type: `CLIENT_SIDE_RISK_ERROR`
- Show Type: `TOAST`
- HTTP Status: `400`

---

## 調用鏈分析

### 模組間關係

```
plt-gateway (API 層)
    ↓ Feign
plt-user (核心服務)
    ↓ MyBatis
PostgreSQL (數據庫)

plt-basics (錯誤碼)
    ↑ Migration
host_error_code 表
```

### 完整調用鏈

1. **Controller 層** (plt-gateway)
   - 文件: `.../controller/risk/BlackListController.java`
   - 方法: `insert(@RequestBody BlackListAddDto dto)`

2. **DomainService 層** (plt-gateway)
   - 文件: `.../domain/risk/impl/BlackListDomainServiceImpl.java`
   - 調用: `userAggregationFeignClient.addBlackList(dto)`

3. **Controller 層** (plt-user)
   - 文件: `.../controller/v1/BlackListController.java`
   - 方法: `add(@RequestBody BlackListAddDto dto)`

4. **DomainService 層** (plt-user)
   - 文件: `.../domain/impl/BlackListDomainServiceImpl.java`
   - 方法: `insert(dto, accountName)`

5. **Service 層** (plt-user)
   - 文件: `.../service/impl/BlackListServiceImpl.java`
   - 操作: `insert(entity)`, `syncData(id)`

6. **Mapper 層** (plt-user)
   - 文件: `.../mapper/BlackListMapper.java`
   - 操作: MyBatis Plus BaseMapper

---

## 注意事項

1. **Bug**: `plt-gateway/BlackListQueryDto.java` 中的錯誤訊息仍顯示 "監控維度最大值為4"，需修正為 "監控維度最大值為5"

2. **USDT 地址驗證**: 目前代碼中只有手機號碼的格式驗證 (`validateMobileNumber`)，未見 USDT 地址的格式驗證邏輯。可能需要在前端或其他層級實施驗證。

3. **數據庫遷移**: 需要執行 Flyway 遷移腳本 `V20250827110133__add_error_code_risk.sql` 來更新錯誤碼版本和新增錯誤訊息。

4. **向後兼容性**: 此變更向後兼容，新增的維度值 5 不影響現有的 0-4 維度功能。

---

## 相關文件

| 類型 | 路徑 |
|------|------|
| Gateway Controller | `plt-gateway/src/main/java/com/galaxy/pltgateway/controller/risk/BlackListController.java` |
| Gateway DTO | `plt-gateway/src/main/java/com/galaxy/pltgateway/model/risk/dto/BlackListAddDto.java` |
| Gateway Query DTO | `plt-gateway/src/main/java/com/galaxy/pltgateway/model/report/dto/BlackListQueryDto.java` |
| Enum | `plt-user/src/main/java/com/galaxy/enumeration/black/DimensionType.java` |
| Migration | `plt-basics/src/main/resources/migration/pg/common/V20250827110133__add_error_code_risk.sql` |
