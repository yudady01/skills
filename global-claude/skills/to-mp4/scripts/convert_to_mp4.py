#!/usr/bin/env python3
"""
MOV to MP4 Video Converter
Converts MOV videos to MP4 format with intelligent compression options.
"""

import argparse
import sys
import subprocess
import os
import re
from pathlib import Path


def check_ffmpeg():
    """Check if FFmpeg is installed."""
    try:
        result = subprocess.run(
            ["ffmpeg", "-version"],
            capture_output=True,
            text=True,
            check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def get_video_info(input_file):
    """Get detailed information about the video file."""
    try:
        result = subprocess.run(
            ["ffmpeg", "-i", input_file],
            capture_output=True,
            text=True
        )
        # FFmpeg writes info to stderr
        output = result.stderr

        info = {
            "duration": None,
            "width": None,
            "height": None,
            "fps": None,
            "video_codec": None,
            "audio_codec": None,
            "size": None
        }

        # Extract duration
        duration_match = re.search(r'Duration: (\d{2}):(\d{2}):(\d{2}\.\d{2})', output)
        if duration_match:
            h, m, s = duration_match.groups()
            info["duration"] = f"{h}:{m}:{s}"

        # Extract resolution
        resolution_match = re.search(r'(\d{3,4})x(\d{3,4})', output)
        if resolution_match:
            info["width"] = resolution_match.group(1)
            info["height"] = resolution_match.group(2)

        # Extract FPS
        fps_match = re.search(r'(\d+\.?\d*) fps', output)
        if fps_match:
            info["fps"] = fps_match.group(1)

        # Extract video codec
        video_codec_match = re.search(r'Video:\s+(\w+)', output)
        if video_codec_match:
            info["video_codec"] = video_codec_match.group(1)

        # Extract audio codec
        audio_codec_match = re.search(r'Audio:\s+(\w+)', output)
        if audio_codec_match:
            info["audio_codec"] = audio_codec_match.group(1)

        # Get file size
        if os.path.exists(input_file):
            size_bytes = os.path.getsize(input_file)
            size_mb = size_bytes / (1024 * 1024)
            info["size"] = f"{size_mb:.2f} MB"

        return info

    except Exception as e:
        print(f"Warning: Could not get video info: {e}")
        return None


def analyze_video(input_file):
    """Analyze video and display detailed information."""
    print(f"\n{'='*60}")
    print(f"视频分析: {input_file}")
    print(f"{'='*60}\n")

    info = get_video_info(input_file)
    if info:
        if info["size"]:
            print(f"文件大小:     {info['size']}")
        if info["duration"]:
            print(f"时长:         {info['duration']}")
        if info["width"] and info["height"]:
            print(f"分辨率:       {info['width']}x{info['height']}")
        if info["fps"]:
            print(f"帧率:         {info['fps']} fps")
        if info["video_codec"]:
            print(f"视频编码:     {info['video_codec']}")
        if info["audio_codec"]:
            print(f"音频编码:     {info['audio_codec']}")
        print(f"\n{'='*60}\n")


def build_ffmpeg_command(input_file, output_file, options):
    """Build FFmpeg command based on options."""
    cmd = ["ffmpeg", "-i", input_file]

    # Video codec
    codec = options.get("codec", "h264")
    if codec == "h264":
        cmd.extend(["-c:v", "libx264"])
    elif codec == "h265":
        cmd.extend(["-c:v", "libx265"])
        # Add hvc1 tag for better compatibility
        cmd.extend(["-tag:v", "hvc1"])

    # Preset (encoding speed)
    preset = options.get("preset", "slow")
    cmd.extend(["-preset", preset])

    # CRF (quality)
    crf = options.get("crf", "23")
    cmd.extend(["-crf", str(crf)])

    # Pixel format (compatibility)
    cmd.extend(["-pix_fmt", "yuv420p"])

    # Scale (resolution)
    if options.get("scale"):
        width = options["scale"]
        # -2 ensures height is even (required by encoders)
        cmd.extend(["-vf", f"scale={width}:-2"])

    # Audio codec
    audio_codec = options.get("audio_codec", "aac")
    if audio_codec == "copy":
        cmd.extend(["-c:a", "copy"])
    elif audio_codec == "libmp3lame":
        cmd.extend(["-c:a", "libmp3lame"])
    else:  # aac
        cmd.extend(["-c:a", "aac"])

    # Audio bitrate
    if audio_codec != "copy" and options.get("audio_bitrate"):
        cmd.extend(["-b:a", options["audio_bitrate"]])
    elif audio_codec != "copy":
        cmd.extend(["-b:a", "128k"])  # Default

    # Web optimization
    if options.get("faststart"):
        cmd.extend(["-movflags", "+faststart"])

    # Overwrite output without asking
    cmd.append("-y")

    # Output file
    cmd.append(output_file)

    return cmd


def convert_video(input_file, output_file, options, verbose=False):
    """
    Convert MOV video to MP4.

    Args:
        input_file: Path to input MOV file
        output_file: Path to output MP4 file
        options: Dictionary of conversion options
        verbose: Show detailed FFmpeg output
    """
    # Check FFmpeg
    if not check_ffmpeg():
        print("❌ 错误: 未找到 FFmpeg")
        print("\n请安装 FFmpeg:")
        print("  macOS:   brew install ffmpeg")
        print("  Ubuntu:  sudo apt install ffmpeg")
        print("  Windows: 从 https://ffmpeg.org/download.html 下载")
        return False

    # Check input file
    if not os.path.exists(input_file):
        print(f"❌ 错误: 找不到输入文件: {input_file}")
        return False

    # Build command
    cmd = build_ffmpeg_command(input_file, output_file, options)

    # Display conversion info
    print(f"\n{'='*60}")
    print(f"开始转换")
    print(f"{'='*60}\n")
    print(f"输入文件:     {input_file}")
    print(f"输出文件:     {output_file}")
    print(f"视频编码:     {options.get('codec', 'h264').upper()}")
    print(f"画质 (CRF):   {options.get('crf', 23)}")
    print(f"编码速度:     {options.get('preset', 'slow')}")

    if options.get("scale"):
        print(f"分辨率:       缩放到宽度 {options.get('scale')}px")

    audio_codec = options.get("audio_codec", "aac")
    if audio_codec == "copy":
        print(f"音频:         复制原始音频")
    else:
        audio_bitrate = options.get("audio_bitrate", "128k")
        print(f"音频:         {audio_codec.upper()} @ {audio_bitrate}")

    if options.get("faststart"):
        print(f"Web 优化:     启用")

    print(f"\n{'='*60}\n")

    try:
        # Run conversion
        if verbose:
            # Show full FFmpeg output
            result = subprocess.run(cmd)
        else:
            # Suppress FFmpeg output, only show progress
            result = subprocess.run(
                cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

        if result.returncode == 0:
            # Get file sizes
            input_size = os.path.getsize(input_file) / (1024 * 1024)
            output_size = os.path.getsize(output_file) / (1024 * 1024)
            compression = (1 - output_size / input_size) * 100

            print(f"\n{'='*60}")
            print(f"✅ 转换完成!")
            print(f"{'='*60}\n")
            print(f"原始大小:     {input_size:.2f} MB")
            print(f"转换后大小:   {output_size:.2f} MB")
            print(f"压缩率:       {compression:.1f}%")
            print(f"输出文件:     {output_file}\n")
            return True
        else:
            print(f"\n❌ 转换失败 (退出码: {result.returncode})")
            return False

    except KeyboardInterrupt:
        print(f"\n\n❌ 转换已取消")
        return False
    except Exception as e:
        print(f"\n❌ 转换出错: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="将 MOV 视频转换为 MP4 格式并进行压缩",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 基本转换
  %(prog)s video.mov

  # 指定输出文件
  %(prog)s video.mov -o output.mp4

  # 高质量转换
  %(prog)s video.mov -crf 18 -p slow

  # 高压缩率 (H.265)
  %(prog)s video.mov -c h265 -crf 28

  # 4K 转 1080p
  %(prog)s video.mov -s 1920

  # Web 优化
  %(prog)s video.mov --faststart

  # 仅分析视频信息
  %(prog)s video.mov --analyze
        """
    )

    # Positional arguments
    parser.add_argument("input", help="输入 MOV 文件路径")

    # Output file
    parser.add_argument(
        "-o", "--output",
        help="输出 MP4 文件路径 (默认: 输入文件名.mp4)"
    )

    # Video codec
    parser.add_argument(
        "-c", "--codec",
        choices=["h264", "h265"],
        default="h264",
        help="视频编码 (默认: h264)"
    )

    # Quality (CRF)
    parser.add_argument(
        "-crf", "--quality",
        type=int,
        default=23,
        dest="crf",
        help="画质 CRF 值 (18-28, 默认: 23, 数值越小画质越好)"
    )

    # Preset
    parser.add_argument(
        "-p", "--preset",
        choices=["ultrafast", "fast", "slow", "veryslow"],
        default="slow",
        help="编码速度 (默认: slow)"
    )

    # Scale
    parser.add_argument(
        "-s", "--scale",
        type=int,
        help="缩放到指定宽度 (高度自动计算, 保持宽高比)"
    )

    # Audio codec
    parser.add_argument(
        "-ac", "--audio-codec",
        choices=["aac", "libmp3lame", "copy"],
        default="aac",
        help="音频编码 (默认: aac)"
    )

    # Audio bitrate
    parser.add_argument(
        "-ab", "--audio-bitrate",
        default="128k",
        help="音频比特率 (默认: 128k)"
    )

    # Web optimization
    parser.add_argument(
        "--faststart",
        action="store_true",
        help="启用 Web 优化 (快速开始播放)"
    )

    # Verbose
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="显示详细转换信息"
    )

    # Analyze only
    parser.add_argument(
        "--analyze",
        action="store_true",
        help="仅分析视频信息, 不执行转换"
    )

    args = parser.parse_args()

    # Analyze mode (handle first, before using other options)
    if args.analyze:
        analyze_video(args.input)
        return 0

    # Determine output file
    if not args.output:
        input_path = Path(args.input)
        args.output = str(input_path.with_suffix(".mp4"))

    # Build options dictionary
    options = {
        "codec": args.codec,
        "crf": args.crf,
        "preset": args.preset,
        "audio_codec": args.audio_codec,
        "audio_bitrate": args.audio_bitrate,
        "faststart": args.faststart
    }

    if args.scale:
        options["scale"] = args.scale

    # Convert video
    success = convert_video(
        input_file=args.input,
        output_file=args.output,
        options=options,
        verbose=args.verbose
    )

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
