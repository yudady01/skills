---
name: skill-fix
description: 检测并修复技能列表管理器中的常见错误，包括插件名称不匹配、路径问题、配置错误等
argument-hint: [--auto-fix] [--dry-run] [--error-type type] [--plugin-name name]
allowed-tools: Read, Write, Edit, Bash
---

# 技能错误修复指令

## 指令用途

自动检测和修复技能生态系统中的常见错误，包括插件名称不匹配、路径问题、配置错误等。

## 参数说明

- `--auto-fix`: 自动修复可修复的问题（默认只检测）
- `--dry-run`: 预览修复操作，不实际执行
- `--error-type`: 指定修复的错误类型（name-mismatch, path-error, config-error）
- `--plugin-name`: 只修复特定插件的问题

## 支持的错误类型

### 1. 名称不匹配错误 (name-mismatch)

**常见问题**：
- marketplace.json 中的插件名称与实际目录名称不符
- 插件配置文件中的名称与目录名称不一致
- CamelCase vs kebab-case 命名不匹配

**修复策略**：
- 统一使用 kebab-case 命名规范
- 更新 marketplace.json 中的插件名称
- 同步更新插件配置文件

### 2. 路径错误 (path-error)

**常见问题**：
- 插件源路径不存在
- 相对路径配置错误
- 目录结构不完整

**修复策略**：
- 修正路径配置
- 创建缺失的目录结构
- 更新相对路径引用

### 3. 配置错误 (config-error)

**常见问题**：
- JSON 格式错误
- 必需字段缺失
- 字段值类型错误
- 版本信息不一致

**修复策略**：
- 修正 JSON 语法
- 添加缺失的必需字段
- 修正数据类型
- 统一版本号

### 4. 配置文件命名错误 (configuration)

**常见问题**：
- 使用 `plugin.json` 而非标准 `marketplace.json`
- 配置文件位置不正确
- 配置文件格式不一致

**修复策略**：
- 重命名配置文件为标准格式
- 简化配置内容为标准字段
- 创建配置文件备份

### 5. 系统设置错误 (settings)

**常见问题**：
- `~/.claude/settings.json` 中插件名称与 marketplace 不匹配
- 驼峰式 vs kebab-case 命名不一致
- 插件状态配置错误
- 缺失插件的启用状态

**修复策略**：
- 自动检测插件名称不匹配
- 统一命名规范为 kebab-case
- 修复插件状态配置
- 禁用缺失的插件

## 执行步骤

### 1. 综合错误检测阶段

1. **基础配置错误检测**：
   - 解析 marketplace.json 语法和结构
   - 验证插件配置完整性
   - 检查必需字段和数据类型

2. **系统兼容性检测**：
   - 对比插件名称与目录名称一致性
   - 检查配置文件命名规范
   - 验证插件注册状态

3. **文件结构验证**：
   - 验证插件路径存在性
   - 检查技能文件完整性
   - 识别命名规范问题

### 2. 错误分类和优先级

1. **自动修复可处理的问题**：
   - JSON 语法错误
   - 配置文件命名错误
   - 路径配置错误
   - 缺失字段补充

2. **需要手动处理的问题**：
   - 复杂的结构性问题
   - 权限相关问题
   - 依赖关系问题

### 3. 修复执行阶段（如果启用 --auto-fix）

1. **安全修复**：
   - 创建配置文件备份
   - 按优先级执行修复
   - 验证每个修复结果

2. **生成综合报告**：
   - 错误统计和分类
   - 修复结果详情
   - 后续操作建议

## 常见修复场景

### 场景1: thirdpartyPayChannel → thirdparty-pay-channel

**问题描述**：
```
✘ thirdpartyPayChannel@yudady-skills
   Plugin 'thirdpartyPayChannel' not found in marketplace 'yudady-skills'
```

**修复步骤**：
1. 检查实际目录名称：`thirdparty-pay-channel`
2. 检查 marketplace.json 配置：`thirdparty-pay-channel`
3. 识别问题：系统内部使用了错误的名称格式
4. 修复建议：重新加载插件缓存或重启系统

**修复代码示例**：
```python
def fix_name_mismatch(marketplace_path, plugin_name, actual_name):
    """修复插件名称不匹配"""
    # 读取 marketplace.json
    with open(marketplace_path, 'r') as f:
        data = json.load(f)

    # 查找并更新插件名称
    for plugin in data['plugins']:
        if plugin['name'] == plugin_name:
            plugin['name'] = actual_name
            break

    # 保存修复后的配置
    with open(marketplace_path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
```

### 场景2: 路径配置错误

**问题描述**：
```
✘ plugin-name
   Source path './nonexistent-path' does not exist
```

**修复步骤**：
1. 检查实际插件目录位置
2. 修正 marketplace.json 中的 source 字段
3. 验证修正后的路径

### 场景3: JSON 格式错误

**问题描述**：
```
✘ marketplace.json
   JSON syntax error: Expecting ',' delimiter
```

**修复步骤**：
1. 使用 JSON 解析器定位错误
2. 修正语法错误
3. 重新验证配置完整性

## 输出格式

### 检测报告（默认模式）
```
🔍 错误检测完成 - 发现 3 个问题

❌ 名称不匹配 (1):
   - thirdpartyPayChannel → thirdparty-pay-channel
     影响: 插件无法正常加载
     修复: 更新插件名称格式

⚠️ 路径错误 (1):
   - plugin-bad-path
     当前: ./wrong/path
     正确: ./plugins/plugin-bad-path
     修复: 更新 source 字段

✅ 配置错误 (1):
   - plugin-config-error
     问题: 缺少 version 字段
     修复: 添加默认版本 "1.0.0"
```

### 修复报告（--auto-fix 模式）
```
🔧 错误修复完成 - 共修复 3 个问题

✅ 名称不匹配已修复:
   - thirdpartyPayChannel → thirdparty-pay-channel
     操作: 更新 marketplace.json

✅ 路径错误已修复:
   - plugin-bad-path
     操作: source "./wrong/path" → "./plugins/plugin-bad-path"

✅ 配置错误已修复:
   - plugin-config-error
     操作: 添加 version 字段

📋 建议:
   - 重启 Claude Code 以重新加载插件
   - 运行 /plugin 命令验证修复结果
```

## 使用示例

1. **检测所有错误**：
   ```bash
   /skill-fix
   ```

2. **预览修复操作**：
   ```bash
   /skill-fix --dry-run
   ```

3. **自动修复所有错误**：
   ```bash
   /skill-fix --auto-fix
   ```

4. **修复特定类型的错误**：
   ```bash
   /skill-fix --error-type name-mismatch --auto-fix
   ```

5. **修复特定插件的问题**：
   ```bash
   /skill-fix --plugin-name thirdpartyPayChannel --auto-fix
   ```

## 安全措施

### 备份策略
- 修复前自动创建备份
- 保留修复历史记录
- 支持一键回滚

### 验证机制
- 修复后自动验证结果
- 确保不引入新错误
- 维护配置一致性

### 权限检查
- 验证文件写入权限
- 检查目录访问权限
- 确认修改安全性

## 注意事项

1. **备份重要文件**：使用 --auto-fix 前建议手动备份重要配置
2. **重启系统**：修复后需要重启 Claude Code 以重新加载插件
3. **验证结果**：修复后运行 /plugin 命令验证修复效果
4. **版本兼容性**：确保修复后的配置与系统版本兼容

## 故障排除

### 修复失败
- 检查文件权限
- 确认磁盘空间
- 验证输入参数

### 修复后问题
- 重启 Claude Code
- 清除插件缓存
- 重新验证配置

### 回滚操作
```bash
# 恢复备份文件
/skill-fix --rollback
```

## 扩展功能

### 自定义修复规则
- 支持用户定义修复规则
- 扩展错误类型检测
- 自定义修复策略

### 批量操作
- 支持批量修复同类型错误
- 并行处理多个插件
- 生成批量修复报告