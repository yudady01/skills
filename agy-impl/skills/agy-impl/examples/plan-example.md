# EZPAY-730-3 分润计算问题修复计划

计划创建日期：2026-01-25
计划状态：待执行

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

### 问题 #2：分润金额计算精度问题

**问题描述**：
分润金额计算时，中间结果的精度不足，导致最终结果有偏差。

**根本原因**：
- 计算过程中使用了 `MathContext.DECIMAL32`（精度 7 位）
- 应该使用 `MathContext.DECIMAL64`（精度 16 位）

**影响范围**：
- 大额分润交易的精度偏差更明显
- 需要重新计算历史分润数据

**解决方案**：
修改计算上下文，使用 `DECIMAL64` 精度。

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

**位置**：第 128-130 行

**修改内容**：
```diff
     private BigDecimal calculateProfit(BigDecimal amount, BigDecimal rate) {
-        MathContext mc = new MathContext(7, RoundingMode.HALF_UP);
+        MathContext mc = new MathContext(16, RoundingMode.HALF_UP);
         return amount.multiply(rate, mc);
     }
```

**理由**：提高计算精度，从 DECIMAL32（7位）提升到 DECIMAL64（16位）

**影响**：分润金额计算精度提高，大额交易的结果更准确

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
mvn test -Dtest="org.xxpay.service.service.profitsharing.ProfitSharingServiceTest"
```

**预期结果**：所有测试通过

### 3. 集成测试

```bash
mvn test -Dtest="org.xxpay.service.service.profitsharing.*Test"
```

**预期结果**：所有分润相关测试通过

## 修改文件清单

| 文件路径 | 操作类型 | 关联问题 |
|---------|---------|---------|
| FeeCalculator.java | MODIFY | #1 |
| ProfitSharingService.java | MODIFY | #2 |

## 预期影响

**功能影响**：
- ✅ 修复费率计算舍入问题
- ✅ 提高分润金额计算精度

**性能影响**：
- 无显著性能影响

**兼容性影响**：
- 需要数据库修复历史分润数据

## 手动验证步骤

1. **登录测试环境**
2. **创建测试交易**，金额为 100.567 元
3. **验证分润计算**：
   - 费率 3.5% 应得到 3.52 元（向上取整）
   - 而非 3.51 元（向下取整）
4. **验证日志输出**：
   - 确认无异常日志
   - 确认计算日志正确

## 后续工作

- [ ] 修复历史分润数据
- [ ] 更新相关文档
- [ ] 通知业务团队

---

**计划版本**：1.0
**创建人**：Claude Code
**审核人**：[待填写]
**执行人**：[待填写]
