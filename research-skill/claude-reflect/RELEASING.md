# 发布流程

## 版本更新清单

1. **更新这些文件中的版本：**
   - `.claude-plugin/plugin.json` — `"version": "X.Y.Z"`
   - `README.md` — 版本徽章 URL

2. **在 CHANGELOG.md 中添加新版本部分**

3. **更新 README.md 中的测试计数**（如果已更改）

4. **运行验证：**
   ```bash
   claude plugin validate .
   python -m pytest tests/ -v
   ```

## 版本控制（语义版本控制）

- **MAJOR**（X.0.0）：重大更改
- **MINOR**（0.X.0）：新功能（向后兼容）
- **PATCH**（0.0.X）：错误修复

## 需要更新的文件

| 文件 | 字段 |
|------|-------|
| `.claude-plugin/plugin.json` | `version` |
| `README.md` | 版本徽章、测试计数徽章 |
| `CHANGELOG.md` | 顶部的新版本部分 |

## 提交和发布

```bash
# 暂存并提交
git add -A
git commit -m "chore: Release vX.Y.Z"

# 标记并推送
git tag vX.Y.Z
git push origin main --tags
```

## 插件验证

```bash
claude plugin validate .
```

常见警告：
- `metadata.description` — 添加描述到 marketplace.json（可选）
