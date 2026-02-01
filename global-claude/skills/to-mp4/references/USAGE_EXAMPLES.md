# to-mp4 使用示例

完整的使用示例和常见场景。

## 目录

- [基本用法](#基本用法)
- [交互模式](#交互模式)
- [质量控制](#质量控制)
- [分辨率调整](#分辨率调整)
- [编码选择](#编码选择)
- [高级选项](#高级选项)
- [故障排查](#故障排查)

---

## 基本用法

### 最简单的转换

使用默认设置（H.264 + CRF 23）：

```bash
python scripts/convert_to_mp4.py video.mov
```

输出：`video.mp4`

### 指定输出文件名

```bash
python scripts/convert_to_mp4.py video.mov -o output.mp4
```

### 指定输入路径

```bash
python scripts/convert_to_mp4.py /path/to/video.mov
```

---

## 交互模式

### 启动交互模式

```bash
python scripts/convert_to_mp4.py video.mov -i
```

或使用完整参数名：

```bash
python scripts/convert_to_mp4.py video.mov --interactive
```

### 交互输出示例

```
============================================================
视频分析: video.mov
============================================================

文件大小:     7.42 MB
时长:         00:00:08.95
分辨率:       4096x2648
帧率:         39.89 fps
视频编码:     h264

============================================================

============================================================
推荐压缩方案
============================================================

┌─────────────────────────────────────────────────────────────┐
│ 方案 1: 标准压缩 (推荐)                                      │
├─────────────────────────────────────────────────────────────┤
│  编码:         H.264                                          │
│  画质:         CRF 23 (高质量)                                │
│  分辨率:       4096x2648 (保持原始)                          │
│  预估压缩率:         70-85%                                  │
│  预估大小:           1.5 MB                                  │
│  适用场景:     通用、分享、存档                                  │
├─────────────────────────────────────────────────────────────┤
│ 方案 2: 高压缩率                                              │
├─────────────────────────────────────────────────────────────┤
│  编码:         H.264                                          │
│  画质:         CRF 23 (高质量)                                │
│  分辨率:       2048x1324 (缩小一半)                          │
│  预估压缩率:         85-92%                                  │
│  预估大小:           0.7 MB                                  │
│  适用场景:     Web 上传、移动设备                                │
├─────────────────────────────────────────────────────────────┤
│ 方案 3: 极限压缩                                              │
├─────────────────────────────────────────────────────────────┤
│  编码:         H.265 (HEVC)                                   │
│  画质:         CRF 28 (可接受画质)                            │
│  分辨率:       2048x1324 (缩小一半)                          │
│  预估压缩率:         92-96%                                  │
│  预估大小:           0.4 MB                                  │
│  适用场景:     存储受限、极限压缩需求                          │
│  注意:         编码时间较长，老设备可能不支持                      │
└─────────────────────────────────────────────────────────────┘

请选择压缩方案 [1-3]:
```

---

## 质量控制

### 高质量（接近无损）

```bash
python scripts/convert_to_mp4.py video.mov -crf 18
```

适用于：需要保存高质量视频的场合

### 标准质量（推荐）

```bash
python scripts/convert_to_mp4.py video.mov -crf 23
```

适用于：大多数使用场景

### 较低质量（体积优先）

```bash
python scripts/convert_to_mp4.py video.mov -crf 28
```

适用于：存储空间有限，画质要求不高

### CRF 值对比

| CRF | 画质 | 文件大小 | 适用场景 |
|-----|------|---------|----------|
| 18 | 接近无损 | 较大 | 专业制作、存档 |
| 20-23 | 很好 | 中等 | 推荐、日常使用 |
| 26 | 可接受 | 较小 | Web 分享 |
| 28+ | 较低 | 很小 | 极限压缩 |

---

## 分辨率调整

### 4K 转 1080p

```bash
python scripts/convert_to_mp4.py video_4k.mov -s 1920
```

### 4K 转 720p

```bash
python scripts/convert_to_mp4.py video_4k.mov -s 1280
```

### 指定任意宽度

```bash
python scripts/convert_to_mp4.py video.mov -s 1600
```

高度会自动计算，保持原始宽高比。

### 组合使用：降分辨率 + 高质量

```bash
python scripts/convert_to_mp4.py video.mov -s 1920 -crf 18
```

---

## 编码选择

### H.264（兼容性最好）

```bash
python scripts/convert_to_mp4.py video.mov -c h264
```

### H.265（高压缩率）

```bash
python scripts/convert_to_mp4.py video.mov -c h265
```

### H.265 + 更高压缩率

```bash
python scripts/convert_to_mp4.py video.mov -c h265 -crf 28
```

### 编码对比

| 编码 | 兼容性 | 压缩率 | 速度 | 推荐场景 |
|------|--------|--------|------|----------|
| H.264 | 极好 | 中等 | 快 | Web、跨平台 |
| H.265 | 较好 | 高 | 慢 | 存储、Apple 设备 |

---

## 高级选项

### Web 优化（流式播放）

```bash
python scripts/convert_to_mp4.py video.mov --faststart
```

### 调整编码速度

```bash
# 快速编码（压缩率较低）
python scripts/convert_to_mp4.py video.mov -p ultrafast

# 标准编码（推荐）
python scripts/convert_to_mp4.py video.mov -p slow

# 最佳压缩（速度慢）
python scripts/convert_to_mp4.py video.mov -p veryslow
```

### 音频设置

```bash
# 降低音频比特率
python scripts/convert_to_mp4.py video.mov -ab 96k

# 提高音频比特率
python scripts/convert_to_mp4.py video.mov -ab 192k

# 复制原始音频（不重新编码）
python scripts/convert_to_mp4.py video.mov -ac copy
```

### 详细输出模式

```bash
python scripts/convert_to_mp4.py video.mov -v
```

显示 FFmpeg 的详细输出信息。

---

## 组合示例

### 1. Web 分享方案

兼容性好、快速开始播放：

```bash
python scripts/convert_to_mp4.py video.mov -c h264 -crf 23 --faststart
```

### 2. 存储优化方案

高压缩率、较小体积：

```bash
python scripts/convert_to_mp4.py video.mov -c h265 -crf 28 -s 1920
```

### 3. 高质量存档

保持原始分辨率和高质量：

```bash
python scripts/convert_to_mp4.py video.mov -crf 18 -p veryslow
```

### 4. 快速预览

快速生成预览版本：

```bash
python scripts/convert_to_mp4.py video.mov -p ultrafast -crf 26 -s 1280
```

### 5. 移动设备优化

降分辨率、标准质量：

```bash
python scripts/convert_to_mp4.py video.mov -s 1280 -crf 23 -ab 96k
```

---

## 分析视频信息

查看视频详细信息，不执行转换：

```bash
python scripts/convert_to_mp4.py video.mov --analyze
```

输出示例：
```
============================================================
视频分析: video.mov
============================================================

文件大小:     7.42 MB
时长:         00:00:08.95
分辨率:       4096x2648
帧率:         39.89 fps
视频编码:     h264
音频编码:     aac

============================================================
```

---

## 故障排查

### 问题：FFmpeg 未找到

```bash
❌ 错误: 未找到 FFmpeg
```

**解决方案**：安装 FFmpeg
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg
```

### 问题：转换时间很长

**解决方案**：
- 使用更快的 preset：`-p fast` 或 `-p ultrafast`
- 降低分辨率：`-s 1920` 或 `-s 1280`
- 使用 H.264 而非 H.265

### 问题：文件太大

**解决方案**：
- 提高 CRF 值：`-crf 26` 或 `-crf 28`
- 降低分辨率：`-s 1920`
- 使用 H.265：`-c h265`

### 问题：画质不够好

**解决方案**：
- 降低 CRF 值：`-crf 20` 或 `-crf 18`
- 保持原始分辨率（不使用 `-s`）
- 使用更慢的 preset：`-p veryslow`

---

## 完整参数参考

```
usage: convert_to_mp4.py [-h] [-o OUTPUT] [-c {h264,h265}] [-crf QUALITY]
                          [-p {ultrafast,fast,slow,veryslow}] [-s SCALE]
                          [-ac {aac,libmp3lame,copy}] [-ab AUDIO_BITRATE]
                          [--faststart] [-v] [--analyze] [-i]
                          input

位置参数:
  input                 输入 MOV 文件路径

可选参数:
  -h, --help            显示帮助信息
  -o, --output OUTPUT   输出 MP4 文件路径
  -c, --codec {h264,h265}
                        视频编码 (默认: h264)
  -crf, --quality QUALITY
                        画质 CRF 值 (18-28, 默认: 23)
  -p, --preset {ultrafast,fast,slow,veryslow}
                        编码速度 (默认: slow)
  -s, --scale SCALE     缩放到指定宽度
  -ac, --audio-codec {aac,libmp3lame,copy}
                        音频编码 (默认: aac)
  -ab, --audio-bitrate AUDIO_BITRATE
                        音频比特率 (默认: 128k)
  --faststart           启用 Web 优化
  -v, --verbose         显示详细转换信息
  --analyze             仅分析视频信息
  -i, --interactive     交互模式
```
