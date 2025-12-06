---
description: 执行单一、具体的任务，专注于精确实现和高效率交付
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, TodoWrite]
---

# 任务命令

这个命令专门用于执行单一、明确的任务，提供精确的实现和快速交付。

## 任务执行流程

### 1. 任务分析

**解析任务请求**：`$ARGUMENTS`

明确任务的核心要素：
- **任务目标** - 具体要完成什么
- **影响范围** - 涉及的文件和组件
- **验收标准** - 完成后的验证条件
- **依赖关系** - 前置条件和后续影响

### 2. 实施策略

**基于任务类型选择执行策略**：

#### 修复类任务
```typescript
// Bug 修复流程
const fixTask = {
  analysis: {
    reproduce: "重现问题的步骤",
    locate: "定位问题代码位置",
    understand: "理解根本原因"
  },
  solution: {
    design: "设计修复方案",
    implement: "实施代码修复",
    test: "验证修复效果"
  },
  validation: {
    regression: "回归测试",
    verify: "确认无副作用",
    document: "更新相关文档"
  }
};
```

#### 功能类任务
```typescript
// 小功能实现流程
const featureTask = {
  design: {
    understand: "理解功能需求",
    interface: "设计接口",
    algorithm: "设计算法逻辑"
  },
  implement: {
    core: "实现核心逻辑",
    error: "添加错误处理",
    test: "编写单元测试"
  },
  integrate: {
    connect: "集成到现有系统",
    config: "更新配置",
    document: "更新文档"
  }
};
```

#### 重构类任务
```typescript
// 代码重构流程
const refactorTask = {
  analyze: {
    current: "分析当前实现",
    issues: "识别问题点",
    goals: "确定重构目标"
  },
  redesign: {
    structure: "重新设计结构",
    pattern: "应用设计模式",
    optimize: "性能优化"
  },
  implement: {
    refactor: "重构代码",
    test: "验证功能一致性",
    performance: "性能基准测试"
  }
};
```

### 3. 质量保证

**任务质量检查清单**：
- [ ] **类型安全** - TypeScript 编译无错误
- [ ] **功能正确** - 按需求正确实现
- [ ] **边界处理** - 错误和异常情况处理
- [ ] **性能合理** - 无性能回归
- [ ] **代码风格** - 符合编码标准
- [ ] **测试覆盖** - 关键路径有测试

### 4. 实施步骤

**标准化任务执行**：

#### 步骤 1：环境准备
```bash
# 确保工作目录整洁
git status

# 拉取最新代码
git pull origin main

# 安装依赖（如果需要）
npm install
```

#### 步骤 2：任务理解
```typescript
// 分析任务需求和上下文
const taskContext = {
  description: "用户的具体需求描述",
  files: "可能涉及的文件列表",
  dependencies: "相关的依赖和模块",
  constraints: "技术和业务约束"
};
```

#### 步骤 3：实施开发
```typescript
// 实现任务的具体代码
const implementation = {
  // 核心实现逻辑
  core: "实现主要功能",

  // 错误处理
  errorHandling: "添加 try-catch 和错误处理",

  // 类型定义
  types: "定义必要的 TypeScript 类型",

  // 测试代码
  tests: "编写相应的测试用例"
};
```

#### 步骤 4：质量验证
```bash
# 类型检查
npm run type-check

# 代码检查
npm run lint

# 运行测试
npm test

# 构建验证
npm run build
```

#### 步骤 5：文档更新
```typescript
// 更新相关文档
const documentation = {
  readme: "更新 README.md（如果需要）",
  api: "更新 API 文档",
  examples: "添加使用示例",
  changelog: "更新变更日志"
};
```

## 使用指南

### 基础用法

```bash
# Bug 修复
/task "修复用户登录时 token 过期处理"

# 小功能添加
/task "为 API 添加响应缓存机制"

# 代码重构
/task "重构用户验证模块，提高可读性"

# 配置更新
/task "更新 TypeScript 配置以支持新的路径别名"
```

### 高级用法

```bash
# 带有具体要求的任务
/task "优化数据库查询性能，目标将查询时间减少 30%"

# 安全相关任务
/task "为 API 端点添加输入验证，防止 SQL 注入"

# 工具集成任务
/task "集成 Redis 作为会话存储，替换内存存储"
```

## 任务类型模板

### Bug 修复模板
```typescript
// 修复特定问题的标准流程
async function fixBug(bugDescription: string) {
  // 1. 重现问题
  await reproduceIssue(bugDescription);

  // 2. 定位问题代码
  const problematicCode = await locateProblematicCode();

  // 3. 分析根本原因
  const rootCause = await analyzeRootCause(problematicCode);

  // 4. 设计修复方案
  const fixStrategy = await designFixStrategy(rootCause);

  // 5. 实施修复
  await implementFix(fixStrategy);

  // 6. 验证修复
  await validateFix();

  // 7. 回归测试
  await regressionTest();

  // 8. 更新文档
  await updateDocumentation();
}
```

### 功能添加模板
```typescript
// 添加小功能的标准流程
async function addFeature(featureSpec: FeatureSpec) {
  // 1. 理解功能需求
  const requirements = await understandRequirements(featureSpec);

  // 2. 设计接口
  const interface = await designInterface(requirements);

  // 3. 实现核心逻辑
  const implementation = await implementCoreLogic(interface);

  // 4. 添加错误处理
  await addErrorHandling(implementation);

  // 5. 编写测试
  await writeTests(implementation);

  // 6. 集成到系统
  await integrateToSystem(implementation);

  // 7. 验证功能
  await validateFeature(requirements);
}
```

### 重构模板
```typescript
// 代码重构的标准流程
async function refactorCode(refactorSpec: RefactorSpec) {
  // 1. 分析当前代码
  const currentCode = await analyzeCurrentCode();

  // 2. 识别问题
  const issues = await identifyIssues(currentCode);

  // 3. 设计新结构
  const newStructure = await designNewStructure(issues);

  // 4. 重构实现
  const refactoredCode = await implementRefactoring(newStructure);

  // 5. 功能验证
  await verifyFunctionality(refactoredCode);

  // 6. 性能测试
  await performanceTest(refactoredCode);

  // 7. 更新文档
  await updateDocumentation(refactoredCode);
}
```

## 质量标准

### 代码质量
- **类型安全**：严格的 TypeScript 类型检查
- **错误处理**：完善的异常和错误情况处理
- **性能**：不引入性能回归
- **可读性**：清晰、易于理解的代码结构

### 测试标准
- **单元测试**：覆盖核心逻辑路径
- **集成测试**：验证与其他组件的交互
- **边界测试**：测试异常和边界情况
- **性能测试**：确保性能符合要求

### 文档标准
- **API 文档**：更新相关 API 文档
- **使用示例**：提供清晰的使用示例
- **变更记录**：记录重要的变更内容

## 常见问题处理

### 问题：任务复杂度超出预期
**症状**：原以为是简单任务，实际实施时发现很复杂

**解决方案**：
1. 评估当前进度
2. 重新定义任务范围
3. 如果需要，转换为 `/implement` 命令处理

### 问题：依赖关系冲突
**症状**：修改一个模块影响到其他模块

**解决方案**：
1. 分析依赖关系
2. 更新相关模块
3. 运行完整的回归测试

### 问题：测试不通过
**症状**：代码实现完成但测试失败

**解决方案**：
1. 检查测试逻辑
2. 验证代码实现
3. 修复不一致的地方

## 最佳实践

### 1. 任务定义
- 明确任务目标和验收标准
- 识别所有相关的文件和组件
- 考虑对现有功能的影响

### 2. 实施过程
- 遵循编码标准和最佳实践
- 及时编写和更新测试
- 保持代码的简洁和可读性

### 3. 质量保证
- 在每个步骤都进行验证
- 不要跳过测试和代码审查
- 确保文档及时更新

### 4. 沟通协调
- 及时报告进展和问题
- 寻求帮助和反馈
- 分享经验和知识

## 相关资源

### 参考文档
- **`@docs/rules/coding-standards.md`** - 编码规范
- **`@docs/rules/project-context.md`** - 项目上下文
- **`quality-assurance`** - 质量保证策略

### 相关技能
- **`typescript-project-setup`** - TypeScript 配置
- **`ai-coding-best-practices`** - 开发最佳实践

### 相关命令
- **`/implement`** - 复杂功能实现
- **`/review`** - 代码审查
- **`/code-quality`** - 质量检查

## 示例工作流

### 示例1：Bug 修复
```bash
# 用户请求
/task "修复 API 返回格式不一致的问题"

# 执行流程
# 1. 分析问题 - 发现不同端点返回格式不同
# 2. 定位代码 - 找到相关的控制器文件
# 3. 统一格式 - 定义统一的响应格式
# 4. 修改代码 - 更新所有相关端点
# 5. 编写测试 - 验证格式统一
# 6. 运行测试 - 确保所有测试通过
# 7. 更新文档 - 更新 API 文档
```

### 示例2：功能添加
```bash
# 用户请求
/task "为用户表添加最后登录时间字段"

# 执行流程
# 1. 数据库设计 - 添加 last_login_at 字段
# 2. 模型更新 - 更新 TypeScript 接口
# 3. 服务层更新 - 修改用户服务逻辑
# 4. API 更新 - 更新相关端点
# 5. 测试编写 - 添加字段更新和查询测试
# 6. 验证功能 - 确保字段正常工作
# 7. 文档更新 - 更新数据模型文档
```

通过这个命令，您可以高效地完成单一、明确的任务，确保每个任务都符合质量标准和最佳实践。