---
name: "develop-web-game"
description: "當 Codex 正在構建或迭代網頁遊戲（HTML/JS）並需要可靠的開發 + 測試循環時使用：實現小變更、運行基於 Playwright 的測試腳本（使用短輸入突發和有意義的暫停）、檢查截圖/文字，並使用 render_game_to_text 檢查控制台錯誤。"
---


# 開發網頁遊戲

以小步驟構建遊戲並驗證每次變更。將每次迭代視為：實現 → 動作 → 暫停 → 觀察 → 調整。

## 技能路徑（設置一次）

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export WEB_GAME_CLIENT="$CODEX_HOME/skills/develop-web-game/scripts/web_game_playwright_client.js"
export WEB_GAME_ACTIONS="$CODEX_HOME/skills/develop-web-game/references/action_payloads.json"
```

用戶範圍的技能安裝在 `$CODEX_HOME/skills` 下（默認：`~/.codex/skills`）。

## 工作流程

1. **選擇目標。** 定義要實現的單個功能或行為。
2. **小步實現。** 做出推動遊戲前進的最小變更。
3. **確保集成點。** 提供單個 canvas 和 `window.render_game_to_text`，以便測試循環可以讀取狀態。
4. **添加 `window.advanceTime(ms)`。** 強烈建議使用確定性步進鉤子，以便 Playwright 腳本可以可靠地推進幀；如果沒有它，自動化測試可能會不穩定。
5. **初始化 progress.md。** 如果 `progress.md` 存在，首先讀取它並確認原始用戶提示記錄在頂部（前綴為 `Original prompt:`）。還要注意前一個代理留下的任何 TODO 和建議。如果缺失，創建它並在頂部寫入 `Original prompt: <prompt>`，然後再追加更新。
6. **驗證 Playwright 可用性。** 確保 `playwright` 可用（本地依賴或全局安裝）。如果不確定，首先檢查 `npx`。
7. **運行 Playwright 測試腳本。** 您必須在每次有意義的變更後運行 `$WEB_GAME_CLIENT`；除非必要，否則不要創建新客戶端。
8. **使用負載參考。** 基於 `$WEB_GAME_ACTIONS` 構建動作，以避免猜測鍵名。
9. **檢查狀態。** 在每次突發後捕獲截圖和文字狀態。
10. **檢查截圖。** 打開最新的截圖，驗證預期的視覺效果，修復任何問題，然後重新運行腳本。重複直到正確。
11. **驗證控制和狀態（多步驟重點）。** 透徹地測試所有重要的交互。對於每個交互，思考它所隱含的完整多步驟序列（原因 → 中間狀態 → 結果），並驗證整個鏈是否端到端工作。確認 `render_game_to_text` 反映屏幕上顯示的相同狀態。如果有任何不對，修復並重新運行。
    重要交互示例：移動、跳躍、射擊/攻擊、交互/使用、菜單中的選擇/確認/取消、暫停/恢復、重新開始，以及請求定義的任何特殊能力或謎題動作。多步驟示例：射擊敵人應該減少其生命值；當生命值達到 0 時，它應該消失並更新分數；收集鑰匙應該解鎖門並允許關卡推進。
12. **檢查錯誤。** 檢查控制台錯誤並在繼續之前修復第一個新問題。
13. **場景之間重置。** 在驗證不同功能時避免交叉測試狀態。
14. **小增量迭代。** 一次更改一個變量（幀、輸入、時序、位置），然後重複步驟 7-13 直到穩定。

示例命令（需要動作）：
```
node "$WEB_GAME_CLIENT" --url http://localhost:5173 --actions-file "$WEB_GAME_ACTIONS" --click-selector "#start-btn" --iterations 3 --pause-ms 250
```

示例動作（內聯 JSON）：
```json
{
  "steps": [
    { "buttons": ["left_mouse_button"], "frames": 2, "mouse_x": 120, "mouse_y": 80 },
    { "buttons": [], "frames": 6 },
    { "buttons": ["right"], "frames": 8 },
    { "buttons": ["space"], "frames": 4 }
  ]
}
```

## 測試檢查清單

測試為請求添加的任何新功能以及邏輯變更可能影響的任何區域。識別問題，修復它們，然後重新運行測試以確認它們已解決。

測試內容示例：
- 主要移動/交互輸入（例如，移動、跳躍、射擊、確認/選擇）。
- 勝/負或成功/失敗轉換。
- 分數/生命值/資源變更。
- 邊界條件（碰撞、牆壁、屏幕邊緣）。
- 菜單/暫停/開始流程（如果存在）。
- 與請求相關的任何特殊動作（增強道具、連擊、能力、謎題、計時器）。

## 要檢查的測試工件

- Playwright 運行的最新截圖。
- 最新的 `render_game_to_text` JSON 輸出。
- 控制台錯誤日誌（在繼續之前修復第一個新錯誤）。
您必須在運行 Playwright 腳本後實際打開並視覺檢查最新的截圖，而不僅僅是生成它們。確保屏幕上應該可見的所有內容實際上都可見。超越開始屏幕並捕獲涵蓋所有新添加功能的遊戲截圖。將截圖視為真相來源；如果缺少某些內容，則構建中缺少它。如果您懷疑無頭/WebGL 捕獲問題，請在有頭模式下重新運行 Playwright 腳本並重新檢查。在緊密循環中修復並重新運行，直到截圖和文字狀態看起來正確。一旦修復得到驗證，重新測試所有重要的交互和控制，確認它們工作，並確保您的變更沒有引入回歸。如果有，修復它們並在一個循環中重新運行所有內容，直到交互、文字狀態和控制都按預期工作。在測試控制時要透徹；壞掉的遊戲是不可接受的。

## 核心遊戲指南

### Canvas + 佈局
- 優先使用居中在窗口中的單個 canvas。

### 視覺效果
- 保持屏幕文字最少；在開始/菜單屏幕上顯示控件，而不是在遊戲過程中疊加它們。
- 除非設計需要，否則避免過暗的場景。使關鍵元素易於看到。
- 在 canvas 本身上繪製背景，而不是依賴 CSS 背景。

### 文字狀態輸出（render_game_to_text）
公開一個 `window.render_game_to_text` 函數，該函數返回一個簡潔的 JSON 字符串，表示當前遊戲狀態。文字應包含足夠的信息以便在沒有視覺效果的玩遊戲。

最小模式：
```js
function renderGameToText() {
  const payload = {
    mode: state.mode,
    player: { x: state.player.x, y: state.player.y, r: state.player.r },
    entities: state.entities.map((e) => ({ x: e.x, y: e.y, r: e.r })),
    score: state.score,
  };
  return JSON.stringify(payload);
}
window.render_game_to_text = renderGameToText;
```

保持負載簡潔並偏向於屏幕/交互元素。優先考慮當前可見的實體而不是完整歷史記錄。
包括清晰的坐標系註釋（原點和軸方向），並編碼所有與玩家相關的狀態：玩家位置/速度、活動障礙物/敵人、可收集物品、計時器/冷卻時間、分數，以及做出正確決策所需的任何模式/狀態標誌。避免大的歷史記錄；只包括當前相關和可見的內容。

### 時間步進鉤子
提供一個確定性的時間步進鉤子，以便 Playwright 客戶端可以以受控的增量推進遊戲。公開 `window.advanceTime(ms)`（或一個轉發到遊戲更新循環的薄包裝器），並讓遊戲循環在存在時使用它。
Playwright 測試腳本使用此鉤子在自動化測試期間確定性步進幀。

最小模式：
```js
window.advanceTime = (ms) => {
  const steps = Math.max(1, Math.round(ms / (1000 / 60)));
  for (let i = 0; i < steps; i++) update(1 / 60);
  render();
};
```

### 全屏切換
- 使用單個鍵（優先 `f`）切換全屏開/關。
- 允許 `Esc` 退出全屏。
- 當全屏切換時，調整 canvas/渲染大小，以便視覺效果和輸入映射保持正確。

## 進度跟踪

如果 `progress.md` 文件不存在，請創建它，並隨著您的進展附加 TODO、註釋、註意事項和未完項，以便另一個代理可以無縫接手。
如果 `progress.md` 文件已存在，請首先閱讀它，包括頂部的原始用戶提示（您可能正在繼續另一個代理的工作）。不要覆蓋原始提示；保留它。
在每個有意義的工作塊（添加功能、發現錯誤、運行測試或做出決策）後更新 `progress.md`。
在您的工作結束時，在 `progress.md` 中為下一個代理留下 TODO 和建議。

## Playwright 先決條件

- 如果項目已經有本地 `playwright` 依賴項，則優先使用它。
- 如果不確定 Playwright 是否可用，請檢查 `npx`：
  ```
  command -v npx >/dev/null 2>&1
  ```
- 如果 `npx` 缺失，請安裝 Node/npm，然後全局安裝 Playwright：
  ```
  npm install -g @playwright/mcp@latest
  ```
- 除非明確要求，否則不要切換到 `@playwright/test`；堅持使用客戶端腳本。

## 腳本

- `$WEB_GAME_CLIENT`（安裝默認：`$CODEX_HOME/skills/develop-web-game/scripts/web_game_playwright_client.js`）— 基於 Playwright 的動作循環，具有虛擬時間步進、截圖捕獲和控制台錯誤緩衝。您必須通過 `--actions-file`、`--actions-json` 或 `--click` 傳遞動作突發。

## 參考

- `$WEB_GAME_ACTIONS`（安裝默認：`$CODEX_HOME/skills/develop-web-game/references/action_payloads.json`）— 示例動作負載（鍵盤 + 鼠標，每幀捕獲）。使用這些來構建您的突發。
