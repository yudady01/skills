---
name: dtg:create-plan
description: 创建 Spring Boot 技术方案与执行计划（固定栈：MyBatis-Plus + Redis + HikariCP + ActiveMQ）。用于架构设计和任务拆解。
tags: [spring-boot, architecture, planning]
metadata:
  short-description: Spring Boot 技术方案
---

# Spring Boot 技术方案与执行计划

## 快速开始

### 适用场景
- 需要设计新的 Spring Boot 应用模块
- 需要对现有功能进行技术重构
- 需要评估第三方技术集成方案
- 需要制定详细的开发任务拆解

### 不适用场景
- 简单的 bug 修复 → 使用 `create-plan`
- 与 Spring Boot 无关的计划 → 使用 `create-plan`

### 固定技术栈

| 组件 | 技术选型 | 版本 |
|------|----------|------|
| 持久层 | MyBatis-Plus | 3.5.x |
| 连接池 | HikariCP | 默认 |
| 缓存 | Redis | 7.x |
| 消息队列 | ActiveMQ | 5.18.x |

## 最小工作流程

1. **理解需求** → 提取核心业务目标（不超过 5 条）
2. **澄清假设** → 明确用户规模、并发量、数据量等假设
3. **设计架构** → 模块划分、数据模型、接口设计
4. **拆解任务** → 按优先级拆解为可验收的任务
5. **评估风险** → 识别技术、业务、性能、安全风险

全程以只读模式操作，不直接写入或修改文件。

## 输出模板

### 一、需求理解

#### 核心业务目标（≤5条）
- 目标 1
- 目标 2
- ...

#### 关键假设
- 用户规模：...
- 并发量：...
- 数据量：...

#### 待澄清问题
- 问题 → 默认假设（显式标注）

### 二、技术方案

#### 系统边界
- web 层：...
- service 层：...
- domain 层：...
- infrastructure 层：...

#### 核心流程
- 步骤 1 → 步骤 2 → 步骤 3

#### 数据模型
- Entity 关键字段
- DTO / VO 说明

#### 接口设计
- REST API 粒度与职责

#### 技术选型
- MyBatis-Plus：BaseMapper CRUD、分页插件、Lambda 构造器
- Redis：@Cacheable、分布式锁、JSON 序列化
- HikariCP：默认连接池，最小配置
- ActiveMQ：JMS、Queue/Topic、重试机制

### 三、任务拆解

#### 阶段名称

##### 任务名称
- **目标**：...
- **改动点**：涉及的类/包/配置
- **输入/输出**：... → ...
- **验收标准**：可验证的标准
- **优先级**：P0（核心）/ P1（重要）/ P2（可选）
- **依赖**：前置任务

### 四、风险与质量

#### 高风险点（3-5个）
1. 技术风险：...
2. 业务风险：...
3. 性能风险：...
4. 安全风险：...

#### 缓解方案
- 对应风险的措施

#### 测试策略
- 单元测试覆盖要求
- 集成测试场景
- 性能测试指标

## 质量检查清单

输出前验证：
- [ ] 所有任务都有明确的验收标准
- [ ] 风险点都有对应的缓解方案
- [ ] 模块划分符合 Spring Boot 最佳实践
- [ ] 任务粒度适中（每人/天可完成）
- [ ] 所有假设都已显式标注
- [ ] 包含测试/验证步骤
- [ ] 包含边缘情况处理

## 注意事项

### 优先级定义
- **P0**：核心功能，必须完成
- **P1**：重要功能，应该完成
- **P2**：可选功能，可以延后

### 设计原则
- **务实性**：使用固定成熟技术栈
- **可验证性**：每个任务都有验收标准
- **风险意识**：主动识别各类风险
- **标准化**：遵循团队统一规范

## 参考资源

### MyBatis-Plus
```java
// 实体类
@TableName("t_user")
public class User {
    @TableId(type = IdType.AUTO)
    private Long id;
}

// Mapper
public interface UserMapper extends BaseMapper<User> {}

// 分页
Page<User> page = new Page<>(1, 10);
userMapper.selectPage(page, null);
```

### Redis
```java
@Cacheable(value = "user", key = "#id")
public User getById(Long id) { ... }

@CacheEvict(value = "user", key = "#id")
public void deleteById(Long id) { ... }
```

### HikariCP 配置
```yaml
spring:
  datasource:
    hikari:
      minimum-idle: 5
      maximum-pool-size: 20
      connection-timeout: 30000
```

### ActiveMQ
```java
// 生产者
jmsTemplate.convertAndSend("queue", message);

// 消费者
@JmsListener(destination = "queue")
public void receive(Message message) { ... }
```

### 详细文档
- MyBatis-Plus 官方文档：https://baomidou.com/
- Spring Data Redis：https://spring.io/projects/spring-data-redis
- ActiveMQ 文档：https://activemq.apache.org/
