---
description: 注入项目上下文配置，建立开发环境和规则标准
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, TodoWrite]
---

# 项目注入命令

这个命令用于建立项目上下文，配置开发环境，并设置专用的开发规则和标准。

## 配置流程

### 1. 项目分析

**当前项目评估**：`$ARGUMENTS`

分析项目的关键特征：
- **项目类型** - 应用类型（web、api、library等）
- **技术栈** - 主要技术和框架
- **团队规模** - 开发团队大小
- **业务领域** - 项目所属业务领域
- **质量标准** - 代码质量要求
- **部署环境** - 目标部署环境

### 2. 环境配置

**项目上下文配置**：

#### 技术栈配置
```typescript
// 项目技术栈定义
interface TechStack {
  language: 'TypeScript' | 'JavaScript' | 'Python';
  framework?: 'React' | 'Express' | 'Fastify' | 'Next.js';
  database?: 'PostgreSQL' | 'MySQL' | 'MongoDB' | 'Redis';
  testing?: 'Vitest' | 'Jest' | 'Mocha';
  buildTools?: 'Vite' | 'Webpack' | 'Rollup';
  deployment?: 'Docker' | 'Serverless' | 'Traditional';
}
```

#### 开发规则配置
```typescript
// 开发规则标准
interface DevelopmentRules {
  codeStyle: 'Biome' | 'ESLint + Prettier';
  typeChecking: 'strict' | 'standard' | 'loose';
  testCoverage: number; // 目标覆盖率百分比
  commitStyle: 'conventional' | 'custom';
  branchStrategy: 'GitFlow' | 'GitHub Flow' | 'trunk';
};
```

### 3. 文件生成

**配置文件生成**：

#### CLAUDE.md 配置
```markdown
# 项目特定配置

## 项目信息
- 名称：${projectName}
- 类型：${projectType}
- 技术栈：${techStack}

## 开发规则
- 编码标准：${codingStandards}
- 测试要求：${testingRequirements}
- 部署流程：${deploymentProcess}
```

#### TypeScript 配置优化
```json
{
  "compilerOptions": {
    "target": "${targetES}",
    "module": "${moduleSystem}",
    "strict": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

#### 测试配置
```typescript
// vitest.config.ts
export default defineConfig({
  test: {
    environment: 'node',
    coverage: {
      thresholds: {
        global: {
          branches: ${testCoverageThreshold},
          functions: ${testCoverageThreshold},
          lines: ${testCoverageThreshold}
        }
      }
    }
  }
});
```

### 4. 脚本配置

**package.json 脚本优化**：

```json
{
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "build": "tsc && tsc-alias",
    "type-check": "tsc --noEmit",
    "test": "vitest run",
    "test:coverage": "vitest run --coverage",
    "lint": "biome check src",
    "lint:fix": "biome check --write src",
    "format": "biome format --write src",
    "check:all": "npm run type-check && npm run lint && npm test"
  }
}
```

### 5. 文档模板生成

**项目文档结构**：

#### README 模板
```markdown
# ${projectName}

${projectDescription}

## 技术栈
${techStackList}

## 开发环境设置
${developmentSetup}

## 项目结构
${projectStructure}

## 开发工作流
${developmentWorkflow}
```

#### 贡献指南
```markdown
# 贡献指南

## 开发环境
${developmentEnvironment}

## 代码规范
${codingStandards}

## 提交流程
${commitProcess}

## 测试要求
${testingRequirements}
```

## 使用指南

### 基础用法

```bash
# 初始化项目配置
/project-inject

# 指定项目类型
/project-inject --type web-app

# 指定技术栈
/project-inject --stack typescript,react,nodejs

# 指定团队规模
/project-inject --team enterprise
```

### 高级配置

```bash
# 完整配置
/project-inject --name "我的项目" --type api-service --stack typescript,express,postgresql --coverage 80

# 自定义配置文件
/project-inject --config ./custom-config.json

# 更新现有配置
/project-inject --update
```

## 配置选项

### 项目类型选项
- **web-app** - Web 应用程序
- **api-service** - API 服务
- **library** - 可重用库
- **cli-tool** - 命令行工具
- **mobile-app** - 移动应用

### 技术栈选项
- **typescript** - TypeScript 语言
- **javascript** - JavaScript 语言
- **react** - React 框架
- **vue** - Vue.js 框架
- **express** - Express.js 服务器
- **fastify** - Fastify 服务器
- **postgresql** - PostgreSQL 数据库
- **mysql** - MySQL 数据库
- **mongodb** - MongoDB 数据库
- **redis** - Redis 缓存
- **docker** - Docker 容器化

### 团队规模选项
- **personal** - 个人项目
- **small** - 小团队（2-5人）
- **medium** - 中等团队（6-15人）
- **large** - 大团队（16+人）
- **enterprise** - 企业级团队

## 生成的配置文件

### 1. 项目配置文件
```
.claude/
├── project-context.md     # 项目上下文
├── development-rules.md   # 开发规则
└── standards.md          # 编码标准
```

### 2. 开发工具配置
```
├── tsconfig.json         # TypeScript 配置
├── vitest.config.ts      # 测试配置
├── biome.json           # 代码质量工具配置
└── package.json         # 项目脚本优化
```

### 3. 文档文件
```
docs/
├── README.md            # 项目说明
├── CONTRIBUTING.md      # 贡献指南
├── CHANGELOG.md         # 变更日志
└── api/                 # API 文档
```

### 4. 工作流配置
```
.github/
├── workflows/           # CI/CD 工作流
└── pull_request_template.md  # PR 模板
```

## 交互式配置

### 配置向导
```typescript
// 交互式配置流程
const configurationWizard = {
  projectInfo: {
    name: "项目名称是什么？",
    description: "项目的主要功能是什么？",
    type: "这是什么类型的项目？"
  },
  techStack: {
    language: "使用什么编程语言？",
    framework: "使用什么框架？",
    database: "使用什么数据库？",
    deployment: "如何部署应用？"
  },
  standards: {
    testCoverage: "测试覆盖率目标是多少？",
    codeStyle: "使用什么代码格式化工具？",
    commitStyle: "使用什么提交信息格式？"
  }
};
```

### 配置验证
```bash
# 验证配置文件
npm run validate:config

# 检查配置一致性
npm run check:consistency

# 测试配置效果
npm run test:config
```

## 自定义配置

### 配置文件模板
```typescript
// custom-config.json
{
  "project": {
    "name": "自定义项目名称",
    "type": "web-app",
    "description": "项目描述"
  },
  "techStack": {
    "language": "TypeScript",
    "framework": "React",
    "database": "PostgreSQL",
    "deployment": "Docker"
  },
  "standards": {
    "testCoverage": 85,
    "codeStyle": "Biome",
    "typeChecking": "strict"
  },
  "team": {
    "size": "medium",
    "workflow": "GitFlow",
    "reviewPolicy": "require-review"
  }
}
```

### 配置扩展
```typescript
// 扩展配置接口
interface ExtendedConfig {
  security: {
    auditFrequency: 'weekly' | 'monthly' | 'quarterly';
    vulnerabilityThreshold: 'moderate' | 'high' | 'critical';
  };
  performance: {
    monitoring: boolean;
    benchmarking: boolean;
    alerting: boolean;
  };
  documentation: {
    apiDocs: boolean;
    userGuide: boolean;
    developerGuide: boolean;
  };
}
```

## 最佳实践

### 1. 配置管理
- 使用版本控制管理配置文件
- 定期审查和更新配置
- 保持配置的一致性

### 2. 团队协作
- 共享配置标准
- 定期同步开发环境
- 建立配置变更流程

### 3. 质量保证
- 自动化配置验证
- 持续监控配置效果
- 收集团队反馈

## 故障排除

### 常见问题

**问题**：配置文件冲突
**解决**：检查现有配置，合并或覆盖冲突项

**问题**：依赖版本不兼容
**解决**：更新依赖版本，确保兼容性

**问题**：配置不生效
**解决**：重启开发服务器，清除缓存

## 相关资源

### 参考文档
- **`typescript-project-setup`** - TypeScript 配置指南
- **`quality-assurance`** - 质量保证策略

### 配置模板
- **`examples/configs/web-app/`** - Web 应用配置
- **`examples/configs/api-service/`** - API 服务配置
- **`examples/configs/library/`** - 库项目配置

### 工具集成
- **`scripts/setup-config.js`** - 配置设置脚本
- **`scripts/validate-config.js`** - 配置验证工具

## 示例工作流

### 完整项目初始化
```bash
# 创建新项目
mkdir my-project
cd my-project

# 初始化项目
npm init -y

# 运行项目注入
/project-inject --name "我的 Web 应用" --type web-app --stack typescript,react,postgresql

# 验证配置
npm run check:all

# 开始开发
npm run dev
```

通过项目注入命令，您可以快速建立标准化的开发环境，确保团队成员使用一致的配置和开发标准。