---
name: dtg:i18n
description: This skill should be used when the user asks to "process i18n translation", "handle i18n translations", "add missing translations", "check i18n keys", "update translation files", or mentions "i18ndata" or "translateMessageByPath". Automatically extracts i18n keys from HTML/JS files and updates corresponding JSON translation files for dtg-pay project.
version: 1.1.0
---

# DTG i18n Translation Processor

Automatically process internationalization (i18n) translations for dtg-pay project. Extract i18n keys from source files and update corresponding JSON translation files (Chinese and English).

## Purpose

This skill handles two i18n patterns commonly used in the dtg-pay project:

1. **HTML attribute pattern**: `i18ndata="path.to.key"`
2. **JavaScript function pattern**: `translateMessageByPath("path.to.key", "default text")`

Scan source files for these patterns, extract the i18n keys, and ensure corresponding translations exist in both Chinese (`zh/translation.json`) and English (`en/translation.json`) files.

## Translation File Locations

The dtg-pay project supports multiple skins, each with its own translation files:

| Skin | Translation Path |
|------|------------------|
| **ezpay** | `xxpay-merchant/src/main/resources/static/ezpay/x_mch/start/json/language/` |
| **724pay** | `xxpay-merchant/src/main/resources/static/724pay/x_mch/start/json/language/` |
| **lupay** | `xxpay-merchant/src/main/resources/static/lupay/x_mch/start/json/language/` |
| **x_mch** | `xxpay-merchant/src/main/resources/static/x_mch/x_mch/start/json/language/` |

Each skin directory contains:
```
start/json/language/
├── zh/
│   └── translation.json
└── en/
    └── translation.json
```

**Important:** When processing a file, apply the same changes to ALL skins to maintain consistency.

## Workflow

### Step 1: Read Source File

When a file path is provided, read the file to extract i18n keys.

### Step 2: Extract i18n Keys

Search for both i18n patterns in the source file:

**Pattern 1 - i18ndata attribute:**
```html
<span i18ndata="account.agentpay_passage.index.status">状态</span>
```

**Pattern 2 - translateMessageByPath function:**
```javascript
translateMessageByPath('account.agentpay_passage.index.disabled', "关闭")
translateMessageByPath("account.agentpay_passage.index.all", "全部")
```

### Step 3: Read Translation Files

Read both translation JSON files (zh and en) to check existing keys.

### Step 4: Identify Missing Translations

Compare extracted keys against existing keys in both JSON files. Identify missing keys.

### Step 5: Generate Translation Values

For missing keys, generate appropriate translations using the common translations reference below.

### Step 6: Update Translation Files

Add missing translations to BOTH JSON files (zh and en), maintaining proper JSON structure.

### Step 7: Apply to All Skins

Repeat the update for all skin directories to ensure consistency across the project.

## Translation Structure

JSON files follow this hierarchical structure:

```json
{
  "account": {
    "agentpay_passage": {
      "index": {
        "home": "首页",
        "status": "状态",
        "all": "全部",
        "noSettings": "未设置"
      }
    }
  }
}
```

## Key Naming Patterns

### Pattern 1: Nested index keys
```
account.{feature}.index.{property}
```
Example: `account.agentpay_passage.index.status`

### Pattern 2: Direct feature keys
```
{feature}.{property}
```
Example: `agentpay_passage.noSettings`

## Common Translations Reference

| 中文 | English |
|---------|---------|
| 首页 | Home |
| 通道ID | Channel ID |
| 通道名称 | Channel Name |
| 费率(%+单笔) | Rate(%+per transaction) |
| 单笔代付上限 | Max Single Amount |
| 单笔代付下限 | Min Single Amount |
| 单笔最大金额 | Max Single Amount |
| 单笔最小金额 | Min Single Amount |
| 状态 | Status |
| 默认 | Default |
| 是/否 | Yes/No |
| 开启/关闭 | Enabled/Disabled |
| 未设置 | Not Set |
| 全部 | All |
| 类别 | Category |
| 币别 | Currency Type |
| 商户管理 | Merchant Management |
| 代付通道 | Agent Pay Channel |
| 支付通道 | Payment Channel |
| 产品ID | Product ID |
| 产品名称 | Product Name |
| 商户费率 | Merchant Rate |
| 请求失败 | Request failed |

## Translation Tips

1. **Consistency:** Use consistent terminology across all skins
2. **Spelling:** Correct "Chanel" to "Channel" in English translations
3. **Context:** Match translations to the specific feature (代付通道 vs 支付通道)
4. **Format:** Preserve format specifiers like `(%+单笔)` → `(%+per transaction)`

## Optimization Tips

### Identifying Common Prefix Pattern

When processing files, many i18n keys may share a common prefix. For example:

```html
<!-- All these keys share the same prefix: account.agentpay_passage.index -->
<span i18ndata="account.agentpay_passage.index.home">首页</span>
<span i18ndata="account.agentpay_passage.index.status">状态</span>
<span i18ndata="account.agentpay_passage.index.all">全部</span>
```

**Optimization Strategy:**

1. **First:** Find the common prefix by looking for repeated patterns
   - Example: `account.agentpay_passage.index` appears multiple times
   - Extract the varying suffixes: `home`, `status`, `all`, etc.

2. **Then:** Process only the varying suffixes as a batch
   - Check all suffixes against translation files
   - Add missing translations in one operation

3. **Benefit:** Reduces redundant lookups and improves efficiency

**Example Workflow:**

```javascript
// Step 1: Identify common prefix
const prefix = "account.agentpay_passage.index";
const suffixes = ["home", "status", "all", "noSettings", "disabled", "enabled", ...];

// Step 2: Check if prefix exists in translation files
// Step 3: Add only missing suffix entries
```

This approach is especially useful for:
- Feature pages with many similar keys (index, list, detail pages)
- Form fields with consistent naming
- Table column headers

### Detecting and Fixing Inconsistent Prefixes

**Issue:** When a file has inconsistent i18n key prefixes, they need to be fixed.

**Common Inconsistencies:**

1. **Typos in the key**
   ```html
   <!-- Wrong: 'passgae' instead of 'passage' -->
   <span i18ndata="account.agentpay_passgae.index.home">首页</span>
   ```

2. **Inconsistent prefix depth**
   ```html
   <!-- Some keys miss the 'index' level -->
   <span i18ndata="account.agentpay_passage.home">首页</span>
   <!-- Should be: -->
   <span i18ndata="account.agentpay_passage.index.home">首页</span>
   ```

3. **Extra nesting levels**
   ```html
   <!-- Double 'index' is wrong -->
   <span i18ndata="account.agentpay_passage.index.index.home">首页</span>
   ```

4. **Mixed prefixes in same file**
   ```html
   <!-- Inconsistent usage -->
   <span i18ndata="account.agentpay_passage.index.status">状态</span>
   <span i18ndata="accountpay_passage.index.enabled">开启</span>
   ```

**Fix Strategy:**

1. **Identify the most common/correct prefix**
   - Count occurrences of each prefix variation
   - The most frequent is usually the correct one
   - Example: `account.agentpay_passage.index.` appears 15 times, others only 1-2 times

2. **Fix inconsistent keys in the source file**
   - Update HTML file to use consistent prefix
   - Example: Change `account.agentpay_passge.index.home` → `account.agentpay_passage.index.home`

3. **Then update translation files**
   - Only need to handle the correct, consistent prefix
   - Remove or merge orphaned keys from incorrect prefixes

**Example Detection Process:**

```javascript
// Extract all unique prefixes
const prefixes = [
  "account.agentpay_passage.index.",  // 15 occurrences ✓ (correct)
  "account.agentpay_passge.index.",   // 2 occurrences ✗ (typo)
  "accountpay_passage.index.",        // 1 occurrence ✗ (missing 'account.')
];

// Use the most common as the standard
const standardPrefix = "account.agentpay_passage.index.";

// Fix source file and translations accordingly
```

**Important:** Always fix the source HTML file first before updating translations, otherwise the keys won't match correctly.

## Validation Checklist

After processing translations:

- [ ] All i18ndata keys have corresponding translations
- [ ] All translateMessageByPath keys have corresponding translations
- [ ] Both zh and en JSON files are updated
- [ ] All skins are updated consistently
- [ ] JSON syntax is valid (no trailing commas, proper quoting)
- [ ] Key paths follow naming conventions
- [ ] Translations are contextually appropriate
- [ ] No duplicate keys exist
- [ ] "Chanel" spelling corrected to "Channel" in English

## Example Usage

**User request:** "帮我处理 i18n 翻译，文件是 agentpay_passage/index.html"

**Processing steps:**
1. Read the HTML file
2. Extract all i18n keys (i18ndata and translateMessageByPath)
3. Read zh/translation.json and en/translation.json for each skin
4. Find and add missing keys
5. Update all skin translation files
6. Output summary table

**Output:** Summary table with columns: Key Path | Chinese | English
