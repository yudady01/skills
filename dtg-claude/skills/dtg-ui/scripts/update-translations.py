#!/usr/bin/env python3
"""
DTG i18n Translation Update Script

Automatically updates zh/translation.json and en/translation.json
with missing i18n keys extracted from source files.
"""

import json
import sys
from pathlib import Path


def set_nested_value(data: dict, path: str, value: str):
    """Set value in nested dict using dot notation."""
    # Handle colon separator for merchant namespace
    path = path.replace(':', '.')
    keys = path.split('.')
    current = data
    for key in keys[:-1]:
        if key not in current:
            current[key] = {}
        elif not isinstance(current[key], dict):
            # Overwrite if not a dict
            current[key] = {}
        current = current[key]
    current[keys[-1]] = value


def update_json_file(json_path: Path, updates: list, language: str):
    """Update JSON file with new translations."""
    # Read existing data
    data = {}
    if json_path.exists():
        data = json.loads(json_path.read_text(encoding='utf-8'))

    # Apply updates
    for key, value in updates:
        set_nested_value(data, key, value)

    # Write back with proper formatting
    json_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + '\n',
        encoding='utf-8'
    )

    print(f"✓ Updated {language} translation file: {json_path}")


def main():
    if len(sys.argv) < 4:
        print("Usage: python update-translations.py <zh_json> <en_json> <updates_json>")
        print("\nUpdates JSON format:")
        print('{')
        print('  "zh": {"key1": "中文1", "key2": "中文2"},')
        print('  "en": {"key1": "English1", "key2": "English2"}')
        print('}')
        sys.exit(1)

    zh_json_path = Path(sys.argv[1])
    en_json_path = Path(sys.argv[2])
    updates_json_path = Path(sys.argv[3])

    # Read updates
    updates = json.loads(updates_json_path.read_text(encoding='utf-8'))

    # Update files
    if 'zh' in updates:
        zh_updates = [(k, v) for k, v in updates['zh'].items()]
        update_json_file(zh_json_path, zh_updates, 'Chinese')

    if 'en' in updates:
        en_updates = [(k, v) for k, v in updates['en'].items()]
        update_json_file(en_json_path, en_updates, 'English')

    print("\n✓ Translation files updated successfully!")


if __name__ == "__main__":
    main()
