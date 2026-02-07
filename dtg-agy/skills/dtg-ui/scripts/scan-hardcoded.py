#!/usr/bin/env python3
"""
DTG Hardcoded Chinese Scanner
Scans HTML/JS files for hardcoded Chinese characters that are NOT
wrapped in i18ndata or translateMessageByPath.
"""

import re
import sys
import os
from pathlib import Path

# Regex to match Chinese characters
CHINESE_PATTERN = re.compile(r'[\u4e00-\u9fff]+')

# Regex to ignore (already internationalized)
# Matches: i18ndata="...", translateMessageByPath("...", "...")
IGNORE_PATTERNS = [
    r'i18ndata\s*=\s*["\'][^"\']*["\']',
    r'translateMessageByPath\s*\(\s*["\'][^"\']*["\']\s*,\s*["\']([^"\']*)["\']',
    r'<!--.*?-->',  # HTML comments
    r'//.*',        # JS comments
    r'/\*[\s\S]*?\*/' # Multi-line comments
]

def scan_file(file_path: Path):
    try:
        content = file_path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        return []

    errors = []
    
    # Mask ignored areas to prevent false positives
    masked_content = content
    for pattern in IGNORE_PATTERNS:
        masked_content = re.sub(pattern, lambda m: " " * len(m.group(0)), masked_content)

    # Find Chinese in remaining content
    lines = masked_content.split('\n')
    for i, line in enumerate(lines):
        matches = CHINESE_PATTERN.findall(line)
        if matches:
            original_line = content.split('\n')[i].strip()
            # Double check: ensure it's not Inside value of i18ndata tag content which is valid 
            # e.g. <span i18ndata="key">中文</span> is VALID.
            # But the masking above only masked the attribute i18ndata="key". 
            # So "中文" is still visible.
            # We need a smarter way or just flag it for review.
            
            # Refined strategy: 
            # If line contains i18ndata, assumes the Chinese in it is valid default text (simplified approach).
            if 'i18ndata=' in original_line:
                continue

            errors.append({
                'line': i + 1,
                'content': matches,
                'code': original_line[:100]
            })
    
    return errors

def main():
    if len(sys.argv) < 2:
        print("Usage: python scan-hardcoded.py <directory_or_file>")
        sys.exit(1)

    target = Path(sys.argv[1])
    files_to_scan = []

    if target.is_file():
        files_to_scan.append(target)
    else:
        for root, _, files in os.walk(target):
            for file in files:
                if file.endswith(('.html', '.js')):
                    files_to_scan.append(Path(root) / file)

    print(f"Scanning {len(files_to_scan)} files for hardcoded Chinese...\n")
    
    total_issues = 0
    for file_path in files_to_scan:
        issues = scan_file(file_path)
        if issues:
            print(f"📄 {file_path}")
            for issue in issues:
                total_issues += 1
                print(f"  Line {issue['line']}: Found {issue['content']}")
                print(f"    Code: {issue['code']}...")
            print("")

    if total_issues == 0:
        print("✅ No hardcoded Chinese found!")
    else:
        print(f"❌ Found {total_issues} potential hardcoded strings.")
        sys.exit(1)

if __name__ == "__main__":
    main()
