---
name: to-mp4
description: MOV 视频转换为 MP4 格式并进行压缩。当用户要求转换 .mov 文件为 .mp4、压缩视频文件、或减小视频体积时使用此技能。支持 H.264 和 H.265 编码、可调节画质（CRF）、分辨率调整、音频压缩等选项。
---

# MOV 转 MP4 视频转换器

将 MOV 视频转换为 MP4 格式并进行智能压缩，显著减小文件体积的同时保持良好画质。

## 快速开始

最简单的使用方式：

```bash
python scripts/convert_to_mp4.py input.mov
```

这会使用默认设置（H.264 + CRF 23）将视频转换为 MP4，**输出文件默认为 `small/input.mp4`**（在输入文件同目录下的 `small/` 文件夹中）。

## 基本选项

### 指定输出文件

**默认行为**：输出文件会保存在输入文件同目录下的 `small/` 文件夹中。

使用 `-o` 或 `--output` 指定自定义输出路径：

```bash
# 指定输出文件名（仍在 small/ 文件夹中）
python scripts/convert_to_mp4.py input.mov -o small/output.mp4

# 指定完整输出路径
python scripts/convert_to_mp4.py input.mov -o /path/to/output.mp4
```

### 选择编码格式

使用 `-c` 或 `--codec` 指定视频编码：

- `h264`（默认）：最佳兼容性，适合大多数场景
- `h265`：更高压缩率，适合存储和 Apple 设备

```bash
# 使用 H.265 编码
python scripts/convert_to_mp4.py input.mov -c h265
```

## 画质控制

### CRF 值设置

使用 `-crf` 或 `--quality` 控制画质/体积平衡：

- `18`：接近无损，体积较大
- `20-23`：推荐范围，画质与体积平衡
- `26`：体积较小，画质明显下降
- `28+`：极限压缩，不推荐常规使用

```bash
# 高质量模式（CRF 18）
python scripts/convert_to_mp4.py input.mov -crf 18

# 标准质量（默认 CRF 23）
python scripts/convert_to_mp4.py input.mov -crf 23

# 高压缩率（CRF 28）
python scripts/convert_to_mp4.py input.mov -crf 28
```

### 编码速度

使用 `-p` 或 `--preset` 控制编码速度/效率：

- `ultrafast`：最快，压缩率最低
- `fast`：较快，日常使用推荐
- `slow`（默认）：较慢，压缩率较好
- `veryslow`：最慢，最佳压缩率

```bash
# 快速编码
python scripts/convert_to_mp4.py input.mov -p fast

# 最佳压缩率
python scripts/convert_to_mp4.py input.mov -p veryslow
```

## 分辨率调整

### 自动缩放

使用 `-s` 或 `--scale` 调整分辨率：

```bash
# 缩放到 1080p
python scripts/convert_to_mp4.py input.mov -s 1920

# 缩放到 720p
python scripts/convert_to_mp4.py input.mov -s 1280

# 缩放到 480p
python scripts/convert_to_mp4.py input.mov -s 854
```

### 保持宽高比

缩放时会自动保持视频的原始宽高比，`-2` 参数确保高度为偶数（编码器要求）。

## 音频设置

### 音频编码

使用 `-ac` 或 `--audio-codec` 指定音频编码：

- `aac`（默认）：最佳兼容性
- `libmp3lame`：MP3 格式
- `copy`：复制原始音频流（不重新编码）

```bash
# 使用 MP3 音频
python scripts/convert_to_mp4.py input.mov -ac libmp3lame

# 复制原始音频
python scripts/convert_to_mp4.py input.mov -ac copy
```

### 音频比特率

使用 `-ab` 或 `--audio-bitrate` 控制音频比特率：

```bash
# 高质量音频（192k）
python scripts/convert_to_mp4.py input.mov -ab 192k

# 标准音频（128k，默认）
python scripts/convert_to_mp4.py input.mov -ab 128k

# 低比特率音频（96k）
python scripts/convert_to_mp4.py input.mov -ab 96k
```

## 预设方案

### 通用方案（推荐）

适合大多数使用场景，兼容性好：

```bash
python scripts/convert_to_mp4.py input.mov -c h264 -crf 23 -p slow
```

### Web 分享方案

适合上传到网站或在线播放：

```bash
python scripts/convert_to_mp4.py input.mov -c h264 -crf 23 -p slow --faststart
```

### 高压缩率方案

使用 H.265 编码，体积减少 30-50%：

```bash
python scripts/convert_to_mp4.py input.mov -c h265 -crf 28 -p slow
```

### 4K 降分辨率方案

将 4K 视频缩小到 1080p：

```bash
python scripts/convert_to_mp4.py input.mov -s 1920 -crf 23
```

### 快速预览方案

快速生成预览版本：

```bash
python scripts/convert_to_mp4.py input.mov -p fast -crf 26 -s 1280
```

## 高级选项

### Web 优化

使用 `--faststart` 启用 Web 优化，允许视频边下载边播放：

```bash
python scripts/convert_to_mp4.py input.mov --faststart
```

### 显示详细信息

使用 `-v` 或 `--verbose` 显示转换过程中的详细信息：

```bash
python scripts/convert_to_mp4.py input.mov -v
```

### 仅分析不转换

使用 `--analyze` 仅显示视频信息，不执行转换：

```bash
python scripts/convert_to_mp4.py input.mov --analyze
```

## 完整示例

### 示例 1：标准转换

将视频转换为 MP4，使用默认设置：

```bash
python scripts/convert_to_mp4.py video.mov
```

### 示例 2：高质量转换

保持高画质，使用 H.264 编码：

```bash
python scripts/convert_to_mp4.py video.mov -crf 18 -p slow -o video_hq.mp4
```

### 示例 3：极限压缩

使用 H.265 编码，最大化压缩率：

```bash
python scripts/convert_to_mp4.py video.mov -c h265 -crf 28 -p veryslow -o video_small.mp4
```

### 示例 4：4K 转 1080p

将 4K 视频缩小到 1080p 并压缩：

```bash
python scripts/convert_to_mp4.py video_4k.mov -s 1920 -crf 23 -o video_1080p.mp4
```

### 示例 5：Web 优化视频

优化视频用于在线播放：

```bash
python scripts/convert_to_mp4.py video.mov --faststart -crf 23 -ab 128k -o video_web.mp4
```

## 工作原理

此技能使用 FFmpeg 进行视频转换和压缩：

- **自动检测 FFmpeg**：脚本会检查 FFmpeg 是否已安装
- **智能参数配置**：根据选项自动构建 FFmpeg 命令
- **进度显示**：显示转换进度和预估时间
- **错误处理**：提供清晰的错误信息和解决建议

## 参数对照表

### 视频编码（codec）

| 编码 | 兼容性 | 压缩率 | 编码速度 | 适用场景 |
|------|--------|--------|----------|----------|
| H.264 | 极好 | 中等 | 快 | 通用、Web、兼容性要求高 |
| H.265 | 较好 | 高 | 慢 | 存储、Apple 设备、高压缩需求 |

### CRF 值（quality）

| CRF | H.264 画质 | H.265 画质 | 文件大小 |
|-----|-----------|-----------|----------|
| 18 | 接近无损 | 接近无损 | 大 |
| 20-23 | 优秀 | 优秀 | 中等 |
| 26 | 良好 | 优秀 | 小 |
| 28+ | 一般 | 良好 | 很小 |

### 编码速度（preset）

| Preset | 编码时间 | 压缩率 | 适用场景 |
|--------|----------|--------|----------|
| ultrafast | 很短 | 差 | 快速预览 |
| fast | 短 | 较差 | 日常使用 |
| slow | 长 | 好 | 推荐 |
| veryslow | 很长 | 最佳 | 存储优化 |

## 常见问题

### Q: 如何选择 CRF 值？

A: 从 CRF 23 开始，如果文件太大或画质不够好，逐步调整：
- 文件太大：增加 CRF（如 26、28）
- 画质不够：降低 CRF（如 20、18）

### Q: H.264 和 H.265 如何选择？

A:
- **选择 H.264**：需要最佳兼容性、Web 使用、跨平台分享
- **选择 H.265**：存储空间有限、Apple 设备、不介意兼容性

### Q: 如何平衡速度和质量？

A:
- **快速预览**：`-p fast -crf 26`
- **日常使用**：`-p slow -crf 23`（默认）
- **最佳质量**：`-p veryslow -crf 18`

### Q: 音频比特率如何选择？

A:
- **音乐/高质量**：192k 或更高
- **标准音质**：128k（默认）
- **语音/低质量**：96k 或更低

### Q: 转换时间很长怎么办？

A:
- 使用更快的 preset：`-p fast` 或 `-p ultrafast`
- 降低 CRF 值（略微牺牲压缩率）
- 考虑分辨率缩放：`-s 1920` 或 `-s 1280`

## 重要说明

### 默认输出位置
- **单文件转换**：默认输出到 `输入文件同目录/small/文件名.mp4`
- **批量转换**：默认输出到 `输入目录/small/文件名.mp4`
- 使用 `-o` 参数可指定自定义输出路径

### 其他说明
- 转换过程会显示实时进度条和预估完成时间
- H.265 编码需要较长时间，但压缩率更高
- Web 优化（`--faststart`）不会影响画质，仅影响播放加载速度
- 脚本会自动处理 FFmpeg 的安装检查
- `small/` 文件夹会自动创建，无需手动创建

## 环境要求

### FFmpeg 安装

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows:**
从 [FFmpeg 官网](https://ffmpeg.org/download.html) 下载并添加到 PATH

### 验证安装

```bash
ffmpeg -version
```

## 预期效果

典型转换效果参考：

| 原始文件 | 编码 | 分辨率 | 转换后方案 | 文件大小 | 压缩率 |
|---------|------|--------|-----------|----------|--------|
| 2GB MOV | ProRes | 4K | H.264 CRF23 | ~300MB | 85% |
| 2GB MOV | ProRes | 4K | H.264 CRF23 1080p | ~150MB | 92.5% |
| 2GB MOV | ProRes | 4K | H.265 CRF28 | ~200MB | 90% |
