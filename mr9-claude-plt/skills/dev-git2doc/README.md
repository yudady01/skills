# Dev Git2Doc Skill

自動從 Git branch 抽取 commits 變更內容，生成開發文檔。

## 功能

- 自動檢測哪些模組有指定分支
- 提取分支的所有 commits
- 自動提取 issue 編號和功能名稱
- 智能追蹤跨模組調用鏈
- 分析枚舉、DTO、API、數據庫變更
- **API 變更時自動調用 api-analyzer skill 進行深度分析**
- 生成標準化的開發文檔

## 使用方法

```bash
/dev-git2doc <branch>

# 範例
/dev-git2doc feature/3831_withdrawSkipSteps

# 指定特定模組
/dev-git2doc feature/3831_withdrawSkipSteps plt-fund-aggregation plt-basics
```

## 輸出

文檔保存到：`.doc/功能開發/{issueId}-{feature-slug}.md`

## 文檔結構

統一使用標準格式，包含以下章節：

```markdown
# 功能開發文檔 #{issueId}：{功能名稱}

## 需求概述
## 變更模組總覽
## 各模組詳細變更
## 數據模型變更
## API 變更 (如有 Controller 變更，自動調用 api-analyzer)
## 數據庫變更
## 錯誤碼變更
## 調用鏈分析
## 注意事項
## 相關文件
```

## API 變更分析

當檢測到有 Controller 變更時，自動：

1. 構造 cURL 命令
2. 調用 `api-analyzer` skill 進行分析
3. 將分析結果合併到文檔的「## API 變更」章節

分析結果包含：
- 請求概況
- 請求頭分析（認證、設備、來源）
- 代碼調用鏈（Gateway → Aggregation → Service）
- 核心功能說明
- 相關模組

## 支持的模組

pay, plt-account, plt-activity, plt-activity-aggregation,
plt-basics, plt-fund, plt-fund-aggregation, plt-game,
plt-game-aggregation, plt-gateway, plt-message, plt-messageagg,
plt-proxy, plt-proxy-aggregation, plt-proxy-gateway, plt-report,
plt-reportagg, plt-risk, plt-user, plt-user-aggregation,
third-party-callback, wallet-aggregation, wallet-service
