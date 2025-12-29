# 管理后台代码示例

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

## BaseController 工具方法

```java
public abstract class BaseController {

    /**
     * 获取当前登录用户
     */
    protected SysUser getUser() {
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        return (SysUser) authentication.getPrincipal();
    }

    /**
     * 获取分页参数
     */
    protected Integer getPageIndex() {
        String pageIndex = getString("pageIndex");
        return pageIndex == null ? 1 : Integer.parseInt(pageIndex);
    }

    protected Integer getPageSize() {
        String pageSize = getString("pageSize");
        return pageSize == null ? 20 : Integer.parseInt(pageSize);
    }

    /**
     * 获取 JSON 参数
     */
    protected JSONObject getJsonParam() {
        String params = getString("params");
        if (StringUtils.isEmpty(params)) {
            return new JSONObject();
        }
        return JSONObject.parseObject(params);
    }

    /**
     * 获取字符串参数
     */
    protected String getString(String key) {
        HttpServletRequest request = ((ServletRequestAttributes) RequestContextHolder.getRequestAttributes()).getRequest();
        return request.getParameter(key);
    }

    /**
     * 获取整数参数
     */
    protected Integer getInteger(String key) {
        String value = getString(key);
        if (StringUtils.isEmpty(value)) {
            return null;
        }
        return Integer.parseInt(value);
    }

    /**
     * 处理金额参数（元转分）
     */
    protected Long getRequiredAmountL(String key) {
        String amount = getString(key);
        if (StringUtils.isEmpty(amount)) {
            throw new BizException(BizCode.PARAM_ERROR, "金额不能为空");
        }
        return new BigDecimal(amount).multiply(new BigDecimal("100")).longValue();
    }
}
```

## 品牌上下文配置

```java
/**
 * 品牌上下文
 */
public class PlatformContext {

    private static final ThreadLocal<String> PLATFORM = new ThreadLocal<>();

    public static void setPlatform(String platform) {
        PLATFORM.set(platform);
    }

    public static String getPlatform() {
        return PLATFORM.get();
    }

    public static void clear() {
        PLATFORM.remove();
    }
}

/**
 * 平台拦截器
 */
@Component
public class PlatformInterceptor implements HandlerInterceptor {

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) {
        String host = request.getServerName();

        // 根据域名判断品牌
        if (host.contains("724pay")) {
            PlatformContext.setPlatform(PlatformConstants.PLATFORM_724PAY);
        } else if (host.contains("ezpay")) {
            PlatformContext.setPlatform(PlatformConstants.PLATFORM_EZPAY);
        } else {
            PlatformContext.setPlatform(PlatformConstants.PLATFORM_DEFAULT);
        }

        return true;
    }

    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) {
        PlatformContext.clear();
    }
}
```

## Dubbo 配置

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

## Spring Security 配置

```java
@Configuration
@EnableWebSecurity
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {

    @Autowired
    private JwtAuthenticationTokenFilter jwtAuthenticationTokenFilter;

    @Autowired
    private JwtAuthenticationEntryPoint jwtAuthenticationEntryPoint;

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.csrf().disable()
            .exceptionHandling().authenticationEntryPoint(jwtAuthenticationEntryPoint)
            .and()
            .sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            .and()
            .authorizeRequests()
                .antMatchers("/api/auth/**").permitAll()
                .antMatchers("/api/google_auth/**").permitAll()
                .antMatchers("/x_agent/**").permitAll()
                .antMatchers("/html/**").permitAll()
                .antMatchers("/actuator/**").permitAll()
                .anyRequest().authenticated();

        http.addFilterBefore(jwtAuthenticationTokenFilter, UsernamePasswordAuthenticationFilter.class);
    }
}
```

## RPC 服务调用示例

```java
@Service
public class RpcCommonService {

    @DubboReference(timeout = 10000, retries = 2, check = false)
    private IMchInfoService rpcMchInfoService;

    @DubboReference(timeout = 10000, retries = 2, check = false)
    private IAgentInfoService rpcAgentInfoService;

    @DubboReference(timeout = 10000, retries = 2, check = false)
    private IPayOrderService rpcPayOrderService;

    // getter 方法
    public IMchInfoService getRpcMchInfoService() {
        return rpcMchInfoService;
    }

    public IAgentInfoService getRpcAgentInfoService() {
        return rpcAgentInfoService;
    }

    public IPayOrderService getRpcPayOrderService() {
        return rpcPayOrderService;
    }
}
```

## 前端资源路由配置

```java
@Configuration
public class WebMvcConfig implements WebMvcConfigurer {

    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        // 品牌化静态资源
        registry.addResourceHandler("/x_agent/**")
                .addResourceLocations("classpath:/static/724pay/x_agent/")
                .addResourceLocations("classpath:/static/ezpay/x_agent/")
                .resourceChain(true)
                .addResolver(new DomainResourceResolver());

        registry.addResourceHandler("/x_merchant/**")
                .addResourceLocations("classpath:/static/724pay/x_merchant/")
                .addResourceLocations("classpath:/static/ezpay/x_merchant/")
                .resourceChain(true)
                .addResolver(new DomainResourceResolver());
    }

    @Override
    public void addViewControllers(ViewControllerRegistry registry) {
        // 根路径转发到 index.html
        registry.addViewController("/")
                .setViewName("forward:/index.html");
    }
}
```

## Cookie 配置

| 模块 | Cookie 名称 | Token 有效期 |
|------|------------|-------------|
| xxpay-manage | `XxPay_Mgr_Token` | 3600 秒 (1小时) |
| xxpay-agent | `XxPay_Agent_Token` | 3600 秒 (1小时) |
| xxpay-merchant | `XxPay_Mch_Token` | 3600 秒 (1小时) |
