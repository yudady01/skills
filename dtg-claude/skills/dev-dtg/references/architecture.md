# DTG-Pay 架构指南

## 代码架构

### 分层结构

```
Controller (ctrl/) → Service (service/) → Channel (channel/)
     ↓                   ↓                    ↓
REST API           业务逻辑          第三方支付通道适配器
```

### 核心接口和抽象类

| 类名 | 用途 |
|------|------|
| `BaseController` | 所有 Controller 的基类 |
| `BasePayNotify` | 支付回调通知的抽象基类 |
| `BasePayment` | 支付下单的抽象基类 |
| `BaseService` | 通道服务的基类 |
| `PaymentInterface` | 支付通道接口定义 |
| `TransNotifyInterface` | 代付通知接口定义 |

## 支付通道实现模式

```
channel/{channel_name}/
├── {ChannelName}Config.java        # 配置类
├── {ChannelName}DepositChannel.java # 支付通道（继承 BasePayment）
├── {ChannelName}PaymentService.java # 支付服务
├── {ChannelName}TransNotifyService.java # 代付通知服务
├── {ChannelName}SignUtils.java      # 签名工具类
└── model/                           # 请求/响应模型
```

## 支付流程

### 支付下单流程

```
1. 接收支付请求 (PayOrderController)
2. 参数验证
3. 创建支付订单
4. 调用支付通道 (BasePayment)
5. 返回支付信息
```

### 回调通知流程

```
1. 接收第三方回调 (PayNotifyController)
2. 验证回调签名
3. 查询订单状态
4. 更新订单状态
5. 发送商户通知 (ActiveMQ)
6. 返回成功响应
```

## RPC 服务调用

- 默认超时：10 秒
- 重试次数：0
- consumer 超时（30 秒）必须 >= provider 超时（60 秒）

## 架构评估

### 质量属性

| 属性 | 说明 |
|------|------|
| 正确性 | 系统功能的正确性和完整性 |
| 可靠性 | 系统在规定条件下的稳定运行能力 |
| 可用性 | 系统可正常运行时间和故障恢复能力 |
| 安全性 | 系统抵抗恶意攻击和保护数据的能力 |
| 性能 | 系统响应速度、处理能力和资源利用率 |
| 可扩展性 | 系统适应负载增长和功能扩展的能力 |

### 架构成熟度等级

| 等级 | 特征 |
|------|------|
| Level 1 | 架构设计缺乏标准化 |
| Level 2 | 有基本的架构规范，但执行不一致 |
| Level 3 | 架构流程标准化，有明确的设计模式 |
| Level 4 | 架构质量可度量，有量化指标 |
| Level 5 | 架构持续优化，自适应业务变化 |

## 反模式识别

### 分布式单体反模式
- **检测**: 服务共享数据库、大量同步通信、紧耦合
- **缓解**: 数据库拆分、异步通信改造

### 共享数据库反模式
- **检测**: 多服务访问相同表、跨服务数据依赖
- **缓解**: 数据库权限分离、API封装数据访问
