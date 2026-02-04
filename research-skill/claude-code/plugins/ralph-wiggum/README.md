# Ralph Wiggum 插件

Ralph Wiggum 技術在 Claude Code 中的實現，用於迭代式、自引用的 AI 開發循環。

## 什麼是 Ralph？

Ralph 是一種基於連續 AI 代理循環的開發方法論。正如 Geoffrey Huntley 所描述的：**「Ralph 是一個 Bash 循環」**——一個簡單的 `while true`，反覆將提示文件提供給 AI 代理，允許它迭代地改進其工作直到完成。

該技術以《辛普森一家》中的 Ralph Wiggum 命名，體現了儘管遇到挫折仍持續迭代的理念。

### 核心概念

此插件使用**停止鉤子（Stop hook）**實現 Ralph，該鉤子攔截 Claude 的退出嘗試：

```bash
# 您運行一次：
/ralph-loop "您的任務描述" --completion-promise "DONE"

# 然後 Claude Code 自動執行：
# 1. 處理任務
# 2. 嘗試退出
# 3. 停止鉤子阻止退出
# 4. 停止鉤子將相同的提示返回
# 5. 重複直到完成
```

循環發生在**您當前的會話內**——您不需要外部 bash 循環。`hooks/stop-hook.sh` 中的停止鉤子通過阻止正常會話退出來創建自引用反饋循環。

這創建了一個**自引用反饋循環**，其中：
- 提示在迭代之間從不改變
- Claude 之前的工作保留在文件中
- 每次迭代都能看到修改的文件和 git 歷史記錄
- Claude 通過閱讀文件中自己過去的工作自主改進

## 快速開始

```bash
/ralph-loop "構建一個用於待辦事項的 REST API。要求：CRUD 操作、輸入驗證、測試。完成時輸出 <promise>COMPLETE</promise>。" --completion-promise "COMPLETE" --max-iterations 50
```

Claude 將：
- 迭代地實現 API
- 運行測試並查看失敗
- 根據測試輸出修復錯誤
- 迭代直到滿足所有要求
- 完成時輸出完成承諾

## 命令

### /ralph-loop

在您當前的會話中啟動 Ralph 循環。

**用法：**
```bash
/ralph-loop "<提示>" --max-iterations <n> --completion-promise "<文本>"
```

**選項：**
- `--max-iterations <n>` - 在 N 次迭代後停止（默認：無限制）
- `--completion-promise <文本>` - 表示完成的短語

### /cancel-ralph

取消活動的 Ralph 循環。

**用法：**
```bash
/cancel-ralph
```

## 提示編寫最佳實踐

### 1. 明確的完成標準

❌ 糟糕：「構建一個待辦事項 API 並把它做好。」

✅ 良好：
```markdown
構建一個用於待辦事項的 REST API。

完成時：
- 所有 CRUD 端點正常工作
- 輸入驗證已到位
- 測試通過（覆蓋率 > 80%）
- 帶有 API 文檔的 README
- 輸出：<promise>COMPLETE</promise>
```

### 2. 增量目標

❌ 糟糕：「創建一個完整的電子商務平台。」

✅ 良好：
```markdown
階段 1：用戶身份驗證（JWT、測試）
階段 2：產品目錄（列表/搜索、測試）
階段 3：購物車（添加/刪除、測試）

所有階段完成時輸出 <promise>COMPLETE</promise>。
```

### 3. 自我修正

❌ 糟糕：「為功能 X 編寫代碼。」

✅ 良好：
```markdown
遵循 TDD 實現功能 X：
1. 編寫失敗的測試
2. 實現功能
3. 運行測試
4. 如果任何測試失敗，調試並修復
5. 如需要，重構
6. 重複直到全部通過
7. 輸出：<promise>COMPLETE</promise>
```

### 4. 逃生艙

始終使用 `--max-iterations` 作為安全網，以防止在不可能的任務上出現無限循環：

```bash
# 推薦：始終設置合理的迭代限制
/ralph-loop "嘗試實現功能 X" --max-iterations 20

# 在您的提示中，包括卡住時該做什麼：
# "15 次迭代後，如果未完成：
#  - 記錄阻礙進度的內容
#  - 列出嘗試過的內容
#  - 建議替代方法"
```

**注意**：`--completion-promise` 使用精確字符串匹配，因此您不能將其用於多個完成條件（如「SUCCESS」與「BLOCKED」）。始終依靠 `--max-iterations` 作為您的主要安全機制。

## 哲學

Ralph 體現了幾個關鍵原則：

### 1. 迭代 > 完美
不要以第一次就完美為目標。讓循環來完善工作。

### 2. 失敗是數據
「確定性不良」意味著失敗是可預測和有信息量的。使用它們來調整提示。

### 3. 操作員技能很重要
成功取決於編寫好的提示，而不僅僅是擁有一個好的模型。

### 4. 堅持就是勝利
不斷嘗試直到成功。循環自動處理重試邏輯。

## 何時使用 Ralph

**適用於：**
- 具有明確成功標準的定義明確的任務
- 需要迭代和改進的任務（例如，讓測試通過）
- 您可以離開的綠地項目
- 具有自動驗證的任務（測試、linter）

**不適用於：**
- 需要人類判斷或設計決策的任務
- 一次性操作
- 成功標準不明確的任務
- 生產調試（改為使用有針對性的調試）

## 真實世界的結果

- 在 Y Combinator 黑客馬拉松測試中成功過夜生成 6 個存儲庫
- 一個 $50k 的合同以 $297 的 API 成本完成
- 使用這種方法在 3 個月內創建了整個編程語言（「cursed」）

## 了解更多

- 原始技術：https://ghuntley.com/ralph/
- Ralph 編排器：https://github.com/mikeyobrien/ralph-orchestrator

## 獲取幫助

在 Claude Code 中運行 `/help` 以獲取詳細的命令參考和示例。
