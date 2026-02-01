#!/usr/bin/env python3
"""
Video to MP4 Converter
Converts any video format to MP4 with intelligent compression options.
For MP4 inputs, only resizes without re-encoding when possible.
Supports batch processing of folders.
"""

import argparse
import sys
import subprocess
import os
import re
import glob
import shutil
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock


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
            "format": None,
            "duration": None,
            "width": None,
            "height": None,
            "fps": None,
            "video_codec": None,
            "audio_codec": None,
            "size": None
        }

        # Extract input format
        format_match = re.search(r'Input #\d+,\s+(\w+),', output)
        if format_match:
            info["format"] = format_match.group(1)

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


def is_mp4_input(input_file):
    """Check if input file is already MP4 format."""
    return Path(input_file).suffix.lower() in ['.mp4', '.m4v']


def is_video_file(file_path):
    """Check if file is a video file based on extension."""
    video_extensions = {
        '.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm',
        '.m4v', '.mpg', '.mpeg', '.3gp', '.ogv', '.ts', '.m2ts',
        '.mov', '.f4v', '.asf', '.rm', '.rmvb', '.vob', '.divx'
    }
    return Path(file_path).suffix.lower() in video_extensions


def find_videos_in_directory(directory):
    """Find all video files in a directory."""
    video_files = []
    directory_path = Path(directory)

    if not directory_path.is_dir():
        return video_files

    # Common video file patterns
    patterns = [
        '*.mp4', '*.mov', '*.avi', '*.mkv', '*.flv', '*.wmv',
        '*.webm', '*.m4v', '*.mpg', '*.mpeg', '*.3gp', '*.ogv',
        '*.ts', '*.m2ts', '*.f4v', '*.asf', '*.rm', '*.rmvb',
        '*.vob', '*.divx', '*.MP4', '*.MOV', '*.AVI', '*.MKV'
    ]

    for pattern in patterns:
        video_files.extend(directory_path.glob(pattern))

    # Remove duplicates and sort
    video_files = sorted(list(set(video_files)))
    return [str(f) for f in video_files]


# Thread-safe print for concurrent processing
print_lock = Lock()

# Global progress tracking for batch processing
progress_dict = {}
progress_lock = Lock()


def safe_print(*args, **kwargs):
    """Thread-safe print function."""
    with print_lock:
        print(*args, **kwargs, flush=True)


def update_progress(index, progress):
    """Update progress for a specific task."""
    with progress_lock:
        progress_dict[index] = progress


def get_progress_report():
    """Get current progress report for all active tasks."""
    with progress_lock:
        return progress_dict.copy()


def parse_ffmpeg_progress(line, duration_seconds=None):
    """Parse FFmpeg progress from stderr line."""
    try:
        # Look for time parameter: time=01:23:45
        time_match = re.search(r'time=(\d+):(\d+):(\d+\.?\d*)', line)
        if time_match and duration_seconds:
            h, m, s = time_match.groups()
            current_seconds = int(h) * 3600 + int(m) * 60 + float(s)
            if duration_seconds > 0:
                progress = min(99, int(current_seconds / duration_seconds * 100))
                return progress
        return None
    except:
        return None


def convert_single_video(input_file, output_file, options, verbose=False, delete_source=False, index=None, total=None):
    """Convert a single video file, returning result info."""
    result = {
        "input": input_file,
        "output": output_file,
        "success": False,
        "error": None,
        "input_size": 0,
        "output_size": 0,
        "progress": 0
    }

    try:
        # Check FFmpeg
        if not check_ffmpeg():
            result["error"] = "FFmpeg 未安装"
            return result

        # Check input file
        if not os.path.exists(input_file):
            result["error"] = "找不到输入文件"
            return result

        # Get input file size and video info
        result["input_size"] = os.path.getsize(input_file) / (1024 * 1024)

        info = get_video_info(input_file)
        input_width = int(info.get("width", 0)) if info else 0
        input_height = int(info.get("height", 0)) if info else 0

        # Get duration for progress calculation
        duration_str = info.get("duration", "") if info else ""
        duration_seconds = 0
        if duration_str:
            try:
                h, m, s = duration_str.split(':')
                duration_seconds = int(h) * 3600 + int(m) * 60 + float(s)
            except:
                pass

        # Check if input is already MP4
        input_is_mp4 = is_mp4_input(input_file)

        # Build command
        cmd = build_ffmpeg_command(input_file, output_file, options,
                                    is_mp4=input_is_mp4,
                                    input_width=input_width,
                                    input_height=input_height)

        # Run conversion with progress tracking
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        # Track progress
        for line in process.stderr:
            if verbose:
                safe_print(line.strip())

            progress = parse_ffmpeg_progress(line, duration_seconds)
            if progress and index is not None:
                update_progress(index, progress)
                result["progress"] = progress

        process.wait()

        if process.returncode == 0:
            result["output_size"] = os.path.getsize(output_file) / (1024 * 1024)
            result["success"] = True
            result["progress"] = 100

            # Delete source if requested
            if delete_source:
                try:
                    os.remove(input_file)
                except:
                    pass
        else:
            result["error"] = f"转换失败 (退出码: {process.returncode})"

    except Exception as e:
        result["error"] = str(e)

    return result


def batch_convert_videos(input_files, output_dir, options, scale=None, verbose=False,
                         delete_source=False, max_workers=2):
    """Convert multiple videos concurrently."""
    total = len(input_files)
    if total == 0:
        print("❌ 没有找到视频文件")
        return

    print(f"\n{'='*60}")
    print(f"批量转换: {total} 个视频")
    print(f"{'='*60}\n")

    # Prepare output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Prepare conversion tasks
    tasks = []
    for i, input_file in enumerate(input_files, 1):
        input_path = Path(input_file)
        stem = input_path.stem
        output_file = str(output_path / f"small-{stem}.mp4")

        tasks.append((input_file, output_file, i))

    # Display task list
    print(f"待处理清单:\n")
    for idx, input_file, _ in tasks:
        info = get_video_info(input_file)
        name = Path(input_file).name
        if info and info.get("size"):
            size = info.get("size", "Unknown")
            fmt = info.get("format") or "Unknown"
            fmt = fmt.upper() if fmt else "Unknown"
            width = str(info.get("width") or "?")
            height = str(info.get("height") or "?")
            res_str = f"{width}x{height}"
            print(f"  [{idx}] {name:30} {fmt:6} {res_str:10}  {size}")
        else:
            print(f"  [{idx}] {name}")

    print(f"\n开始并发转换 (最多 {max_workers} 个任务)...\n")
    print("每 10 秒报告一次进度\n")

    # Import for progress reporting
    import time

    # Progress reporting
    stop_progress = False
    start_time = time.time()

    # Store file names for progress display
    file_names = {i: Path(f).name for i, f in enumerate(input_files, 1)}

    def progress_reporter():
        """Thread that reports progress every 10 seconds."""
        nonlocal stop_progress
        last_report_time = start_time

        while not stop_progress:
            time.sleep(1)
            current_time = time.time()

            # Report every 10 seconds
            if current_time - last_report_time >= 10:
                with print_lock:
                    elapsed = int(current_time - start_time)
                    print(f"[{elapsed:3d}s] 进度报告:", flush=True)

                current_progress = get_progress_report()

                if not current_progress:
                    safe_print("  等待任务开始...")
                else:
                    for idx, progress in sorted(current_progress.items()):
                        name = file_names.get(idx, "Unknown")
                        safe_print(f"  [{idx}] {name:30} 进度: {progress}%")

                safe_print("")  # Empty line for readability
                last_report_time = current_time

    # Start progress reporter thread
    import threading
    progress_thread = threading.Thread(target=progress_reporter, daemon=True)
    progress_thread.start()

    # Convert videos concurrently
    completed = 0
    failed = 0
    total_input_size = 0
    total_output_size = 0

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_task = {}
        for input_file, output_file, idx in tasks:
            future = executor.submit(
                convert_single_video,
                input_file, output_file, options, verbose, delete_source, idx, total
            )
            future_to_task[future] = (input_file, output_file, idx)

        for future in as_completed(future_to_task):
            input_file, output_file, idx = future_to_task[future]
            result = future.result()

            completed += 1
            total_input_size += result["input_size"]

            if result["success"]:
                total_output_size += result["output_size"]
                compression = (1 - result["output_size"] / result["input_size"]) * 100
                safe_print(
                    f"✅ [{completed}/{total}] {Path(input_file).name:30} "
                    f"{result['input_size']:.1f}MB → {result['output_size']:.1f}MB "
                    f"({compression:.1f}%)"
                )
            else:
                failed += 1
                safe_print(
                    f"❌ [{completed}/{total}] {Path(input_file).name:30} "
                    f"失败: {result['error']}"
                )

    # Stop progress reporter
    stop_progress = True
    progress_thread.join(timeout=2)

    # Final summary
    overall_compression = (1 - total_output_size / total_input_size) * 100 if total_input_size > 0 else 0
    elapsed_time = int(time.time() - start_time)

    print(f"\n{'='*60}")
    print(f"批量转换完成! (耗时: {elapsed_time}秒)")
    print(f"{'='*60}\n")
    print(f"成功:       {completed - failed}/{total}")
    print(f"失败:       {failed}/{total}")
    print(f"原始大小:   {total_input_size:.1f} MB")
    print(f"转换后大小: {total_output_size:.1f} MB")
    print(f"总体压缩率: {overall_compression:.1f}%")
    print(f"输出目录:   {output_dir}\n")

    return completed - failed == total


def analyze_video(input_file):
    """Analyze video and display detailed information."""
    print(f"\n{'='*60}")
    print(f"视频分析: {input_file}")
    print(f"{'='*60}\n")

    info = get_video_info(input_file)
    if info:
        if info["size"]:
            print(f"文件大小:     {info['size']}")
        if info["format"]:
            print(f"格式:         {info['format'].upper()}")
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
    return info


def show_compression_presets(info):
    """Show 3 compression preset options based on video analysis."""
    width = int(info.get("width", 1920))
    height = int(info.get("height", 1080))
    size_mb = float(info["size"].split()[0]) if info.get("size") else 100

    print(f"\n{'='*60}")
    print("推荐压缩方案")
    print(f"{'='*60}\n")

    # 方案 1: 保持分辨率，H.264 + CRF 23
    preset1_compression = "70-85%"
    preset1_size = f"{size_mb * 0.2:.1f} MB"

    # 方案 2: 分辨率减半，H.264 + CRF 23
    preset2_width = width // 2
    preset2_compression = "85-92%"
    preset2_size = f"{size_mb * 0.1:.1f} MB"

    # 方案 3: 分辨率减半 + H.265 + CRF 28 (极限压缩)
    preset3_width = width // 2
    preset3_compression = "92-96%"
    preset3_size = f"{size_mb * 0.05:.1f} MB"

    print("┌─────────────────────────────────────────────────────────────┐")
    print("│ 方案 1: 标准压缩 (推荐)                                      │")
    print("├─────────────────────────────────────────────────────────────┤")
    print(f"│  编码:         H.264                                          │")
    print(f"│  画质:         CRF 23 (高质量)                                │")
    print(f"│  分辨率:       {width}x{height} (保持原始)                          │")
    print(f"│  预估压缩率:   {preset1_compression:>12}                              │")
    print(f"│  预估大小:     {preset1_size:>12}                              │")
    print("│  适用场景:     通用、分享、存档                                  │")
    print("├─────────────────────────────────────────────────────────────┤")
    print("│ 方案 2: 高压缩率                                              │")
    print("├─────────────────────────────────────────────────────────────┤")
    print(f"│  编码:         H.264                                          │")
    print(f"│  画质:         CRF 23 (高质量)                                │")
    print(f"│  分辨率:       {preset2_width}x{height * preset2_width // width} (缩小一半)                    │")
    print(f"│  预估压缩率:   {preset2_compression:>12}                              │")
    print(f"│  预估大小:     {preset2_size:>12}                              │")
    print("│  适用场景:     Web 上传、移动设备                                │")
    print("├─────────────────────────────────────────────────────────────┤")
    print("│ 方案 3: 极限压缩                                              │")
    print("├─────────────────────────────────────────────────────────────┤")
    print("│  编码:         H.265 (HEVC)                                   │")
    print("│  画质:         CRF 28 (可接受画质)                             │")
    print(f"│  分辨率:       {preset3_width}x{height * preset3_width // width} (缩小一半)                    │")
    print(f"│  预估压缩率:   {preset3_compression:>12}                              │")
    print(f"│  预估大小:     {preset3_size:>12}                              │")
    print("│  适用场景:     存储受限、极限压缩需求                            │")
    print("│  注意:         编码时间较长，老设备可能不支持                      │")
    print("└─────────────────────────────────────────────────────────────┘")

    # 定义预设方案
    presets = {
        "1": {
            "name": "标准压缩",
            "codec": "h264",
            "crf": 23,
            "preset": "slow",
            "scale": None,
            "audio_codec": "aac",
            "audio_bitrate": "128k",
            "faststart": True
        },
        "2": {
            "name": "高压缩率",
            "codec": "h264",
            "crf": 23,
            "preset": "slow",
            "scale": preset2_width,
            "audio_codec": "aac",
            "audio_bitrate": "128k",
            "faststart": True
        },
        "3": {
            "name": "极限压缩",
            "codec": "h265",
            "crf": 28,
            "preset": "slow",
            "scale": preset3_width,
            "audio_codec": "aac",
            "audio_bitrate": "96k",
            "faststart": True
        }
    }

    return presets


def interactive_mode(input_file, output_file, delete_source=False):
    """Interactive mode with preset selection."""
    # Analyze video
    info = analyze_video(input_file)
    if not info:
        print("❌ 无法分析视频信息")
        return False

    # Show compression presets
    presets = show_compression_presets(info)

    # Get user choice
    print("\n请选择压缩方案 [1-3]: ", end="", flush=True)
    choice = input().strip()

    if choice not in presets:
        print(f"❌ 无效选择: {choice}")
        return False

    selected = presets[choice]
    print(f"\n已选择: 方案 {choice} - {selected['name']}\n")

    # Convert with selected preset
    return convert_video(input_file, output_file, selected, verbose=False, delete_source=delete_source)


def calculate_scale_size(input_width, input_height, target_width):
    """Calculate output dimensions with minimum 1280x720 limit."""
    # Ensure target width is at least 1280
    width = max(target_width, 1280)

    # Calculate height maintaining aspect ratio
    height = int(input_height * width / input_width)

    # Ensure height is even (required by encoders)
    if height % 2 != 0:
        height += 1

    # Ensure minimum height of 720
    if height < 720:
        height = 720
        # Recalculate width to maintain aspect ratio with min height
        width = int(input_width * 720 / input_height)
        if width % 2 != 0:
            width += 1
        # But still ensure minimum width
        width = max(width, 1280)

    return width, height


def build_ffmpeg_command(input_file, output_file, options, is_mp4=False, input_width=None, input_height=None):
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

    # Preset (encoding speed) - use faster preset for MP4 input
    preset = options.get("preset", "slow")
    if is_mp4 and preset == "slow":
        preset = "fast"  # Use faster preset for MP4 resizing
    cmd.extend(["-preset", preset])

    # CRF (quality) - skip CRF if MP4 input and no scale requested
    # to preserve original quality when just converting MP4 to MP4
    if not (is_mp4 and not options.get("scale")):
        crf = options.get("crf", "23")
        cmd.extend(["-crf", str(crf)])

    # Pixel format (compatibility)
    cmd.extend(["-pix_fmt", "yuv420p"])

    # Scale (resolution) with minimum limit of 1280x720
    if options.get("scale") and input_width and input_height:
        target_width, target_height = calculate_scale_size(
            input_width, input_height, options["scale"]
        )
        cmd.extend(["-vf", f"scale={target_width}:{target_height}"])
    elif options.get("scale"):
        # Fallback if dimensions not available
        width = max(options["scale"], 1280)
        cmd.extend(["-vf", f"scale={width}:-2"])

    # Audio codec - copy audio for MP4 input to preserve quality
    audio_codec = options.get("audio_codec", "aac")
    if is_mp4 and audio_codec == "aac":
        cmd.extend(["-c:a", "copy"])  # Copy audio for MP4 input
    elif audio_codec == "copy":
        cmd.extend(["-c:a", "copy"])
    elif audio_codec == "libmp3lame":
        cmd.extend(["-c:a", "libmp3lame"])
    else:  # aac
        cmd.extend(["-c:a", "aac"])

    # Audio bitrate - skip for MP4 input when copying audio
    if audio_codec != "copy" and not (is_mp4 and options.get("audio_codec") == "aac"):
        if options.get("audio_bitrate"):
            cmd.extend(["-b:a", options["audio_bitrate"]])
        else:
            cmd.extend(["-b:a", "128k"])  # Default

    # Web optimization
    if options.get("faststart"):
        cmd.extend(["-movflags", "+faststart"])

    # Overwrite output without asking
    cmd.append("-y")

    # Output file
    cmd.append(output_file)

    return cmd


def convert_video(input_file, output_file, options, verbose=False, delete_source=False):
    """
    Convert any video to MP4.

    Args:
        input_file: Path to input video file
        output_file: Path to output MP4 file
        options: Dictionary of conversion options
        verbose: Show detailed FFmpeg output
        delete_source: Delete source file after successful conversion
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

    # Get video info for dimensions
    info = get_video_info(input_file)
    input_width = int(info.get("width", 0)) if info else 0
    input_height = int(info.get("height", 0)) if info else 0

    # Check if input is already MP4
    input_is_mp4 = is_mp4_input(input_file)

    # Build command with dimensions
    cmd = build_ffmpeg_command(input_file, output_file, options,
                                is_mp4=input_is_mp4,
                                input_width=input_width,
                                input_height=input_height)

    # Get input format for display
    input_ext = Path(input_file).suffix.upper().lstrip('.')

    # Calculate target resolution for display
    target_resolution = None
    if options.get("scale") and input_width and input_height:
        target_width, target_height = calculate_scale_size(
            input_width, input_height, options["scale"]
        )
        target_resolution = f"{target_width}x{target_height}"

    # Display conversion info
    print(f"\n{'='*60}")
    if input_is_mp4:
        print(f"MP4 缩小尺寸处理")
    else:
        print(f"开始转换")
    print(f"{'='*60}\n")
    print(f"输入文件:     {input_file} ({input_ext})")
    print(f"输出文件:     {output_file} (MP4)")
    print(f"视频编码:     {options.get('codec', 'h264').upper()}")

    # Adjust preset display for MP4 input
    preset = options.get('preset', 'slow')
    if input_is_mp4 and preset == 'slow':
        preset = 'fast (MP4优化)'
    print(f"编码速度:     {preset}")

    if input_is_mp4 and not options.get("scale"):
        print(f"处理模式:     保持原始画质 (仅格式保证)")
    elif target_resolution:
        print(f"分辨率:       {input_width}x{input_height} → {target_resolution} (最小 1280x720)")
    elif options.get("scale"):
        print(f"分辨率:       缩放到宽度 {options.get('scale')}px (最小 1280x720)")
    else:
        print(f"画质 (CRF):   {options.get('crf', 23)}")

    audio_codec = options.get("audio_codec", "aac")
    if input_is_mp4 and audio_codec == "aac":
        print(f"音频:         复制原始音频 (保持质量)")
    elif audio_codec == "copy":
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

            # Delete source file if requested
            if delete_source:
                try:
                    os.remove(input_file)
                    print(f"🗑️  已删除原始文件: {input_file}\n")
                except Exception as e:
                    print(f"⚠️  警告: 无法删除原始文件: {e}\n")

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
        description="将任意视频格式转换为 MP4 并进行压缩。支持 MOV、MP4、AVI、MKV 等格式。支持批量处理文件夹。",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 基本转换 (任意视频格式)
  %(prog)s video.mov
  %(prog)s video.avi
  %(prog)s video.mkv

  # MP4 缩小尺寸
  %(prog)s video.mp4 -s 1920

  # 批量转换文件夹
  %(prog)s /path/to/videos
  %(prog)s /path/to/videos -s 1920
  %(prog)s /path/to/videos -j 4

  # 指定输出文件
  %(prog)s video.mov -o output.mp4

  # 高质量转换
  %(prog)s video.mov -crf 18

  # 高压缩率 (H.265)
  %(prog)s video.mov -c h265 -crf 28

  # 交互模式
  %(prog)s video.mov -i

  # 仅分析视频信息
  %(prog)s video.mov --analyze
        """
    )

    # Positional arguments
    parser.add_argument("input", help="输入视频文件路径或文件夹 (支持 MOV、MP4、AVI、MKV 等)")

    # Output file/directory
    parser.add_argument(
        "-o", "--output",
        help="输出 MP4 文件路径或输出目录 (默认: small-{filename}.mp4 或 input_dir/small)"
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

    # Interactive mode
    parser.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="交互模式: 从 3 个推荐方案中选择"
    )

    # Delete source file
    parser.add_argument(
        "--rm",
        action="store_true",
        help="转换成功后删除原始文件"
    )

    # Batch mode
    parser.add_argument(
        "-j", "--jobs",
        type=int,
        default=2,
        help="批量转换时的并发任务数 (默认: 2)"
    )

    args = parser.parse_args()

    # Check if input is a directory
    input_path = Path(args.input)
    if input_path.is_dir():
        # Batch mode: process all videos in directory
        video_files = find_videos_in_directory(args.input)

        if not video_files:
            print(f"❌ 在目录 {args.input} 中没有找到视频文件")
            return 1

        # Determine output directory (default: input_dir/small)
        if args.output:
            output_dir = args.output
        else:
            output_dir = str(input_path / "small")

        # Build options
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

        # Run batch conversion
        success = batch_convert_videos(
            video_files, output_dir, options,
            scale=args.scale,
            verbose=args.verbose,
            delete_source=args.rm,
            max_workers=args.jobs
        )
        return 0 if success else 1

    # Single file mode continues below...

    # Interactive mode (highest priority)
    if args.interactive:
        # Determine output file with "small-" prefix
        if not args.output:
            input_path = Path(args.input)
            stem = input_path.stem
            args.output = str(input_path.parent / f"small-{stem}.mp4")
        success = interactive_mode(args.input, args.output, delete_source=args.rm)
        return 0 if success else 1

    # Analyze mode (handle first, before using other options)
    if args.analyze:
        analyze_video(args.input)
        return 0

    # Determine output file with "small-" prefix
    if not args.output:
        input_path = Path(args.input)
        stem = input_path.stem
        args.output = str(input_path.parent / f"small-{stem}.mp4")

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
        verbose=args.verbose,
        delete_source=args.rm
    )

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
