---
name: dev-git2doc
description: 抽取 Git branch 變更內容，自動生成開發文檔。當用戶請求分析 git branch 的 commits 並生成開發文檔、抽取功能分支的變更作為新增類似功能的參考、記錄多模組的關聯變更時使用此 Skill。
version: 1.0.0
tags: ["git", "documentation", "commit-analysis", "multi-module", "plt"]
triggers:
  - "dev-git2doc"
  - "git2doc"
  - "/dev-git2doc"
  - "分析 git branch"
  - "生成開發文檔"
  - "抽取 git 變更"
---

# Dev Git2Doc

抽取 Git branch 變更內容，自動生成開發文檔。

## 使用方式

```
/dev-git2doc <branch>

範例：
/dev-git2doc feature/3831_withdrawSkipSteps
```

**可選**：指定特定模組
```
/dev-git2doc <branch> <module1> <module2> ...

範例：
/dev-git2doc feature/3831_withdrawSkipSteps plt-fund-aggregation plt-basics
```

## 執行流程

### Step 1: 解析輸入並驗證

1. 解析用戶輸入，提取分支名稱
2. 如果用戶指定了模組，只處理指定的模組
3. 如果未指定模組，自動檢測所有模組中哪些有該分支

### Step 2: 檢測分支存在的模組

對每個模組檢查分支是否存在：

```bash
cd /Users/tommy/Documents/git/mr9/backend/plt/<module>
git rev-parse --verify origin/<branch> 2>/dev/null
```

如果分支存在，添加到處理列表。

**完整模組列表**：
```
pay, plt-account, plt-activity, plt-activity-aggregation,
plt-basics, plt-fund, plt-fund-aggregation, plt-game,
plt-game-aggregation, plt-gateway, plt-message, plt-messageagg,
plt-proxy, plt-proxy-aggregation, plt-proxy-gateway, plt-report,
plt-reportagg, plt-risk, plt-user, plt-user-aggregation,
third-party-callback, wallet-aggregation, wallet-service
```

### Step 3: 收集 Branch 資訊

對每個有該分支的模組執行：

```bash
cd /Users/tommy/Documents/git/mr9/backend/plt/<module>

# 獲取分支相對於 master/main 的 commits
git log origin/master..origin/<branch> --oneline

# 對每個 commit 獲取詳細資訊
git show <commit> --pretty=format:"%H%n%an%n%ae%n%ad%n%s%n%b" --no-patch
git show <commit> --stat
git show <commit>
```

提取資訊：
| 欄位 | 說明 |
|------|------|
| hash | 完整 commit hash |
| shortHash | 短 hash (前7位) |
| author | 作者 |
| date | 日期 |
| message | commit message |
| issueId | issue 編號 (從 message 提取) |
| files | 變更文件列表 |
| diff | 完整變更內容 |

### Step 4: 分析變更內容

對每個 commit 分析：

1. **變更類型判斷**：
   - 新增文件
   - 修改文件
   - 刪除文件
   - 重命名文件

2. **文件類型分類**：
   - Java 源碼
   - SQL Migration
   - 配置文件
   - 其他

3. **Java 變更分析**：
   - 枚舉新增/修改
   - DTO/VO 變更
   - Controller 變更
   - Service 變更
   - Mapper 變更
   - Handler 新增（報表）

4. **相關性分析**：
   - 跨模組調用關係
   - 依賴順序（底層 → 上層）

### Step 5: 生成文檔標題資訊

從分支名稱或 commit 提取：
- **Issue 編號**：正則匹配 `#(\d+)` 或 `feature #(\d+)` 或從分支名提取
- **功能名稱**：AI 分析 commit message 和變更內容生成
- **功能簡述**：用於文件名，轉為 kebab-case（如 `withdraw-skip-steps`）

### Step 6: 智能追蹤調用鏈

根據變更的文件類型和內容，智能判斷是否需要追蹤：

| 變更文件類型 | 是否追蹤 | 追蹤範圍 |
|-------------|---------|----------|
| DTO/VO | 是 | 找到對應的 Controller、Service |
| Enum | 是 | 找到使用該 Enum 的文件 |
| Controller | 是 | 追蹤到 DomainService、FeignClient |
| Handler (報表) | 是 | 追蹤到 DomainService、FeignClient |
| Migration SQL | 是 | 分析對應的 Entity、錯誤碼 |

調用鏈追蹤路徑：
```
Controller → DomainService → FeignClient → (跨模組) → DomainService → Service → Mapper → Entity
```

### Step 7: API 變更分析

檢測是否有 API 相關變更，如果有則調用 `api-analyzer` skill 進行分析。

**檢測條件**：
- 變更文件包含 `Controller` 或 `Controller.java`
- 變更文件位於 `controller/` 目錄下

**執行 api-analyzer**：

如果檢測到 Controller 變更，對每個變更的 Controller 執行：

1. **構造 cURL 命令**：
   - 根據 Controller 的 `@RequestMapping` 和 `@XxxMapping` 提取 API 路徑
   - 根據方法參數提取請求參數
   - 添加必要的請求頭（如 token, sign, timestamp）

2. **調用 api-analyzer skill**：
   ```
   /api-analyzer curl '...'
   ```

3. **合併分析結果**：
   - 將 api-analyzer 生成的「API 分析」內容合併到文檔的「## API 變更」章節
   - 包含：請求概況、請求頭分析、代碼調用鏈、核心功能說明

**API 變更章節格式**：
```markdown
## API 變更

### {API名稱}

#### 請求概況
| 項目 | 值 |
|------|-----|
| **環境** | {環境} |
| **方法** | {HTTP方法} |
| **路徑** | {API路徑} |

#### 請求頭分析
### 認證相關
| 請求頭 | 值 | 說明 |
|--------|-----|------|
| **token** | `{token}` | JWT 認證令牌 |
...

#### 代碼調用鏈
### Gateway 層
**Controller**: ...
...

### Aggregation 層
...

### Service 層
...

#### 核心功能說明
{功能描述}
```

### Step 8: 生成文檔

#### 文檔路徑
```
/Users/tommy/Documents/git/mr9/backend/plt/.doc/功能開發/
```

#### 文件命名
```
{issueId}-{feature-slug}.md

範例：3831-withdraw-skip-steps.md
```

如果無 issue 編號，使用日期：
```
{yyyyMMdd}-{feature-slug}.md

範例：20260203-withdraw-skip.md
```

#### 文檔結構

統一使用標準格式：
```markdown
# 功能開發文檔 #{issueId}：{功能名稱}

## 需求概述

## 變更模組總覽

## 各模組詳細變更

## 數據模型變更

## API 變更

## 數據庫變更

## 錯誤碼變更

## 調用鏈分析

## 注意事項

## 相關文件
```

---

## 文檔模板

### 標準模板

```markdown
# 功能開發文檔 #{issueId}：{功能名稱}

## 需求概述

{AI 生成的需求描述}

## 變更模組總覽

| 模組 | Commits | 說明 |
|------|---------|------|
| {module1} | {count1} commits | {desc1} |
| {module2} | {count2} commits | {desc2} |

---

## 各模組詳細變更

### {模組名稱}

#### Commits 總覽

| Commit | 日期 | 說明 |
|--------|------|------|
| {shortHash1} | {date1} | {message1} |
| {shortHash2} | {date2} | {message2} |

#### Commit {shortHash} ({date})

**作者**: {author} <{email}>
**變更說明**: {description}

**變更文件**:
| 文件 | 變更類型 |
|------|----------|
| `{path}` | 新增/修改/刪除 |

**變更詳情**:

**文件**: `{filePath}`
\`\`\`diff
{diff}
\`\`\`

**說明**: {AI 分析此變更的影響}

---

## 數據模型變更

### 枚舉變更

**文件**: `{EnumPath}`

\`\`\`java
// 變更前
{before}

// 變更後
{after}
\`\`\`

| 變更項 | 變更前 | 變更後 |
|--------|--------|--------|
| {field} | {before} | {after} |

---

## API 變更

### {API名稱}

#### 請求概況
| 項目 | 值 |
|------|-----|
| **環境** | {環境} |
| **方法** | {HTTP方法} |
| **路徑** | {API路徑模板} |

#### 完整 cURL 命令
\`\`\`bash
curl '{url}' \\
  -H 'token: {token}' \\
  -H 'timestamp: {timestamp}' \\
  ...
\`\`\`

#### 請求頭分析
### 認證相關
| 請求頭 | 值 | 說明 |
|--------|-----|------|
| **token** | `{值}` | JWT 認證令牌 |
| **sign** | `{值}` | 請求簽名 |
| **timestamp** | `{值}` | 時間戳 |

### 設備相關
| 請求頭 | 值 | 說明 |
|--------|-----|------|
| **device-id** | `{值}` | 設備標識 |
| **os-type** | `{值}` | 操作系統 |

### 來源相關
| 請求頭 | 值 | 說明 |
|--------|-----|------|
| **referer** | `{值}` | 請求來源頁面 |

#### 查詢參數
| 參數 | 類型 | 說明 |
|------|------|------|
| {param} | {type} | {description} |

#### 代碼調用鏈
### Gateway 層 ({module})
**Controller**: `{ControllerName}`
- 文件: `{controllerPath}`
- 方法: `{method}()`
- 權限: `{@PreAuthorize}`

**DomainService**: `{DomainServiceImpl}`
- 文件: `{domainServicePath}`
- 調用: `{feignClient}`

### Aggregation 層 ({module})
**DomainService**: `{DomainServiceImpl}`
- 文件: `{domainServicePath}`
- 方法: `{method}()`

### Service 層 ({module})
**Service**: `{Service}`
- 文件: `{servicePath}`
- 方法: `{method}()`

**Mapper**: `{Mapper}`
- 文件: `{mapperPath}`

#### 核心功能說明
{根據代碼分析，說明 API 實際實現的功能}

#### 相關模組
| 模組 | 職責 |
|------|------|
| {module} | {description} |

---

## 數據庫變更

### Migration 文件

**文件**: `{migrationPath}`

\`\`\`sql
{sql}
\`\`\`

**說明**: {description}

---

## 錯誤碼變更

| 錯誤碼 | 語言 | 說明 |
|--------|------|------|
| {code} | {lang} | {message} |

---

## 調用鏈分析

### 模組間關係

\`\`\`
{上游模組}
    ↓ Feign
{下游模組}
    ↓ Service
{數據庫層}
\`\`\`

### 完整調用鏈

1. **Controller 層** ({module})
   - 文件: `{controllerPath}`
   - 方法: `{method}()`

2. **DomainService 層** ({module})
   - 文件: `{domainServicePath}`
   - 調用: `{feignClient}`

3. **Service 層** ({module})
   - 文件: `{servicePath}`
   - 操作: `{mapper}`

---

## 注意事項

1. **{注意點1}**: {說明}
2. **{注意點2}**: {說明}

---

## 相關文件

| 類型 | 路徑 |
|------|------|
| Controller | `{path}` |
| DTO | `{path}` |
| Enum | `{path}` |
| Migration | `{path}` |
```

---

## 配置

### 項目路徑

```yaml
project:
  root: /Users/tommy/Documents/git/mr9/backend/plt/
  modules:
    - pay
    - plt-account
    - plt-activity
    - plt-activity-aggregation
    - plt-basics
    - plt-fund
    - plt-fund-aggregation
    - plt-game
    - plt-game-aggregation
    - plt-gateway
    - plt-message
    - plt-messageagg
    - plt-proxy
    - plt-proxy-aggregation
    - plt-proxy-gateway
    - plt-report
    - plt-reportagg
    - plt-risk
    - plt-user
    - plt-user-aggregation
    - third-party-callback
    - wallet-aggregation
    - wallet-service
```

### 文檔輸出

```yaml
output:
  basePath: /Users/tommy/Documents/git/mr9/backend/plt/.doc/功能開發/
  naming: "{issueId}-{featureSlug}.md"
  fallbackNaming: "{yyyyMMdd}-{featureSlug}.md"
```

---

## 提取規則

### Issue 編號提取

**來源優先順序**：
1. 分支名稱：`feature/3831_xxx` → `3831`
2. Commit message：正則匹配 `#(\d+)` 或 `feature #(\d+)`

正則表達式：
```regex
#?(\d{4,})
```

匹配範例：
| 來源 | 範例 | 提取結果 |
|------|------|----------|
| 分支名 | `feature/3831_withdrawSkipSteps` | `3831` |
| 分支名 | `feature#2275_usdt` | `2275` |
| Commit | `feature #2275 黑名單新增USDT` | `2275` |
| Commit | `#2275 黑名單新增USDT` | `2275` |
| Commit | `fix #12345` | `12345` |

### 功能簡述生成

從分支名稱或 commit message 提取關鍵詞，轉為 kebab-case：

| 來源 | 原始 | 功能簡述 |
|------|------|----------|
| 分支名 | `feature/3831_withdrawSkipSteps` | `withdraw-skip-steps` |
| 分支名 | `feature#2275_usdt_wallet` | `usdt-wallet` |
| Commit | `黑名單新增USDT錢包地址` | `usdt-wallet-address` |
| Commit | `fix qry` | `fix-qry` |
| Commit | `add error code` | `add-error-code` |

---

## 錯誤處理

| 情況 | 處理方式 |
|------|----------|
| 分支在所有模組都不存在 | 提示錯誤並中止 |
| 分支只在部分模組存在 | 跳過不存在的模組，繼續處理 |
| 目錄不是 git 倉庫 | 跳過該模組 |
| 無法提取 issue 編號 | 使用日期代替 |
| 無 commits | 跳過該模組並警告 |

警告訊息格式：
```
⚠️ 警告：模組 {module} 沒有分支 {branch}，已跳過
⚠️ 警告：模組 {module} 的分支 {branch} 沒有 commits
```

---

## 範例

### 輸入
```
/dev-git2doc feature/3831_withdrawSkipSteps
```

### 執行過程
1. 解析分支名稱：`feature/3831_withdrawSkipSteps`
2. 提取 issue 編號：`3831`
3. 檢測所有模組，找出有該分支的模組
4. 收集每個模組的 commits
5. 分析變更內容
6. 追蹤調用鏈
7. 生成文檔

### 輸出
```
文檔已生成：.doc/功能開發/3831-withdraw-skip-steps.md
```

---

## 完整實作範例：feature/3831_withdrawSkipSteps

### 輸入
```
/dev-git2doc feature/3831_withdrawSkipSteps
```

### 檢測結果
```
找到分支的模組：
- plt-fund-aggregation (2 commits)
- plt-basics (1 commit)
- plt-gateway (1 commit)
- plt-account (1 commit)

無分支的模組（已跳過）：
- plt-user, plt-game, ... (其他 20 個模組)
```

### 輸出文檔結構
```
# 功能開發文檔 #3831：出款步驟省略

## 需求概述
...

## 變更模組總覽
| 模組 | Commits | 說明 |
|------|---------|------|
| plt-fund-aggregation | 2 commits | 報表 Handler + 枚舉 |
| plt-basics | 1 commit | 枚舉項 |
| plt-gateway | 1 commit | 權限枚舉 |
| plt-account | 1 commit | Migration 權限 |

## 各模組詳細變更
...

## 調用鏈分析
...

## 注意事項
...

## 相關文件
...
```
