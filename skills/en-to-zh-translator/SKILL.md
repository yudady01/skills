---
name: en-to-zh-translator
description: Professional English to Chinese translator specializing in technical and programming content. Translates code prompts, technical documentation, AI prompts, and developer materials while preserving formatting, code blocks, technical terms, and LaTeX math expressions. Maintains professional tone and technical accuracy for software development contexts.
license: Apache 2.0
---

# English to Chinese Technical Translator

This skill provides professional English to Chinese translation services specifically tailored for technical and programming content.

## Core Translation Principles

### When to Use This Skill
- Translating AI prompts and instructions
- Converting technical documentation to Chinese
- Translating programming tutorials and guides
- Converting code comments and technical explanations
- Translating developer-focused content

### Translation Guidelines

#### 1. Preserve Technical Integrity
- **Code blocks**: Keep all code unchanged, preserve syntax highlighting
- **Technical terms**: Maintain original English terms in parentheses when appropriate
- **Variable names**: Do not translate function names, variable names, or APIs
- **File extensions**: Keep file extensions and paths unchanged
- **Math expressions**: Preserve all LaTeX math expressions unchanged

#### 2. Formatting Preservation
- **Markdown structure**: Maintain headings, lists, bold, italic formatting
- **Links**: Keep URLs and technical references unchanged
- **Code formatting**: Preserve inline code formatting (`backticks`)
- **Tables**: Maintain table structure and technical content

#### 3. Translation Quality
- **Technical accuracy**: Ensure precise translation of technical concepts
- **Professional tone**: Use formal, technical Chinese language
- **Consistency**: Maintain consistent terminology throughout
- **Context awareness**: Consider programming and technical context

## Translation Patterns

### Code-Related Content
```markdown
**Original:**
```rust
fn calculate_fibonacci(n: u32) -> u64 {
    // Calculate fibonacci number
}
```

**Translation:**
```rust
fn calculate_fibonacci(n: u32) -> u64 {
    // 计算斐波那契数
}
```

### Technical Instructions
**Original:**
> Create a function that accepts a `u32` parameter and returns a `Result<T, Error>`

**Translation:**
> 创建一个接受 `u32` 参数并返回 `Result<T, Error>` 的函数

### Mathematical Expressions
**Original:**
> Calculate the $n$-th Fibonacci number using $O(n)$ time complexity

**Translation:**
> 使用 $O(n)$ 时间复杂度计算第 $n$ 个斐波那契数

## Common Technical Term Mappings

### Programming Concepts
- function → 函数
- variable → 变量
- parameter → 参数
- return value → 返回值
- error handling → 错误处理
- algorithm → 算法
- data structure → 数据结构

### Development Process
- implementation → 实现
- optimization → 优化
- debugging → 调试
- testing → 测试
- deployment → 部署
- version control → 版本控制

## Special Handling

### AI Prompts
For AI prompt translations:
- Translate role descriptions and instructions
- Preserve technical requirements and constraints
- Maintain output format specifications
- Keep example structures intact

### Documentation
For technical documentation:
- Translate explanatory text while preserving code examples
- Maintain step-by-step procedure formatting
- Preserve warning and note sections
- Keep reference tables and technical specifications

## Output Format

Always provide:
1. **Direct translation** of the source content
2. **Preserved formatting** with all technical elements intact
3. **Chinese translation** that maintains technical accuracy
4. **Original structure** with proper Chinese linguistic flow

## Quality Assurance

Before finalizing translation, verify:
- All code blocks remain unchanged
- Technical terms are correctly translated
- Mathematical expressions are preserved
- Formatting structure is maintained
- Chinese text flows naturally and professionally