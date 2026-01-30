---
name: api-analyzer
description: 分析 cURL 請求並自動生成 API 文檔。當用戶提供 curl 命令時，自動分析請求方法、路徑、請求頭、認證方式、代碼調用鏈，並生成結構化的文檔保存到指定目錄。文檔按 Swagger @Tag 分類組織。
license: MIT
---

# API 分析器

此技能自動分析 cURL 請求並生成結構化的 API 文檔，按照 Swagger @Tag 分類組織目錄，包含完整的代碼調用鏈分析。

## 何時使用此技能

當用戶提供以下內容時使用此技能：
- cURL 命令（curl 開頭的命令）
- API 請求的原始數據
- 需要分析並記錄 API 的情況

## 分析流程

### 1. 解析 cURL 命令

從 cURL 命令中提取以下信息：

| 項目 | 說明 |
|------|------|
| **URL** | 完整的請求地址 |
| **方法** | GET, POST, PUT, DELETE, PATCH 等 |
| **路徑** | API 路徑，提取參數（如 userId） |
| **環境** | 從 URL 域名判斷（sit, uat, prod 等） |

### 2. 解析請求頭

分類分析請求頭：

#### 認證相關
- `token` / `authorization` - 認證令牌
- `sign` / `signature` - 請求簽名
- `timestamp` - 時間戳

#### 設備相關
- `device-id` / `device-id` - 設備標識
- `os-type` / `user-agent` - 操作系統和瀏覽器信息

#### 來源相關
- `referer` - 請求來源頁面
- `origin` - 請求源域名

#### 其他
- `content-type` - 內容類型
- `accept` - 接受的響應類型

### 3. 解析請求體

- 分析請求體內容（JSON、表單數據等）
- 識別請求參數

### 4. 推斷 Swagger @Tag 分類

根據 URL 路徑推斷對應的 Swagger @Tag 分類：

| URL 路徑模式 | @Tag 分類 | 目錄名稱 |
|--------------|-----------|----------|
| `/v1/wallet/game/transfer/*` | 客戶列表/資金往來 | `客戶列表-資金往來` |
| `/v1/wallet/*` | 客戶列表/資金往來 | `客戶列表-資金往來` |
| `/v1/fund/recharge/*` | 財務管理-充值管理-充值列表 | `財務管理-充值管理-充值列表` |
| `/v1/fund/withdraw/*` | 提現管理 | `提現管理` |
| `/v1/fund/*` | 資金配置管理 | `資金配置管理` |
| `/v1/proxy/*` | 代理管理/代理列表 | `代理管理-代理列表` |
| `/v1/user/*` | 客戶管理 | `客戶管理` |
| `/v1/game/*` | 遊戲管理 | `遊戲管理` |
| `/v1/report/*` | 報表管理 | `報表管理` |
| `/v1/risk/*` | 風控管理 | `風控管理` |
| `/v1/activity/*` | 活動管理 | `活動管理` |
| `/v1/basics/*` | 基本配置 | `基本配置` |
| `/v1/account/*` | 帳號管理 | `帳號管理` |
| `/v1/message/*` | 消息管理 | `消息管理` |

### 5. 代碼調用鏈分析

#### 5.1 找到 Controller

根據 URL 路徑和 HTTP 方法，搜索對應的 Controller：

```bash
# 搜索 Controller
# 路徑模式: plt-gateway/src/main/java/com/galaxy/pltgateway/controller/[module]/v1/*Controller.java
# 匹配條件: @RequestMapping 匹配 URL 前綴, @XxxMapping 匹配方法和路徑
```

#### 5.2 追蹤調用鏈

從 Controller 追蹤到實際實現：

```
┌─────────────────────────────────────────────────────────────────┐
│  Gateway 層 (plt-gateway)                                        │
│  ├── Controller: 接收 HTTP 請求                                  │
│  ├── DomainService: 業務邏輯入口                                  │
│  └── FeignClient: 調用其他服務                                   │
└─────────────────────────────────────────────────────────────────┘
                              ↓ Feign
┌─────────────────────────────────────────────────────────────────┐
│  Aggregation 層 (wallet-aggregation, plt-fund-aggregation, ...)  │
│  ├── DomainService: 聚合多個服務                                  │
│  └── FeignClient: 調用下游服務                                   │
└─────────────────────────────────────────────────────────────────┘
                              ↓ Feign
┌─────────────────────────────────────────────────────────────────┐
│  Service 層 (wallet-service, plt-fund, plt-game, ...)           │
│  ├── DomainService: 核心業務邏輯                                 │
│  ├── Service: 數據庫操作                                          │
│  └── Mapper: MyBatis 持久化                                      │
└─────────────────────────────────────────────────────────────────┘
```

#### 5.3 提取關鍵信息

從代碼中提取：

| 信息類型 | 說明 |
|----------|------|
| **方法簽名** | 完整的方法名和參數 |
| **權限控制** | @PreAuthorize 權限要求 |
| **操作日誌** | @ActionLog 操作記錄配置 |
| **事務管理** | @Transactional 事務配置 |
| **核心邏輯** | 主要的業務處理步驟 |
| **依賴服務** | 調用的其他服務 (Feign) |
| **數據庫操作** | 涉及的表和操作類型 |

### 6. 生成文檔

生成包含以下內容的 Markdown 文檔：

```markdown
# API 分析：[功能名稱]

## 請求概況
| 項目 | 值 |
|------|-----|
| **環境** | 環境名稱 |
| **方法** | HTTP 方法 |
| **路徑** | API 路徑模板 |
| **參數** | 提取的參數值 |

## 完整 cURL 命令
\```bash
curl '...' ...
\```

## 請求頭分析
### 認證相關
| 請求頭 | 值 | 說明 |
|--------|-----|------|
... |

### 設備相關
...

### 來源相關
...

## 代碼調用鏈

### Gateway 層 (plt-gateway)
**Controller**: `GameTransferController`
- 文件: `plt-gateway/src/main/java/com/galaxy/pltgateway/controller/wallet/v1/GameTransferController.java`
- 方法: `updateAllGameWallets(@PathVariable Long userId)`
- 權限: `@PreAuthorize("hasAuthority('user:user:detail:financial:wallet:refresh')")`

**DomainService**: `GameTransferDomainServiceImpl`
- 文件: `plt-gateway/src/main/java/com/galaxy/pltgateway/domain/wallet/impl/GameTransferDomainServiceImpl.java`
- 調用: `gameTransferFeignClient.updateAllGameWallets(userId)`

### Aggregation 層 (wallet-aggregation)
**DomainService**: `GameTransferDomainServiceImpl`
- 文件: `wallet-aggregation/src/main/java/com/galaxy/domain/impl/GameTransferDomainServiceImpl.java`
- 方法: `updateAllGameWallets(Long userId, String currency)`
- 核心邏輯:
  1. 驗證用戶存在: `pltUserFeignClient.checkIfUserIdExistsOrThrow(userId)`
  2. 獲取所有遊戲錢包: `gameWalletFeignClient.getAllGameWalletsByCurrency(userId)`
  3. 更新遊戲餘額: `pltGameFeignClient.updateGameBalancesByCurrency(userId, gameWallets)`
  4. 更新本地數據: `gameWalletFeignClient.updateGameWalletBalances(result)`

### Service 層 (wallet-service, plt-game)
... (根據實際追蹤結果填寫)

## 核心功能說明

[根據代碼分析，說明 API 實際實現的功能]

## 相關模組

| 模組 | 職責 |
|------|------|
| `plt-gateway` | API 網關，路由和認證 |
| `wallet-aggregation` | 錢包聚合服務，協調多個服務 |
| `wallet-service` | 錢包核心服務，數據庫操作 |
| `plt-game` | 遊戲服務，第三方遊戲平台交互 |

## 備註

重要注意事項
```

## 輸出位置

文檔保存到當前目錄下的 `.doc/` 文件夾：
```
.doc/[@Tag分類]/
```

### 目錄結構示例

```
.doc/
├── 客戶列表-資金往來/
│   ├── game-balance-sync.md
│   └── transfer-log.md
├── 財務管理-充值管理-充值列表/
│   └── recharge-list.md
├── 代理管理-代理列表/
│   └── proxy-commission.md
├── 客戶管理/
│   └── user-detail.md
├── 遊戲管理/
│   └── game-config.md
├── 報表管理/
│   └── daily-report.md
├── 風控管理/
│   └── risk-rule.md
└── 活動管理/
    └── activity-bonus.md
```

### 文件命名規則

根據 API 功能生成描述性文件名：

| API 功能 | 文件名範例 |
|----------|-----------|
| 更新餘額 | `update-balance.md` |
| 轉帳操作 | `transfer-operation.md` |
| 查詢記錄 | `query-records.md` |
| 刷新同步 | `refresh-sync.md` |
| 審核操作 | `audit-action.md` |

命名原則：
- 使用小寫英文字母
- 單詞間用 `-` 連接
- 簡潔描述 API 核心功能
- 避免使用中文或特殊字符

## 輸出格式

**重要：直接創建文件和目錄**

1. 使用 Bash 工具創建目錄（如不存在）
2. 使用 Write 工具直接創建 Markdown 文檔
3. 不要輸出文件內容到對話中

創建目錄命令：
```bash
mkdir -p ".doc/[分類目錄名]"
```

## 分析要點

1. **路徑參數提取**：從 URL 中提取動態參數（如 `{userId}`, `{orderId}`）
2. **域名解析**：識別環境（sit, uat, prod）和服務類型
3. **簽名機制**：注意 sign 和 timestamp 的組合，可能是防篡改機制
4. **功能推斷**：結合 URL 路徑和 HTTP 方法推斷 API 語義
5. **分類映射**：根據 URL 路徑準確映射到 Swagger @Tag 分類
6. **代碼追蹤**：從 Controller 到 Service 的完整調用鏈
7. **核心邏輯**：提取主要的業務處理步驟

## 質量保證

生成文檔前驗證：
- [ ] 目錄已正確創建
- [ ] 所有請求頭已正確分類
- [ ] URL 路徑參數已提取
- [ ] @Tag 分類映射正確
- [ ] 代碼調用鏈完整追蹤
- [ ] 核心邏輯已提取
- [ ] 文檔格式正確
- [ ] 文件名符合命名規則
