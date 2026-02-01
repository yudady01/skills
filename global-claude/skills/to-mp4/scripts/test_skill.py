#!/usr/bin/env python3
"""
Test script for to-mp4 skill
Verifies that all components are working correctly.
"""

import sys
import subprocess
import os
from pathlib import Path


def test_ffmpeg():
    """Test if FFmpeg is installed and accessible."""
    print("测试 1: 检查 FFmpeg 安装...")
    try:
        result = subprocess.run(
            ["ffmpeg", "-version"],
            capture_output=True,
            text=True,
            check=True
        )
        print("✅ FFmpeg 已安装")
        # Extract version
        version_line = result.stdout.split('\n')[0]
        print(f"   {version_line}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ FFmpeg 未安装")
        print("\n请安装 FFmpeg:")
        print("  macOS:   brew install ffmpeg")
        print("  Ubuntu:  sudo apt install ffmpeg")
        print("  Windows: 从 https://ffmpeg.org/download.html 下载")
        return False


def test_script_exists():
    """Test if the conversion script exists."""
    print("\n测试 2: 检查转换脚本...")
    script_path = Path(__file__).parent / "convert_to_mp4.py"
    if script_path.exists():
        print(f"✅ 转换脚本存在: {script_path}")
        return True
    else:
        print(f"❌ 转换脚本不存在: {script_path}")
        return False


def test_script_help():
    """Test if the script can show help."""
    print("\n测试 3: 测试脚本帮助功能...")
    script_path = Path(__file__).parent / "convert_to_mp4.py"
    try:
        result = subprocess.run(
            ["python3", str(script_path), "--help"],
            capture_output=True,
            text=True,
            check=True
        )
        if "将 MOV 视频转换为 MP4 格式" in result.stdout:
            print("✅ 脚本帮助功能正常")
            return True
        else:
            print("❌ 脚本帮助输出异常")
            return False
    except Exception as e:
        print(f"❌ 脚本帮助测试失败: {e}")
        return False


def test_documentation():
    """Test if all documentation files exist."""
    print("\n测试 4: 检查文档文件...")
    base_dir = Path(__file__).parent.parent

    docs = [
        ("SKILL.md", "Skill 定义文件"),
        ("README.md", "使用文档"),
        ("QUICKSTART.md", "快速开始指南"),
        ("USAGE_EXAMPLES.md", "使用示例")
    ]

    all_exist = True
    for doc_file, description in docs:
        doc_path = base_dir / doc_file
        if doc_path.exists():
            print(f"✅ {description}: {doc_file}")
        else:
            print(f"❌ {description} 不存在: {doc_file}")
            all_exist = False

    return all_exist


def main():
    """Run all tests."""
    print("="*60)
    print("to-mp4 Skill 测试")
    print("="*60)

    results = []

    # Run tests
    results.append(("FFmpeg 安装", test_ffmpeg()))
    results.append(("转换脚本", test_script_exists()))
    results.append(("脚本帮助", test_script_help()))
    results.append(("文档文件", test_documentation()))

    # Summary
    print("\n" + "="*60)
    print("测试总结")
    print("="*60)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for test_name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"{test_name}: {status}")

    print(f"\n总计: {passed}/{total} 测试通过")

    if passed == total:
        print("\n🎉 所有测试通过！skill 已准备就绪。")
        print("\n快速开始:")
        print("  python scripts/convert_to_mp4.py your_video.mov")
        return 0
    else:
        print("\n⚠️  部分测试失败，请检查上述问题。")
        return 1


if __name__ == "__main__":
    sys.exit(main())
