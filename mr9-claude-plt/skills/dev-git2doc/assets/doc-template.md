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

**作者**: {author} <{email}>

**變更說明**: {description}

**變更文件**:
| 文件 | 變更類型 |
|------|----------|
| `{path}` | 新增/修改/刪除 |

**變更詳情**:

**文件**: `{filePath}`
```diff
{diff content}
```

**說明**: {AI 分析此變更的影響}

---

## 數據模型變更

### 枚舉變更

**文件**: `{EnumPath}`

```java
// 變更前
{before code}

// 變更後
{after code}
```

| 變更項 | 變更前 | 變更後 |
|--------|--------|--------|
| {field} | {before} | {after} |

---

## API 變更

### {API名稱}

**路徑**: `{method} {path}`

**請求參數**:
```json
{dto example}
```

**驗證規則**:
- {field}: {validation}

**變更說明**: {description}

---

## 數據庫變更

### Migration 文件

**文件**: `{migrationPath}`

```sql
{sql content}
```

**說明**: {description}

---

## 錯誤碼變更

### {errorCode} - {錯誤名稱}

| 語言 | 錯誤訊息 |
|------|----------|
| EN | {message} |
| TW | {message} |
| ZH | {message} |

**屬性**:
- Type: `{type}`
- Show Type: `{showType}`
- HTTP Status: `{status}`

---

## 調用鏈分析

### 模組間關係

```
{上游模組}
    ↓ Feign
{下游模組}
    ↓ Service
{數據庫層}
```

### 完整調用鏈

1. **Controller 層** ({module})
   - 文件: `{controllerPath}`
   - 方法: `{method}()`
   - 權限: `{@PreAuthorize}`

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
3. **{注意點3}**: {說明}

---

## 相關文件

| 類型 | 路徑 |
|------|------|
| Controller | `{path}` |
| DTO | `{path}` |
| VO | `{path}` |
| Enum | `{path}` |
| Service | `{path}` |
| Mapper | `{path}` |
| Migration | `{path}` |
