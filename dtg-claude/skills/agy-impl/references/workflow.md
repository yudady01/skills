# Antigravity 实作详细工作流程

本文档提供 Antigravity 计划实作的详细工作流程指南。

## 阶段 1：计划检索与加载

### 步骤 1.1：搜索计划文件

使用 Glob 工具在 `~/.gemini/antigravity/brain` 目录下搜索：

```
~/.gemini/antigravity/brain/**/implementation_plan.md.resolved
```

### 步骤 1.2：匹配计划名称

对找到的每个文件：
1. 使用 Read 工具读取文件内容
2. 检查标题是否包含计划名称
3. 计划名称通常在第一行：`# EZPAY-730-3 分润计算问题修复计划`

### 步骤 1.3：处理搜索结果

**找到唯一匹配**：
- 加载该计划文件
- 继续执行

**找到多个匹配**：
- 向用户列出所有匹配的文件
- 要求用户确认使用哪一个

**未找到匹配**：
- 列出所有可用的计划
- 提示用户确认计划名称

## 阶段 2：计划分析与准备

### 步骤 2.1：问题理解

阅读并理解以下部分：

1. **问题概要表格**：
   - 问题描述
   - 风险等级（高/中/低）
   - 影响范围

2. **问题分析**：
   - 根本原因
   - 技术背景
   - 业务影响

### 步骤 2.2：修改范围确认

从计划中提取：
1. 所有需要修改的文件路径
2. 每个文件的修改类型（MODIFY/DELETE/ADD）
3. 修改之间的依赖关系
4. 修改的先后顺序

### 步骤 2.3：创建任务清单

使用 TodoWrite 工具创建任务列表：

```javascript
TodoWrite({
  todos: [
    { content: "读取 FeeCalculator.java", status: "pending", activeForm: "读取 FeeCalculator.java" },
    { content: "修改费率计算方法", status: "pending", activeForm: "修改费率计算方法" },
    { content: "运行单元测试", status: "pending", activeForm: "运行单元测试" },
    // ...
  ]
})
```

### 步骤 2.4：向用户展示计划

在开始执行前，向用户展示：
```
📋 找到 Antigravity 计划：EZPAY-730-3

🎯 实作概要：
- 问题数量：2
- 修改文件：2 个文件
- 风险等级：高

📝 实作任务：
1. 修改 FeeCalculator.java 的费率计算方法
2. 修改 ProfitSharingService.java 的分润逻辑
3. 运行单元测试
4. 运行集成测试

开始实作...
```

## 阶段 3：代码实作

### 步骤 3.1：读取原始文件

对每个需要修改的文件：

```
Read /path/to/FeeCalculator.java
```

理解：
- 文件的整体结构
- 需要修改的位置
- 相关的导入语句
- 方法和类的上下文

### 步骤 3.2：应用 MODIFY 修改

1. **找到修改位置**：
   - 根据计划中的"位置"信息（如"第 41 行"）
   - 或通过代码内容搜索

2. **使用 Edit 工具**：
   ```javascript
   Edit({
     file_path: "/path/to/FeeCalculator.java",
     old_string: "BigDecimal floatingAmount = XXPayUtil.calOrderMultiplyRate(orderAmount, layer.getFloatingRate());",
     new_string: "BigDecimal floatingAmount = XXPayUtil.calOrderMultiplyRateforFee(orderAmount, layer.getFloatingRate());"
   })
   ```

3. **验证修改**：
   - 重新读取文件
   - 确认修改正确
   - 检查语法

### 步骤 3.3：应用 DELETE 修改

1. **定位要删除的代码**：
   - 可以是单行、多行或整个方法

2. **使用 Edit 工具删除**：
   ```javascript
   Edit({
     file_path: "/path/to/File.java",
     old_string: "// 要删除的多行代码\n包括这里\n和这里",
     new_string: ""
   })
   ```

3. **检查依赖**：
   - 确认没有其他代码引用被删除的部分
   - 如有引用，需要一并处理

### 步骤 3.4：应用 ADD 修改

1. **确定添加位置**：
   - 文件开头（导入语句）
   - 指定方法内
   - 指定行号

2. **使用 Edit 工具添加**：
   ```javascript
   Edit({
     file_path: "/path/to/File.java",
     old_string: "public class File {",
     new_string: "public class File {\n    // 新添加的字段\n    private String newField;"
   })
   ```

3. **验证集成**：
   - 确认新代码与现有代码正确集成
   - 检查是否需要添加导入语句

## 阶段 4：验证与测试

### 步骤 4.1：编译验证

```bash
# Maven
mvn compile

# Gradle
gradle build

# 检查输出
# - 确认没有编译错误
# - 注意新增的警告
```

### 步骤 4.2：运行单元测试

```bash
# 运行特定测试类
mvn test -Dtest="FeeCalculatorTest"

# 运行特定包的测试
mvn test -Dtest="org.xxpay.service.service.profitsharing.*Test"
```

### 步骤 4.3：运行集成测试

```bash
mvn verify
```

### 步骤 4.4：质量检查

手动检查：
- [ ] 代码符合项目编码规范
- [ ] 没有引入新的性能问题
- [ ] 没有引入安全问题
- [ ] 导入语句正确且无冗余
- [ ] 注释准确且有意义

## 阶段 5：完成报告

### 步骤 5.1：汇总实作内容

```
✨ 实作完成！

📊 实作总结：
- 修改文件：
  - FeeCalculator.java (MODIFY)
  - ProfitSharingService.java (MODIFY)
- 修改行数：约 15 行
- 新增代码：5 行
- 删除代码：10 行
```

### 步骤 5.2：报告验证结果

```
🧪 验证结果：
- 编译状态：✅ 成功
- 单元测试：✅ 12/12 通过
- 集成测试：✅ 8/8 通过
- 质量检查：✅ 通过
```

### 步骤 5.3：后续建议

```
📌 后续步骤：
1. 在测试环境中验证修改
2. 进行手动测试验证
3. 代码审查
4. 合并到主分支
```

## 错误处理流程

### 修改不匹配

如果计划的 diff 与当前代码不匹配：

1. **暂停执行**
2. **报告问题**：
   ```
   ⚠️ 修改文件时遇到问题：FeeCalculator.java

   问题：代码已变更，diff 不匹配

   计划中：calOrderMultiplyRate
   当前代码：calOrderMultiplyRateV2

   建议解决方案：
   1. 手动检查文件状态
   2. 更新计划文件
   3. 或手动完成修改

   等待用户指示...
   ```
3. **等待用户指示**

### 测试失败

如果测试失败：

1. **分析失败原因**
2. **报告失败**：
   ```
   ❌ 验证失败：FeeCalculatorTest.testCalculateFee

   失败原因：
   Expected: 100.50
   Actual: 100.00

   建议：检查舍入模式设置

   实作暂停，等待问题解决...
   ```
3. **等待用户决定下一步**

## 进度追踪

在整个实作过程中，使用 TodoWrite 工具追踪进度：

```javascript
// 开始任务
TodoWrite({ todos: [...], index: 0 })  // 标记第一个任务为 in_progress

// 完成任务
TodoWrite({ todos: [...], index: 0 })  // 标记第一个任务为 completed

// 继续下一个任务
TodoWrite({ todos: [...], index: 1 })  // 标记第二个任务为 in_progress
```

## 最佳实践

1. **逐个文件修改**：完成一个文件的所有修改后，再进行下一个文件
2. **立即验证**：每个修改后立即验证，不要等待所有修改完成
3. **保持透明**：及时向用户报告进度和问题
4. **质量优先**：不跳过验证步骤
5. **尊重计划**：不要添加计划中未提及的修改
