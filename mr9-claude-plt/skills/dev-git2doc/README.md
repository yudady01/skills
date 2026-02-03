# Dev Git2Doc Skill

自動從 Git commits 抽取變更內容，生成開發文檔。

## 功能

- 解析多個模組的 git commits
- 自動提取 issue 編號和功能名稱
- 智能追蹤跨模組調用鏈
- 分析枚舉、DTO、API、數據庫變更
- 生成標準化的開發文檔

## 使用方法

```bash
/dev-git2doc <module>:<commit> [<module>:<commit> ...]
```

### 範例

```bash
# 單個 commit
/dev-git2doc plt-gateway:d8a30116

# 多個 commits
/dev-git2doc plt-gateway:d8a30116 plt-user:b24cf743 plt-basics:5f5d85d1
```

## 輸出

文檔保存到：`.doc/功能開發/{issueId}-{feature-slug}.md`

## 文檔結構

根據變更大小自動調整：
- **小變更**：簡潔版
- **大變更**：包含調用鏈、測試建議等完整章節

## 項目配置

- 項目根目錄：`/Users/tommy/Documents/git/mr9/backend/plt/`
- 模組前綴：`plt-`
- 每個模組為獨立 git 倉庫
