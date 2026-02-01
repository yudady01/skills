# to-mp4 快速开始指南

5 分钟上手 MOV 转 MP4 视频转换器。

## 安装 FFmpeg

### macOS
```bash
brew install ffmpeg
```

### Ubuntu/Debian
```bash
sudo apt update
sudo apt install ffmpeg
```

### Windows
从 [ffmpeg.org](https://ffmpeg.org/download.html) 下载并添加到 PATH

### 验证安装
```bash
ffmpeg -version
```

## 基本使用

### 交互模式（推荐）

```bash
cd /path/to/to-mp4
python scripts/convert_to_mp4.py video.mov -i
```

系统会显示 3 个压缩方案供选择。

### 基本转换

```bash
python scripts/convert_to_mp4.py video.mov
```

## 常用命令

| 场景 | 命令 |
|------|------|
| 基本转换 | `python scripts/convert_to_mp4.py video.mov` |
| 交互模式 | `python scripts/convert_to_mp4.py video.mov -i` |
| 高质量 | `python scripts/convert_to_mp4.py video.mov -crf 18` |
| 高压缩率 | `python scripts/convert_to_mp4.py video.mov -c h265 -crf 28` |
| 4K 转 1080p | `python scripts/convert_to_mp4.py video.mov -s 1920` |
| 分析视频 | `python scripts/convert_to_mp4.py video.mov --analyze` |

## 三种预设方案

| 方案 | 编码 | 分辨率 | 压缩率 | 适用场景 |
|------|------|--------|--------|----------|
| 方案 1 | H.264 | 保持原始 | 70-85% | 通用、分享、存档 |
| 方案 2 | H.264 | 缩小一半 | 85-92% | Web 上传、移动设备 |
| 方案 3 | H.265 | 缩小一半 | 92-96% | 存储受限、极限压缩 |

## 典型效果

| 原始 | 转换方案 | 结果 |
|------|---------|------|
| 7.4MB MOV | H.264 CRF23 | 1.4MB (81% 压缩) |
| 7.4MB MOV | H.264 + 降分辨率 | 0.6MB (92% 压缩) |
| 7.4MB MOV | H.265 + 降分辨率 | 0.5MB (93% 压缩) |

## 下一步

- 查看 [README.md](../README.md) 了解详细功能
- 查看 [USAGE_EXAMPLES.md](./USAGE_EXAMPLES.md) 获取更多示例
