# MOV 转 MP4 视频转换器

将 MOV 视频转换为 MP4 格式并进行智能压缩，显著减小文件体积的同时保持良好画质。

## 功能特性

- **格式转换**: MOV → MP4
- **智能压缩**: 支持 H.264 和 H.265 编码
- **画质控制**: 可调节 CRF 值（18-28）
- **分辨率调整**: 自动缩放并保持宽高比
- **音频优化**: 支持多种音频编码和比特率
- **Web 优化**: 支持快速开始播放
- **视频分析**: 查看视频详细信息

## 快速开始

### 1. 安装 FFmpeg

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

### 2. 验证安装

```bash
ffmpeg -version
```

### 3. 转换视频

最简单的使用方式：

```bash
python scripts/convert_to_mp4.py video.mov
```

## 使用示例

### 基本转换

使用默认设置（H.264 + CRF 23）：

```bash
python scripts/convert_to_mp4.py video.mov
```

### 指定输出文件

```bash
python scripts/convert_to_mp4.py video.mov -o output.mp4
```

### 高质量转换

```bash
python scripts/convert_to_mp4.py video.mov -crf 18 -p slow
```

### 高压缩率（H.265）

```bash
python scripts/convert_to_mp4.py video.mov -c h265 -crf 28
```

### 4K 转 1080p

```bash
python scripts/convert_to_mp4.py video_4k.mov -s 1920
```

### Web 优化

```bash
python scripts/convert_to_mp4.py video.mov --faststart
```

### 分析视频信息

```bash
python scripts/convert_to_mp4.py video.mov --analyze
```

## 命令行选项

### 基本选项

| 选项 | 说明 | 默认值 |
|------|------|--------|
| `input` | 输入 MOV 文件路径 | - |
| `-o, --output` | 输出 MP4 文件路径 | 输入文件名.mp4 |

### 视频设置

| 选项 | 说明 | 可选值 | 默认值 |
|------|------|--------|--------|
| `-c, --codec` | 视频编码 | h264, h265 | h264 |
| `-crf, --quality` | 画质 CRF 值 | 18-28 | 23 |
| `-p, --preset` | 编码速度 | ultrafast, fast, slow, veryslow | slow |
| `-s, --scale` | 缩放到指定宽度 | 任意正整数 | 不缩放 |

### 音频设置

| 选项 | 说明 | 可选值 | 默认值 |
|------|------|--------|--------|
| `-ac, --audio-codec` | 音频编码 | aac, libmp3lame, copy | aac |
| `-ab, --audio-bitrate` | 音频比特率 | 如 128k, 192k | 128k |

### 其他选项

| 选项 | 说明 |
|------|------|
| `--faststart` | 启用 Web 优化（快速开始播放） |
| `-v, --verbose` | 显示详细转换信息 |
| `--analyze` | 仅分析视频信息，不执行转换 |

## 参数说明

### CRF 值（画质控制）

| CRF 值 | 效果 |
|--------|------|
| 18 | 接近无损，体积较大 |
| 20-23 | 推荐（画质/体积平衡） |
| 26 | 体积小，画质明显下降 |
| 28+ | 极限压缩，不推荐常规使用 |

### 编码速度（Preset）

| Preset | 编码时间 | 压缩率 | 适用场景 |
|--------|----------|--------|----------|
| ultrafast | 很短 | 差 | 快速预览 |
| fast | 短 | 较差 | 日常使用 |
| slow | 长 | 好 | 推荐 |
| veryslow | 很长 | 最佳 | 存储优化 |

### 视频编码

| 编码 | 兼容性 | 压缩率 | 编码速度 | 适用场景 |
|------|--------|--------|----------|----------|
| H.264 | 极好 | 中等 | 快 | 通用、Web、兼容性要求高 |
| H.265 | 较好 | 高 | 慢 | 存储、Apple 设备、高压缩需求 |

## 预设方案

### 通用方案（推荐）

适合大多数使用场景，兼容性好：

```bash
python scripts/convert_to_mp4.py video.mov -c h264 -crf 23 -p slow
```

### Web 分享方案

适合上传到网站或在线播放：

```bash
python scripts/convert_to_mp4.py video.mov -c h264 -crf 23 -p slow --faststart
```

### 高压缩率方案

使用 H.265 编码，体积减少 30-50%：

```bash
python scripts/convert_to_mp4.py video.mov -c h265 -crf 28 -p slow
```

### 4K 降分辨率方案

将 4K 视频缩小到 1080p：

```bash
python scripts/convert_to_mp4.py video.mov -s 1920 -crf 23
```

### 快速预览方案

快速生成预览版本：

```bash
python scripts/convert_to_mp4.py video.mov -p fast -crf 26 -s 1280
```

## 典型效果

| 原始文件 | 编码 | 分辨率 | 转换方案 | 文件大小 | 压缩率 |
|---------|------|--------|----------|----------|--------|
| 2GB MOV | ProRes | 4K | H.264 CRF23 | ~300MB | 85% |
| 2GB MOV | ProRes | 4K | H.264 CRF23 1080p | ~150MB | 92.5% |
| 2GB MOV | ProRes | 4K | H.265 CRF28 | ~200MB | 90% |

## 常见问题

### Q: 如何选择 CRF 值？

A: 从 CRF 23 开始，根据结果调整：
- 文件太大：增加 CRF（如 26、28）
- 画质不够：降低 CRF（如 20、18）

### Q: H.264 和 H.265 如何选择？

A:
- **选择 H.264**：需要最佳兼容性、Web 使用、跨平台分享
- **选择 H.265**：存储空间有限、Apple 设备、不介意兼容性

### Q: 转换时间很长怎么办？

A:
- 使用更快的 preset：`-p fast` 或 `-p ultrafast`
- 考虑分辨率缩放：`-s 1920` 或 `-s 1280`

### Q: 音频比特率如何选择？

A:
- **音乐/高质量**：192k 或更高
- **标准音质**：128k（默认）
- **语音/低质量**：96k 或更低

## 技术细节

### FFmpeg 参数说明

**H.264 基本命令：**
```bash
ffmpeg -i input.mov \
  -c:v libx264 \
  -preset slow \
  -crf 23 \
  -pix_fmt yuv420p \
  -movflags +faststart \
  -c:a aac \
  -b:a 128k \
  output.mp4
```

**参数解释：**
- `libx264`: H.264 视频编码器
- `-preset slow`: 用编码时间换压缩率
- `-crf 23`: 恒定质量模式（18-28）
- `yuv420p`: 像素格式，确保兼容性
- `faststart`: Web 优化，支持流式播放
- `aac`: 音频编码器
- `-b:a 128k`: 音频比特率

**H.265 命令：**
```bash
ffmpeg -i input.mov \
  -c:v libx265 \
  -preset slow \
  -crf 28 \
  -tag:v hvc1 \
  -c:a aac \
  -b:a 128k \
  output.mp4
```

**分辨率缩放：**
```bash
-vf "scale=1920:-2"  # 宽度 1920，高度自动计算，-2 确保偶数
```

## 文件结构

```
to-mp4/
├── SKILL.md              # Skill 定义文件
├── README.md             # 使用文档
└── scripts/
    └── convert_to_mp4.py # 转换脚本
```

## 依赖项

- Python 3.6+
- FFmpeg 4.0+

## 许可证

MIT License
