# Antigravity 计划文件格式规范

本文档定义 `implementation_plan.md.resolved` 文件的标准格式。

## 文件位置

```
~/.gemini/antigravity/brain/
├── [uuid-1]/
│   └── implementation_plan.md.resolved
├── [uuid-2]/
│   └── implementation_plan.md.resolved
└── ...
```

## 文件格式模板

```markdown
# [计划名称] [标题]

计划创建日期：YYYY-MM-DD
计划状态：[待执行/进行中/已完成]

## 问题概要

| 问题编号 | 问题描述 | 风险等级 | 影响范围 |
|---------|---------|---------|---------|
| #1 | 费率计算舍入模式不匹配 | 🔴 高 | 可能导致财务损失 |
| #2 | 分润金额计算精度问题 | 🟡 中 | 需要数据修复 |

**总体风险等级**：🔴 高

## 问题分析

### 问题 #1：费率计算舍入模式不匹配

**问题描述**：
当前使用 `calOrderMultiplyRate` 方法进行费率计算，该方法使用向下取整（FLOOR）的舍入模式。但根据业务需求，应该使用向上取整（CEILING）模式。

**根本原因**：
- `calOrderMultiplyRate` 内部使用 `RoundingMode.DOWN`
- 业务要求分润金额应向上取整，确保商户获得应得的全部收益

**影响范围**：
- 影响所有使用该费率计算器的分润交易
- 可能导致每笔交易损失最多 0.01 元

**解决方案**：
使用已有的 `calOrderMultiplyRateforFee` 方法，该方法使用 `RoundingMode.CEILING`。

### 问题 #2：[...]

## 修改方案

### [MODIFY] src/main/java/org/xxpay/service/service/profitsharing/FeeCalculator.java

**位置**：第 41 行

**修改内容**：
```diff
-BigDecimal floatingAmount = XXPayUtil.calOrderMultiplyRate(orderAmount, layer.getFloatingRate());
+BigDecimal floatingAmount = XXPayUtil.calOrderMultiplyRateforFee(orderAmount, layer.getFloatingRate());
```

**理由**：使用已有的 calOrderMultiplyRateforFee 方法实现向上取整

**影响**：修改后费率计算将使用正确的舍入模式

### [MODIFY] src/main/java/org/xxpay/service/service/profitsharing/ProfitSharingService.java

**位置**：第 128 行

**修改内容**：
```diff
-    // TODO: 修复精度问题
     profitAmount = calculateProfit(amount, rate);
+    profitAmount = calculateProfitWithPrecision(amount, rate);
```

**理由**：使用新的高精度计算方法

**影响**：分润金额计算精度从 2 位小数提高到 4 位小数

### [DELETE] src/main/java/org/xxpay/service/service/profitsharing/LegacyCalculator.java

**删除内容**：
```diff
-public class LegacyCalculator {
-    // 已废弃的旧版计算器
-}
```

**理由**：该类已被新的计算器替代，不再使用

### [ADD] src/main/java/org/xxpay/service/service/profitsharing/ProfitValidator.java

**添加内容**：
```java
public class ProfitValidator {
    /**
     * 验证分润金额的合法性
     */
    public static boolean validateProfitAmount(BigDecimal amount) {
        return amount != null && amount.compareTo(BigDecimal.ZERO) >= 0;
    }
}
```

**理由**：添加分润金额验证工具类

**位置**：文件新建于 `profitsharing` 包下

## 验证计划

### 1. 编译验证

```bash
cd /Users/tommy/Documents/work.nosync/dtg/dtg-pay
mvn clean compile
```

**预期结果**：编译成功，无错误

### 2. 单元测试

```bash
mvn test -Dtest="org.xxpay.service.service.profitsharing.FeeCalculatorTest"
```

**预期结果**：所有测试通过

**关键测试**：
- `testCalculateFeeWithCeilingRounding` - 验证向上取整
- `testCalculateFeeWithZeroRate` - 验证零费率处理
- `testCalculateFeeWithMaximumAmount` - 验证最大金额处理

### 3. 集成测试

```bash
mvn test -Dtest="org.xxpay.service.service.profitsharing.*Test"
```

**预期结果**：所有分润相关测试通过

### 4. 质量检查

- [ ] 代码符合项目编码规范
- [ ] 无新的 Checkstyle 警告
- [ ] 无新的 SpotBugs 问题

## 修改文件清单

| 文件路径 | 操作类型 | 关联问题 |
|---------|---------|---------|
| FeeCalculator.java | MODIFY | #1 |
| ProfitSharingService.java | MODIFY | #2 |
| LegacyCalculator.java | DELETE | #2 |
| ProfitValidator.java | ADD | #2 |

## 依赖关系

```
FeeCalculator.java (MODIFY)
    ↓
ProfitSharingService.java (MODIFY)
    ↓
LegacyCalculator.java (DELETE)
    ↓
ProfitValidator.java (ADD)
```

## 预期影响

**功能影响**：
- ✅ 修复费率计算舍入问题
- ✅ 提高分润金额计算精度
- ✅ 移除废弃代码
- ✅ 添加金额验证

**性能影响**：
- 无显著性能影响

**兼容性影响**：
- 可能需要数据库修复（历史分润数据）

## 回滚方案

如果修改后出现问题，可以：
1. 还原修改的代码文件
2. 使用 Git 撤销提交
3. 从数据库备份恢复数据

## 手动验证步骤

1. **登录测试环境**
2. **创建测试交易**
3. **验证分润计算**
   - 检查费率计算是否向上取整
   - 检查分润金额精度是否正确
4. **验证日志输出**
   - 确认无异常日志
   - 确认计算日志正确

## 后续工作

- [ ] 修复历史分润数据
- [ ] 更新相关文档
- [ ] 通知相关人员

---

**计划版本**：1.0
**创建人**：Claude Code
**审核人**：[待填写]
**执行人**：[待填写]
