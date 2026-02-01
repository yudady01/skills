# to-mp4 Skill 快速开始

这是一个将 MOV 视频转换为 MP4 格式并进行压缩的实用工具。

## 5 分钟快速上手

### 步骤 1：安装 FFmpeg（仅需一次）

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# 验证安装
ffmpeg -version
```

### 步骤 2：转换你的第一个视频

```bash
# 进入 skill 目录
cd global-claude/skills/to-mp4

# 转换视频
python scripts/convert_to_mp4.py your_video.mov
```

就这么简单！转换后的视频将保存为 `your_video.mp4`。

## 常用命令速查

| 需求 | 命令 |
|------|------|
| 基本转换 | `python scripts/convert_to_mp4.py video.mov` |
| 高质量 | `python scripts/convert_to_mp4.py video.mov -crf 18` |
| 高压缩率 | `python scripts/convert_to_mp4.py video.mov -c h265 -crf 28` |
| 4K → 1080p | `python scripts/convert_to_mp4.py video.mov -s 1920` |
| Web 优化 | `python scripts/convert_to_mp4.py video.mov --faststart` |
| 查看视频信息 | `python scripts/convert_to_mp4.py video.mov --analyze` |

## 典型压缩效果

| 原始文件 | 转换方案 | 结果 |
|---------|---------|------|
| 2GB MOV (4K) | H.264 + CRF23 | ~300MB (压缩 85%) |
| 2GB MOV (4K) | H.264 + CRF23 + 1080p | ~150MB (压缩 92.5%) |
| 2GB MOV (4K) | H.265 + CRF28 | ~200MB (压缩 90%) |

## 推荐设置

### 日常使用（推荐）
```bash
python scripts/convert_to_mp4.py video.mov -c h264 -crf 23
```

### Web 分享
```bash
python scripts/convert_to_mp4.py video.mov -c h264 -crf 23 --faststart
```

### 极限压缩
```bash
python scripts/convert_to_mp4.py video.mov -c h265 -crf 28 -s 1920
```

### 高质量存档
```bash
python scripts/convert_to_mp4.py video.mov -crf 18 -p veryslow
```

## 参数说明

**CRF 值（画质）：**
- `18` - 接近无损
- `23` - 推荐（默认）
- `28` - 高压缩率

**编码（Codec）：**
- `h264` - 最佳兼容性（默认）
- `h265` - 更高压缩率

**Preset（速度）：**
- `fast` - 快速
- `slow` - 推荐（默认）
- `veryslow` - 最佳压缩率

## 获取帮助

查看完整选项：
```bash
python scripts/convert_to_mp4.py --help
```

## 更多资源

- **完整文档**: [README.md](README.md)
- **使用示例**: [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md)
- **Skill 定义**: [SKILL.md](SKILL.md)

## 常见问题

**Q: 转换时间太长？**
```bash
# 使用更快的 preset
python scripts/convert_to_mp4.py video.mov -p fast
```

**Q: 文件太大？**
```bash
# 提高 CRF 值或使用 H.265
python scripts/convert_to_mp4.py video.mov -c h265 -crf 28
```

**Q: 画质不够好？**
```bash
# 降低 CRF 值
python scripts/convert_to_mp4.py video.mov -crf 18
```

**Q: 4K 视频太大？**
```bash
# 降低分辨率
python scripts/convert_to_mp4.py video.mov -s 1920
```

## 下一步

1. 阅读 [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md) 了解更多实际使用场景
2. 查看 [README.md](README.md) 了解所有参数和选项
3. 尝试不同的参数组合，找到最适合你的设置
