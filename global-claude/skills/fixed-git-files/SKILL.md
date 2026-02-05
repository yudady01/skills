---
name: local:fixed-git-files
description: 自动查找当前文件夹下的所有文本文件并转换换行符为 LF（Unix 格式）。排除 .git 文件夹，使用 sed 命令将所有 CRLF（Windows）转换为 LF。
---

# Git 文件换行符修复

此技能自动将文件夹下的所有文件转换为 LF 格式（Unix 换行符），确保 Git 仓库中的换行符一致性。

## 何时使用此技能

- 当你从 Windows 系统克隆或获取代码后
- 当 Git 显示换行符警告（CRLF/LF 混合）时
- 当需要统一项目换行符为 Unix 格式时
- 当你提交代码前希望确保换行符一致性时

## 使用方法

### 基本使用

直接使用脚本处理当前目录：

```bash
scripts/convert-to-lf.sh
```

### 处理指定目录

```bash
# 在目标目录中运行
cd /path/to/your/project
scripts/convert-to-lf.sh
```

## 工作原理

脚本执行以下操作：

1. **排除 .git 文件夹**：避免修改 Git 内部文件
2. **递归查找所有文件**：遍历当前目录及其子目录
3. **转换换行符**：将所有 CRLF（`\r\n`）转换为 LF（`\n`）
4. **保留二进制文件**：sed 只处理文本文件

### 核心命令

```bash
find . -type d -name ".git" -prune -o -type f -print0 | xargs -0 sed -i 's/\r$//'
```

**命令解析：**
- `find . -type d -name ".git" -prune`：查找并排除 .git 目录
- `-o -type f -print0`：输出所有文件名（以 null 分隔）
- `xargs -0`：处理 null 分隔的文件名
- `sed -i 's/\r$//'`：移除行尾的回车符（CR）

## 输出示例

```
正在将所有文件转换为 LF 格式...
[处理文件: src/main.ts]
[处理文件: src/utils.ts]
[处理文件: README.md]
转换完成！
```

## 注意事项

- 此脚本会**就地修改文件**
- 建议在执行前提交或备份代码
- 仅转换文本文件，二进制文件不会被损坏
- Git 配置 `core.autocrlf` 可能影响此操作的效果

## Git 配置建议

确保正确的 Git 换行符配置：

```bash
# macOS/Linux 推荐
git config --global core.autocrlf input

# Windows 推荐
git config --global core.autocrlf true

# 添加 .gitattributes
echo "* text=auto eol=lf" >> .gitattributes
```
