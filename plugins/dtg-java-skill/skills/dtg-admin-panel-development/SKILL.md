---
name: dtg-admin-panel-development
description: This skill should be used when the user asks to "develop admin panel", "create management interface", "build admin dashboard", "LayuiAdmin", "admin authentication", or mentions management backend, admin panel, JWT authentication, or Dubbo service integration for admin systems. Provides LayuiAdmin management panel development guidance with JWT authentication and Dubbo service integration.
version: 3.0.0
tags: ["admin-panel", "layui", "jwt", "dubbo-consumer", "management-interface"]
---

# 管理后台开发技能

用于开发 dtg-pay 项目中的管理后台模块：xxpay-manage（运营平台）、xxpay-agent（代理商系统）、xxpay-merchant（商户系统）。

## 模块信息

| 模块 | HTTP端口 | Dubbo端口 | 类型 | 品牌 |
|------|----------|-----------|------|------|
| xxpay-manage | 8193 | 28193 | 运营管理平台 | 单一 |
| xxpay-agent | 8192 | 28192 | 代理商系统 | 724pay, ezpay |
| xxpay-merchant | 8191 | 28191 | 商户系统 | 724pay, ezpay |

## 技术栈

| 技术 | 版本 |
|------|------|
| Java | 11 |
| Spring Boot | 2.7.18 |
| Apache Dubbo | 3.2.14 |
| Spring Security + JWT | 最新 |
| MyBatis | 最新 |
| FreeMarker | 最新 |
| Layui | v2.3.0 |
| jQuery | 最新 |
| ECharts | 最新 |

## 构建和运行

```bash
# 编译依赖模块
./mvnw -f xxpay-core clean install -Dmaven.test.skip=true
./mvnw -f xxpay-service clean package -Dmaven.test.skip=true

# 编译当前模块
./mvnw clean package -Dmaven.test.skip=true

# 运行
./mvnw spring-boot:run
# 或
java -jar target/xxpay-manage-1.0.0.jar
```

## 模块依赖关系

```
xxpay-manage / xxpay-agent / xxpay-merchant
    ↓ (依赖)
xxpay-core (公共API、实体、常量)
    ↓ (Dubbo RPC调用)
xxpay-service (业务服务实现)
    ↓
数据库
```

## 核心概念

### 1. JWT 认证
- `JwtAuthenticationTokenFilter` - JWT过滤器
- `JwtTokenUtil` - JWT生成和验证
- `JwtUserDetailsServiceImpl` - 用户详情服务
- `WebSecurityConfig` - Security配置

### 2. 多品牌支持
- `DomainResourceResolver` - 根据域名解析前端资源
- `PlatformInterceptor` - 根据域名设置品牌上下文
- `MainConfig` - 根据品牌获取配置

### 3. Dubbo RPC 调用
```java
@Autowired
private RpcCommonService rpcCommonService;

AgentInfo agentInfo = rpcCommonService.rpcAgentInfoService.findByAgentId(agentId);
```

### 4. 控制器基类
- 继承 `BaseController`
- 提供用户认证、参数解析、分页、金额处理、谷歌验证等功能

### 5. 请求拦截器链
```
请求 → MdcHandlerInterceptor → LogHandlerInterceptor → PlatformInterceptor → Controller
```

## 环境配置

### 环境
- `local` - 本地开发
- `dtg-stg` - 测试环境
- `dtg-prod` - 生产环境

### 关键环境变量

| 变量 | 说明 |
|------|------|
| `ZOOKEEPER` | Zookeeper 地址 |
| `REDIS_HOST` / `REDIS_PASSWORD` | Redis 配置 |
| `ACTIVEMQ_BROKER` / `ACTIVEMQ_USER` / `ACTIVEMQ_PASSWORD` | ActiveMQ 配置 |
| `NODE` | 服务节点标识 |

## Dubbo 配置

```yaml
dubbo:
  application:
    name: xxpay-manage  # 根据模块调整
  registry:
    address: zookeeper://${ZOOKEEPER:localhost:2181}
  protocol:
    port: 28193  # manage: 28193, agent: 28192, merchant: 28191
  consumer:
    timeout: 10000
    retries: 2
    check: false
```

## 时区配置

全局使用 `Asia/Shanghai` 时区：
- Jackson: `spring.jackson.time-zone: Asia/Shanghai`
- 数据库: `serverTimezone=GMT%2B0`
- Java Main: `TimeZone.setDefault()`

## API 路径规范

- 所有API以 `/api/` 开头
- 认证相关: `/api/auth`, `/api/google_auth`
- 静态资源: `/x_agent/**`, `/html/**`, `/actuator/**` 无需认证

## Cookie 配置

| 模块 | Cookie 名称 | 有效期 |
|------|------------|--------|
| xxpay-manage | `XxPay_Mgr_Token` | 3600秒 |
| xxpay-agent | `XxPay_Agent_Token` | 3600秒 |
| xxpay-merchant | `XxPay_Mch_Token` | 3600秒 |

## 部署顺序

1. xxpay-flyway
2. xxpay-service
3. xxpay-pay
4. xxpay-task
5. xxpay-manage / xxpay-agent / xxpay-merchant
