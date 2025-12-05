---
name: skill-validate
description: 验证技能配置和内容质量，检查文件结构、frontmatter 格式和最佳实践
argument-hint: [--plugin-name name] [--all] [--strict] [--fix]
allowed-tools: Read, Write, Bash
---

# 技能验证指令

## 指令用途

验证技能的配置正确性和内容质量，确保技能符合 Claude Code 插件标准和最佳实践。

## 参数说明

- `--plugin-name`: 验证特定插件/技能名称
- `--all`: 验证所有发现的技能
- `--strict`: 启用严格模式，检查更多细节
- `--fix`: 尝试自动修复可修复的问题

## 验证标准

### 基础验证（默认模式）

**文件结构检查**：
- [ ] 技能目录存在
- [ ] SKILL.md 文件存在
- [ ] 目录命名符合 kebab-case 规范
- [ ] 必需的子目录存在（如需要）

**Frontmatter 验证**：
- [ ] YAML 格式正确
- [ ] name 字段存在且非空
- [ ] description 字段存在且非空
- [ ] description 使用第三人称表述
- [ ] 包含具体的触发短语

**内容验证**：
- [ ] Markdown 语法正确
- [ ] 标题层级合理
- [ ] 内容长度适中（1500-2000 词）
- [ ] 使用祈使/不定式形式

### 严格验证（--strict）

**质量检查**：
- [ ] 描述包含具体触发短语
- [ ] 避免模糊或通用描述
- [ ] 内容结构符合渐进式披露
- [ ] 正确引用 supporting 文件

**最佳实践验证**：
- [ ] 使用 CLAUDE_PLUGIN_ROOT 环境变量
- [ ] 避免硬编码绝对路径
- [ ] 命名约定符合标准
- [ ] 包含工作示例

**安全性检查**：
- [ ] 不包含敏感信息
- [ ] 路径引用安全
- [ ] 脚本权限正确

## 执行步骤

1. **确定验证范围**：
   - 如果指定 --plugin-name，只验证特定技能
   - 如果指定 --all，验证所有技能
   - 否则，提示用户指定验证目标

2. **扫描技能目录**：
   - 读取 marketplace.json 获取插件列表
   - 扫描每个插件的 skills/ 目录
   - 收集所有 SKILL.md 文件路径

3. **执行验证检查**：
   - 读取 SKILL.md 文件内容
   - 解析 YAML frontmatter
   - 验证文件结构和内容
   - 应用标准验证规则
   - 如果启用 --strict，执行额外检查

4. **生成验证报告**：
   - 汇总验证结果
   - 分类显示问题和建议
   - 提供修复指导
   - 如果启用 --fix，尝试自动修复

## 输出格式

### 成功报告
```
✅ 验证完成 - 共检查 3 个技能

✅ thirdparty-pay-channel:skills
   - 结构完整
   - frontmatter 正确
   - 内容质量良好

✅ repeatable-sql:skills
   - 结构完整
   - frontmatter 正确
   - 内容质量良好

⚠️  en-to-zh-translator:skills
   - 结构完整
   - frontmatter 正确
   - 建议：添加更多使用示例
```

### 错误报告
```
❌ 验证发现问题 - 共检查 2 个技能

❌ broken-skill
   - SKILL.md 文件不存在
   - 技能目录缺失
   - 建议：检查插件安装完整性

⚠️  incomplete-skill
   - description 字段为空
   - 缺少触发短语
   - 建议：更新 frontmatter 描述
```

## 自动修复（--fix）

支持自动修复的问题：

- **空字段**：添加默认值
- **格式错误**：修正 YAML 语法
- **路径问题**：转换为相对路径
- **命名规范**：修正目录名称
- **权限问题**：设置正确权限

无法自动修复的问题会提供详细的修复指导。

## 使用示例

1. **验证所有技能**：
   ```bash
   /skill-validate --all
   ```

2. **严格验证特定技能**：
   ```bash
   /skill-validate --plugin-name repeatable-sql --strict
   ```

3. **验证并自动修复**：
   ```bash
   /skill-validate --all --fix
   ```

4. **生成详细报告**：
   ```bash
   /skill-validate --all --strict --format json > validation-report.json
   ```

## 返回代码

- `0`: 所有验证通过
- `1`: 发现警告但可继续使用
- `2`: 发现错误需要修复
- `3`: 发生系统错误

## 注意事项

1. **备份重要文件**：使用 --fix 前建议备份重要技能文件
2. **权限要求**：确保有足够权限读取和修改技能文件
3. **网络依赖**：某些验证可能需要访问外部资源
4. **性能考虑**：验证大量技能可能需要较长时间

## 故障排除

**常见问题**：
- 权限不足：使用 sudo 或修改文件权限
- 文件被占用：关闭其他程序对文件的访问
- 路径问题：使用绝对路径或检查工作目录
- 编码问题：确保文件使用 UTF-8 编码

**调试模式**：
```bash
/skill-validate --all --strict --debug
```