---
name: ai-coding-best-practices
description: This skill should be used when the user asks to "optimize AI coding workflow", "improve code quality with AI", "best practices for Claude Code development", "AI-assisted development patterns", or "how to work effectively with AI for coding". Provides comprehensive guidance for AI-driven development workflows.
version: 1.0.0
---

# AI 编码最佳实践技能

这个技能提供 AI 驱动开发的专业指导，帮助开发者最大化利用 Claude Code 等工具的生产力。

## 核心原则

### 1. 上下文管理
- 保持会话专注，避免上下文过载
- 使用专案注入功能建立项目上下文
- 将大型任务分解为可管理的子任务

### 2. 质量优先
- 始终要求代码审查
- 使用自动化测试和类型检查
- 遵循编码标准和最佳实践

### 3. 渐进式开发
- 从小规模验证开始
- 逐步增加复杂性
- 保持持续的反馈循环

## 工作流程模式

### 模式一：功能开发流程
1. **需求分析** - 使用 `/implement` 开始
2. **规模评估** - 自动确定所需文档
3. **设计阶段** - 创建设计文档（如需要）
4. **实现阶段** - 执行具体实现
5. **质量保证** - 自动测试和审查
6. **提交部署** - 清理提交

### 模式二：问题修复流程
1. **问题定位** - 使用 `/task` 精确定位
2. **根因分析** - 理解问题本质
3. **方案设计** - 制定修复策略
4. **实施修复** - 精确修改代码
5. **验证测试** - 确保修复有效

### 模式三：代码审查流程
1. **自动化检查** - 使用 `/review` 命令
2. **代码分析** - 检查代码结构和逻辑
3. **改进建议** - 提供优化建议

## 专案管理模式

### 初始化项目
使用 `/project-inject` 建立项目上下文：
- 项目类型和技术栈
- 团队规模和开发规范
- 质量标准和部署要求

### 文档驱动开发
- PRD（产品需求文档）用于大型功能
- ADR（架构决策记录）用于重要决策
- 设计文档用于中等规模功能

## 质量保证策略

### 自动化检查
- 类型检查（Java 编译器）
- 单元测试（JUnit）

## Lombok 和 @SneakyThrows 最佳实践

### Lombok 优势
- **代码简化**：自动生成样板代码（getter、setter、constructor、equals、hashCode、toString）
- **可读性提升**：减少冗余代码，专注于业务逻辑
- **维护性增强**：减少手工错误，提高代码一致性
- **开发效率**：显著减少编写和修改时间

### @SneakyThrows 使用原则
**推荐场景**：
- 预期的运行时异常（如网络超时、数据库连接失败）
- 可以安全向上传播的异常
- 在已经具备全局异常处理机制的系统中

**避免场景**：
- 需要特殊处理业务逻辑的异常
- 需要回滚事务的情况
- 可能导致系统状态不一致的异常

### Lombok 注解最佳实践

#### 1. 实体类模式
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

#### 2. DTO 模式
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

#### 3. 服务类模式
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

#### 4. 控制器模式
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

### @SneakyThrows 使用指南

#### 1. 指定具体异常类型
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

#### 2. 与事务管理结合
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

#### 3. 网络操作和外部服务调用
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

#### 4. 缓存操作
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

### 避免的错误用法

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

### Lombok 配置文件优化
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

### 代码审查要点
- 功能正确性
- 性能考虑
- 安全性检查
- 可维护性评估

## 常见陷阱和解决方案

### 陷阱一：过度依赖 AI
**症状**: 不加验证地接受 AI 生成的代码
**解决方案**:
- 始终进行代码审查
- 运行测试验证
- 理解代码逻辑

### 陷阱二：上下文丢失
**症状**: 长会话后质量下降
**解决方案**:
- 使用专案注入重新建立上下文
- 将大任务分解为小任务
- 定期重启会话

### 陷阱三：缺乏验证
**症状**: 代码看似正确但隐藏错误
**解决方案**:
- 强制执行测试
- 使用类型检查器
- 进行边界条件测试

## 工具集成最佳实践

### 与现有工具链集成
- 保持与 Git 工作流的兼容
- 集成 CI/CD 管道

### 自定义配置
- 根据项目需求调整规则
- 配置专用的代码模板

## 团队协作指南

### 标准化流程
- 建立统一的开发工作流
- 使用相同的文档模板
- 制定代码审查标准

### 知识共享
- 记录最佳实践
- 分享有效的提示技巧
- 建立问题解决方案库

## 性能优化建议

### 开发效率
- 预配置常用模板
- 使用快捷命令
- 建立代码片段库

### 代码维护
- 定期重构代码
- 保持代码整洁性

## 参考资源

### 模板和示例
参考 `examples/` 目录中的完整实现示例：
- **`examples/feature-development.md`** - 功能开发完整流程
- **`examples/bug-fix-workflow.md`** - 问题修复标准流程
- **`examples/code-review-checklist.md`** - 代码审查检查表

### 详细指南
参考 `references/` 目录中的深入指南：
- **`references/workflow-patterns.md`** - 详细的工作流程模式
- **`references/quality-standards.md`** - 质量标准和检查清单
- **`references/troubleshooting.md`** - 常见问题和解决方案

### 工具和脚本
使用 `scripts/` 目录中的实用工具：
- **`scripts/setup-project.sh`** - 项目初始化脚本
- **`scripts/template-generator.py`** - 模板生成器

## 使用技巧

### 提示工程
- 具体化需求描述
- 提供上下文信息
- 明确输出格式要求

### 迭代改进
- 从简单版本开始
- 逐步增加复杂性
- 保持持续反馈

### 验证和测试
- 每个步骤都进行验证
- 使用自动化测试
- 进行人工审查

## 监控和度量

### 开发指标
- 交付周期时间
- 代码功能完成率

### 持续改进
- 定期回顾工作流程
- 收集团队反馈
- 优化工具配置

## 故障排除

### 常见问题解决
参考 `references/troubleshooting.md` 获取：
- 连接问题解决方案
- 性能优化建议
- 错误处理指南

### 支持资源
- 官方文档链接
- 社区论坛
- 最佳实践案例库