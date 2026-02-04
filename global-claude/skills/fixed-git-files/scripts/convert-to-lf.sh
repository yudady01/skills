#!/bin/bash
# 自动查找当前文件夹下的所有文本文件并转换换行符为 LF

echo "正在将所有文件转换为 LF 格式..."

# 使用 find 排除 .git 文件夹，并调用 dos2unix 进行转换
# 如果没有 dos2unix，可以使用 sed
find . -type d -name ".git" -prune -o -type f -print0 | xargs -0 sed -i '' 's/\r$//'

echo "转换完成！"
