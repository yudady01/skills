---
description: 注入 Spring Boot 2.7 + Dubbo 微服务项目上下文配置，建立企业级开发环境和规则标准
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, TodoWrite]
---

# Spring Boot 2.7 + Dubbo 微服务项目注入命令

这个命令用于建立 Spring Boot 2.7 + Dubbo 微服务项目上下文，配置企业级开发环境，并设置专用的开发规则和标准。

## 配置流程

### 1. 项目分析

**当前项目评估**：`$ARGUMENTS`

分析微服务项目的关键特征：
- **微服务类型** - 微服务领域（用户服务、订单服务、支付服务等）
- **技术栈** - Spring Boot 2.7 + Dubbo 技术栈
- **团队规模** - 开发团队大小
- **业务领域** - 项目所属业务领域
- **质量标准** - 企业级代码质量要求
- **部署环境** - 分布式部署环境

### 2. 环境配置

**Spring Boot 2.7 + Dubbo 微服务项目上下文配置**：

#### 微服务技术栈配置
```java
// 微服务技术栈定义
public class MicroserviceTechStack {
    public enum Language {
        JAVA_11
    }

    public enum Framework {
        SPRING_BOOT_2_7
    }

    public enum MicroserviceFramework {
        APACHE_DUBBO_3_2
    }

    public enum Database {
        MYSQL_8_0, MONGODB, REDIS
    }

    public enum MessageQueue {
        ACTIVEMQ, RABBITMQ, KAFKA
    }

    public enum Registry {
        ZOOKEEPER, NACOS
    }
}
```

#### 开发规则配置
```java
// 企业级开发规则标准
public class EnterpriseDevelopmentRules {
    public enum CodeStyle {
        CHECKSTYLE, GOOGLE_STYLE, ALI_STYLE
    }

    public enum QualityGate {
        STRICT, STANDARD, BASIC
    }

    public enum TestCoverage {
        CRITICAL(90), HIGH(80), STANDARD(70), BASIC(60);

        private final int threshold;
        TestCoverage(int threshold) {
            this.threshold = threshold;
        }
    }

    public enum DeploymentStrategy {
        DOCKER, KUBERNETES, TRADITIONAL
    }
}

### 3. 文件生成

**微服务配置文件生成**：

#### CLAUDE.md 配置
```markdown
# Spring Boot 2.7 + Dubbo 微服务项目特定配置

## 项目信息
- 服务名称：${serviceName}
- 微服务类型：${microserviceType}
- 技术栈：Spring Boot 2.7 ${springBootVersion} + Apache Dubbo ${dubboVersion}

## 开发规则
- 编码标准：${codingStandards}
- 质量门禁：${qualityGate}
- 部署策略：${deploymentStrategy}
```

#### Maven 配置优化 (pom.xml)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>

    <groupId>${companyGroup}</groupId>
    <artifactId>${serviceName}</artifactId>
    <version>${serviceVersion}</version>
    <packaging>jar</packaging>

    <properties>
        <java.version>11</java.version>
        <spring-boot.version>${springBootVersion}</spring-boot.version>
        <dubbo.version>${dubboVersion}</dubbo.version>
        <mybatis-plus.version>3.5.7</mybatis-plus.version>
    </properties>

    <dependencies>
        <!-- Spring Boot 2.7 Starter -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <!-- Apache Dubbo -->
        <dependency>
            <groupId>org.apache.dubbo</groupId>
            <artifactId>dubbo-spring-boot-starter</artifactId>
            <version>${dubbo.version}</version>
        </dependency>
    </dependencies>
</project>
```

#### Spring Boot 2.7 配置
```yaml
# application.yml
spring:
  application:
    name: ${serviceName}
  profiles:
    active: ${environment}

server:
  port: ${servicePort}

dubbo:
  application:
    name: ${serviceName}
  registry:
    address: zookeeper://${registryHost}:2181
  protocol:
    name: dubbo
    port: ${dubboPort}
```

### 4. 质量门禁配置

**Maven 质量检查配置**：

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-checkstyle-plugin</artifactId>
    <version>3.2.0</version>
</plugin>

<plugin>
    <groupId>com.github.spotbugs</groupId>
    <artifactId>spotbugs-maven-plugin</artifactId>
    <version>4.7.3.0</version>
</plugin>

<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.8</version>
</plugin>
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
/project-inject --stack java,spring-boot,dubbo

# 指定团队规模
/project-inject --team enterprise
```

### 高级配置

```bash
# 完整配置
/project-inject --name "我的项目" --type api-service --stack java,spring-boot,dubbo,mysql --coverage 80

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
- **java** - Java 语言
- **spring-boot** - Spring Boot 2.7 框架
- **dubbo** - Apache Dubbo 微服务框架
- **mybatis-plus** - MyBatis-Plus ORM框架
- **postgresql** - PostgreSQL 数据库
- **mysql** - MySQL 数据库
- **mongodb** - MongoDB 数据库
- **redis** - Redis 缓存
- **activemq** - ActiveMQ 消息队列
- **zookeeper** - Zookeeper 注册中心
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
├── pom.xml               # Maven 配置
├── application.yml       # Spring Boot 2.7 配置
├── dubbo.properties      # Dubbo 配置
└── checkstyle.xml        # 代码质量工具配置
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
```java
// 交互式配置流程
public class ConfigurationWizard {
    public static class ProjectInfo {
        public String name = "项目名称是什么？";
        public String description = "项目的主要功能是什么？";
        public String type = "这是什么类型的项目？";
    }

    public static class TechStack {
        public String language = "使用什么编程语言？";
        public String framework = "使用什么框架？";
        public String database = "使用什么数据库？";
        public String deployment = "如何部署应用？";
    }

    public static class Standards {
        public String testCoverage = "测试覆盖率目标是多少？";
        public String codeStyle = "使用什么代码格式化工具？";
        public String commitStyle = "使用什么提交信息格式？";
    }
}
```

### 配置验证
```bash
# 验证配置文件
mvn validate

# 检查配置一致性
mvn checkstyle:check

# 测试配置效果
mvn test
```

## 自定义配置

### 配置文件模板
```yaml
# custom-config.yml
project:
  name: "自定义项目名称"
  type: "microservice"
  description: "项目描述"

techStack:
  language: "Java"
  framework: "Spring Boot 2.7"
  microservice: "Apache Dubbo"
  database: "MySQL"
  deployment: "Docker"

standards:
  testCoverage: 85
  codeStyle: "Checkstyle"
  buildTool: "Maven"

team:
  size: "medium"
  workflow: "GitFlow"
  reviewPolicy: "require-review"
```

### 配置扩展
```java
// 扩展配置类
public class ExtendedConfig {
    public static class Security {
        public String auditFrequency; // weekly, monthly, quarterly
        public String vulnerabilityThreshold; // moderate, high, critical
    }

    public static class Performance {
        public boolean monitoring;
        public boolean benchmarking;
        public boolean alerting;
    }

    public static class Documentation {
        public boolean apiDocs;
        public boolean userGuide;
        public boolean developerGuide;
    }
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
- **`springboot-project-setup`** - Spring Boot 2.7 配置指南
- **`quality-assurance`** - 质量保证策略

### 配置模板
- **`examples/configs/web-app/`** - Web 应用配置
- **`examples/configs/api-service/`** - API 服务配置
- **`examples/configs/library/`** - 库项目配置

### 工具集成
- **`scripts/setup-config.sh`** - 配置设置脚本
- **`scripts/validate-config.sh`** - 配置验证工具

## 示例工作流

### 完整项目初始化
```bash
# 创建新项目
mkdir my-microservice
cd my-microservice

# 初始化 Maven 项目
mvn archetype:generate -DgroupId=com.example -DartifactId=my-service

# 运行项目注入
/project-inject --name "我的微服务" --type microservice --stack java,spring-boot,dubbo,mysql

# 验证配置
mvn validate
mvn checkstyle:check

# 开始开发
mvn spring-boot:run
```

通过项目注入命令，您可以快速建立标准化的开发环境，确保团队成员使用一致的配置和开发标准。