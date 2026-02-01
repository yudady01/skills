# to-mp4 Skill 使用示例

本文档提供了 to-mp4 skill 的实际使用示例。

## 前置条件

在使用此 skill 之前，请确保已安装 FFmpeg：

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# 验证安装
ffmpeg -version
```

## 基本使用

### 示例 1：最简单的转换

将 `video.mov` 转换为 `video.mp4`，使用默认设置：

```bash
python scripts/convert_to_mp4.py video.mov
```

**输出：**
```
============================================================
开始转换
============================================================

输入文件:     video.mov
输出文件:     video.mp4
视频编码:     H264
画质 (CRF):   23
编码速度:     slow
音频:         AAC @ 128k

============================================================

============================================================
✅ 转换完成!
============================================================

原始大小:     2048.00 MB
转换后大小:   312.50 MB
压缩率:       84.7%
输出文件:     video.mp4
```

### 示例 2：指定输出文件名

```bash
python scripts/convert_to_mp4.py input.mov -o output.mp4
```

## 画质控制

### 示例 3：高质量转换

使用 CRF 18 获得接近无损的画质：

```bash
python scripts/convert_to_mp4.py video.mov -crf 18 -p slow -o video_hq.mp4
```

**适用场景：**
- 需要保留最高画质
- 文件大小不是主要考虑因素
- 后期制作或存档

### 示例 4：标准质量（推荐）

使用 CRF 23，画质与体积的最佳平衡：

```bash
python scripts/convert_to_mp4.py video.mov -crf 23 -p slow
```

**适用场景：**
- 日常使用
- 视频分享
- 一般存档

### 示例 5：高压缩率

使用 CRF 28，显著减小文件大小：

```bash
python scripts/convert_to_mp4.py video.mov -crf 28 -p slow -o video_small.mp4
```

**适用场景：**
- 存储空间有限
- 网络传输
- 不太关注画质细节

## 编码格式选择

### 示例 6：H.264 编码（默认）

最佳兼容性，适合大多数场景：

```bash
python scripts/convert_to_mp4.py video.mov -c h264 -crf 23
```

**优点：**
- 兼容性极佳
- 编码速度快
- 适合 Web 播放

**缺点：**
- 压缩率不如 H.265

### 示例 7：H.265 编码

更高压缩率，体积减少 30-50%：

```bash
python scripts/convert_to_mp4.py video.mov -c h265 -crf 28 -o video_h265.mp4
```

**优点：**
- 压缩率更高
- 适合存储
- Apple 设备原生支持

**缺点：**
- 编码时间长
- 老旧设备可能不支持

## 分辨率调整

### 示例 8：4K 转换为 1080p

将 4K 视频缩小到全高清：

```bash
python scripts/convert_to_mp4.py video_4k.mov -s 1920 -o video_1080p.mp4
```

**效果：**
- 宽度：1920px
- 高度：自动计算（保持比例）
- 文件大小显著减小

### 示例 9：4K 转换为 720p

将 4K 视频缩小到高清：

```bash
python scripts/convert_to_mp4.py video_4k.mov -s 1280 -o video_720p.mp4
```

### 示例 10：转换为 480p

生成较小的预览版本：

```bash
python scripts/convert_to_mp4.py video.mov -s 854 -o video_480p.mp4
```

## Web 优化

### 示例 11：Web 优化视频

启用 faststart，支持流式播放：

```bash
python scripts/convert_to_mp4.py video.mov --faststart -o video_web.mp4
```

**优点：**
- 视频可以边下载边播放
- 改善用户体验
- 不影响画质

**适用场景：**
- 网站视频
- 在线播放平台
- CDN 分发

## 音频控制

### 示例 12：高质量音频

使用 192k 音频比特率：

```bash
python scripts/convert_to_mp4.py video.mov -ab 192k -o video_hqa.mp4
```

**适用场景：**
- 音乐视频
- 高质量音频内容

### 示例 13：标准音频

使用 128k 音频比特率（默认）：

```bash
python scripts/convert_to_mp4.py video.mov -ab 128k
```

**适用场景：**
- 大多数视频内容
- 语音内容

### 示例 14：低比特率音频

使用 96k 音频比特率：

```bash
python scripts/convert_to_mp4.py video.mov -ab 96k -o video_lqa.mp4
```

**适用场景：**
- 纯语音内容
- 进一步减小文件大小

### 示例 15：复制原始音频

不重新编码音频：

```bash
python scripts/convert_to_mp4.py video.mov -ac copy
```

**注意：** 如果原始音频是 PCM，文件大小不会有明显减小。

## 编码速度控制

### 示例 16：快速转换

使用 fast preset：

```bash
python scripts/convert_to_mp4.py video.mov -p fast -crf 23
```

**适用场景：**
- 快速预览
- 时间紧迫
- 临时文件

### 示例 17：最佳压缩率

使用 veryslow preset：

```bash
python scripts/convert_to_mp4.py video.mov -p veryslow -crf 23 -o video_best.mp4
```

**适用场景：**
- 最终存档
- 最大化压缩率
- 不在意编码时间

## 组合示例

### 示例 18：高质量 Web 视频

```bash
python scripts/convert_to_mp4.py video.mov \
  -c h264 \
  -crf 20 \
  -p slow \
  --faststart \
  -ab 192k \
  -o video_web_hq.mp4
```

**特点：**
- H.264 编码（最佳兼容性）
- 高画质（CRF 20）
- Web 优化
- 高质量音频

### 示例 19：极限压缩

```bash
python scripts/convert_to_mp4.py video_4k.mov \
  -c h265 \
  -crf 28 \
  -p slow \
  -s 1920 \
  -ab 96k \
  -o video_compressed.mp4
```

**特点：**
- H.265 编码（高压缩率）
- 4K → 1080p
- 低比特率音频
- 最大程度减小文件

### 示例 20：快速预览

```bash
python scripts/convert_to_mp4.py video.mov \
  -p fast \
  -crf 26 \
  -s 1280 \
  -o video_preview.mp4
```

**特点：**
- 快速编码
- 720p 分辨率
- 较低画质
- 快速生成预览

## 视频分析

### 示例 21：查看视频信息

不进行转换，仅显示视频详细信息：

```bash
python scripts/convert_to_mp4.py video.mov --analyze
```

**输出：**
```
============================================================
视频分析: video.mov
============================================================

文件大小:     2048.00 MB
时长:         00:05:30
分辨率:       3840x2160
帧率:         30.00 fps
视频编码:     h264
音频编码:     aac

============================================================
```

## 实际场景

### 场景 1：iPhone 视频压缩

iPhone 录制的视频通常很大，压缩后方便分享：

```bash
# 压缩 iPhone 4K 视频
python scripts/convert_to_mp4.py IMG_1234.MOV \
  -c h264 \
  -crf 23 \
  -s 1920 \
  -ab 128k \
  -o IMG_1234_compressed.mp4
```

### 场景 2：YouTube 上传

准备上传到 YouTube 的视频：

```bash
python scripts/convert_to_mp4.py raw_footage.mov \
  -c h264 \
  -crf 23 \
  -p slow \
  --faststart \
  -ab 192k \
  -o youtube_ready.mp4
```

### 场景 3：存档空间优化

长期存档的视频，使用 H.265 最大化压缩：

```bash
python scripts/convert_to_mp4.py archive_footage.mov \
  -c h265 \
  -crf 24 \
  -p veryslow \
  -ab 128k \
  -o archive_compressed.mp4
```

### 场景 4：快速生成多个版本

批量生成不同质量的版本：

```bash
# 原始版本
python scripts/convert_to_mp4.py video.mov -o video_4k.mp4

# 1080p 版本
python scripts/convert_to_mp4.py video.mov -s 1920 -o video_1080p.mp4

# 720p 版本
python scripts/convert_to_mp4.py video.mov -s 1280 -o video_720p.mp4

# 480p 预览版本
python scripts/convert_to_mp4.py video.mov -s 854 -crf 26 -p fast -o video_preview.mp4
```

## 故障排查

### 问题：FFmpeg 未找到

**错误信息：**
```
❌ 错误: 未找到 FFmpeg
```

**解决方法：**
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg
```

### 问题：转换时间过长

**解决方法：**
```bash
# 使用更快的 preset
python scripts/convert_to_mp4.py video.mov -p fast

# 或降低分辨率
python scripts/convert_to_mp4.py video.mov -s 1920
```

### 问题：文件太大

**解决方法：**
```bash
# 提高 CRF 值
python scripts/convert_to_mp4.py video.mov -crf 28

# 使用 H.265
python scripts/convert_to_mp4.py video.mov -c h265 -crf 28

# 降低分辨率
python scripts/convert_to_mp4.py video.mov -s 1920
```

### 问题：画质不够好

**解决方法：**
```bash
# 降低 CRF 值
python scripts/convert_to_mp4.py video.mov -crf 18 -p veryslow
```

## 最佳实践

1. **先测试参数**：使用小段视频测试不同参数组合
2. **备份原始文件**：转换前保留原始 MOV 文件
3. **选择合适的 preset**：日常使用 `slow`，追求质量用 `veryslow`
4. **逐步调整 CRF**：从 23 开始，根据结果调整
5. **考虑使用场景**：
   - Web 分享：H.264 + faststart
   - 长期存档：H.265 + 较低 CRF
   - 快速预览：fast preset + 降低分辨率

## 性能参考

基于现代计算机（M1/M2 芯片或 Intel i7）的参考时间：

| 视频长度 | 分辨率 | 编码 | Preset | 预计时间 |
|---------|--------|------|--------|----------|
| 1 分钟 | 1080p | H.264 | slow | ~30 秒 |
| 1 分钟 | 4K | H.264 | slow | ~2 分钟 |
| 1 分钟 | 4K | H.265 | slow | ~5 分钟 |
| 1 分钟 | 4K → 1080p | H.264 | fast | ~1 分钟 |

**注意：** 实际时间取决于 CPU 性能、视频复杂度和可用资源。
