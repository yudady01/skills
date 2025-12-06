---
description: 协调从需求到部署的完整实现生命周期，智能化管理开发流程
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, TodoWrite, Task]
---

# 实现命令

这个命令协调完整的开发流程，从需求分析到最终部署，确保每个阶段都遵循最佳实践。

## 执行决策流程

### 1. 当前情况评估

**分析用户请求**：`$ARGUMENTS`

根据当前情况选择执行路径：

| 情况模式 | 判断标准 | 执行策略 |
|---------|---------|----------|
| 新功能需求 | 没有现有文档，新功能开发 | 启动需求分析代理 |
| 继续开发 | 存在 PRD/设计文档，继续工作 | 识别当前阶段并执行下一步 |
| 质量问题 | 检测到错误、测试失败、构建问题 | 执行质量修复流程 |
| 模糊请求 | 意图不明确，需要澄清 | 向用户询问具体需求 |

### 2. 流程管理

**规模确定和任务注册**：
当确定工作规模后，将所有必要步骤注册到 TodoWrite：

```typescript
// 小规模任务示例
const smallScaleTasks = [
  "分析当前代码结构",
  "实现功能代码",
  "编写单元测试",
  "运行质量检查",
  "提交代码"
];

// 中等规模任务示例
const mediumScaleTasks = [
  "创建设计文档",
  "制定工作计划",
  ...smallScaleTasks
];

// 大规模任务示例
const largeScaleTasks = [
  "创建 PRD",
  "架构设计（需要 ADR）",
  ...mediumScaleTasks
];
```

### 3. 代理协调

**调用专用代理**：
根据任务类型和规模，调用相应的专业化代理：

#### 需求分析阶段
```typescript
// 启动需求分析代理
const requirementAnalysis = await Task({
  subagent_type: 'general-purpose',
  prompt: `分析以下需求并确定开发规模：${userRequest}

  请评估：
  - 任务复杂度和影响范围
  - 需要的文档类型（PRD/ADR/设计文档）
  - 预估开发时间和资源

  参考文档：@docs/rules/documentation-criteria.md`
});
```

#### 设计阶段（如果需要）
```typescript
// 对于中等以上规模的功能
if (scale === 'medium' || scale === 'large') {
  const designPhase = await Task({
    subagent_type: 'general-purpose',
    prompt: `基于需求分析结果创建技术设计文档

    需求：${requirementAnalysis}

    请包含：
    - 系统架构设计
    - 数据流设计
    - API 设计
    - 技术选型说明`
  });
}
```

#### 实现阶段
```typescript
// 任务执行代理
const implementation = await Task({
  subagent_type: 'general-purpose',
  prompt: `基于设计文档实现功能：

  设计文档：${designDoc}
  工作计划：${workPlan}

  请：
  1. 遵循编码标准 @docs/rules/coding-standards.md
  2. 实现核心功能
  3. 编写相应的测试
  4. 确保类型安全`
});
```

### 4. 质量保证流程

**自动化质量检查**：
```typescript
// 质量检查清单
const qualityChecks = [
  'TypeScript 类型检查',
  '代码格式检查',
  '单元测试执行',
  '集成测试验证',
  '性能基准测试'
];

// 执行质量检查
for (const check of qualityChecks) {
  const result = await executeQualityCheck(check);
  if (!result.passed) {
    // 启动质量修复代理
    await fixQualityIssues(result.issues);
  }
}
```

### 5. 文档更新

**维护项目文档**：
- 更新 README.md
- 更新 API 文档
- 记录架构决策（如果有）
- 更新变更日志

## 使用指南

### 基础用法

```bash
# 小功能实现
/implement "添加用户登录功能"

# 复杂功能实现
/implement "实现完整的电商系统用户管理模块"

# 继续之前的工作
/implement "继续实现支付功能"
```

### 高级用法

```bash
# 带有具体需求的功能
/implement "实现 RESTful API，支持 CRUD 操作，使用 JWT 认证"

# 修复和优化
/implement "重构数据访问层，提高性能并添加缓存"

# 集成新功能
/implement "集成第三方支付网关，支持支付宝和微信支付"
```

## 最佳实践

### 1. 需求明确化
- 提供具体的功能描述
- 说明业务背景和目标
- 列出关键的验收标准

### 2. 规模评估
- 小功能：1-2 个文件，单一职责
- 中等功能：3-5 个文件，涉及多个组件
- 大功能：6+ 个文件，架构级变更

### 3. 质量标准
- 100% TypeScript 严格模式
- 80%+ 测试覆盖率
- 零 lint 错误
- 完整的文档

### 4. 提交规范
- 使用约定式提交格式
- 包含测试和文档更新
- 通过所有质量检查

## 常见场景

### 场景1：新功能开发
```bash
/implement "添加用户评论功能，支持嵌套回复和点赞"
```

预期流程：
1. 需求分析（中等规模）
2. 设计文档创建
3. 数据库设计
4. API 实现
5. 前端组件开发
6. 测试编写
7. 文档更新

### 场景2：性能优化
```bash
/implement "优化 API 响应时间，目标减少 50% 延迟"
```

预期流程：
1. 性能基准测试
2. 瓶颈分析
3. 优化方案设计
4. 代码重构
5. 性能验证
6. 文档更新

### 场景3：Bug 修复
```bash
/implement "修复用户登录时 token 刷新失败的问题"
```

预期流程：
1. 问题复现和分析
2. 根因定位
3. 修复方案
4. 测试验证
5. 回归测试

## 故障排除

### 常见问题

**问题**：任务规模评估错误
**解决**：使用 `/task` 命令重新评估当前任务

**问题**：质量检查失败
**解决**：使用 `/code-quality` 命令手动运行质量检查

**问题**：依赖关系冲突
**解决**：检查 package.json 并运行 `npm audit fix`

## 相关资源

### 参考文档
- **`@docs/rules/project-context.md`** - 项目上下文和约束
- **`@docs/rules/documentation-criteria.md`** - 文档标准
- **`@docs/rules/coding-standards.md`** - 编码规范

### 相关技能
- **`ai-coding-best-practices`** - 开发最佳实践
- **`typescript-project-setup`** - TypeScript 配置
- **`quality-assurance`** - 质量保证策略

### 相关命令
- **`/task`** - 单一任务执行
- **`/design`** - 设计文档创建
- **`/review`** - 代码审查
- **`/code-quality`** - 质量检查

## 示例工作流

### 完整功能开发示例

```bash
# 用户请求
/implement "创建博客系统，支持文章发布、评论和用户管理"

# 系统自动执行的流程
# 1. 需求分析 → 确定为大规模功能，需要 PRD
# 2. 创建 PRD → 详细的产品需求文档
# 3. 技术设计 → 系统架构和技术选型
# 4. 工作计划 → 任务分解和时间估算
# 5. 逐步实现 → 按模块依次开发
# 6. 质量保证 → 测试和审查
# 7. 部署准备 → 文档和配置
# 8. 最终提交 → 清理的代码提交
```

通过这个命令，您可以享受到从概念到部署的完整开发流程管理，确保每个环节都符合最佳实践标准。