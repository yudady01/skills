# XXPay Java 代码风格规范

在编写或修改本项目 (`dtg`) 的 Java 代码时，请始终遵循以下规范：

## 1. 导入规范 (Imports)
- **禁止通配符 (Wildcard) 导入**：
  - 类导入阈值设置为 100 (`CLASS_COUNT_TO_USE_IMPORT_ON_DEMAND` = 100)，意味着除非同一包引用超过 100 个类，否则必须明确列出导入。
  - 静态导入阈值设置为 200。
  - **规则**：始终使用全名导入，不要使用 `import java.util.*;`。

- **导入布局顺序**：
  1. 所有普通包导入 (包含子包)。
  2. **两个空行**。
  3. 静态导入 (`import static ...`)。

## 2. 代码格式 (Formatting)
- **行宽 (Right Margin)**：150 字符。
- **缩进**：使用 4 个空格。
- **注释**：
  - 行注释 (`//`) 必须缩进至代码层级 (`LINE_COMMENT_AT_FIRST_COLUMN` = false)。
  - `//` 符号后必须紧跟一个空格。
- **换行**：
  - 二元操作符 (Binary Operation) 应位于**下一行**行首 (e.g., `+`, `&&` 等符号换行后在新行开头)。
  - 变量注解换行策略：Wrap if long / Always (Value 2)。

## 3. 类成员排列顺序 (Arrangement)
请严格按照以下顺序组织类内部成员：

1. **静态常量与字段 (Static Fields)**
   - 顺序：`public static final` -> `static final` -> `static`
   - 可见性顺序：Public -> Protected -> Package-Private -> Private
2. **静态初始化块 (Static Initializers)**
3. **静态方法 (Static Methods)**
   - 包含所有静态方法 (Public/Private)。
4. **实例字段 (Instance Fields)**
   - 顺序：`public final` -> `final` -> 普通字段
   - 可见性顺序：Public -> Protected -> Package-Private -> Private
5. **初始化块 (Instance Initializers)**
6. **构造函数 (Constructors)**
7. **实例方法 (Instance Methods)**
8. **内部类型 (Inner Types)**
   - Enum -> Interface -> Static Class -> Class

## 4. 其他
- XML 属性换行：不换行 (Do not wrap)。
