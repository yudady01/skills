# to-mp4 Scripts

这个目录包含 to-mp4 skill 的所有可执行脚本。

## 可用脚本

### convert_to_mp4.py

主转换脚本，用于将 MOV 视频转换为 MP4 格式。

**基本用法：**
```bash
python convert_to_mp4.py video.mov
```

**主要功能：**
- MOV → MP4 格式转换
- 支持 H.264 和 H.265 编码
- 可调节画质（CRF 18-28）
- 分辨率调整
- 音频优化
- Web 优化（faststart）

**常用选项：**
- `-o OUTPUT`: 指定输出文件
- `-c {h264,h265}`: 选择视频编码
- `-crf VALUE`: 设置画质（18-28）
- `-p PRESET`: 编码速度（ultrafast/fast/slow/veryslow）
- `-s WIDTH`: 缩放到指定宽度
- `-ac CODEC`: 音频编码（aac/libmp3lame/copy）
- `-ab BITRATE`: 音频比特率
- `--faststart`: Web 优化
- `--analyze`: 仅分析视频信息

**查看完整帮助：**
```bash
python convert_to_mp4.py --help
```

### test_skill.py

测试脚本，用于验证 skill 是否正常工作。

**用法：**
```bash
python test_skill.py
```

**测试项目：**
1. FFmpeg 安装检查
2. 转换脚本存在性
3. 脚本帮助功能
4. 文档文件完整性

## 使用示例

### 基本转换
```bash
python convert_to_mp4.py video.mov
```

### 高质量转换
```bash
python convert_to_mp4.py video.mov -crf 18 -p slow
```

### 高压缩率（H.265）
```bash
python convert_to_mp4.py video.mov -c h265 -crf 28
```

### 4K 转 1080p
```bash
python convert_to_mp4.py video.mov -s 1920
```

### Web 优化
```bash
python convert_to_mp4.py video.mov --faststart
```

### 分析视频
```bash
python convert_to_mp4.py video.mov --analyze
```

## 依赖项

- Python 3.6+
- FFmpeg 4.0+

## 安装 FFmpeg

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt install ffmpeg
```

**Windows:**
从 [FFmpeg 官网](https://ffmpeg.org/download.html) 下载并添加到 PATH

## 文档

完整文档请参考上级目录：
- [SKILL.md](../SKILL.md) - Skill 定义
- [README.md](../README.md) - 完整文档
- [QUICKSTART.md](../QUICKSTART.md) - 快速开始
- [USAGE_EXAMPLES.md](../USAGE_EXAMPLES.md) - 使用示例
- [PROJECT.md](../PROJECT.md) - 项目概述

## 故障排查

### FFmpeg 未找到
```
❌ 错误: 未找到 FFmpeg
```
**解决方法：** 安装 FFmpeg（见上方说明）

### 转换时间过长
**解决方法：**
```bash
python convert_to_mp4.py video.mov -p fast
```

### 文件太大
**解决方法：**
```bash
python convert_to_mp4.py video.mov -c h265 -crf 28 -s 1920
```

## 许可证

MIT License
