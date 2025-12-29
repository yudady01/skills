# AI 编码最佳实践代码示例

## Lombok 实体类模式

```java
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode(callSuper = false)
@TableName("users")
public class User extends BaseEntity {

    @TableId(type = IdType.ASSIGN_ID)
    private Long id;

    @NotBlank
    @TableField("username")
    private String username;

    @JsonIgnore
    private String password;

    @Builder.Default
    private Integer status = 1;
}
```

## Lombok DTO 模式

```java
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class UserDTO {

    private Long id;
    private String username;

    @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss")
    private LocalDateTime createTime;

    public static UserDTO fromEntity(User user) {
        return UserDTO.builder()
                .id(user.getId())
                .username(user.getUsername())
                .createTime(user.getCreateTime())
                .build();
    }
}
```

## Lombok 服务类模式

```java
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
                .build();

        userMapper.insert(user);
        log.info("Created user: {}", user.getId());

        return UserDTO.fromEntity(user);
    }

    @Override
    @SneakyThrows(DataAccessException.class)
    public UserDTO getUserById(Long id) {
        // 数据库操作，允许异常向上传播
        User user = userMapper.selectById(id);
        if (user == null) {
            throw new UserNotFoundException("用户不存在: " + id);
        }
        return UserDTO.fromEntity(user);
    }
}
```

## Lombok 控制器模式

```java
@RestController
@RequestMapping("/api/users")
@Slf4j
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    @GetMapping("/{id}")
    @SneakyThrows(UserNotFoundException.class)
    public ResponseEntity<ApiResponse<UserDTO>> getUser(@PathVariable Long id) {
        // 允许业务异常向上传播，由全局异常处理器处理
        UserDTO user = userService.getUserById(id);
        return ResponseEntity.ok(ApiResponse.success(user, "获取成功"));
    }
}
```

## @SneakyThrows 指定具体异常类型

```java
// ✅ 推荐：指定具体的异常类型
@SneakyThrows(IOException.class)
public String readFile(String path) {
    return Files.readString(Paths.get(path));
}

// ✅ 推荐：多个异常类型
@SneakyThrows({IOException.class, SecurityException.class})
public String readFileWithSecurity(String path) {
    return Files.readString(Paths.get(path));
}
```

## @SneakyThrows 与事务管理结合

```java
@Service
@Transactional
public class OrderServiceImpl implements OrderService {

    @Override
    @SneakyThrows({DataAccessException.class, OptimisticLockingFailureException.class})
    public Order createOrder(CreateOrderRequest request) {
        // 数据库操作异常会触发事务回滚
        Order order = Order.builder()
                .userId(request.getUserId())
                .totalAmount(request.getTotalAmount())
                .build();

        orderMapper.insert(order);
        return order;
    }
}
```

## @SneakyThrows 网络操作

```java
@Service
@RequiredArgsConstructor
public class ExternalApiService {

    private final RestTemplate restTemplate;

    @Override
    @SneakyThrows({RestClientException.class, SocketTimeoutException.class})
    public String callExternalService(String url) {
        // 网络异常通常是临时的，可以向上传播由重试机制处理
        return restTemplate.getForObject(url, String.class);
    }
}
```

## @SneakyThrows 缓存操作

```java
@Service
@RequiredArgsConstructor
public class CacheService {

    private final RedisTemplate<String, Object> redisTemplate;

    @Override
    @SneakyThrows(RedisConnectionFailureException.class)
    public void setCache(String key, Object value, long timeout, TimeUnit unit) {
        // Redis 连接失败通常可以向上传播，由降级策略处理
        redisTemplate.opsForValue().set(key, value, timeout, unit);
    }
}
```

## Lombok 配置文件

```properties
# lombok.config
config.stopBubbling = true

# 启用 Lombok 生成注解
lombok.addLombokGeneratedAnnotation = true

# Builder 模式优化
lombok.builder.flagUsage = OK
lombok.anyConstructor.addConstructorProperties = true

# 字段默认设置
lombok.fieldDefaults.defaultPrivate = final
lombok.fieldDefaults.defaultProtected = final
lombok.fieldDefaults.defaultPackage = final

# 链式调用
lombok.accessors.chain = true
lombok.accessors.fluent = false

# ToString 优化
lombok.toString.includeFieldNames = true
lombok.toString.callSuper = CALL
lombok.toString.doNotUseGetters = false

# 允许 @SneakyThrows
lombok.sneakyThrows.flagUsage = OK
```

## 避免的错误用法

```java
// ❌ 错误：不应该包装所有异常
@SneakyThrows(Exception.class)  // 过于宽泛
public void doSomething() {
    // 业务逻辑
}

// ❌ 错误：需要特殊处理的业务异常
@SneakyThrows(BusinessException.class)
public void processPayment(PaymentRequest request) {
    if (request.getAmount() <= 0) {
        throw new BusinessException("金额必须大于0");  // 应该明确处理
    }
    // 处理支付逻辑
}

// ❌ 错误：在需要事务回滚的场景
@Transactional
@SneakyThrows(DataException.class)
public void transferMoney(TransferRequest request) {
    // 这里应该明确处理异常以确保事务正确回滚
}
```
