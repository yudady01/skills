---
name: dtg-intelligent-architecture-analysis
description: This skill should be used when the user asks to "analyze architecture", "review architecture", "assess design", "evaluate microservices", "check service boundaries", "DDD analysis", "domain driven design", or mentions architecture patterns, microservices design, distributed system architecture, service decomposition, or architectural assessment. Provides intelligent architecture analysis for Spring Boot 2.7 + Apache Dubbo 3 microservices, including service boundary evaluation, pattern recognition, performance architecture assessment, and DDD principles.
license: Apache 2.0
---

# 智能架构分析技能

为 Spring Boot 2.7 + Apache Dubbo 3 微服务架构提供智能化架构分析支持。

## 核心能力

### 1. Spring Boot 2.7 架构分析
- 分层架构模式 (Controller、Service、Repository)
- 依赖注入架构 (IoC容器、Bean生命周期)
- 配置架构管理 (多环境配置、配置隔离)
- AOP架构应用 (切面编程、性能影响)
- 自动配置机制 (自动配置原理、冲突解决)

### 2. Apache Dubbo 3 微服务架构
- 服务接口架构 (接口设计、契约管理)
- 服务治理架构 (负载均衡、服务发现、熔断降级)
- 分布式事务架构 (事务处理模式、一致性保证)
- 性能架构优化 (调用性能优化、网络通信设计)
- 版本管理架构 (版本兼容性、灰度发布)

### 3. 领域驱动设计(DDD)
- 限界上下文分析 (服务边界划分)
- 聚合设计模式 (聚合根、实体、值对象)
- 领域事件建模 (事件设计、事件存储)
- 上下文映射策略 (关系映射、集成模式)
- 反腐败层设计 (防腐层原则、实现策略)

### 4. 微服务架构模式
- 服务拆分策略 (拆分原则、方法)
- 架构模式识别 (六边形架构、CQRS、事件驱动)
- 数据一致性模式 (一致性解决方案、补偿事务)
- 容错架构模式 (熔断器、舱壁模式、重试模式)
- API网关架构 (API管理、路由策略)

## 架构分析维度

### 结构分析
- 模块化程度分析
- 层次结构分析
- 组件职责分析
- 接口设计分析

### 性能分析
- 响应时间分析
- 吞吐量分析
- 资源利用率分析
- 并发处理分析

### 可维护性分析
- 代码复杂度分析
- 测试覆盖率分析
- 文档完整性分析
- 变更影响分析

## 架构评估框架

### 质量属性评估

| 属性 | 说明 |
|------|------|
| 正确性 | 系统功能的正确性和完整性 |
| 可靠性 | 系统在规定条件下的稳定运行能力 |
| 可用性 | 系统可正常运行时间和故障恢复能力 |
| 安全性 | 系统抵抗恶意攻击和保护数据的能力 |
| 性能 | 系统响应速度、处理能力和资源利用率 |
| 可扩展性 | 系统适应负载增长和功能扩展的能力 |
| 可维护性 | 系统修改、维护和升级的难易程度 |

### 架构成熟度等级

| 等级 | 特征 | 改进建议 |
|------|------|----------|
| Level 1: 初始级 | 架构设计缺乏标准化 | 建立基本的架构规范和设计原则 |
| Level 2: 已管理级 | 有基本的架构规范，但执行不一致 | 建立架构评审机制和标准化流程 |
| Level 3: 已定义级 | 架构流程标准化，有明确的设计模式 | 引入更高级的架构模式和技术 |
| Level 4: 量化管理级 | 架构质量可度量，有量化指标 | 优化度量指标，提升预测能力 |
| Level 5: 优化级 | 架构持续优化，自适应业务变化 | 保持技术领先，推动架构创新 |

## 常见反模式识别

### 分布式单体反模式
- **检测标准**: 服务共享数据库、大量同步通信、紧耦合
- **缓解策略**: 数据库拆分、异步通信改造

### 共享数据库反模式
- **检测标准**: 多服务访问相同表、跨服务数据依赖
- **缓解策略**: 数据库权限分离、API封装数据访问

## 性能优化策略

### 数据库架构优化
- 读写分离
- 分库分表
- 索引优化

### 缓存架构优化
- 多级缓存 (本地缓存 + 分布式缓存)
- 缓存预热
