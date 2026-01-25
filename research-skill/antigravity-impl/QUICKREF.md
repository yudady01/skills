# Antigravity Implementation Plugin - 快速参考

## 一命令上手

```bash
antigravity-impl [计划名称]
```

示例：
```
antigravity-impl EZPAY-730-3
```

## 文件结构

```
/Users/tommy/.claude/plugins/antigravity-impl/
├── plugin.json              # 插件配置
├── README.md               # 插件说明
├── USAGE.md                # 详细使用指南
├── QUICKREF.md             # 本文件
└── agents/
    └── antigravity-impl.md # 代理定义 (258 行)
```

## 计划文件位置

```
~/.gemini/antigravity/brain/
├── [uuid-1]/
│   └── implementation_plan.md.resolved
├── [uuid-2]/
│   └── implementation_plan.md.resolved
└── ...
```

## 代理工作流程

```
用户输入计划名称
    ↓
搜索 ~/.gemini/antigravity/brain/**/implementation_plan.md.resolved
    ↓
匹配包含计划名称的文件
    ↓
解析计划内容
    ↓
创建任务清单
    ↓
执行代码修改 (MODIFY/DELETE/ADD)
    ↓
运行验证测试
    ↓
生成完成报告
```

## 支持的操作

| 操作 | 说明 | 示例 |
|------|------|------|
| MODIFY | 修改现有代码 | 替换方法实现 |
| DELETE | 删除代码或方法 | 移除过时代码 |
| ADD | 添加新代码 | 新增方法或类 |

## 输出符号说明

| 符号 | 含义 |
|------|------|
| 📋 | 计划信息 |
| 📄 | 文件路径 |
| 🎯 | 实作概要 |
| 📝 | 修改操作 |
| ✅ | 成功 |
| ❌ | 失败 |
| ⚠️ | 警告 |
| 🧪 | 测试验证 |
| ✨ | 完成报告 |
| 💡 | 提示 |
| 📊 | 统计信息 |
| 📌 | 后续步骤 |
| 🎉 | 完成 |

## 常用命令

### 列出所有计划
```
ls ~/.gemini/antigravity/brain/*/implementation_plan.md.resolved
```

### 查看计划内容
```
cat ~/.gemini/antigravity/brain/[uuid]/implementation_plan.md.resolved
```

### 搜索特定计划
```
grep -r "EZPAY-730-3" ~/.gemini/antigravity/brain/*/implementation_plan.md.resolved
```

## 触发示例

### 英文
```
antigravity-impl EZPAY-730-3
```

### 中文
```
执行 EZPAY-730-3 计划
实作 EZPAY-730-3
帮我完成 EZPAY-730-3 的修改
```

## 计划文件格式模板

```markdown
# [计划名称] [标题]

## 问题概要
| 问题 | 风险等级 | 影响 |
|------|---------|------|
| 1. ... | ... | ... |

## 修改方案

### [MODIFY] [文件路径]
**位置**：第 N 行

```diff
-旧代码
+新代码
```

**理由**：[说明]

## 验证计划

### 自动化测试
```bash
mvn test -Dtest="..."
```

## 修改文件清单
| 文件 | 操作 | 问题 |
|------|------|------|
| ... | MODIFY | #1 |
```

## 代理能力

- ✅ 自动搜索和匹配计划
- ✅ 解析 Markdown 格式计划
- ✅ 精确应用 diff 修改
- ✅ 执行 Maven/Gradle 测试
- ✅ 验证编译状态
- ✅ 生成详细报告
- ✅ 处理依赖关系
- ✅ 错误处理和恢复

## 配置参数

| 参数 | 值 | 说明 |
|------|---|------|
| name | antigravity-impl | 代理标识符 |
| model | inherit | 跟随默认模型 |
| color | green | 创建/生成类任务 |
| tools | 7个核心工具 | Bash, Glob, Grep, Read, Edit, Write, NotebookEdit |

## 故障排除

| 问题 | 解决方案 |
|------|----------|
| 找不到计划 | 检查计划名称，确认文件存在 |
| 修改失败 | 检查代码是否已变更，更新计划 |
| 测试失败 | 分析失败原因，修复代码 |
| 编译错误 | 检查语法，修复错误 |

## 最佳实践

1. ✅ 在测试分支上执行
2. ✅ 逐个验证修改
3. ✅ 运行完整测试套件
4. ✅ 检查编译警告
5. ✅ 阅读完成报告
6. ✅ 进行手动验证
7. ✅ 代码审查后再合并

## 版本信息

- **版本**: 1.0.0
- **创建**: 2026-01-25
- **作者**: Claude Code
- **状态**: ✅ 活跃

## 相关资源

- [README.md](README.md) - 插件说明
- [USAGE.md](USAGE.md) - 详细使用指南
- [agent 定义](agents/antigravity-impl.md) - 完整代理配置

---

**提示**: 将此文件添加到书签或快速访问，以便随时参考！
