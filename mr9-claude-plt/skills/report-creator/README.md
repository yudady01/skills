# Report Creator Skill

這是一個專為 `plt` 專案設計的 AI Skill，旨在自動化生成報表下載處理器（DownloadReportHandler）的代碼。它能根據資料來源 API 自動分析資料結構，並生成符合專案規範的 Java 代碼。

## ✨ 功能亮點

- **多模組支援**：自動識別並處理 5 個不同模組 (`fund`, `activity`, `proxy`, `reportagg`, `user`) 的配置差異。
- **智能分析**：自動分析 Response VO 欄位，生成對應的 CSV 映射邏輯。
- **模式識別**：自動選擇適合的代碼模板（簡單報表 vs 複雜報表/含子單/隱碼）。
- **規範遵循**：生成的代碼嚴格遵循各模組的 import 路徑和命名規範。

## 📂 目錄結構

```
.agent/skills/report-creator/
├── SKILL.md                    # 核心指令文檔，定義 AI 的執行邏輯
├── module-config.yaml          # 模組配置映射表 (定義 package 路徑、類名差異)
├── README.md                   # 本說明文件
├── templates/                  # 代碼模板
│   ├── simple-handler.java     # 簡單報表模板 (單一 VO)
│   └── complex-handler.java    # 複雜報表模板 (含子單、隱碼處理)
└── examples/                   # 定錨範例 (供 AI 參考)
    ├── RechargeProxyReport.java     # 簡單範例
    ├── WithdrawSummaryReport.java   # 複雜範例
    └── UserQueryReport.java         # 用戶模組範例 (特殊路徑)
```

## 🚀 如何使用

在 Cursor 中與 AI 對話時，只需包含相關關鍵字即可觸發：

1. **基本指令**：
   > "使用 report-creator skill 幫我建立一個新的報表處理器"

2. **提供 curl 命令 (推薦)**：
   > "幫我為這個 API 建立報表導出功能：
   > `curl 'https://.../api/v1/fund/recharge/manage/list' ...`"

3. **指定模組與需求**：
   > "在 plt-fund-aggregation 模組中新增一個「充值匯總報表」，資料來源是 RechargeDomainService"

## ⚙️ 支援的模組與差異

Skill 會自動處理由 `module-config.yaml` 定義的以下差異：

| 模組 | Import 差異 | Handler 拼寫 | ReportType 路徑 |
|------|-------------|--------------|-----------------|
| **plt-fund-aggregation** | BasicFeignClient | `Hanlder` (錯) | `basics.ReportType` |
| **plt-activity-aggregation** | BasicsFeignClient | `Hanlder` (錯) | `ReportType` |
| **plt-proxy-aggregation** | BasicsFeignClient | `Hanlder` (錯) | `basics.ReportType` |
| **plt-reportagg** | BasicsFeignClient | `Hanlder` (錯) | `ReportType` |
| **plt-user-aggregation** | BasicsReportFeignClient | `Handler` (對) | `ReportType` |

## 🛠️ 維護指南

如果專案架構變更，請更新以下文件：

- **新增模組或修改路徑**：更新 `module-config.yaml`
- **修改代碼規範**：更新 `templates/` 下的模板文件
- **調整 AI 邏輯**：更新 `SKILL.md`
