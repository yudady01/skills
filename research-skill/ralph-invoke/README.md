讓 Claude Code 調用自己的 Ralph-Wiggum 循環的技能（無需用戶命令）
Built with Claude
我創建了一個技能，讓 Claude 可以在沒有使用者命令的情況下啟動自主的 Ralph-Wiggum 循環

Ralph-Wiggum 插件非常適合迭代 AI 開發，但它需要使用者手動運行/ralph-loop "任務"。 Claude 不能自行啟動循環。

所以我做了一個簡單的技能，教 Claude 直接透過 Bash 呼叫設定腳本。

安裝 ：

mkdir -p .claude/skills/ralph-invoke

curl -o .claude/skills/ralph-invoke/SKILL.md \

https://raw.githubusercontent.com/muyen/vibe-to-prod/main/.claude/skills/ralph-invoke/SKILL.md

需要 ralph-wiggum 外掛：

/plugin install ralph-wiggum@claude-code-plugins

/plugin enable ralph-wiggum@claude-code-plugins

GitHub： https://github.com/muyen/vibe-to-prod

