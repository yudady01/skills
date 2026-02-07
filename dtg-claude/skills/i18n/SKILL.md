---
name: dtg:i18n
description: 当用户要求"处理 i18n 翻译"、"处理国际化翻译"、"添加缺失的翻译"、"检查 i18n 键"、"更新翻译文件"，或提及 "i18ndata" 或 "translateMessageByPath" 时，应使用此技能。自动从 HTML/JS 文件中提取 i18n 键并更新 dtg-pay 项目对应的 JSON 翻译文件。
version: 1.1.0
---

# DTG i18n 翻译处理器

自动处理 dtg-pay 项目的国际化（i18n）翻译。从源文件中提取 i18n 键并更新对应的 JSON 翻译文件（中文和英文）。

## 用途

此技能处理 dtg-pay 项目中常用的两种 i18n 模式：

1. **HTML 属性模式**：`i18ndata="path.to.key"`
2. **JavaScript 函数模式**：`translateMessageByPath("path.to.key", "默认文本")`

扫描源文件中的这些模式，提取 i18n 键，确保中文（`zh/translation.json`）和英文（`en/translation.json`）文件中存在对应的翻译。

## 翻译文件位置

dtg-pay 项目支持多个皮肤，每个皮肤都有自己的翻译文件：

| 皮肤 | 翻译路径 |
|------|------------------|
| **ezpay** | `xxpay-merchant/src/main/resources/static/ezpay/x_mch/start/json/language/` |
| **724pay** | `xxpay-merchant/src/main/resources/static/724pay/x_mch/start/json/language/` |
| **lupay** | `xxpay-merchant/src/main/resources/static/lupay/x_mch/start/json/language/` |
| **x_mch** | `xxpay-merchant/src/main/resources/static/x_mch/x_mch/start/json/language/` |

每个皮肤目录包含：
```
start/json/language/
├── zh/
│   └── translation.json
└── en/
    └── translation.json
```

**重要**：处理文件时，请将相同的更改应用到**所有皮肤**以保持一致性。

## 工作流程

### 第 1 步：读取源文件

当提供文件路径时，读取文件以提取 i18n 键。

### 第 2 步：提取 i18n 键

在源文件中搜索两种 i18n 模式：

**模式 1 - i18ndata 属性：**
```html
<span i18ndata="account.agentpay_passage.index.status">状态</span>
```

**模式 2 - translateMessageByPath 函数：**
```javascript
translateMessageByPath('account.agentpay_passage.index.disabled', "关闭")
translateMessageByPath("account.agentpay_passage.index.all", "全部")
```

### 第 3 步：读取翻译文件

读取两个翻译 JSON 文件（zh 和 en）以检查现有的键。

### 第 4 步：识别缺失的翻译

将提取的键与两个 JSON 文件中的现有键进行比较。识别缺失的键。

### 第 5 步：生成翻译值

对于缺失的键，使用下面的常用翻译参考生成适当的翻译。

### 第 6 步：更新翻译文件

将缺失的翻译添加到**两个** JSON 文件（zh 和 en），保持正确的 JSON 结构。

### 第 7 步：应用到所有皮肤

对所有皮肤目录重复更新，以确保项目的一致性。

## 翻译结构

JSON 文件遵循此层次结构：

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

## 键命名模式

### 模式 1：嵌套的 index 键
```
account.{feature}.index.{property}
```
示例：`account.agentpay_passage.index.status`

### 模式 2：直接的 feature 键
```
{feature}.{property}
```
示例：`agentpay_passage.noSettings`

## 常用翻译参考

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

## 翻译提示

1. **一致性**：在所有皮肤中使用一致的术语
2. **拼写**：在英文翻译中将 "Chanel" 更正为 "Channel"
3. **上下文**：将翻译与特定功能匹配（代付通道 vs 支付通道）
4. **格式**：保留格式说明符，如 `(%+单笔)` → `(%+per transaction)`

## 优化提示

### 识别公共前缀模式

处理文件时，许多 i18n 键可能共享一个公共前缀。例如：

```html
<!-- 所有这些键共享相同的前缀：account.agentpay_passage.index -->
<span i18ndata="account.agentpay_passage.index.home">首页</span>
<span i18ndata="account.agentpay_passage.index.status">状态</span>
<span i18ndata="account.agentpay_passage.index.all">全部</span>
```

**优化策略：**

1. **首先**：通过查找重复模式来找到公共前缀
   - 示例：`account.agentpay_passage.index` 出现多次
   - 提取可变后缀：`home`、`status`、`all` 等

2. **然后**：仅批量处理可变后缀
   - 对照翻译文件检查所有后缀
   - 在一个操作中添加缺失的翻译

3. **好处**：减少冗余查找并提高效率

**示例工作流程：**

```javascript
// 步骤 1：识别公共前缀
const prefix = "account.agentpay_passage.index";
const suffixes = ["home", "status", "all", "noSettings", "disabled", "enabled", ...];

// 步骤 2：检查前缀是否存在于翻译文件中
// 步骤 3：仅添加缺失的后缀条目
```

此方法特别适用于：
- 具有许多相似键的功能页面（index、list、detail 页面）
- 具有一致命名的表单字段
- 表格列标题

### 检测和修复不一致的前缀

**问题**：当文件的 i18n 键前缀不一致时，需要修复它们。

**常见不一致：**

1. **键中的拼写错误**
   ```html
   <!-- 错误：'passgae' 而不是 'passage' -->
   <span i18ndata="account.agentpay_passgae.index.home">首页</span>
   ```

2. **前缀深度不一致**
   ```html
   <!-- 一些键缺少 'index' 层级 -->
   <span i18ndata="account.agentpay_passage.home">首页</span>
   <!-- 应该是：-->
   <span i18ndata="account.agentpay_passage.index.home">首页</span>
   ```

3. **额外的嵌套层级**
   ```html
   <!-- 双重 'index' 是错误的 -->
   <span i18ndata="account.agentpay_passage.index.index.home">首页</span>
   ```

4. **同一文件中的混合前缀**
   ```html
   <!-- 不一致的用法 -->
   <span i18ndata="account.agentpay_passage.index.status">状态</span>
   <span i18ndata="accountpay_passage.index.enabled">开启</span>
   ```

**修复策略：**

1. **识别最常见/正确的前缀**
   - 统计每个前缀变体的出现次数
   - 最频繁的通常是正确的
   - 示例：`account.agentpay_passage.index.` 出现 15 次，其他仅出现 1-2 次

2. **修复源文件中不一致的键**
   - 更新 HTML 文件以使用一致的前缀
   - 示例：更改 `account.agentpay_passge.index.home` → `account.agentpay_passage.index.home`

3. **然后更新翻译文件**
   - 只需要处理正确的、一致的前缀
   - 删除或合并不正确前缀中的孤立键

**示例检测过程：**

```javascript
// 提取所有唯一的前缀
const prefixes = [
  "account.agentpay_passage.index.",  // 15 次出现 ✓（正确）
  "account.agentpay_passge.index.",   // 2 次出现 ✗（拼写错误）
  "accountpay_passage.index.",        // 1 次出现 ✗（缺少 'account.'）
];

// 使用最常见的作为标准
const standardPrefix = "account.agentpay_passage.index.";

// 相应地修复源文件和翻译
```

**重要**：在更新翻译之前，始终先修复源 HTML 文件，否则键将无法正确匹配。

## 验证清单

处理翻译后：

- [ ] 所有 i18ndata 键都有对应的翻译
- [ ] 所有 translateMessageByPath 键都有对应的翻译
- [ ] zh 和 en JSON 文件都已更新
- [ ] 所有皮肤都一致更新
- [ ] JSON 语法有效（无尾随逗号，正确的引号）
- [ ] 键路径遵循命名约定
- [ ] 翻译在上下文中是适当的
- [ ] 不存在重复的键
- [ ] 英文中的 "Chanel" 拼写已更正为 "Channel"

## 使用示例

**用户请求**："帮我处理 i18n 翻译，文件是 agentpay_passage/index.html"

**处理步骤：**
1. 读取 HTML 文件
2. 提取所有 i18n 键（i18ndata 和 translateMessageByPath）
3. 为每个皮肤读取 zh/translation.json 和 en/translation.json
4. 查找并添加缺失的键
5. 更新所有皮肤翻译文件
6. 输出汇总表

**输出**：包含列的汇总表：键路径 | 中文 | 英文
