# Apple Style 处理指南

本指南提供详细的转换步骤和实际案例，帮助将任何内容转换为符合 Apple 官网风格的 Obsidian 笔记。

## 四步工作流详解

### Step 1: Clean（清理）

#### 目标

移除所有格式噪音，创建干净的文本基础。

#### 具体操作

**1. 移除多余空行**

```markdown
Before:
第一段内容。




第二段内容。

After:
第一段内容。

第二段内容。
```

**规则**: 元素之间保留单个空行，不要有连续的空行。

**2. 修正标点符号**

```markdown
Before:
这是第一句。这是第二句，这是第三句

After:
这是第一句。这是第二句，这是第三句。
```

**规则**:
- 句号后加空格
- 逗号后加空格
- 中文标点不需要空格

**3. 标准化引号和破折号**

```markdown
Before:
"双引号" '单引号' --破折号---

After:
"双引号" '单引号' — 破折号
```

**4. 移除 Markdown 残留**

```markdown
Before:
**加粗文本** 还有 *斜体* 还有 # 标题符号

After:
加粗文本 还有 斜体 还有 标题符号
```

**注意**: 如果格式是故意的（如强调），则保留。

**5. 清理行尾空白**

```markdown
Before:
文本内容[空格][空格][空格]

After:
文本内容
```

---

### Step 2: Structure（结构化）

#### 目标

建立清晰的三级标题层级，创建逻辑流畅的内容结构。

#### 标题识别策略

**1. 扫描内容，识别主要主题**

主要主题通常具有以下特征：
- 概括性的内容
- 包含多个子话题
- 字数较多（100字以上）
- 有独立的完整性

**转换为 H1**

**2. 识别次要主题**

次要主题特征：
- 从属于某个主要主题
- 包含 2-5 个相关点
- 字数中等（50-100字）

**转换为 H2**

**3. 识别小节**

小节特征：
- 具体的单个话题
- 字数较少（50字以下）
- 细节说明

**转换为 H3**

#### 层级平化规则

如果原始内容有超过三级的结构：

```markdown
Before:
# H1
## H2
### H3
#### H4  ← 不符合 Apple 风格
##### H5

After (方案 1 - 平化):
# H1
## H2
### H3 (原 H3 + H4 合并)

After (方案 2 - 拆分):
# H1
## H2
### H3

# 新文档 (原 H4+ 内容)
## H2
### H3
```

#### 内容组织原则

**1. 同级标题数量**

| 层级 | 建议数量 | 说明 |
|------|---------|------|
| H1 | 2-4 个 | 主要章节，不宜过多 |
| H2 | 3-6 个/H1 | 子章节，中等密度 |
| H3 | 2-5 个/H2 | 细节说明，适度使用 |

**2. 逻辑流向**

```
H1: 概论
  H2: 背景
  H2: 核心概念
    H3: 概念 A
    H3: 概念 B
  H2: 应用场景
  H2: 总结

H1: 详细指南
  H2: 准备工作
  H2: 步骤说明
  H2: 常见问题
```

**3. 章节分隔**

在主要主题切换时使用 `---`：

```markdown
## H2 最后一小节

内容结束。

---

# H1 新的主要章节

新的主题开始。
```

---

### Step 3: Enhance（增强）

#### 目标

添加 Obsidian 特有功能，提升文档的元数据管理和可读性。

#### YAML Frontmatter 构建

**最小配置**

```yaml
---
title: 文档标题
created: 2024-01-25
cssclass: apple-style
---
```

**完整配置**

```yaml
---
title: 文档标题
description: 简短描述文档内容
created: 2024-01-25
updated: 2024-01-25
tags: [tag1, tag2, tag3]
cssclass: apple-style
type: docs
status: complete
author: 作者名
category: 技术文档
---

# 文档内容开始
```

**字段提取规则**

| 字段 | 提取方式 |
|------|---------|
| `title` | 使用第一个 H1，或生成描述性标题 |
| `created` | 文档创建日期（YYYY-MM-DD） |
| `updated` | 最后修改日期 |
| `tags` | 从内容中提取关键词（3-5个） |
| `description` | 第一段或概括性语句 |

#### Callout 转换规则

**何时使用 [!abstract]**

- 核心概念定义
- 内容摘要
- 主要论点
- 设计原则

```markdown
原文：
异步编程的核心思想是不阻塞主线程。

转换后：
> [!abstract] 核心思想
> 异步编程的核心思想是不阻塞主线程，允许程序在等待耗时操作时执行其他任务。
```

**何时使用 [!note]**

- 重要提示
- 最佳实践
- 关键要点
- 使用建议

```markdown
原文：
注意：一定要在使用前检查配置。

转换后：
> [!note] 配置检查
> 使用前务必检查配置文件，确保所有必需的参数都已正确设置。
```

**何时使用 [!info]**

- 背景信息
- 补充说明
- 参考数据
- 历史信息

```markdown
原文：
这个功能是在 2.0 版本中添加的。

转换后：
> [!info] 版本历史
> 此功能于 2023 年在 2.0 版本中引入，旨在改善用户体验。
```

**何时使用 [!warning]**

- 错误警告
- 限制条件
- 常见陷阱
- 注意事项

```markdown
原文：
小心不要删除这个文件。

转换后：
> [!warning] 数据丢失风险
> 删除此文件将导致所有配置丢失，操作前请务必备份。
```

#### 其他增强

**1. 列表转换**

将普通描述性列表转换为任务列表（如果合适）：

```markdown
Before:
需要完成的任务：
1. 完成设计
2. 编写代码
3. 测试功能

After:
待完成任务：
- [ ] 完成设计
- [ ] 编写代码
- [ ] 测试功能
```

**2. 表格创建**

将结构化数据转换为表格：

```markdown
Before:
Python 版本和支持情况：
Python 3.8 支持所有功能
Python 3.9 支持大部分功能
Python 3.10 支持所有功能并优化

After:
| Python 版本 | 支持状态 | 说明 |
|-------------|---------|------|
| 3.8 | 完全支持 | 稳定版本 |
| 3.9 | 部分支持 | 部分特性不可用 |
| 3.10 | 完全支持 | 推荐版本 |
```

**3. 代码块格式化**

确保代码块有适当的语言标识：

```markdown
Before:
```
print("hello")
```

After:
```python
print("hello")
```
```

---

### Step 4: Font（字体）

#### 字体栈应用

**主要文本（正文和标题）**

```css
font-family: -apple-system, BlinkMacSystemFont,
             "SF Pro Display", "SF Pro Text",
             "PingFang SC", "Hiragino Sans GB",
             "Helvetica Neue", Arial, sans-serif;
```

**优先级**:
1. Apple 系统字体（-apple-system, SF Pro）
2. 中文字体（PingFang SC, 冬青黑）
3. 经典字体（Helvetica Neue）
4. 通用回退（Arial, sans-serif）

**代码字体**

```css
font-family: "SF Mono", "Menlo", "Monaco",
             "Consolas", "Liberation Mono", monospace;
```

**优先级**:
1. Apple 等宽字体（SF Mono）
2. macOS 等宽字体（Menlo, Monaco）
3. 跨平台等宽字体（Consolas）
4. 通用回退（monospace）

#### 字号应用

| 内容类型 | 字号 | 行高 | 说明 |
|---------|------|------|------|
| H1 | 28px | 1.4 | 主标题，醒目 |
| H2 | 21px | 1.5 | 次标题，清晰 |
| H3 | 18px | 1.6 | 小标题，适中 |
| 正文 | 16px | 1.8 | 舒适阅读 |
| 行内代码 | 14px | - | 清晰可辨 |
| 代码块 | 14px | 1.6 | 等宽显示 |

---

## 完整转换示例

### 输入：原始技术文章

```
Python 装饰器入门指南

什么是装饰器
装饰器是 Python 的一个强大功能，它允许你修改函数或类的行为。
装饰器本质上是一个函数，它接受另一个函数作为参数，并返回一个新的函数。

为什么要使用装饰器
装饰器可以让代码更简洁。你可以在不修改原函数的情况下添加功能。
常见的用途包括日志记录、性能测试、事务处理等。

如何编写装饰器
基本语法如下：
@decorator
def function():
    pass

这等同于：
def function():
    pass
function = decorator(function)

装饰器示例
以下是一个简单的装饰器例子：
def timer(func):
    import time
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"耗时: {end - start}")
    return wrapper

@timer
def slow_function():
    time.sleep(1)

slow_function()
```

### 输出：Apple 风格笔记

```markdown
---
title: Python 装饰器入门指南
created: 2024-01-25
tags: [python, decorator, programming, guide]
cssclass: apple-style
type: tutorial
level: beginner
---

# Python 装饰器入门指南

> [!abstract] 核心概念
> 装饰器是 Python 的强大功能，允许在不修改原函数的情况下动态扩展其功能。

## 什么是装饰器

装饰器本质上是一个函数，它接受另一个函数作为参数，并返回一个新的函数。这种设计模式实现了横切关注点的分离。

### 工作原理

装饰器在函数定义时被应用，可以修改函数的行为、添加前置/后置逻辑、或完全替换函数的实现。

---

## 为什么使用装饰器

> [!note] 主要优势
> 装饰器提供了优雅的方式来扩展功能，同时保持代码的简洁性和可维护性。

### 代码简洁性

避免在每个函数中重复编写相同的代码。

### 关注点分离

将核心业务逻辑与辅助功能（日志、缓存、权限检查）分离。

### 常见应用场景

- **日志记录**: 自动记录函数调用信息
- **性能测试**: 测量函数执行时间
- **事务处理**: 数据库事务管理
- **权限验证**: 检查用户权限
- **缓存机制**: 缓存函数结果

---

## 基本语法

### 装饰器应用

```python
@decorator
def function():
    pass
```

### 等价写法

```python
def function():
    pass

function = decorator(function)
```

> [!info] 语法糖
> `@` 符号只是语法糖，使代码更简洁易读。两种写法完全等价。

---

## 实战示例

### 计时装饰器

以下是一个测量函数执行时间的装饰器：

```python
import time

def timer(func):
    """计时装饰器"""
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"耗时: {end - start:.2f} 秒")
    return wrapper

@timer
def slow_function():
    """模拟耗时操作"""
    time.sleep(1)

slow_function()
# 输出: 耗时: 1.00 秒
```

---

## 最佳实践

### 装饰器设计原则

**1. 保持透明**

装饰器不应改变原函数的返回值类型和签名：

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # 保留原函数的元信息
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

**2. 支持参数**

使用 `*args` 和 `**kwargs` 确保装饰器适用于各种函数：

```python
def flexible_decorator(func):
    def wrapper(*args, **kwargs):
        # 可以访问所有参数
        return func(*args, **kwargs)
    return wrapper
```

**3. 文档完整**

为装饰器添加清晰的文档字符串：

```python
def log_calls(func):
    """
    记录函数调用的装饰器

    Args:
        func: 被装饰的函数

    Returns:
        包装后的函数
    """
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

---

## 常见问题

> [!warning] 装饰器顺序
> 当使用多个装饰器时，顺序很重要。装饰器从下往上应用。

```python
@decorator_a  # 最后应用
@decorator_b  # 先应用
def function():
    pass

# 等价于:
# function = decorator_a(decorator_b(function))
```

---

## 进阶话题

### 带参数的装饰器

```python
def repeat(times):
    """重复执行函数指定次数"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet():
    print("Hello!")

greet()
# 输出:
# Hello!
# Hello!
# Hello!
```

### 类装饰器

```python
class CountCalls:
    """计数装饰器类"""
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"调用次数: {self.count}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()  # 调用次数: 1
say_hello()  # 调用次数: 2
```

---

## 总结

> [!abstract] 关键要点
> - 装饰器是修改函数行为的强大工具
> - 使用 `@` 语法让代码更简洁
> - 遵循最佳实践确保装饰器的可维护性
> - 从简单开始，逐步掌握高级用法

**下一步学习**:
- [[Python functools 模块]]
- [[上下文管理器]]
- [[元类编程]]

---

**创建时间**: 2024-01-25
**难度**: 入门
**预计阅读时间**: 10 分钟
```

---

## 转换检查清单

使用此清单确保转换质量：

### 清理阶段

- [ ] 移除多余空行
- [ ] 修正标点符号间距
- [ ] 标准化引号和破折号
- [ ] 移除不必要的 Markdown 格式
- [ ] 清理行尾空白

### 结构阶段

- [ ] 建立三级标题层级
- [ ] 平化超过三级的内容
- [ ] 确保逻辑流向清晰
- [ ] 使用 `---` 分隔主要章节
- [ ] 检查标题数量合理

### 增强阶段

- [ ] 添加 YAML frontmatter
- [ ] 提取相关 tags
- [ ] 转换重点为 callouts
- [ ] 优化列表格式
- [ ] 创建必要的表格

### 字体阶段

- [ ] 应用系统字体栈
- [ ] 设置正确的字号
- [ ] 确保行高为 1.8
- [ ] 验证代码使用等宽字体

---

**记住**: 好的转换保持内容准确性，同时大幅提升视觉体验和可读性。
