---
name: admin-panel-development
description: This skill should be used when developing admin panel modules (xxpay-manage, xxpay-agent, xxpay-merchant) in dtg-pay project. It provides guidance for LayuiAdmin-based management interfaces, JWT authentication, and Dubbo service integration.
version: 1.0.0
tags: ["admin-panel", "layui", "jwt", "dubbo-consumer", "management-interface"]
---

# 管理后台开发技能

这个技能用于开发 dtg-pay 项目中的管理后台模块：xxpay-manage（运营平台）、xxpay-agent（代理商系统）、xxpay-merchant（商户系统）。

## 适用模块

| 模块名称 | HTTP 端口 | Dubbo 端口 | 模块类型 | 品牌支持 |
|---------|----------|-----------|---------|---------|
| xxpay-manage | 8193 | 28193 | 运营管理平台 | 单一 |
| xxpay-agent | 8192 | 28192 | 代理商系统 | 724pay, ezpay |
| xxpay-merchant | 8191 | 28191 | 商户系统 | 724pay, ezpay |

## 核心技术栈

### 后端技术栈
- **Java 11** - 编程语言
- **Spring Boot 2.7.18** - 应用框架
- **Apache Dubbo 3.2.14** - RPC 框架
- **Spring Security + JWT** - 安全认证
- **MyBatis** - 持久化（通过 xxpay-service）
- **FreeMarker** - 模板引擎

### 前端技术栈
- **Layui v2.3.0** - UI框架
- **jQuery** - JavaScript库
- **ECharts** - 图表库

## 构建和运行

### 编译项目

```bash
# 从项目根目录编译（需先编译依赖模块）
./mvnw -f xxpay-core clean install -Dmaven.test.skip=true
./mvnw -f xxpay-service clean package -Dmaven.test.skip=true

# 编译当前模块
./mvnw clean package -Dmaven.test.skip=true
```

### 运行应用

```bash
# 开发环境运行
./mvnw spring-boot:run

# 或直接运行 jar
java -jar target/xxpay-manage-1.0.0.jar
```

## 项目架构

### 模块依赖关系

```
xxpay-manage / xxpay-agent / xxpay-merchant
    ↓ (依赖)
xxpay-core (公共API、实体、常量)
    ↓ (Dubbo RPC调用)
xxpay-service (业务服务实现)
    ↓
数据库
```

### 代码结构

```
src/main/java/org/xxpay/{module}/
├── common/
│   ├── config/           # 配置类 (MainConfig等)
│   ├── ctrl/             # 通用控制器 (BaseController, CommonController)
│   └── service/          # RPC服务聚合 (RpcCommonService)
├── merchant/             # 商户管理
├── agent/               # 代理商管理
├── order/               # 订单管理
├── settlement/          # 结算管理
├── statistics/          # 统计报表
├── user/                # 用户管理
│   ├── ctrl/            # AuthController, AccountController
│   ├── service/         # UserService
│   └── model/           # AuthRequest
├── security/            # 安全相关
│   └── hander/          # 拦截器
└── sys/                 # 系统相关

src/main/resources/
├── static/
│   ├── 724pay/x_{module}/   # 724pay品牌前端资源
│   └── ezpay/x_{module}/    # ezpay品牌前端资源
├── templates/                # FreeMarker模板
├── application.yml
└── logback-spring.xml
```

## 核心架构概念

### 1. JWT 认证

**关键组件**:
- `JwtAuthenticationTokenFilter`: JWT过滤器，拦截请求验证token
- `JwtTokenUtil`: JWT生成和验证工具
- `JwtUserDetailsServiceImpl`: 用户详情服务
- `WebSecurityConfig`: Security配置

**登录流程**:
1. 用户访问 `/api/auth` 登录
2. 系统根据 host 判断品牌（agent/merchant）
3. 通过 username + brand 查找用户
4. 验证用户名密码
5. 生成 JWT token

### 2. 多品牌支持

**关键组件**:
- `DomainResourceResolver`: 根据域名解析前端资源 (724pay/ 或 ezpay/ 目录)
- `PlatformInterceptor`: 根据域名设置品牌上下文 (`PlatformContext`)
- `MainConfig`: 根据品牌获取不同的配置

**品牌常量定义**:
- `PLATFORM_724PAY`
- `PLATFORM_EZPAY`
- `XXPAY_724PAY_AGENT_HOST`
- `XXPAY_EZPAY_AGENT_HOST`

### 3. Dubbo RPC 调用

通过 `RpcCommonService` 调用 xxpay-service 提供的 Dubbo 服务：

```java
@Autowired
private RpcCommonService rpcCommonService;

// 调用服务
AgentInfo agentInfo = rpcCommonService.rpcAgentInfoService.findByAgentId(agentId);
```

### 4. 控制器基类

所有控制器继承 `BaseController`，提供：
- 用户认证信息获取 (`getUser()`, `getCurrentAgentId()`, `getCurrentBrand()`)
- 参数解析工具 (`getJsonParam()`, `getString()`, `getInteger()` 等)
- 分页参数处理 (`getPageIndex()`, `getPageSize()`)
- 金额处理 (`getRequiredAmountL()`, `handleParamAmount()`)
- 谷歌验证码验证 (`checkGoogleCode()`)
- 支付安全验证 (`verifyPay()`)

### 5. 请求拦截器链

```
请求 → MdcHandlerInterceptor (设置MDC) → LogHandlerInterceptor (日志) → PlatformInterceptor (品牌) → Controller
```

### 6. 前端资源路由

- 根路径 `/` 转发到 `/index.html`
- `DomainResourceResolver` 根据 host 决定返回 `724pay/x_agent/` 或 `ezpay/x_agent/` 的资源
- 如果子目录没找到，回退到默认位置

## Controller 开发示例

```java
@RestController
@RequestMapping("/api/merchant")
@Slf4j
public class MchInfoController extends BaseController {

    @Autowired
    private RpcCommonService rpcCommonService;

    /**
     * 查询商户列表
     */
    @PostMapping("/list")
    public ApiResponse listMerchant() {
        // 获取当前登录用户
        SysUser sysUser = getUser();

        // 获取分页参数
        Integer pageIndex = getPageIndex();
        Integer pageSize = getPageSize();
        String mchName = getString("mchName");

        // 调用 Dubbo 服务
        PageInfo<MchInfo> pageInfo = rpcCommonService.rpcMchInfoService.list(
            pageIndex, pageSize, mchName
        );

        return ApiResponse.buildSuccess(pageInfo);
    }

    /**
     * 添加商户
     */
    @PostMapping("/add")
    public ApiResponse addMerchant() {
        JSONObject param = getJsonParam();

        MchInfo mchInfo = new MchInfo();
        mchInfo.setMchName(param.getString("mchName"));
        mchInfo.setLoginName(param.getString("loginName"));
        // ... 设置其他属性

        int result = rpcCommonService.rpcMchInfoService.add(mchInfo);

        if (result > 0) {
            return ApiResponse.buildSuccess();
        }
        return ApiResponse.build(RetEnum.RET_COMM_OPERATE_FAIL);
    }
}
```

## JWT 配置

### Cookie 名称

| 模块 | Cookie 名称 | Token 有效期 |
|------|------------|-------------|
| xxpay-manage | `XxPay_Mgr_Token` | 3600 秒 (1小时) |
| xxpay-agent | `XxPay_Agent_Token` | 3600 秒 (1小时) |
| xxpay-merchant | `XxPay_Mch_Token` | 3600 秒 (1小时) |

### JWT 配置示例

```java
@Configuration
public class JwtConfig {

    @Value("${jwt.secret}")
    private String secret;

    @Value("${jwt.expiration}")
    private Long expiration;

    public String generateToken(String username, String userId) {
        Map<String, Object> claims = new HashMap<>();
        claims.put("username", username);
        claims.put("userId", userId);

        return Jwts.builder()
                .setClaims(claims)
                .setSubject(username)
                .setIssuedAt(new Date())
                .setExpiration(new Date(System.currentTimeMillis() + expiration))
                .signWith(SignatureAlgorithm.HS512, secret)
                .compact();
    }
}
```

## 环境配置

通过 `spring.profiles.active` 切换环境：

- `local`: 本地开发
- `dtg-stg`: 测试环境
- `dtg-prod`: 生产环境

### 关键环境变量

| 变量 | 说明 |
|------|------|
| `ZOOKEEPER` | Zookeeper 地址 |
| `REDIS_HOST` / `REDIS_PASSWORD` | Redis 配置 |
| `ACTIVEMQ_BROKER` / `ACTIVEMQ_USER` / `ACTIVEMQ_PASSWORD` | ActiveMQ 配置 |
| `NODE` | 服务节点标识 (分布式环境下每个节点不同) |

## Dubbo 配置

### 通用配置

```yaml
dubbo:
  application:
    name: xxpay-manage  # 根据模块调整
  registry:
    address: zookeeper://${ZOOKEEPER:localhost:2181}
  protocol:
    port: 28193  # manage: 28193, agent: 28192, merchant: 28191
  provider:
    timeout: 10000
    retries: 0
  consumer:
    timeout: 10000
    retries: 2
    check: false
```

## 时区配置

全局使用 `Asia/Shanghai` 时区：
- Jackson: `spring.jackson.time-zone: Asia/Shanghai`
- 数据库连接串: `serverTimezone=GMT%2B0`
- Java Main: `@PostConstruct void setDefaultTimezone() { TimeZone.setDefault(TimeZone.getTimeZone("Asia/Shanghai")); }`

## 日志配置

使用 Logback，配置文件 `logback-spring.xml`：

- **local**: 控制台输出 (STDOUT)
- **dtg-stg/dtg-prod**: 文件输出 (RollingFile)，保留30天，单文件最大10MB
- JSON格式: 包含 traceId 用于链路追踪

## 前端资源

### 静态资源目录

```
src/main/resources/static/
├── 724pay/
│   └── x_agent/          # 724pay 代理商前端
│   └── x_merchant/       # 724pay 商户前端
└── ezpay/
    └── x_agent/          # ezpay 代理商前端
    └── x_merchant/       # ezpay 商户前端
```

### 前端构建

```bash
cd src/main/resources/static/x_agent
gulp
```

## API 路径规范

- 所有API以 `/api/` 开头
- 认证相关: `/api/auth`, `/api/google_auth`
- 静态资源: `/x_agent/**`, `/html/**`, `/actuator/**` 无需认证

### Controller 路径示例

```java
// 运营平台
@RestController
@RequestMapping("/api/mch")       // 商户管理
@RequestMapping("/api/agent")     // 代理商管理
@RequestMapping("/api/payorder")  // 支付订单

// 代理商系统
@RestController
@RequestMapping("/api/agentMch")        # 代理商下的商户管理
@RequestMapping("/api/agentSett")       # 代理商结算
```

## 开发约定

### 包命名

- 控制器: `*Controller`，位于 `ctrl` 包
- 服务: `*Service`，位于 `service` 包
- 统一继承 `BaseController`

### 参数处理

- 前端参数通过 `params` 字段传递JSON字符串
- 使用 `getJsonParam(request)` 解析
- 金额单位：前端传入"元"，后端转换为"分"

### 响应格式

- 成功: `XxPayResponse.buildSuccess(data)`
- 失败: `BizResponse.build(RetEnum)`

## 部署顺序

部署时需按以下顺序：
1. xxpay-flyway
2. xxpay-service
3. xxpay-pay
4. xxpay-task
5. xxpay-manage / xxpay-agent / xxpay-merchant

## 常见问题

### Dubbo shutdown 报错

已知 issue: https://github.com/apache/dubbo/issues/10150

可通过配置日志级别禁用相关错误：
```yaml
logging:
  level:
    org.springframework.jms.listener.DefaultMessageListenerContainer: OFF
    org.apache.curator.framework.recipes.cache.NodeCache: OFF
```

### 品牌识别问题

确保域名配置正确：
- 724pay 代理商: `agent.724pay.com`
- ezpay 代理商: `agent.ezpay.com`

### 权限控制

使用 `@RequiresOperation` 注解进行操作权限校验，由 `PermissionAspect` AOP 拦截处理。
