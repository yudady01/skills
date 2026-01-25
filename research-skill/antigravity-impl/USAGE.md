# Antigravity Implementation Plugin - 使用指南

## 快速开始

### 1. 确认计划存在

首先，确认你的 Antigravity 计划已保存在 `~/.gemini/antigravity/brain/` 目录下：

```bash
ls -la ~/.gemini/antigravity/brain/*/
```

你应该能看到类似这样的结构：
```
94d94e52-6074-43a0-9a9e-bc2d171dad84/
├── implementation_plan.md.resolved
└── ...
```

### 2. 调用代理

在 Claude Code 中，使用以下任一方式触发代理：

**方式 1：直接调用**
```
antigravity-impl EZPAY-730-3
```

**方式 2：自然语言**
```
帮我执行 EZPAY-730-3 的实作计划
```

**方式 3：中文指令**
```
实作 Antigravity 计划 EZPAY-730-3
```

### 3. 查看可用计划

如果你不确定有哪些可用的计划，可以让代理列出它们：

```
列出所有可用的 Antigravity 计划
```

## 工作流程详解

### 第一步：计划检索

代理会在 `~/.gemini/antigravity/brain` 目录下搜索所有 `implementation_plan.md.resolved` 文件，并查找包含你指定计划名称的文件。

### 第二步：计划解析

代理会解析计划文件的以下部分：
- 问题概要
- 问题分析
- 修改方案（MODIFY/DELETE/ADD 操作）
- 验证计划
- 修改文件清单

### 第三步：实作执行

代理会按照计划中的顺序，逐个文件进行修改。每个修改都会：
1. 读取原始文件
2. 应用 diff 修改
3. 验证修改结果
4. 报告完成状态

### 第四步：验证测试

代理会执行计划中定义的所有测试：
- 编译验证
- 单元测试
- 集成测试
- 质量检查

### 第五步：完成报告

代理会生成详细的实作报告，包括：
- 修改的文件列表
- 修改的代码行数
- 测试结果
- 后续建议

## 计划文件示例

一个有效的 `implementation_plan.md.resolved` 文件应该包含：

```markdown
# EZPAY-730-3 分润计算问题修复计划

## 问题概要
| 问题 | 风险等级 | 影响 |
|------|---------|------|
| 1. 费率计算舍入模式不匹配 | 🔴 高 | 可能导致财务损失 |

## 问题分析
[详细的问题分析...]

## 修改方案

### [MODIFY] FeeCalculator.java
**位置**：第 41 行

```diff
-BigDecimal floatingAmount = XXPayUtil.calOrderMultiplyRate(orderAmount, layer.getFloatingRate());
+BigDecimal floatingAmount = XXPayUtil.calOrderMultiplyRateforFee(orderAmount, layer.getFloatingRate());
```

**理由**：使用已有的 calOrderMultiplyRateforFee 方法实现向上取整

## 验证计划

### 自动化测试
```bash
cd /Users/tommy/Documents/work.nosync/dtg/dtg-pay
mvn test -Dtest="org.xxpay.service.service.profitsharing.*Test"
```

## 修改文件清单
| 文件 | 操作 | 问题 |
|------|------|------|
| FeeCalculator.java | MODIFY | #1 |
```

## 常见问题

### Q: 如果找不到计划怎么办？

A: 代理会列出所有可用的计划供你选择。你可以：
1. 从列表中选择正确的计划名称
2. 检查计划是否已保存到正确的目录
3. 确认计划文件的文件名是否为 `implementation_plan.md.resolved`

### Q: 如果修改失败怎么办？

A: 代理会暂停并报告问题。可能的原因：
1. 当前代码已经变更，与计划中的 diff 不匹配
2. 文件路径不正确
3. 权限问题

你需要：
1. 手动检查文件状态
2. 决定是否需要更新计划
3. 或手动完成修改

### Q: 测试失败怎么办？

A: 代理会报告失败的测试和原因。你需要：
1. 分析失败原因
2. 修复代码问题
3. 重新运行测试

### Q: 可以只执行部分计划吗？

A: 当前版本不支持部分执行。代理会执行完整的计划。如需部分执行，请：
1. 手动选择需要的修改
2. 或创建一个新的简化计划

## 最佳实践

1. **保持计划更新**：确保 `implementation_plan.md.resolved` 文件反映最新的代码状态
2. **测试环境**：在测试环境中先验证，再应用到生产环境
3. **版本控制**：在执行前创建新的分支
4. **备份重要文件**：在执行重大修改前备份
5. **逐步验证**：每个修改后立即验证，不要等待所有修改完成

## 高级用法

### 自定义验证步骤

如果你的计划需要特殊的验证步骤，可以在计划文件中添加：

```markdown
## 自定义验证

### 数据库验证
```bash
mysql -u root -p -e "USE xxpay; SELECT * FROM pay_order WHERE id = 'test';"
```

### API 验证
```bash
curl -X POST http://localhost:8080/api/test -d '{"test": "data"}'
```
```

### 多文件修改

计划可以包含多个文件的修改：

```markdown
## 修改方案

### [MODIFY] File1.java
[diff...]

### [MODIFY] File2.java
[diff...]

### [ADD] File3.java
```java
public class File3 {
    // 新文件内容
}
```
```

### 条件修改

对于需要用户选择的修改，使用：

```markdown
## 问题 2：方法选择

### 选项 A：使用 V2 方法（推荐）
[diff...]

### 选项 B：保留 V1 方法
[diff...]

> [!NOTE]
> 用户已选择：选项 A
```

## 技术细节

### 代理配置

- **模型**：inherit（跟随 Claude Code 默认模型）
- **颜色**：green（代表创建和生成）
- **工具**：Bash, Glob, Grep, Read, Edit, Write, NotebookEdit

### 工作目录

代理始终在当前项目根目录下工作，不会切换到其他目录。

### 权限要求

- 读取 `~/.gemini/antigravity/brain/` 目录
- 读写项目代码文件
- 执行 Maven/Gradle 命令
- 执行测试命令

## 支持

如果遇到问题：
1. 查看代理的详细输出
2. 检查计划文件格式是否正确
3. 验证文件路径和权限
4. 查看 Claude Code 的日志

## 版本历史

- **1.0.0** (2026-01-25): 初始版本
  - 支持基本的计划检索和实作
  - 支持 MODIFY/DELETE/ADD 操作
  - 支持自动测试验证
  - 生成详细的实作报告
