---
name: quality-assurance
description: This skill should be used when the user asks to "ensure code quality", "run quality checks", "setup quality gates", "implement code review", "testing strategy", or "quality assurance workflow". Provides comprehensive quality assurance and testing strategies for Spring Boot 2.7 enterprise applications.
version: 2.7.0
---

# Spring Boot 2.7 企业级质量保证技能

这个技能提供全面的 Spring Boot 2.7 企业级应用代码质量保证策略，包括自动化检查、测试策略和代码审查流程。

## 质量检查层级

### 1. 静态分析
自动代码分析，无需运行代码：
- **Java 编译器** - 类型检查和语法验证
- **SonarQube** - 综合代码质量分析

### 2. 动态分析
运行时代码分析：
- **单元测试** - 类和方法级别测试
- **端到端测试** - 完整业务流程测试
- **安全测试** - 安全漏洞扫描

### 3. 人工审查
代码审查和质量评估：
- **代码审查** - 同行评审
- **架构审查** - 设计模式评估
- **安全审查** - 安全漏洞检查
- **性能审查** - 性能瓶颈分析

## 自动化质量门

### Pre-commit 检查
配置 Git hooks 进行提交前检查：

```bash
#!/bin/sh
# .git/hooks/pre-commit

echo "Running quality checks..."

# Maven 格式化检查
mvn spotless:check

# 编译检查
mvn compile

# 运行单元测试
mvn test

echo "Quality checks passed!"
```

### Maven 配置质量插件
```xml
<build>
    <plugins>
        <!-- 代码格式化 -->
        <plugin>
            <groupId>com.diffplug.spotless</groupId>
            <artifactId>spotless-maven-plugin</artifactId>
            <version>2.27.0</version>
            <configuration>
                <java>
                    <googleJavaFormat>
                        <version>1.15.0</version>
                        <style>GOOGLE</style>
                    </googleJavaFormat>
                    <removeUnusedImports/>
                    <importOrder>
                        <order>java,javax,org,com</order>
                    </importOrder>
                </java>
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>check</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>

      </plugins>
</build>
```

## 测试策略

### 测试金字塔
```
    /\
   /  \     E2E Tests (少量)
  /____\
 /      \   Integration Tests (适量)
/__________\ Unit Tests (大量)
```

### 单元测试策略
使用 JUnit 5 和 Mockito 进行单元测试：

```java
// src/test/java/com/enterprise/service/UserServiceTest.java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {

    @Mock
    private UserRepository userRepository;

    @Mock
    private PasswordEncoder passwordEncoder;

    @Mock
    private ApplicationEventPublisher eventPublisher;

    @InjectMocks
    private UserServiceImpl userService;

    @Test
    @DisplayName("应该成功创建用户")
    void shouldCreateUserSuccessfully() {
        // Given
        UserCreateRequest request = UserCreateRequest.builder()
                .username("testuser")
                .email("test@example.com")
                .password("password123")
                .firstName("Test")
                .lastName("User")
                .build();

        User savedUser = User.builder()
                .id(1L)
                .username(request.getUsername())
                .email(request.getEmail())
                .firstName(request.getFirstName())
                .lastName(request.getLastName())
                .status(UserStatus.ACTIVE)
                .build();

        when(userRepository.existsByUsername(request.getUsername())).thenReturn(false);
        when(userRepository.existsByEmail(request.getEmail())).thenReturn(false);
        when(passwordEncoder.encode(request.getPassword())).thenReturn("encodedPassword");
        when(userRepository.save(any(User.class))).thenReturn(savedUser);

        // When
        UserResponse response = userService.createUser(request);

        // Then
        assertThat(response.getId()).isEqualTo(1L);
        assertThat(response.getUsername()).isEqualTo("testuser");
        assertThat(response.getEmail()).isEqualTo("test@example.com");

        verify(userRepository).save(any(User.class));
        verify(eventPublisher).publishEvent(any(UserCreatedEvent.class));
    }

    @Test
    @DisplayName("当用户名已存在时应该抛出异常")
    void shouldThrowExceptionWhenUsernameAlreadyExists() {
        // Given
        UserCreateRequest request = UserCreateRequest.builder()
                .username("existinguser")
                .email("test@example.com")
                .password("password123")
                .build();

        when(userRepository.existsByUsername(request.getUsername())).thenReturn(true);

        // When & Then
        assertThrows(UserAlreadyExistsException.class,
            () -> userService.createUser(request));

        verify(userRepository, never()).save(any(User.class));
    }
}
```


### 端到端测试策略
使用 Selenium WebDriver：

```java
// src/test/java/com/enterprise/e2e/UserRegistrationE2ETest.java
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.DEFINED_PORT)
@ActiveProfiles("e2e")
class UserRegistrationE2ETest {

    private static WebDriver driver;
    private static WebDriverWait wait;

    @BeforeAll
    static void setup() {
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless");
        options.addArguments("--no-sandbox");
        options.addArguments("--disable-dev-shm-usage");

        driver = new ChromeDriver(options);
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    @AfterAll
    static void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }

    @Test
    @DisplayName("应该完成用户注册流程")
    void shouldCompleteUserRegistrationFlow() {
        // Given
        driver.get("http://localhost:8080/register");

        // 填写注册表单
        WebElement usernameField = wait.until(
            ExpectedConditions.presenceOfElementLocated(By.id("username"))
        );
        usernameField.sendKeys("e2euser");

        driver.findElement(By.id("email")).sendKeys("e2e@example.com");
        driver.findElement(By.id("password")).sendKeys("password123");
        driver.findElement(By.id("confirmPassword")).sendKeys("password123");
        driver.findElement(By.id("firstName")).sendKeys("E2E");
        driver.findElement(By.id("lastName")).sendKeys("Test");

        // 提交表单
        driver.findElement(By.id("registerButton")).click();

        // 验证重定向到仪表板
        wait.until(ExpectedConditions.urlContains("/dashboard"));

        WebElement welcomeMessage = wait.until(
            ExpectedConditions.presenceOfElementLocated(By.className("welcome-message"))
        );
        assertThat(welcomeMessage.getText()).contains("E2E Test");
    }
}
```


### SonarQube 集成
```xml
<plugin>
    <groupId>org.sonarsource.scanner.maven</groupId>
    <artifactId>sonar-maven-plugin</artifactId>
    <version>3.9.1.2184</version>
</plugin>
```

```bash
# 运行 SonarQube 扫描
mvn clean verify sonar:sonar \
  -Dsonar.projectKey=my-project \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=your-token
```

## 代码质量指标

### 复杂度测量
使用 JavaNCSS 测量代码复杂度：

```xml
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>javasrc-maven-plugin</artifactId>
    <version>0.3.1</version>
    <executions>
        <execution>
            <goals>
                <goal>javasrc</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

### 技术债务分析
SonarQube 技术债务指标：
- **可维护性评级** (A-E)
- **技术债务比率**
- **代码异味数量**
- **重复代码百分比**





### 持续改进
基于质量数据进行持续改进：

1. **设定质量目标**
   - 代码复杂度平均值 ≤ 10
   - 重复代码 ≤ 3%

2. **定期评估**
   - 每日构建质量检查
   - 每周质量报告
   - 每月质量回顾

3. **问题识别**
   - 实时质量监控
   - 质量趋势分析
   - 异常质量告警

4. **改进措施**
   - 代码重构计划
   - 测试策略优化
   - 工具链升级

## 企业级最佳实践

### 代码审查清单
- [ ] 代码符合项目编码规范
- [ ] 单元测试通过
- [ ] 没有明显的性能问题
- [ ] 错误处理完善
- [ ] 文档更新及时

### 质量门标准
- **构建状态**: 成功
- **代码质量**: SonarQube Gate 通过

### 团队协作
- **结对编程**: 提高代码质量
- **代码审查**: 知识共享和质量保证
- **技术分享**: 提升团队整体水平
- **质量培训**: 建立质量意识

## 参考资源

### 质量检查脚本
使用 `scripts/` 目录中的自动化工具：
- **`scripts/quality-gate.sh`** - 质量门检查脚本
- **`scripts/coverage-report.sh`** - 覆盖率报告生成

### 配置模板
参考项目中的配置文件：

### 详细指南
参考企业级开发最佳实践：
- **代码质量标准**
- **测试策略指南**
- **安全开发规范**
- **性能优化指南**

## 故障排除

### 常见质量问题
- **测试覆盖率不足**: 增加测试用例，提高测试覆盖率
- **代码重复率高**: 提取公共方法，使用设计模式
- **复杂度过高**: 重构复杂方法，应用 SOLID 原则
- **性能回归**: 性能测试，定位性能瓶颈

### 解决方案
1. **质量分析报告**: 使用工具生成详细的质量报告
2. **问题定位**: 结合多种工具定位具体问题
3. **重构计划**: 制定系统性的代码重构计划
4. **持续监控**: 建立质量监控和告警机制