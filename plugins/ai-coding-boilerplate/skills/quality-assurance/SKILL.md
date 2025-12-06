---
name: quality-assurance
description: This skill should be used when the user asks to "ensure code quality", "run quality checks", "setup quality gates", "implement code review", "testing strategy", or "quality assurance workflow". Provides comprehensive quality assurance and testing strategies for TypeScript projects.
version: 1.0.0
---

# 质量保证技能

这个技能提供全面的代码质量保证策略，包括自动化检查、测试策略和代码审查流程。

## 质量检查层级

### 1. 静态分析
自动代码分析，无需运行代码：
- **TypeScript 编译器** - 类型检查和语法验证
- **ESLint/Biome** - 代码风格和潜在问题检测
- **Prettier/Biome** - 代码格式化
- **Madge** - 依赖循环检测

### 2. 动态分析
运行时代码分析：
- **单元测试** - 函数和类级别测试
- **集成测试** - 模块间交互测试
- **端到端测试** - 完整功能流程测试
- **性能测试** - 性能基准和回归测试

### 3. 人工审查
代码审查和质量评估：
- **代码审查** - 同行评审
- **架构审查** - 设计模式评估
- **安全审查** - 安全漏洞检查

## 自动化质量门

### Pre-commit 检查
配置 Git hooks 进行提交前检查：

```json
// package.json
{
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  "lint-staged": {
    "src/**/*.{ts,tsx}": [
      "biome check --write",
      "biome format --write"
    ]
  }
}
```

### CI/CD 质量门
GitHub Actions 配置：

```yaml
name: Quality Gates
on: [push, pull_request]
jobs:
  quality-check:
    runs-on: ubuntu-latest
    steps:
      - name: Type Check
        run: npm run type-check

      - name: Lint Check
        run: npm run lint

      - name: Format Check
        run: npm run format:check

      - name: Unused Exports
        run: npm run check:unused

      - name: Circular Dependencies
        run: npm run check:deps

      - name: Unit Tests
        run: npm test

      - name: Coverage Check
        run: npm run test:coverage
```

## 测试策略

### 测试金字塔
```
    /\
   /  \     E2E Tests (少量)
  /____\
 /      \   Integration Tests (适量)
/__________\ Unit Tests (大量)
```

### 单元测试策略
使用 Vitest 进行单元测试：

```typescript
// __tests__/utils/validator.test.ts
import { describe, it, expect, test } from 'vitest';
import { validateEmail, validatePassword } from '@/lib/utils/validator';

describe('Validator Utils', () => {
  describe('validateEmail', () => {
    it('should validate correct email format', () => {
      expect(validateEmail('user@example.com')).toBe(true);
    });

    it('should reject invalid email formats', () => {
      const invalidEmails = [
        'invalid',
        'user@',
        '@example.com',
        'user.example.com'
      ];

      invalidEmails.forEach(email => {
        expect(validateEmail(email)).toBe(false);
      });
    });
  });

  describe('validatePassword', () => {
    it('should enforce password complexity', () => {
      const weakPassword = '123';
      const strongPassword = 'ComplexPass123!';

      expect(validatePassword(weakPassword)).toBe(false);
      expect(validatePassword(strongPassword)).toBe(true);
    });
  });
});
```

### 集成测试策略
测试模块间交互：

```typescript
// __tests__/integration/user-service.test.ts
import { describe, it, expect, beforeAll, afterAll } from 'vitest';
import { UserService } from '@/lib/services/user-service';
import { TestDatabase } from '@/lib/__tests__/helpers/test-database';

describe('UserService Integration', () => {
  let userService: UserService;
  let testDb: TestDatabase;

  beforeAll(async () => {
    testDb = new TestDatabase();
    await testDb.setup();
    userService = new UserService(testDb.connection);
  });

  afterAll(async () => {
    await testDb.cleanup();
  });

  it('should create and retrieve user', async () => {
    const userData = {
      name: 'Test User',
      email: 'test@example.com',
      password: 'SecurePass123!'
    };

    const createdUser = await userService.create(userData);
    const retrievedUser = await userService.findById(createdUser.id);

    expect(retrievedUser).toBeDefined();
    expect(retrievedUser.email).toBe(userData.email);
  });
});
```

### 端到端测试策略
完整功能流程测试：

```typescript
// __tests__/e2e/user-registration.test.ts
import { test, expect } from '@playwright/test';

test.describe('User Registration Flow', () => {
  test('should complete user registration process', async ({ page }) => {
    await page.goto('/register');

    // 填写注册表单
    await page.fill('[data-testid=name-input]', 'John Doe');
    await page.fill('[data-testid=email-input]', 'john@example.com');
    await page.fill('[data-testid=password-input]', 'SecurePass123!');

    // 提交表单
    await page.click('[data-testid=register-button]');

    // 验证重定向到仪表板
    await expect(page).toHaveURL('/dashboard');
    await expect(page.locator('[data-testid=welcome-message]')).toContainText('John');
  });
});
```

## 代码覆盖率

### 覆盖率配置
Vitest 覆盖率设置：

```typescript
// vitest.config.ts
export default defineConfig({
  test: {
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html', 'lcov'],
      thresholds: {
        global: {
          branches: 80,
          functions: 80,
          lines: 80,
          statements: 80
        }
      },
      exclude: [
        'node_modules/',
        'dist/',
        '**/*.d.ts',
        '**/*.config.*',
        '**/test/**'
      ]
    }
  }
});
```

### 覆盖率报告
生成详细的覆盖率报告：

```bash
# 生成覆盖率报告
npm run test:coverage

# 查看覆盖率摘要
npm run test:coverage:summary

# 在浏览器中查看详细报告
open coverage/index.html
```

## 代码质量指标

### 复杂度测量
使用圈复杂度评估代码质量：

```bash
# 安装复杂度测量工具
npm install -D complexity-report

# 运行复杂度分析
npx complexity-report -f json src/ > complexity.json

# 设置复杂度阈值
npx complexity-report -t 10 src/
```

### 代码重复检测
查找重复代码：

```bash
# 安装重复代码检测工具
npm install -D jscpd

# 运行重复代码检测
npx jscpd src/ --min-lines 5 --threshold 5

# 生成重复代码报告
npx jscpd src/ --format json > duplicate-report.json
```

## 性能质量

### 性能测试
使用性能基准测试：

```typescript
// __tests__/performance/sorting.test.ts
import { describe, it, expect } from 'vitest';
import { quickSort, bubbleSort } from '@/lib/utils/sorting';

describe('Performance Tests', () => {
  it('quickSort should be faster than bubbleSort for large arrays', () => {
    const largeArray = Array.from({ length: 10000 }, () => Math.random());

    const quickSortStart = performance.now();
    quickSort([...largeArray]);
    const quickSortTime = performance.now() - quickSortStart;

    const bubbleSortStart = performance.now();
    bubbleSort([...largeArray]);
    const bubbleSortTime = performance.now() - bubbleSortStart;

    expect(quickSortTime).toBeLessThan(bubbleSortTime);
  });
});
```

### 内存泄漏检测
监控内存使用：

```typescript
// __tests__/performance/memory-leak.test.ts
import { describe, it, expect, beforeAll, afterAll } from 'vitest';

describe('Memory Leak Detection', () => {
  it('should not leak memory when creating instances', async () => {
    const initialMemory = process.memoryUsage().heapUsed;

    // 创建大量实例
    const instances = [];
    for (let i = 0; i < 10000; i++) {
      instances.push(new SomeClass());
    }

    // 清理引用
    instances.length = 0;

    // 强制垃圾回收（如果可用）
    if (global.gc) {
      global.gc();
    }

    const finalMemory = process.memoryUsage().heapUsed;
    const memoryIncrease = finalMemory - initialMemory;

    // 内存增长应该很小
    expect(memoryIncrease).toBeLessThan(1024 * 1024); // 1MB
  });
});
```

## 安全质量

### 安全漏洞扫描
使用自动化安全扫描：

```json
// package.json
{
  "scripts": {
    "audit": "npm audit",
    "audit:fix": "npm audit fix",
    "security-check": "npx audit-ci --moderate"
  }
}
```

### 依赖安全检查
配置依赖安全监控：

```yaml
# .github/workflows/security.yml
name: Security Check
on:
  schedule:
    - cron: '0 0 * * *' # 每日运行
  workflow_dispatch:

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '20'

      - name: Audit dependencies
        run: npm audit --audit-level moderate

      - name: Run Snyk security scan
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
```

## 质量监控和报告

### 质量仪表板
创建质量指标收集：

```typescript
// scripts/quality-reporter.ts
interface QualityMetrics {
  testCoverage: number;
  codeComplexity: number;
  duplicateCode: number;
  securityVulnerabilities: number;
  lintErrors: number;
  buildTime: number;
}

export class QualityReporter {
  async generateReport(): Promise<QualityMetrics> {
    return {
      testCoverage: await this.getCoverage(),
      codeComplexity: await this.getComplexity(),
      duplicateCode: await this.getDuplicateCodePercentage(),
      securityVulnerabilities: await this.getSecurityVulnerabilities(),
      lintErrors: await this.getLintErrors(),
      buildTime: await this.getBuildTime()
    };
  }
}
```

### 持续改进
基于质量数据进行持续改进：

1. **设定质量目标** - 明确的质量指标和阈值
2. **定期评估** - 周期性质量检查和报告
3. **问题识别** - 及时发现质量问题
4. **改进措施** - 制定并实施改进计划

## 参考资源

### 质量检查脚本
使用 `scripts/` 目录中的自动化工具：
- **`scripts/quality-gate.sh`** - 质量门检查脚本
- **`scripts/coverage-report.sh`** - 覆盖率报告生成
- **`scripts/security-audit.sh`** - 安全审计脚本

### 配置模板
参考 `examples/` 目录中的质量配置示例：
- **`examples/quality-config/`** - 完整的质量配置
- **`examples/ci-workflows/`** - CI/CD 工作流示例
- **`examples/monitoring/`** - 质量监控配置

### 详细指南
参考 `references/` 目录中的深入指南：
- **`references/testing-strategies.md`** - 详细测试策略
- **`references/code-review-guidelines.md`** - 代码审查指南
- **`references/performance-quality.md`** - 性能质量指南

## 故障排除

### 常见质量问题
- 测试覆盖率不足
- 代码重复率高
- 复杂度过高
- 性能回归

### 解决方案
参考 `references/troubleshooting.md` 获取详细的问题解决方案。