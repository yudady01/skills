---
name: dev-git2doc
description: 抽取 Git commits 變更內容，自動生成開發文檔
---

# Dev Git2Doc Skill

## 觸發條件

當用戶請求以下任務時使用此 Skill：
- 分析 git commits 並生成開發文檔
- 抽取舊代碼變更作為新增類似功能的參考
- 記錄多模組的關聯變更

## 輸入格式

```
/dev-git2doc <module>:<commit> [<module>:<commit> ...]

範例：
/dev-git2doc plt-gateway:d8a30116 plt-user:b24cf743
```

## 執行流程

### Step 1: 解析輸入並驗證

1. 解析用戶輸入，提取模組名和 commit hash
2. 驗證模組目錄是否存在
3. 驗證 commit 是否有效
4. 遇到錯誤時跳過並警告，繼續處理其他 commits

### Step 2: 收集 Commit 資訊

對每個 commit 執行：

```bash
cd /Users/tommy/Documents/git/mr9/backend/plt/<module>
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
| issueId | issue 編號 (從 message 提取 `#2275`) |
| files | 變更文件列表 |
| diff | 完整變更內容 |

### Step 3: 分析變更內容

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

4. **相關性分析**：
   - 跨模組調用關係
   - 依賴順序（底層 → 上層）

### Step 4: 生成文檔標題資訊

從 commit 提取：
- **Issue 編號**：正則匹配 `#(\d+)` 或 `feature #(\d+)`
- **功能名稱**：AI 分析 commit message 和變更內容生成
- **功能簡述**：用於文件名，轉為 kebab-case（如 `usdt-wallet-address`）

### Step 5: 智能追蹤調用鏈

根據變更的文件類型和內容，智能判斷是否需要追蹤：

| 變更文件類型 | 是否追蹤 | 追蹤範圍 |
|-------------|---------|----------|
| DTO/VO | 是 | 找到對應的 Controller、Service |
| Enum | 是 | 找到使用該 Enum 的文件 |
| Controller | 是 | 追蹤到 DomainService、FeignClient |
| Migration SQL | 是 | 分析對應的 Entity、錯誤碼 |

調用鏈追蹤路徑：
```
Controller → DomainService → FeignClient → (跨模組) → DomainService → Service → Mapper → Entity
```

### Step 6: 生成文檔

#### 文檔路徑
```
/Users/tommy/Documents/git/mr9/backend/plt/.doc/功能開發/
```

#### 文件命名
```
{issueId}-{feature-slug}.md

範例：2275-usdt-wallet-address.md
```

如果無 issue 編號，使用日期：
```
{yyyyMMdd}-{feature-slug}.md

範例：20250828-usdt-wallet.md
```

#### 文檔結構（自適應詳略）

根據變更大小自動調整：

**小變更**（1-3 個文件，簡單修改）：
```markdown
# 功能開發文檔 #{issueId}：{功能名稱}

## 變更總覽

## 詳細變更

## 相關文件
```

**大變更**（多文件、跨模組）：
```markdown
# 功能開發文檔 #{issueId}：{功能名稱}

## 需求概述

## 變更模組總覽

## 各模組詳細變更
### {模組1}
### {模組2}

## 數據模型變更

## API 變更

## 數據庫變更

## 錯誤碼變更

## 調用鏈分析

## 注意事項

## 測試建議

## 相關文件
```

---

## 文檔模板

### 小變更模板

```markdown
# 功能開發文檔 #{issueId}：{功能名稱}

## 變更總覽

| 模組 | Commit | 說明 |
|------|--------|------|
| {module} | {shortHash} | {description} |

---

## 詳細變更

### Commit {shortHash} ({date})

**作者**: {author}

**變更文件**:
- `{path1}` - {changeType}
- `{path2}` - {changeType}

**變更內容**:
\`\`\`diff
{diff}
\`\`\`

---

## 相關文件

| 類型 | 路徑 |
|------|------|
| {type} | {path} |
```

### 大變更模板

```markdown
# 功能開發文檔 #{issueId}：{功能名稱}

## 需求概述

{AI 生成的需求描述}

## 變更模組總覽

| 模組 | Commit | 說明 |
|------|--------|------|
| {module1} | {shortHash1} | {desc1} |
| {module2} | {shortHash2} | {desc2} |

---

## 各模組詳細變更

### {模組名稱}

#### Commit {shortHash} ({date})

**作者**: {author}
**變更說明**: {description}

**變更文件**:
| 文件 | 變更類型 |
|------|----------|
| `{path}` | {新增/修改/刪除} |

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

**路徑**: `{method} {path}`

**請求參數**:
\`\`\`json
{dto}
\`\`\`

**變更說明**: {description}

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
  modulePrefix: plt-
  modules:
    - plt-gateway
    - plt-user
    - plt-basics
    - plt-fund
    - plt-game
    - plt-proxy
    - plt-account
    - plt-activity
    - plt-message
    - plt-report
    - plt-risk
    # ... 其他模組
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

正則表達式：
```regex
#?(\d{4,})
```

匹配範例：
- `feature #2275` → `2275`
- `#2275 黑名單新增USDT` → `2275`
- `fix #12345` → `12345`

### 功能簡述生成

從 commit message 提取關鍵詞，轉為 kebab-case：

| Commit Message | 功能簡述 |
|----------------|----------|
| `黑名單新增USDT錢包地址` | `usdt-wallet-address` |
| `fix qry` | `fix-qry` |
| `add error code` | `add-error-code` |

---

## 錯誤處理

| 情況 | 處理方式 |
|------|----------|
| 模組不存在 | 跳過該 commit，警告用戶 |
| Commit hash 無效 | 跳過該 commit，警告用戶 |
| 目錄不是 git 倉庫 | 跳過該模組，警告用戶 |
| 無法提取 issue 編號 | 使用日期代替 |

警告訊息格式：
```
⚠️ 警告：模組 {module} 的 commit {hash} 不存在，已跳過
```

---

## 範例

### 輸入
```
/dev-git2doc plt-gateway:d8a30116 plt-user:b24cf743 plt-basics:5f5d85d1
```

### 執行過程
1. 解析輸入 → 3 個 commits
2. 提取 commit 資訊
3. 分析變更內容
4. 追蹤調用鏈
5. 生成文檔

### 輸出
```
文檔已生成：.doc/功能開發/2275-usdt-wallet-address.md
```

---

## 完整實作範例：#2275 黑名單新增USDT錢包地址

### 輸入
```
/dev-git2doc plt-gateway:d8a30116 plt-user:b24cf743 plt-basics:5f5d85d1
```

### 輸出文檔結構
```
# 功能開發文檔 #2275：黑名單新增USDT錢包地址

## 需求概述
...

## 變更模組總覽
| 模組 | Commit | 說明 |
|------|--------|------|
| plt-gateway | d8a30116 | 新增 USDT 錢包地址維度到黑名單 |
| plt-user | b24cf743 | 新增 USDT_ADDRESS 枚舉值 |
| plt-basics | 5f5d85d1 | 新增錯誤碼定義 |

## 各模組詳細變更
...

## 調用鏈分析
...

## 注意事項
...

## 相關文件
...
```
