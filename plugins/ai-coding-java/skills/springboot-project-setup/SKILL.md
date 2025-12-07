---
name: springboot-project-setup
description: This skill should be used when the user asks to "setup Spring Boot 2.7 project", "configure Spring Boot 2.7", "create application.properties", "setup build tools", "configure testing", or "initialize Spring Boot 2.7 development environment". Provides comprehensive Spring Boot 2.7 + Apache Dubbo 3.2.14 enterprise microservice project configuration guidance.
version: 2.7.0
---

# Spring Boot 2.7 + Apache Dubbo 企业级微服务项目配置技能

这个技能提供完整的 Spring Boot 2.7 + Apache Dubbo 3.2.14 企业级微服务项目配置指导，从基础设置到分布式微服务架构配置模式。专为高级开发者设计。

## 核心配置组件

### 1. Spring Boot 2.7 + Dubbo 微服务项目基础配置

#### Maven 配置 (pom.xml)
创建企业级 Spring Boot 2.7 + Apache Dubbo 3.2.14 微服务项目配置：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.7.18</version>
        <relativePath/>
    </parent>

    <groupId>com.enterprise</groupId>
    <artifactId>dubbo-microservice-template</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <properties>
        <java.version>11</java.version>
        <dubbo.version>3.2.14</dubbo.version>
        <mybatis-plus.version>3.5.7</mybatis-plus.version>
        <lombok.version>1.18.30</lombok.version>
        <mysql.version>8.0.33</mysql.version>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <!-- Spring Boot 2.7 Starters -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-security</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-validation</artifactId>
        </dependency>

        <!-- Apache Dubbo -->
        <dependency>
            <groupId>org.apache.dubbo</groupId>
            <artifactId>dubbo-spring-boot-starter</artifactId>
            <version>${dubbo.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.dubbo</groupId>
            <artifactId>dubbo-registry-zookeeper</artifactId>
            <version>${dubbo.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.dubbo</groupId>
            <artifactId>dubbo-registry-nacos</artifactId>
            <version>${dubbo.version}</version>
        </dependency>

        <!-- Database & ORM -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>${mysql.version}</version>
        </dependency>
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-boot-starter</artifactId>
            <version>${mybatis-plus.version}</version>
        </dependency>
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-extension</artifactId>
            <version>${mybatis-plus.version}</version>
        </dependency>

        <!-- Cache -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>

        <!-- Message Queue -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-activemq</artifactId>
        </dependency>

        <!-- MongoDB -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-mongodb</artifactId>
        </dependency>

  
        <!-- Documentation -->
        <dependency>
            <groupId>org.springdoc</groupId>
            <artifactId>springdoc-openapi-ui</artifactId>
            <version>1.6.15</version>
        </dependency>

        <!-- Lombok for Code Generation -->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>${lombok.version}</version>
            <scope>provided</scope>
        </dependency>

        <!-- Utilities -->
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-lang3</artifactId>
        </dependency>
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>fastjson2</artifactId>
            <version>2.0.46</version>
        </dependency>

        <!-- Testing -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.security</groupId>
            <artifactId>spring-security-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.apache.dubbo</groupId>
            <artifactId>dubbo-test</artifactId>
            <version>${dubbo.version}</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.testcontainers</groupId>
            <artifactId>junit-jupiter</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.testcontainers</groupId>
            <artifactId>mysql</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
          </plugins>
    </build>
</project>
```

#### 应用配置 (application.yml)
创建 Spring Boot 2.7 + Dubbo 分布式微服务配置文件：

```yaml
# application.yml
server:
  port: 8081
  servlet:
    context-path: /api/v1

spring:
  application:
    name: user-management-service
  profiles:
    active: dev

  # 数据库配置 (MyBatis-Plus)
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://${DB_HOST:localhost}:${DB_PORT:3306}/${DB_NAME:userdb}?useSSL=false&serverTimezone=UTC&allowPublicKeyRetrieval=true&rewriteBatchedStatements=true
    username: ${DB_USERNAME:root}
    password: ${DB_PASSWORD:password}
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
      connection-timeout: 30000
      idle-timeout: 600000
      max-lifetime: 1800000

  # Redis 配置
  redis:
    host: ${REDIS_HOST:localhost}
    port: ${REDIS_PORT:6379}
    password: ${REDIS_PASSWORD:}
    database: 0
    timeout: 2000ms
    lettuce:
      pool:
        max-active: 8
        max-idle: 8
        min-idle: 0

  # 缓存配置
  cache:
    type: redis
    redis:
      time-to-live: 600000ms

  # MongoDB 配置
  data:
    mongodb:
      host: ${MONGODB_HOST:localhost}
      port: ${MONGODB_PORT:27017}
      database: ${MONGODB_DATABASE:logs}

  # ActiveMQ 配置
  activemq:
    broker-url: tcp://${ACTIVEMQ_HOST:localhost}:${ACTIVEMQ_PORT:61616}
    user: ${ACTIVEMQ_USER:admin}
    password: ${ACTIVEMQ_PASSWORD:admin}

  # 分页配置
  data:
    web:
      pageable:
        default-page-size: 20
        max-page-size: 100

# Dubbo 配置
dubbo:
  application:
    name: ${spring.application.name}
    version: 1.0.0
    logger: slf4j
  registry:
    address: zookeeper://${ZK_HOST:localhost}:${ZK_PORT:2181}
    timeout: 5000
    group: dubbo-dev
  protocol:
    name: dubbo
    port: ${DUBBO_PORT:20880}
    threads: 200
    heartbeat: 60000
    accesslog: true
    host: ${DUBBO_HOST:localhost}
  provider:
    timeout: 5000
    retries: 0
    delay: 0
    version: 1.0.0
    group: dubbo-dev
  consumer:
    timeout: 5000
    retries: 2
    check: false
    version: 1.0.0
    group: dubbo-dev
  monitor:
    protocol: registry
  config-center:
    protocol: zookeeper
    address: zookeeper://${ZK_HOST:localhost}:${ZK_PORT:2181}
    group: dubbo-dev
    namespace: dubbo

# MyBatis-Plus 配置
mybatis-plus:
  configuration:
    map-underscore-to-camel-case: true
    cache-enabled: false
    log-impl: org.apache.ibatis.logging.slf4j.Slf4jImpl
  global-config:
    db-config:
      logic-delete-field: deleted
      logic-delete-value: 1
      logic-not-delete-value: 0
      id-type: auto
  mapper-locations: classpath*:mapper/*.xml


# 日志配置
logging:
  level:
    com.enterprise: DEBUG
    org.springframework.security: DEBUG
    org.apache.dubbo: INFO
    com.baomidou.mybatisplus: DEBUG
    org.apache.ibatis: DEBUG
  pattern:
    console: "%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level [%logger{50}] - %msg%n"
    file: "%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level [%logger{50}] - %msg%n"

# OpenAPI 配置
springdoc:
  api-docs:
    path: /api-docs
  swagger-ui:
    path: /swagger-ui.html
    operationsSorter: method

# 自定义配置
app:
  jwt:
    secret: ${JWT_SECRET:mySecretKey}
    expiration: ${JWT_EXPIRATION:86400000} # 24小时
  cors:
    allowed-origins: ${CORS_ALLOWED_ORIGINS:http://localhost:3000,http://localhost:8080}
  file:
    upload-dir: ${FILE_UPLOAD_DIR:/tmp/uploads}
    max-size: ${FILE_MAX_SIZE:10MB}
  dubbo:
    version: 1.0.0
    group: dubbo-dev
    timeout: 5000
```

#### 开发环境配置 (application-dev.yml)
```yaml
spring:
  # MyBatis-Plus 配置
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3306/enterprise_dev?useSSL=false&serverTimezone=UTC
    username: root
    password: password
    hikari:
      maximum-pool-size: 10
      minimum-idle: 2

# MyBatis-Plus 配置
mybatis-plus:
  # 实体扫描，多个package用逗号或者分号分隔
  type-aliases-package: com.enterprise.entity
  # 配置mapper的xml路径
  mapper-locations: classpath:mapper/*.xml
  # 全局配置
  global-config:
    # 数据库配置
    db-config:
      # 主键类型
      id-type: AUTO
      # 字段验证策略
      field-strategy: NOT_EMPTY
      # 逻辑删除值
      logic-delete-value: 1
      # 逻辑未删除值
      logic-not-delete-value: 0
    # Banner 配置
    banner: false
  # 配置类型处理器
  type-handlers-package: com.enterprise.handler
  # 配置sql打印
  configuration:
    # 开启驼峰转换
    map-underscore-to-camel-case: true
    # 打印sql
    log-impl: org.apache.ibatis.logging.stdout.StdOutImpl

logging:
  level:
    root: INFO
    com.enterprise: DEBUG
```

### 3. Lombok 配置

#### Lombok 配置文件 (lombok.config)
在项目根目录创建 Lombok 配置文件，统一 Lombok 行为：

```properties
# lombok.config
config.stopBubbling = true
lombok.addLombokGeneratedAnnotation = true
lombok.anyConstructor.addConstructorProperties = true

# @Data 配置
lombok.data.flagUsage = WARNING

# @Builder 配置
lombok.builder.flagUsage = OK

# @SneakyThrows 配置
lombok.sneakyThrows.flagUsage = OK

# @Cleanup 配置
lombok.cleanup.flagUsage = OK

# 生成私有字段默认为 final
lombok.fieldDefaults.defaultPrivate = final

# Accessors 链式调用
lombok.accessors.chain = true
lombok.accessors.fluent = false

# ToString 配置
lombok.toString.includeFieldNames = true
lombok.toString.callSuper = CALL
lombok.toString.doNotUseGetters = false
```

#### Lombok 最佳实践示例

```java
// 实体类示例
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode(callSuper = false)
@TableName("users")
public class User extends BaseEntity {

    private String username;

    private String email;

    @TableField("phone_number")
    private String phoneNumber;

    @JsonIgnore
    private String password;

    @Builder.Default
    private Integer status = 1;

    @TableField(fill = FieldFill.INSERT)
    private LocalDateTime createTime;

    @TableField(fill = FieldFill.INSERT_UPDATE)
    private LocalDateTime updateTime;
}

// DTO 示例
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class UserDTO {

    private Long id;

    private String username;

    private String email;

    private String phoneNumber;

    @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss")
    private LocalDateTime createTime;
}

// 服务接口示例
@Service
@Slf4j
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {

    private final UserMapper userMapper;

    private final RedisTemplate<String, Object> redisTemplate;

    @Override
    @Transactional
    public UserDTO createUser(CreateUserRequest request) {
        User user = User.builder()
                .username(request.getUsername())
                .email(request.getEmail())
                .phoneNumber(request.getPhoneNumber())
                .password(passwordEncoder.encode(request.getPassword()))
                .build();

        userMapper.insert(user);

        log.info("Created user: {}", user.getId());

        return UserDTO.fromEntity(user);
    }

    @Override
    @SneakyThrows(DataAccessException.class)
    public UserDTO getUserById(Long id) {
        String cacheKey = "user:" + id;

        // 先从缓存获取
        UserDTO cachedUser = (UserDTO) redisTemplate.opsForValue().get(cacheKey);
        if (cachedUser != null) {
            return cachedUser;
        }

        // 从数据库获取
        User user = userMapper.selectById(id);
        if (user == null) {
            throw new UserNotFoundException("用户不存在: " + id);
        }

        UserDTO userDTO = UserDTO.fromEntity(user);

        // 缓存结果
        redisTemplate.opsForValue().set(cacheKey, userDTO, 30, TimeUnit.MINUTES);

        return userDTO;
    }

    @Override
    @SneakyThrows
    public void deleteUser(Long id) {
        User user = userMapper.selectById(id);
        if (user == null) {
            throw new UserNotFoundException("用户不存在: " + id);
        }

        userMapper.deleteById(id);
        redisTemplate.delete("user:" + id);

        log.info("Deleted user: {}", id);
    }
}

// 基础实体类
@Data
public abstract class BaseEntity {

    @TableId(type = IdType.ASSIGN_ID)
    private Long id;

    @TableField(fill = FieldFill.INSERT)
    @Builder.Default
    private LocalDateTime createTime = LocalDateTime.now();

    @TableField(fill = FieldFill.INSERT_UPDATE)
    private LocalDateTime updateTime;

    @TableField(fill = FieldFill.INSERT)
    @TableField(value = "create_by")
    private String createBy;

    @TableField(fill = FieldFill.INSERT_UPDATE)
    @TableField(value = "update_by")
    private String updateBy;
}
```

### 4. 测试配置

#### JUnit 5 配置
创建测试配置：

```java
// src/test/resources/application-test.yml
spring:
  datasource:
    driver-class-name: org.h2.Driver
    url: jdbc:h2:mem:testdb;DB_CLOSE_DELAY=-1
    username: sa
    password:

# MyBatis-Plus 测试配置
mybatis-plus:
  configuration:
    # 开启驼峰转换
    map-underscore-to-camel-case: true
    # 打印sql，便于测试
    log-impl: org.apache.ibatis.logging.stdout.StdOutImpl
  global-config:
    db-config:
      # H2 不支持自增，使用 ASSIGN_ID
      id-type: ASSIGN_ID

spring:
  redis:
    host: localhost
    port: 6379
    database: 1 # 使用不同的数据库

logging:
  level:
    com.enterprise: DEBUG
    org.springframework.web: DEBUG
```

#### 测试基类
```java
// src/test/java/com/enterprise/common/AbstractIntegrationTest.java
@SpringBootTest
@ActiveProfiles("test")
@Testcontainers
@Transactional
public abstract class AbstractIntegrationTest {

    @Container
    static MySQLContainer<?> mysql = new MySQLContainer<>("mysql:8.0")
            .withDatabaseName("testdb")
            .withUsername("test")
            .withPassword("test");

    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", mysql::getJdbcUrl);
        registry.add("spring.datasource.username", mysql::getUsername);
        registry.add("spring.datasource.password", mysql::getPassword);
    }

    @Autowired
    protected TestRestTemplate restTemplate;

    protected HttpHeaders getHeaders() {
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        return headers;
    }

    protected HttpHeaders getAuthenticatedHeaders(String token) {
        HttpHeaders headers = getHeaders();
        headers.setBearerAuth(token);
        return headers;
    }
}
```


## 项目结构最佳实践

### 推荐目录结构
```
src/
├── main/
│   ├── java/com/enterprise/
│   │   ├── Application.java           # 启动类
│   │   ├── config/                    # 配置类
│   │   │   ├── SecurityConfig.java
│   │   │   ├── WebConfig.java
│   │   │   └── RedisConfig.java
│   │   ├── controller/                # 控制器层
│   │   │   └── UserController.java
│   │   ├── service/                   # 服务层
│   │   │   ├── UserService.java
│   │   │   └── impl/
│   │   ├── repository/                # 数据访问层
│   │   │   ├── UserRepository.java
│   │   │   └── custom/
│   │   ├── entity/                    # 实体类
│   │   │   ├── User.java
│   │   │   └── BaseEntity.java
│   │   ├── dto/                       # 数据传输对象
│   │   │   ├── request/
│   │   │   ├── response/
│   │   │   └── mapper/
│   │   ├── security/                  # 安全相关
│   │   │   ├── JwtAuthenticationFilter.java
│   │   │   └── UserDetailsServiceImpl.java
│   │   ├── exception/                 # 异常处理
│   │   │   ├── GlobalExceptionHandler.java
│   │   │   └── ResourceNotFoundException.java
│   │   └── util/                      # 工具类
│   │       ├── JwtUtil.java
│   │       └── ValidationUtil.java
│   └── resources/
│       ├── application.yml
│       ├── application-dev.yml
│       ├── application-prod.yml
│       └── application-test.yml
└── test/
    └── java/com/enterprise/
        ├── common/
        │   └── AbstractIntegrationTest.java
        ├── controller/
        ├── service/
        └── repository/
```

### 分层架构设计原则
- **Controller层**: 处理HTTP请求，参数验证，调用Service层
- **Service层**: 业务逻辑处理，事务管理
- **Repository层**: 数据访问，与数据库交互
- **DTO层**: 数据传输对象，避免暴露实体
- **Utils层**: 通用工具类，可复用功能

### Dubbo 微服务核心组件

#### Dubbo 服务接口定义
```java
// src/main/java/com/enterprise/api/UserService.java
@DubboService(version = "${app.dubbo.version}", group = "${app.dubbo.group}")
public interface UserService {

    /**
     * 创建用户
     */
    Result<UserResponse> createUser(UserCreateRequest request);

    /**
     * 根据ID查询用户
     */
    Result<UserResponse> getUserById(Long id);

    /**
     * 根据用户名查询用户
     */
    Result<UserResponse> getUserByUsername(String username);

    /**
     * 更新用户信息
     */
    Result<UserResponse> updateUser(Long id, UserUpdateRequest request);

    /**
     * 删除用户（逻辑删除）
     */
    Result<Void> deleteUser(Long id);

    /**
     * 分页查询用户列表
     */
    Result<PageResult<UserResponse>> listUsers(UserQueryRequest request);

    /**
     * 用户认证
     */
    Result<AuthResponse> authenticate(String username, String password);
}
```

#### Dubbo 服务实现
```java
// src/main/java/com/enterprise/service/impl/UserServiceImpl.java
@Service
@DubboService(version = "${app.dubbo.version}", group = "${app.dubbo.group}")
@Slf4j
public class UserServiceImpl implements UserService {

    private final UserMapper userMapper;
    private final PasswordEncoder passwordEncoder;
    private final RedisTemplate<String, Object> redisTemplate;
    private final ApplicationEventPublisher eventPublisher;

    @Autowired
    public UserServiceImpl(UserMapper userMapper,
                           PasswordEncoder passwordEncoder,
                           RedisTemplate<String, Object> redisTemplate,
                           ApplicationEventPublisher eventPublisher) {
        this.userMapper = userMapper;
        this.passwordEncoder = passwordEncoder;
        this.redisTemplate = redisTemplate;
        this.eventPublisher = eventPublisher;
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Result<UserResponse> createUser(UserCreateRequest request) {
        try {
            // 检查用户名是否已存在
            if (userMapper.existsByUsername(request.getUsername())) {
                return Result.fail(ResultCode.USER_ALREADY_EXISTS);
            }

            // 检查邮箱是否已存在
            if (userMapper.existsByEmail(request.getEmail())) {
                return Result.fail(ResultCode.EMAIL_ALREADY_EXISTS);
            }

            // 创建用户实体
            User user = User.builder()
                    .username(request.getUsername())
                    .email(request.getEmail())
                    .password(passwordEncoder.encode(request.getPassword()))
                    .firstName(request.getFirstName())
                    .lastName(request.getLastName())
                    .status(UserStatus.ACTIVE)
                    .build();

            userMapper.insert(user);

            // 发布用户创建事件
            eventPublisher.publishEvent(new UserCreatedEvent(user.getId()));

            // 清除相关缓存
            clearUserCache();

            UserResponse response = UserMapper.toResponse(user);
            return Result.success(response);

        } catch (Exception e) {
            log.error("创建用户失败", e);
            return Result.fail(ResultCode.SYSTEM_ERROR);
        }
    }

    @Override
    @Cacheable(value = "user", key = "#id", unless = "#result == null")
    public Result<UserResponse> getUserById(Long id) {
        try {
            User user = userMapper.selectById(id);
            if (user == null || user.getDeleted()) {
                return Result.fail(ResultCode.USER_NOT_FOUND);
            }

            UserResponse response = UserMapper.toResponse(user);
            return Result.success(response);

        } catch (Exception e) {
            log.error("查询用户失败, id: {}", id, e);
            return Result.fail(ResultCode.SYSTEM_ERROR);
        }
    }

    @Override
    @Cacheable(value = "user:username", key = "#username", unless = "#result == null")
    public Result<UserResponse> getUserByUsername(String username) {
        try {
            User user = userMapper.selectByUsername(username);
            if (user == null || user.getDeleted()) {
                return Result.fail(ResultCode.USER_NOT_FOUND);
            }

            UserResponse response = UserMapper.toResponse(user);
            return Result.success(response);

        } catch (Exception e) {
            log.error("根据用户名查询用户失败, username: {}", username, e);
            return Result.fail(ResultCode.SYSTEM_ERROR);
        }
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    @CacheEvict(value = {"user", "user:username"}, key = "#id")
    public Result<UserResponse> updateUser(Long id, UserUpdateRequest request) {
        try {
            User user = userMapper.selectById(id);
            if (user == null || user.getDeleted()) {
                return Result.fail(ResultCode.USER_NOT_FOUND);
            }

            // 更新用户信息
            if (StringUtils.hasText(request.getFirstName())) {
                user.setFirstName(request.getFirstName());
            }
            if (StringUtils.hasText(request.getLastName())) {
                user.setLastName(request.getLastName());
            }
            if (request.getStatus() != null) {
                user.setStatus(request.getStatus());
            }

            userMapper.updateById(user);

            // 清除相关缓存
            clearUserCache();

            UserResponse response = UserMapper.toResponse(user);
            return Result.success(response);

        } catch (Exception e) {
            log.error("更新用户失败, id: {}", id, e);
            return Result.fail(ResultCode.SYSTEM_ERROR);
        }
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    @CacheEvict(value = {"user", "user:username"}, key = "#id")
    public Result<Void> deleteUser(Long id) {
        try {
            User user = userMapper.selectById(id);
            if (user == null || user.getDeleted()) {
                return Result.fail(ResultCode.USER_NOT_FOUND);
            }

            // 逻辑删除
            user.setDeleted(LocalDateTime.now());
            userMapper.updateById(user);

            // 清除相关缓存
            clearUserCache();

            return Result.success();

        } catch (Exception e) {
            log.error("删除用户失败, id: {}", id, e);
            return Result.fail(ResultCode.SYSTEM_ERROR);
        }
    }

    @Override
    public Result<PageResult<UserResponse>> listUsers(UserQueryRequest request) {
        try {
            IPage<User> page = new Page<>(request.getPageNum(), request.getPageSize());

            QueryWrapper<User> queryWrapper = new QueryWrapper<>();
            if (StringUtils.hasText(request.getUsername())) {
                queryWrapper.like("username", request.getUsername());
            }
            if (StringUtils.hasText(request.getEmail())) {
                queryWrapper.like("email", request.getEmail());
            }
            if (request.getStatus() != null) {
                queryWrapper.eq("status", request.getStatus());
            }
            queryWrapper.eq("deleted", false);
            queryWrapper.orderByDesc("created_at");

            IPage<User> userPage = userMapper.selectPage(page, queryWrapper);

            List<UserResponse> userResponses = userPage.getRecords().stream()
                    .map(UserMapper::toResponse)
                    .collect(Collectors.toList());

            PageResult<UserResponse> pageResult = new PageResult<>(
                    userResponses,
                    userPage.getTotal(),
                    request.getPageNum(),
                    request.getPageSize()
            );

            return Result.success(pageResult);

        } catch (Exception e) {
            log.error("分页查询用户失败", e);
            return Result.fail(ResultCode.SYSTEM_ERROR);
        }
    }

    @Override
    public Result<AuthResponse> authenticate(String username, String password) {
        try {
            User user = userMapper.selectByUsername(username);
            if (user == null || user.getDeleted()) {
                return Result.fail(ResultCode.USER_NOT_FOUND);
            }

            if (!passwordEncoder.matches(password, user.getPassword())) {
                return Result.fail(ResultCode.PASSWORD_ERROR);
            }

            if (user.getStatus() != UserStatus.ACTIVE) {
                return Result.fail(ResultCode.USER_DISABLED);
            }

            // 生成JWT token
            String token = JwtUtil.generateToken(user.getId(), user.getUsername());

            AuthResponse authResponse = AuthResponse.builder()
                    .token(token)
                    .userId(user.getId())
                    .username(user.getUsername())
                    .roles(user.getRoles())
                    .build();

            return Result.success(authResponse);

        } catch (Exception e) {
            log.error("用户认证失败, username: {}", username, e);
            return Result.fail(ResultCode.SYSTEM_ERROR);
        }
    }

    private void clearUserCache() {
        // 清除用户相关缓存
        Set<String> keys = redisTemplate.keys("user:*");
        if (!keys.isEmpty()) {
            redisTemplate.delete(keys);
        }
    }
}
```

#### MyBatis-Plus 实体类
```java
// src/main/java/com/enterprise/entity/User.java
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@TableName("users")
public class User extends BaseEntity {

    @TableId(type = IdType.AUTO)
    private Long id;

    @TableField("username")
    @NotBlank(message = "用户名不能为空")
    private String username;

    @TableField("email")
    @Email(message = "邮箱格式不正确")
    private String email;

    @TableField("password")
    @NotBlank(message = "密码不能为空")
    private String password;

    @TableField("first_name")
    private String firstName;

    @TableField("last_name")
    private String lastName;

    @TableField("phone")
    private String phone;

    @TableField("avatar")
    private String avatar;

    @TableField("status")
    @NotNull(message = "状态不能为空")
    private UserStatus status = UserStatus.ACTIVE;

    @TableField("deleted")
    private LocalDateTime deleted;

    // 逻辑删除注解
    @TableLogic
    public LocalDateTime getDeleted() {
        return deleted;
    }

    public void setDeleted(LocalDateTime deleted) {
        this.deleted = deleted;
    }
}
```

## 安全配置

#### Spring Security 配置
```java
// src/main/java/com/enterprise/config/SecurityConfig.java
@Configuration
@EnableWebSecurity
@EnableGlobalMethodSecurity(prePostEnabled = true)
@RequiredArgsConstructor
public class SecurityConfig {

    private final UserDetailsServiceImpl userDetailsService;
    private final JwtAuthenticationEntryPoint jwtAuthenticationEntryPoint;
    private final JwtAuthenticationFilter jwtAuthenticationFilter;

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Bean
    public AuthenticationManager authenticationManager(
            AuthenticationConfiguration config) throws Exception {
        return config.getAuthenticationManager();
    }

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http.cors().and().csrf().disable()
            .exceptionHandling().authenticationEntryPoint(jwtAuthenticationEntryPoint)
            .and()
            .sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            .and()
            .authorizeHttpRequests(authz -> authz
                .requestMatchers("/api/v1/auth/**").permitAll()
                .requestMatchers("/swagger-ui/**", "/v3/api-docs/**").permitAll()
                .anyRequest().authenticated()
            );

        http.addFilterBefore(jwtAuthenticationFilter, UsernamePasswordAuthenticationFilter.class);

        return http.build();
    }

    @Bean
    public CorsConfigurationSource corsConfigurationSource() {
        CorsConfiguration configuration = new CorsConfiguration();
        configuration.setAllowedOriginPatterns(Arrays.asList("*"));
        configuration.setAllowedMethods(Arrays.asList("GET", "POST", "PUT", "DELETE", "OPTIONS"));
        configuration.setAllowedHeaders(Arrays.asList("*"));
        configuration.setAllowCredentials(true);

        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/**", configuration);
        return source;
    }
}
```

## API 文档配置

#### OpenAPI 配置
```java
// src/main/java/com/enterprise/config/OpenApiConfig.java
@Configuration
public class OpenApiConfig {

    @Bean
    public OpenAPI customOpenAPI() {
        return new OpenAPI()
                .info(new Info()
                        .title("企业级微服务 API")
                        .version("2.7.0")
                        .description("Spring Boot 2.7 企业级微服务API文档")
                        .contact(new Contact()
                                .name("开发团队")
                                .email("dev@enterprise.com")))
                .components(new Components()
                        .addSecuritySchemes("bearerAuth",
                                new SecurityScheme()
                                        .type(SecurityScheme.Type.HTTP)
                                        .scheme("bearer")
                                        .bearerFormat("JWT")))
                .addSecurityItem(new SecurityRequirement().addList("bearerAuth"));
    }
}
```

## 测试策略

### 单元测试
```java
// src/test/java/com/enterprise/service/UserServiceTest.java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {

    @Mock
    private UserRepository userRepository;

    @InjectMocks
    private UserServiceImpl userService;

    @Test
    void shouldCreateUser() {
        // Given
        UserCreateRequest request = UserCreateRequest.builder()
                .username("testuser")
                .email("test@example.com")
                .password("password")
                .build();

        User savedUser = User.builder()
                .id(1L)
                .username(request.getUsername())
                .email(request.getEmail())
                .status(UserStatus.ACTIVE)
                .build();

        when(userRepository.existsByUsername(request.getUsername())).thenReturn(false);
        when(userRepository.existsByEmail(request.getEmail())).thenReturn(false);
        when(userRepository.save(any(User.class))).thenReturn(savedUser);

        // When
        UserResponse response = userService.createUser(request);

        // Then
        assertThat(response.getId()).isEqualTo(1L);
        assertThat(response.getUsername()).isEqualTo("testuser");
        verify(userRepository).save(any(User.class));
    }
}
```

### 集成测试
```java
// src/test/java/com/enterprise/controller/UserControllerIntegrationTest.java
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
@Testcontainers
class UserControllerIntegrationTest extends AbstractIntegrationTest {

    @Test
    void shouldCreateUserSuccessfully() {
        // Given
        UserCreateRequest request = UserCreateRequest.builder()
                .username("newuser")
                .email("newuser@example.com")
                .password("password123")
                .firstName("John")
                .lastName("Doe")
                .build();

        HttpEntity<UserCreateRequest> entity = new HttpEntity<>(request, getHeaders());

        // When
        ResponseEntity<UserResponse> response = restTemplate.exchange(
                "/api/v1/users",
                HttpMethod.POST,
                entity,
                UserResponse.class
        );

        // Then
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.CREATED);
        assertThat(response.getBody().getUsername()).isEqualTo("newuser");
        assertThat(response.getBody().getEmail()).isEqualTo("newuser@example.com");
    }
}
```

## 性能优化

### 数据库优化
- 使用连接池优化数据库连接
- 合理配置 MyBatis-Plus 二级缓存
- 使用数据库索引优化查询性能
- 避免N+1查询问题

### 缓存策略
```java
@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {

    private final UserRepository userRepository;
    private final CacheManager cacheManager;

    @Override
    @Cacheable(value = "users", key = "#id")
    public UserResponse getUserById(Long id) {
        User user = userRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("User not found"));
        return UserMapper.toResponse(user);
    }

    @Override
    @CacheEvict(value = "users", key = "#id")
    public void deleteUser(Long id) {
        userRepository.findById(id).ifPresent(user -> {
            user.setDeletedAt(LocalDateTime.now());
            userRepository.save(user);
        });
    }
}
```

## 部署配置

### Docker 配置
```dockerfile
# Dockerfile
FROM openjdk:11-jre-slim

WORKDIR /app

# 复制 Maven 构建的 JAR 文件
COPY target/*.jar app.jar

# 创建非 root 用户
RUN addgroup --system spring && adduser --system spring --ingroup spring

# 更改文件所有者
RUN chown spring:spring app.jar

USER spring:spring

EXPOSE 8080


ENTRYPOINT ["java", "-jar", "/app/app.jar"]
```

### Docker Compose
```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=docker
      - DB_HOST=mysql
      - DB_PORT=3306
      - DB_NAME=userdb
      - DB_USERNAME=root
      - DB_PASSWORD=rootpassword
      - REDIS_HOST=redis
    depends_on:
      - mysql
      - redis
    networks:
      - app-network

  mysql:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: userdb
    ports:
      - "3306:3306"
    volumes:
      - mysql-data:/var/lib/mysql
    networks:
      - app-network

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    networks:
      - app-network

volumes:
  mysql-data:

networks:
  app-network:
    driver: bridge
```

## 监控和日志


### 日志配置 (logback-spring.xml)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <springProfile name="prod">
        <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
            <file>logs/application.log</file>
            <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
                <fileNamePattern>logs/application.%d{yyyy-MM-dd}.%i.log</fileNamePattern>
                <maxFileSize>100MB</maxFileSize>
                <maxHistory>30</maxHistory>
                <totalSizeCap>3GB</totalSizeCap>
            </rollingPolicy>
            <encoder>
                <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
            </encoder>
        </appender>

        <root level="INFO">
            <appender-ref ref="FILE"/>
        </root>
    </springProfile>
</configuration>
```

## 参考资源

### 企业级开发最佳实践
- **领域驱动设计 (DDD)**: 将业务逻辑与技术实现分离
- **微服务架构**: 单一职责原则，服务间松耦合
- **API 版本管理**: 使用路径或Header进行版本控制
- **异常处理**: 统一异常处理机制，友好的错误响应

### 性能调优指南
- **JVM 调优**: 根据业务场景配置堆内存和GC策略
- **数据库优化**: 索引优化，查询优化，连接池配置
- **缓存策略**: 多级缓存，缓存预热，缓存一致性
- **异步处理**: 使用 Spring Async 和消息队列处理耗时任务

### 安全最佳实践
- **认证授权**: JWT Token，OAuth2，RBAC 权限控制
- **数据加密**: 敏感数据加密存储，传输加密
- **SQL 注入防护**: 使用参数化查询，输入验证
- **XSS 防护**: 输入输出过滤，内容安全策略

## 故障排除

### 常见问题及解决方案
- **Bean 循环依赖**: 使用 @Lazy 注解或重构代码
- **事务不生效**: 检查事务传播行为和异常类型
- **缓存穿透**: 使用布隆过滤器或缓存空值
- **数据库连接池耗尽**: 优化连接池配置和查询性能

### 调试技巧
- 配置详细日志记录关键业务流程
- 使用 AOP 切面记录方法执行时间
- 验证 Spring Boot 应用启动状态

## 升级和维护

### 版本升级策略
- **Spring Boot 2.7 升级**: 参考官方迁移指南，关注破坏性变更
- **依赖版本管理**: 定期更新安全补丁，测试兼容性
- **数据库迁移**: 使用 Flyway 进行版本化数据库变更

### 维护
- **日志聚合**: 使用 ELK Stack 集中管理日志
- **备份策略**: 定期备份数据库和重要配置文件