# 项目上下文：PLT 后端

## 概述
这是一个大规模的 Java/Spring Boot 微服务后端项目，可能用于金融或游戏平台（"plt"）。它遵循多模块 Maven 架构，其中每个目录（例如 `pay`、`plt-user`、`plt-fund`）代表一个独立的服务或模块。

## 核心技术
- **语言：** Java（可能是 17+）
- **框架：** Spring Boot 3.x
- **构建工具：** Maven
- **数据库：** PostgreSQL（使用 Flyway 进行迁移）
- **ORM：** MyBatis Plus
- **缓存/键值存储：** Redis (Redisson)
- **消息传递：** RabbitMQ
- **可观测性：** Micrometer、Prometheus、OpenTelemetry
- **工具库：** Lombok、MapStruct、FastJSON

## 当前任务：提现系统重构
**状态：** 进行中（阶段 2 - 后端实现）
**目标：** 通过移除"提款分配"和"异常提現處理"步骤来简化提现流程，创建"直通车"模式。

**关键变更：**
1.  **流程简化：**
    *   手动提现：`待审核 (1)` -> `待支付 (3)` -> `已支付 (4)`（跳过状态 `2`）。
    *   第三方提现：`待审核 (1)` -> `待支付 (3)` -> `处理中 (7)`（跳过状态 `2`）。
2.  **废弃策略：**
    *   **不要删除代码/列。**
    *   对 Java 类/方法/字段使用 `@Deprecated` 注解。
    *   对 SQL 列和 Mapper XML 使用 `DEPRECATED` 注释。
    *   前端将隐藏 UI 元素而不是删除代码。

**参考文档：**
*   `doc/action-plan.md`：详细的分步执行计划。**（主要事实来源）**
*   `pay/README.md`：重构目标和状态变更概述。
*   `doc/task.md`：具体任务跟踪。

## 目录结构
*   `pay/`：支付服务模块。
*   `plt-fund/`：资金管理服务模块（当前重构的核心）。
*   `plt-user/`：用户管理服务模块。
*   `doc/`：项目文档、SQL 脚本和行动计划。
*   `pom.xml`：（在子目录中）Maven 构建配置。

## 构建与运行
**构建：**
标准 Maven 构建（开发期间必要时跳过测试）：
```bash
mvn clean install -DskipTests
```

**运行：**
Spring Boot 应用程序通常通过其主类或 Maven 插件运行：
```bash
mvn spring-boot:run
```

## 开发约定
*   **版本控制：** 检查 `pom.xml` 中的依赖项。使用 `com.galaxy:parent` 作为父 POM。
*   **代码风格：** 标准 Java/Spring 约定。使用 Lombok 减少样板代码。
*   **测试：** 预期有 JUnit 测试。
*   **废弃：** 对于当前的提现重构任务，严格遵循"标注，不删除"规则。

## Mermaid 文档规则
在 markdown 文件中创建 Mermaid 图表时，**必须遵循 Obsidian Mermaid 技能**：`.agent/skills/obsidian-mermaid/SKILL.md`

