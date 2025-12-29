---
name: common-module-development
description: This skill should be used when developing xxpay-core module (common library) in dtg-pay project. It provides guidance for creating common utilities, entity beans, service interfaces, and shared constants.
version: 1.0.0
tags: ["common-module", "entity", "service-interface", "utilities", "constants"]
---

# 公共模块开发技能

xxpay-core 是 DTG-Pay 支付系统的核心模块，作为公共库被其他服务模块引用。包含实体 Bean、API 接口定义、常量、工具类等。

## 模块信息

- **模块名称**: xxpay-core
- **模块类型**: 公共模块
- **打包方式**: jar
- **主要职责**: 实体 Bean、Dubbo 服务接口定义、常量、工具类

## 核心技术栈

- **Java 11** - 编程语言
- **Spring Boot 2.7.18** - 应用框架
- **Dubbo 3.2.14** - RPC 框架
- **MyBatis-Plus 3.5.7** - ORM 框架（provided scope）
- **FastJSON 2.0.51** - JSON 处理
- **OkHttp 4.12.0** - HTTP 客户端
- **MongoDB** - 文档存储（provided scope）
- **Redis** - 缓存（provided scope）

## 构建命令

```bash
# 编译并安装到本地仓库（跳过测试）
./mvnw -f xxpay-core clean install -Dmaven.test.skip=true

# 单独编译当前模块
mvn clean install -Dmaven.test.skip=true
```

注意：xxpay-core 没有 main 类，作为 jar 库被其他模块依赖。

## 代码架构

### 包结构

```
org.xxpay.core/
├── common/           # 公共组件
│   ├── annotation/   # 注解 (@I18n 国际化, @MethodLog 方法日志)
│   ├── constant/     # 常量定义
│   ├── domain/       # 通用领域对象 (RpcBaseParam, RpcBaseResult)
│   ├── enumm/        # 枚举类
│   ├── Exception/    # 自定义异常
│   ├── util/         # 工具类 (签名, 加密, 日期等)
│   └── vo/           # 值对象 (VO)
├── dto/              # 数据传输对象
├── entity/           # 数据库实体 (MyBatis-Plus注解)
├── service/          # Dubbo服务接口定义 (IService)
├── document/         # MongoDB文档定义
├── springboot/       # Spring配置 (OkHttp客户端工厂)
└── mdc/              # MDC日志上下文工具
```

## 核心概念

### 1. RPC 通信模型

所有 Dubbo 服务接口调用都基于 `RpcBaseParam` / `RpcBaseResult` 模型：

#### RpcBaseParam（RPC 调用入参基类）

```java
@Data
public class RpcBaseParam implements Serializable {

    /** 调用方 ID */
    private String rpcSrcSysId;

    /** 调用时间 */
    private String rpcDateTime;

    /** 随机通讯码 */
    private String rpcSeqNo;

    /** 签名方式 (0-明文, 1-SHA1) */
    private Integer rpcSignType;

    /** RPC 签名 (用于验证调用方合法性) */
    private String rpcSign;

    /** 业务流水号 (格式: 业务前缀+日期时间+6位流水号) */
    private String bizSeqNo;

    /** 业务签名 */
    private String bizSign;
}
```

#### RpcBaseResult（RPC 返回值基类）

```java
@Data
public class RpcBaseResult extends RpcBaseParam implements Serializable {

    /** 返回码 (0000 表示成功) */
    private String rpcRetCode;

    /** 返回错误描述 */
    private String rpcRetMsg;

    /** 数据库错误信息 */
    private String dbErrorCode;

    /** 数据库错误消息 */
    private String dbErrorMsg;
}
```

### 2. 返回码枚举

`RetEnum` 定义了所有业务返回码，按模块分类：

```java
public enum RetEnum {

    // 公共返回码 (10xxx)
    RET_COMM_SUCCESS("0000", "成功"),
    RET_COMM_FAIL("9999", "系统异常"),
    RET_COMM_OPERATE_FAIL("1001", "操作失败"),

    // 业务中心返回码 (11xxx)
    RET_SERVICE_SYSTEM_ERROR("1100", "系统错误"),

    // 商户系统返回码 (12xxx)
    RET_MCH_NOT_EXIST("1201", "商户不存在"),
    RET_MCH_STATE_STOP("1202", "商户已停用");

    private String code;
    private String message;
}
```

### 3. 实体类特点

```java
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@TableName("pay_order")
public class PayOrder {

    @TableId(type = IdType.INPUT)
    private String payOrderId;

    @TableField("mch_id")
    private String mchId;

    @TableField("amount")
    private Long amount;

    @TableField(value = "create_time", fill = FieldFill.INSERT)
    private LocalDateTime createTime;

    @TableField(value = "update_time", fill = FieldFill.INSERT_UPDATE)
    private LocalDateTime updateTime;
}
```

**实体类特点**：
- 使用 `@TableName` 指定表名
- 使用 `@TableId` 指定主键（通常为 `IdType.INPUT`）
- 使用 `@TableField` 映射字段名（支持驼峰转下划线）
- 使用 Lombok 注解简化代码

### 4. 服务接口定义

所有服务接口都在 `org.xxpay.core.service` 包下，命名规范为 `I{EntityName}Service`。

接口默认方法提供空实现，由 xxpay-service 模块实现具体逻辑。

```java
public interface IPayOrderService {

    /**
     * 根据支付订单号查询
     */
    PayOrder findByPayOrderId(String payOrderId);

    /**
     * 创建支付订单
     */
    int insert(PayOrder payOrder);

    /**
     * 更新支付订单
     */
    int update(PayOrder payOrder);
}
```

### 5. 国际化支持

使用 `@I18n` 注解标记需要国际化的字段：

```java
@Target({ElementType.FIELD})
@Retention(RetentionPolicy.RUNTIME)
public @interface I18n {
    /**
     * 国际化 key 前缀
     */
    String prefix() default "";
}

// 使用示例
public class MchInfo {
    @I18n(prefix = "mch.type")
    private Integer mchType;
}
```

### 6. 异常处理

使用 `ServiceException` 抛出业务异常：

```java
public class ServiceException extends RuntimeException {

    private RetEnum retEnum;

    private String extraMsg;

    public ServiceException(RetEnum retEnum) {
        super(retEnum.getMessage());
        this.retEnum = retEnum;
    }

    public ServiceException(RetEnum retEnum, String extraMsg) {
        super(retEnum.getMessage() + ": " + extraMsg);
        this.retEnum = retEnum;
        this.extraMsg = extraMsg;
    }
}
```

## 常量定义

### MchConstant（商户相关常量）

```java
public class MchConstant {

    /** 商户状态 */
    public static final int MCH_STATUS_INIT = 0;
    public static final int MCH_STATUS_ACTIVE = 1;
    public static final int MCH_STATUS_STOP = 2;

    /** 业务类型 */
    public static final int MCH_BIZ_TYPE_PAY = 1;
    public static final int MCH_BIZ_TYPE_AGENTPAY = 2;

    /** 结算方式 */
    public static final int SETTLE_MODE_DAILY = 1;
    public static final int SETTLE_MODE_WEEKLY = 2;
    public static final int SETTLE_MODE_MANUAL = 3;
}
```

### PayConstant（支付相关常量）

```java
public class PayConstant {

    /** 支付渠道 */
    public static final String PAY_CHANNEL_ALIPAY = "alipay";
    public static final String PAY_CHANNEL_WECHAT = "wxpay";
    public static final String PAY_CHANNEL_UNIONPAY = "unionpay";

    /** 订单状态 */
    public static final int PAY_STATUS_INIT = 0;
    public static final int PAY_STATUS_PAYING = 1;
    public static final int PAY_STATUS_SUCCESS = 2;
    public static final int PAY_STATUS_FAIL = 3;
    public static final int PAY_STATUS_REFUND = 4;

    /** 支付方式 */
    public static final String PAY_MODE_ALIPAY_SDK = "alipay_sdk";
    public static final String PAY_MODE_WECHAT_SDK = "wxpay_sdk";
    public static final String PAY_MODE_FAST_PAY = "fast_pay";
}
```

### RedisConstant（Redis 相关常量）

```java
public class RedisConstant {

    /** Redis Key 前缀 */
    public static final String PREFIX = "xxpay:";

    /** 用户登录 Token */
    public static final String USER_TOKEN = PREFIX + "user:token:";

    /** 支付订单缓存 */
    public static final String PAY_ORDER = PREFIX + "pay:order:";

    /** 缓存过期时间（秒） */
    public static final int EXPIRE_HOUR = 3600;
    public static final int EXPIRE_DAY = 86400;
}
```

## 工具类

### 签名工具类

```java
public class SignatureUtils {

    /**
     * 生成签名
     */
    public static String generateSign(Map<String, Object> params, String secretKey) {
        // 1. 参数排序
        TreeMap<String, Object> sortedParams = new TreeMap<>(params);

        // 2. 拼接字符串
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<String, Object> entry : sortedParams.entrySet()) {
            if (entry.getValue() != null && !"".equals(entry.getValue())) {
                sb.append(entry.getKey()).append("=").append(entry.getValue()).append("&");
            }
        }
        sb.append("key=").append(secretKey);

        // 3. MD5 加密
        return DigestUtils.md5Hex(sb.toString());
    }

    /**
     * 验证签名
     */
    public static boolean verifySign(Map<String, Object> params, String sign, String secretKey) {
        String calculatedSign = generateSign(params, secretKey);
        return calculatedSign.equalsIgnoreCase(sign);
    }
}
```

### 日期工具类

```java
public class DateUtils {

    /**
     * 获取当前时间戳
     */
    public static long getCurrentTimestamp() {
        return System.currentTimeMillis();
    }

    /**
     * 生成业务流水号
     * 格式: 业务前缀 + 日期时间 + 6位流水号
     */
    public static String genSeqNo(String prefix) {
        String dateTime = DateFormatUtils.format(new Date(), "yyyyMMddHHmmss");
        String random = RandomStringUtils.randomNumeric(6);
        return prefix + dateTime + random;
    }
}
```

### HTTP 客户端工具类

```java
public class OkHttpClientUtil {

    private static final OkHttpClient CLIENT = new OkHttpClient.Builder()
            .connectTimeout(30, TimeUnit.SECONDS)
            .readTimeout(30, TimeUnit.SECONDS)
            .writeTimeout(30, TimeUnit.SECONDS)
            .build();

    /**
     * POST JSON 请求
     */
    public static String doPostJson(String url, String jsonBody) {
        try {
            RequestBody body = RequestBody.create(
                MediaType.parse("application/json; charset=utf-8"),
                jsonBody
            );

            Request request = new Request.Builder()
                    .url(url)
                    .post(body)
                    .build();

            Response response = CLIENT.newCall(request).execute();

            if (response.isSuccessful() && response.body() != null) {
                return response.body().string();
            }

            return null;

        } catch (Exception e) {
            throw new RuntimeException("HTTP 请求失败", e);
        }
    }

    /**
     * POST Form 表单请求
     */
    public static String doPostFormUrlencoded(String url, Map<String, String> params) {
        try {
            FormBody.Builder builder = new FormBody.Builder();
            for (Map.Entry<String, String> entry : params.entrySet()) {
                builder.add(entry.getKey(), entry.getValue());
            }

            RequestBody body = builder.build();

            Request request = new Request.Builder()
                    .url(url)
                    .post(body)
                    .build();

            Response response = CLIENT.newCall(request).execute();

            if (response.isSuccessful() && response.body() != null) {
                return response.body().string();
            }

            return null;

        } catch (Exception e) {
            throw new RuntimeException("HTTP 请求失败", e);
        }
    }
}
```

## MongoDB 文档定义

```java
@Document(collection = "pay_order")
@Data
public class PayOrderDocument {

    @Id
    private String id;

    @Field("pay_order_id")
    @Indexed
    private String payOrderId;

    @Field("mch_id")
    @Indexed
    private String mchId;

    @Field("amount")
    private Long amount;

    @Field("status")
    @Indexed
    private Integer status;

    @Field("create_time")
    @Indexed
    private LocalDateTime createTime;

    @Field("update_time")
    private LocalDateTime updateTime;
}
```

## Spring 配置

### OkHttp 客户端工厂

```java
@Configuration
public class OkHttpConfig {

    @Bean
    public OkHttpClient okHttpClient() {
        return new OkHttpClient.Builder()
                .connectTimeout(30, TimeUnit.SECONDS)
                .readTimeout(30, TimeUnit.SECONDS)
                .writeTimeout(30, TimeUnit.SECONDS)
                .connectionPool(new ConnectionPool(20, 5, TimeUnit.MINUTES))
                .build();
    }
}
```

## 开发指南

### 添加新实体

1. 在 `xxpay-generator` 生成 MyBatis 代码
2. 将 Model 拷贝到 `xxpay-core/entity`
3. 将 Mapper 拷贝到 `xxpay-service`（需比对是否有修改）
4. 在 `xxpay-core/service` 创建服务接口
5. 在 `xxpay-service` 创建实现类

### 添加新常量

- 支付渠道常量添加到 `PayConstant`
- 业务返回码添加到 `RetEnum`
- 商户业务类型添加到 `MchConstant`

### 添加新服务接口

1. 在 `org.xxpay.core.service` 包下创建接口
2. 接口命名以 `I` 开头
3. 定义方法签名和返回值
4. 添加 Javadoc 注释

### 调用 Dubbo 服务

确保使用 `RpcBaseParam` 作为入参基类，并正确设置签名相关字段。

## 时区配置

项目使用 **Asia/Shanghai** 时区：

- Spring Jackson: `spring.jackson.time-zone: "Asia/Shanghai"`
- JDBC URL: `serverTimezone=GMT%2B0`
- Java Main: 通过 `@PostConstruct` 设置 `TimeZone.setDefault()`

## 依赖配置

### Provided 依赖

```xml
<dependencies>
    <!-- MyBatis-Plus (provided) -->
    <dependency>
        <groupId>com.baomidou</groupId>
        <artifactId>mybatis-plus-boot-starter</artifactId>
        <version>${mybatis-plus.version}</version>
        <scope>provided</scope>
    </dependency>

    <!-- MongoDB (provided) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-mongodb</artifactId>
        <scope>provided</scope>
    </dependency>

    <!-- Redis (provided) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-redis</artifactId>
        <scope>provided</scope>
    </dependency>
</dependencies>
```

## 日志

使用 `@MethodLog` 注解记录方法调用日志，MDC 工具类 (`MDCs`) 用于设置 traceId。

## 部署顺序

部署时需按以下顺序发布：
1. xxpay-flyway
2. xxpay-core
3. xxpay-service
4. 其他模块

## 相关模块

xxpay-core 是以下模块的基础依赖：
- xxpay-service
- xxpay-manage
- xxpay-merchant
- xxpay-agent
- xxpay-pay
- xxpay-task
- xxpay-consumer
- rbgi
