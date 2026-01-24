#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "yt-dlp",
# ]
# ///

import sys
import re
import subprocess
import os
from pathlib import Path
from datetime import timedelta


def sanitize_filename(title):
    """Clean video title for filesystem compatibility."""
    return title.replace("/", "_").replace(":", "-").replace("?", "").replace('"', "").replace("<", "").replace(">", "").replace("|", "").replace("*", "").strip()


def get_video_info(url):
    """Get the video title and channel name from YouTube URL."""
    result = subprocess.run(
        ["yt-dlp", "--print", "%(title)s|||%(channel)s", url],
        capture_output=True,
        text=True,
        check=True,
    )
    title, channel = result.stdout.strip().split("|||")
    return sanitize_filename(title), sanitize_filename(channel)


def list_subtitles(url):
    """List available subtitles for the video."""
    print("Checking available subtitles...")
    subprocess.run(["yt-dlp", "--list-subs", url])


def download_subtitles(url, output_name):
    """Try to download subtitles, manual first, then auto-generated."""
    print("Attempting to download manual subtitles...")
    result = subprocess.run(
        ["yt-dlp", "--write-sub", "--skip-download", "--sub-lang", "en", "--sub-format", "vtt", "--output", output_name, url],
        capture_output=True,
        text=True,
    )

    print(f"Manual subtitle download stdout: {result.stdout}")
    print(f"Manual subtitle download stderr: {result.stderr}")

    if result.returncode == 0:
        print("[OK] Manual subtitles downloaded successfully!")
        # Check if file actually exists
        vtt_file = find_vtt_file()
        if vtt_file:
            return True

    print("Manual subtitles not available. Trying auto-generated...")
    result = subprocess.run(
        [
            "yt-dlp",
            "--write-auto-sub",
            "--skip-download",
            "--sub-lang",
            "en",
            "--sub-format",
            "vtt",
            "--output",
            output_name,
            url,
        ],
        capture_output=True,
        text=True,
    )

    print(f"Auto subtitle download stdout: {result.stdout}")
    print(f"Auto subtitle download stderr: {result.stderr}")

    if result.returncode == 0:
        print("[OK] Auto-generated subtitles downloaded successfully!")
        return True

    print("[WARN] No subtitles available for this video")
    return False


def parse_timestamp(ts_str):
    """Parse VTT timestamp to seconds."""
    # Format: 00:00:00.000 or 00:00.000
    parts = ts_str.split(":")
    if len(parts) == 3:
        h, m, s = parts
        return int(h) * 3600 + int(m) * 60 + float(s)
    elif len(parts) == 2:
        m, s = parts
        return int(m) * 60 + float(s)
    return 0


def format_timestamp(seconds):
    """Format seconds as HH:MM:SS or MM:SS."""
    td = timedelta(seconds=int(seconds))
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def convert_vtt_to_markdown(vtt_file, output_file, video_title, video_url):
    """Convert VTT file to markdown with timestamps and time windows."""
    print("Converting to markdown format with timestamps...")

    # Parse VTT file
    segments = []
    current_timestamp = None

    with open(vtt_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # Look for timestamp line
            if "-->" in line:
                timestamp_match = re.match(r"(\d{2}:\d{2}:\d{2}\.\d{3}|\d{2}:\d{2}\.\d{3})\s*-->\s*", line)
                if timestamp_match:
                    current_timestamp = parse_timestamp(timestamp_match.group(1))

                    # Get the text from next lines
                    i += 1
                    text_lines = []
                    while i < len(lines) and lines[i].strip() and "-->" not in lines[i]:
                        text = lines[i].strip()
                        # Remove HTML tags
                        text = re.sub("<[^>]*>", "", text)
                        # Decode HTML entities
                        text = text.replace("&amp;", "&").replace("&gt;", ">").replace("&lt;", "<").replace("&quot;", '"').replace("&#39;", "'")
                        if text:
                            text_lines.append(text)
                        i += 1

                    if text_lines and current_timestamp is not None:
                        segments.append((current_timestamp, " ".join(text_lines)))
                    continue

            i += 1

    # Remove duplicate consecutive lines
    deduplicated = []
    seen = set()
    for ts, text in segments:
        if text not in seen:
            deduplicated.append((ts, text))
            seen.add(text)
        else:
            # If we've seen this text, check if it's not consecutive
            if deduplicated and deduplicated[-1][1] != text:
                deduplicated.append((ts, text))

    # Group into time windows (every 60 seconds)
    window_size = 60  # 1 minute windows
    time_windows = []
    current_window = []
    current_window_start = 0

    for ts, text in deduplicated:
        window_idx = int(ts // window_size)
        window_start = window_idx * window_size

        if window_start != current_window_start and current_window:
            time_windows.append((current_window_start, current_window))
            current_window = []

        current_window_start = window_start
        current_window.append((ts, text))

    if current_window:
        time_windows.append((current_window_start, current_window))

    # Write markdown file
    with open(output_file, "w", encoding="utf-8") as f:
        # Header
        f.write(f"# {video_title}\n\n")
        f.write(f"**Video URL:** {video_url}\n\n")
        f.write("---\n\n")
        f.write("## Full Transcript\n\n")

        for window_start, segments in time_windows:
            window_end = window_start + window_size
            f.write(f"### [{format_timestamp(window_start)} - {format_timestamp(window_end)}]\n\n")

            for ts, text in segments:
                f.write(f"**[{format_timestamp(ts)}]** {text}\n\n")

            f.write("\n")


def find_vtt_file():
    """Find the downloaded VTT file in the current directory."""
    vtt_files = list(Path(".").glob("*.vtt"))
    if vtt_files:
        return vtt_files[0]
    return None


def main():
    if len(sys.argv) < 2:
        print("Usage: uv run script.py <youtube_url>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        # Get video title and channel name
        video_title, channel_name = get_video_info(url)
        temp_output = "transcript_temp"

        print(f"Video: {video_title}")
        print(f"Channel: {channel_name}")

        # List available subtitles
        list_subtitles(url)

        # Download subtitles
        if not download_subtitles(url, temp_output):
            sys.exit(1)

        # Find the downloaded VTT file
        vtt_file = find_vtt_file()
        if not vtt_file:
            print("[WARN] No VTT file found after download")
            sys.exit(1)

        # Create output directory: youtube/{channel_name}/
        output_dir = Path("youtube") / channel_name
        output_dir.mkdir(parents=True, exist_ok=True)

        # Convert to markdown with timestamps
        output_file = output_dir / f"transcript-{video_title}.md"
        convert_vtt_to_markdown(vtt_file, output_file, video_title, url)

        print(f"[OK] Saved to: {output_file}")

        # Clean up temporary VTT file
        os.remove(vtt_file)
        print("[OK] Cleaned up temporary VTT file")
        print("[OK] Complete!")

    except subprocess.CalledProcessError as e:
        print(f"Error running yt-dlp: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
