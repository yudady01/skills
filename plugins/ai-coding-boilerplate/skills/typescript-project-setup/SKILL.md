---
name: typescript-project-setup
description: This skill should be used when the user asks to "setup TypeScript project", "configure TypeScript", "create tsconfig.json", "setup build tools", "configure testing", or "initialize TypeScript development environment". Provides comprehensive TypeScript project configuration guidance.
version: 1.0.0
---

# TypeScript 项目配置技能

这个技能提供完整的 TypeScript 项目配置指导，从基础设置到高级配置模式。

## 核心配置组件

### 1. TypeScript 编译器配置

#### 基础 tsconfig.json
创建严格的 TypeScript 配置以获得最佳开发体验：

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "allowImportingTsExtensions": true,
    "strict": true,
    "noImplicitAny": true,
    "noImplicitReturns": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitOverride": true,
    "noPropertyAccessFromIndexSignature": true,
    "noUncheckedIndexedAccess": true
  }
}
```

#### 高级配置选项
启用所有类型安全检查：
- `strictNullChecks` - 严格的 null 检查
- `strictFunctionTypes` - 严格的函数类型检查
- `strictBindCallApply` - 严格的 bind/call/apply 检查

### 2. 构建工具配置

#### 使用现代构建工具
推荐配置：
- **tsc-alias** - 路径别名支持
- **tsx** - 快速 TypeScript 执行器
- **Vite** - 开发服务器和构建工具

#### 构建脚本示例
```json
{
  "scripts": {
    "build": "tsc && tsc-alias",
    "dev": "tsx src/index.ts",
    "type-check": "tsc --noEmit",
    "watch": "tsx watch src/index.ts"
  }
}
```

### 3. 测试配置

#### Vitest 配置
创建 `vitest.config.ts`：

```typescript
import { defineConfig } from 'vitest/config';
import { resolve } from 'path';

export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: ['node_modules/', 'dist/', '**/*.d.ts']
    }
  },
  resolve: {
    alias: {
      '@': resolve(__dirname, './src')
    }
  }
});
```

### 4. 代码质量工具

#### Biome 配置
创建 `biome.json`：

```json
{
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true,
      "complexity": {
        "noUselessConstructor": "error"
      },
      "correctness": {
        "noUnusedVariables": "error"
      },
      "style": {
        "useConst": "error"
      }
    }
  },
  "formatter": {
    "enabled": true,
    "formatWithErrors": false
  }
}
```

## 项目结构最佳实践

### 推荐目录结构
```
src/
├── index.ts           # 入口文件
├── lib/              # 核心库代码
│   ├── core/         # 核心功能
│   ├── utils/        # 工具函数
│   └── types/        # 类型定义
├── modules/          # 功能模块
├── config/           # 配置文件
└── __tests__/        # 测试文件
```

### 模块化设计原则
- 单一职责原则
- 依赖倒置原则
- 接口隔离原则

## 类型系统设计

### 基础类型定义
创建 `src/lib/types/index.ts`：

```typescript
// 基础类型
export interface BaseEntity {
  id: string;
  createdAt: Date;
  updatedAt: Date;
}

// 错误类型
export interface AppError {
  code: string;
  message: string;
  details?: Record<string, unknown>;
}

// API 响应类型
export interface ApiResponse<T = unknown> {
  success: boolean;
  data?: T;
  error?: AppError;
}
```

### 高级类型模式
使用工具类型和条件类型：
```typescript
// 深度只读
export type DeepReadonly<T> = {
  readonly [P in keyof T]: T[P] extends object ? DeepReadonly<T[P]> : T[P];
};

// 选择性必需
export type RequiredFields<T, K extends keyof T> = T & Required<Pick<T, K>>;
```

## 路径别名配置

### TypeScript 路径映射
在 `tsconfig.json` 中配置：
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"],
      "@/lib/*": ["./src/lib/*"],
      "@/types/*": ["./src/lib/types/*"]
    }
  }
}
```

### 构建工具支持
使用 `tsc-alias` 处理路径别名：
```json
{
  "scripts": {
    "build": "tsc && tsc-alias",
    "build:watch": "tsc --watch & tsc-alias --watch"
  }
}
```

## 环境配置

### 环境变量管理
创建类型安全的环境变量：

```typescript
// src/lib/config/env.ts
import { z } from 'zod';

const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'production', 'test']),
  PORT: z.string().transform(Number),
  DATABASE_URL: z.string().url(),
});

export const env = envSchema.parse(process.env);
```

### 配置文件结构
```
config/
├── development.json
├── production.json
├── test.json
└── default.json
```

## 测试策略

### 单元测试
使用 Vitest 进行单元测试：
```typescript
// __tests__/utils.test.ts
import { describe, it, expect } from 'vitest';
import { formatName } from '../lib/utils/formatters';

describe('formatName', () => {
  it('should format name correctly', () => {
    expect(formatName('john', 'doe')).toBe('John Doe');
  });
});
```

### 集成测试
创建完整的集成测试：
```typescript
// __tests__/integration/api.test.ts
import { describe, it, expect, beforeAll } from 'vitest';
import { setupTestServer } from '../helpers/test-server';

describe('API Integration', () => {
  beforeAll(async () => {
    await setupTestServer();
  });

  it('should handle requests correctly', async () => {
    // 测试实现
  });
});
```

## 性能优化

### 编译性能
- 使用 `tsx` 进行快速开发
- 配置增量编译
- 优化 `tsconfig.json` 设置

### 运行时性能
- 启用 tree-shaking
- 使用动态导入
- 配置代码分割

## 部署配置

### Docker 配置
创建优化的 Dockerfile：
```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY dist ./dist
CMD ["node", "dist/index.js"]
```

### CI/CD 配置
GitHub Actions 工作流：
```yaml
name: Build and Test
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '20'
      - run: npm ci
      - run: npm run type-check
      - run: npm test
      - run: npm run build
```

## 参考资源

### 配置模板
参考 `examples/` 目录中的完整配置示例：
- **`examples/basic-setup/`** - 基础项目配置
- **`examples/advanced-config/`** - 高级配置示例
- **`examples/monorepo/`** - Monorepo 配置

### 工具和脚本
使用 `scripts/` 目录中的自动化工具：
- **`scripts/init-typescript.sh`** - TypeScript 项目初始化
- **`scripts/setup-testing.sh`** - 测试环境配置
- **`scripts/configure-linting.sh`** - 代码质量工具配置

### 详细文档
参考 `references/` 目录中的深入指南：
- **`references/advanced-types.md`** - 高级类型系统指南
- **`references/performance-optimization.md`** - 性能优化技巧
- **`references/testing-patterns.md`** - 测试模式和最佳实践

## 故障排除

### 常见配置问题
- 类型声明文件缺失
- 路径别名不工作
- 构建工具冲突

### 调试技巧
- 使用 `tsc --noEmit` 检查类型错误
- 启用详细输出日志
- 使用 TypeScript Playground 验证类型

## 升级和维护

### 版本管理
- 使用语义化版本控制
- 定期更新依赖项
- 监控安全漏洞

### 迁移指南
参考 `references/migration.md` 获取版本迁移指导。