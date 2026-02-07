#!/usr/bin/env python3
"""
DTG i18n Key Extraction Script

Extracts i18n keys from HTML/JS files and generates translation updates.
Supports two patterns:
1. i18ndata="path.to.key"
2. translateMessageByPath("path.to.key", "default")
"""

import re
import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Set


# Common translations mapping
COMMON_TRANSLATIONS = {
    # Navigation
    "首页": "Home",
    "返回": "Return",
    "确定": "Confirm",
    "提交": "Submit",
    "保存": "Save",
    "搜索": "Search",
    "导出": "Export",
    "查看": "View",
    "详情": "Detail",
    "编辑": "Edit",
    "删除": "Delete",
    "添加": "Add",
    "新增": "Add New",

    # Account & User
    "商户": "Merchant",
    "商户管理": "Merchant Management",
    "账户名": "Account Name",
    "用户名": "Username",
    "状态": "Status",

    # Payment & Channel
    "支付通道": "Payment Channel",
    "代付通道": "Agent Pay Channel",
    "通道ID": "Channel ID",
    "通道名称": "Channel Name",
    "产品ID": "Product ID",
    "产品名称": "Product Name",
    "费率(%+单笔)": "Rate(%+per transaction)",
    "商户费率": "Merchant Rate",
    "手续费": "Service Fee",
    "元/笔": "CNY per Order",
    "单笔代付上限": "Max Single Amount",
    "单笔代付下限": "Min Single Amount",
    "单笔最大金额": "Max Single Amount",
    "单笔最小金额": "Min Single Amount",

    # Currency & Type
    "币别": "Currency Type",
    "类别": "Category",
    "类型": "Type",

    # Status
    "开启": "Enabled",
    "关闭": "Disabled",
    "启用": "Enable",
    "禁用": "Disable",
    "默认": "Default",
    "是": "Yes",
    "否": "No",
    "未设置": "Not Set",
    "全部": "All",

    # Error messages
    "请求失败": "Request Failed",
    "提示": "Tip",
}


def extract_i18n_keys(content: str) -> List[Tuple[str, str]]:
    """
    Extract i18n keys from file content.

    Returns:
        List of (key, default_text) tuples
    """
    results = []

    # Pattern 1: i18ndata="key"
    i18ndata_pattern = r'i18ndata\s*=\s*["\']([^"\']+)["\']'
    for match in re.finditer(i18ndata_pattern, content):
        key = match.group(1)
        # Try to find default text in the same element
        start = match.start()
        end = match.end()
        # Look for closing tag content
        after_match = content[end:end+100]
        text_match = re.search(r'>([^<]+)<', after_match)
        default_text = text_match.group(1).strip() if text_match else ""
        results.append((key, default_text))

    # Pattern 2: translateMessageByPath("key", "default")
    translate_pattern = r'translateMessageByPath\s*\(\s*["\']([^"\']+)["\']\s*,\s*["\']([^"\']*)["\']'
    for match in re.finditer(translate_pattern, content):
        key = match.group(1)
        default_text = match.group(2)
        results.append((key, default_text))

    return results


def get_nested_value(data: dict, path: str) -> any:
    """Get value from nested dict using dot notation."""
    keys = path.replace(':', '.').split('.')
    value = data
    for key in keys:
        if isinstance(value, dict) and key in value:
            value = value[key]
        else:
            return None
    return value


def set_nested_value(data: dict, path: str, value: any):
    """Set value in nested dict using dot notation."""
    keys = path.split('.')
    current = data
    for key in keys[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]
    current[keys[-1]] = value


def generate_english_translation(chinese_text: str) -> str:
    """Generate English translation from Chinese text."""
    if chinese_text in COMMON_TRANSLATIONS:
        return COMMON_TRANSLATIONS[chinese_text]
    # For unknown text, return a placeholder
    return f"[Translate: {chinese_text}]"


def process_file(source_file: Path, zh_json: Path, en_json: Path) -> Dict:
    """Process source file and update translation files."""
    # Read source file
    source_content = source_file.read_text(encoding='utf-8')

    # Extract i18n keys
    extracted = extract_i18n_keys(source_content)

    # Read existing translation files
    zh_data = json.loads(zh_json.read_text(encoding='utf-8'))
    en_data = json.loads(en_json.read_text(encoding='utf-8'))

    # Build Reverse Translation Memory from existing data
    # Map: Chinese Text -> English Translation
    reverse_tm = {}
    
    def build_tm(prefix, z_data, e_data):
        if isinstance(z_data, dict) and isinstance(e_data, dict):
            for k, v in z_data.items():
                if k in e_data:
                    build_tm(f"{prefix}.{k}" if prefix else k, v, e_data[k])
        elif isinstance(z_data, str) and isinstance(e_data, str):
            # Only store significant translations (skip empty or placeholders)
            if z_data and e_data and "[" not in e_data:
                reverse_tm[z_data] = e_data

    try:
        build_tm("", zh_data, en_data)
    except Exception:
        # Ignore errors during TM build, it's an optimization
        pass

    # Find missing keys
    missing_zh = []
    missing_en = []

    for key, default_text in extracted:
        # Skip empty keys
        if not key:
            continue

        # Check if key exists (handle colon separator for merchant namespace)
        lookup_key = key.replace(':', '.')

        chinese_text = ""
        if get_nested_value(zh_data, lookup_key) is None:
            chinese_text = default_text if default_text else generate_chinese_from_key(key)
            missing_zh.append((key, chinese_text))

        if get_nested_value(en_data, lookup_key) is None:
            # Strategies for English generation:
            # 1. Look up Reverse TM using explicit default text
            # 2. Look up Reverse TM using generated Chinese text
            # 3. Look up Common Dictionary
            # 4. Fallback to placeholder
            
            english = ""
            
            # Try to determine the Chinese source for lookup
            source_chinese = default_text if default_text else generate_chinese_from_key(key)
            
            if source_chinese in reverse_tm:
                english = reverse_tm[source_chinese]
            elif default_text:
                english = generate_english_translation(default_text)
            else:
                english = generate_english_from_key(key)
                
            missing_en.append((key, english))

    return {
        "missing_zh": missing_zh,
        "missing_en": missing_en,
        "extracted_keys": [(k, v) for k, v in extracted],
        "tm_stats": len(reverse_tm)
    }

def generate_chinese_from_key(key: str) -> str:
    """Generate Chinese text from key name."""
    key_lower = key.lower()
    if "status" in key_lower:
        return "状态"
    elif "chanelid" in key_lower or "channelid" in key_lower:
        return "通道ID"
    elif "chanelname" in key_lower or "channelname" in key_lower:
        return "通道名称"
    elif "balance" in key_lower and "type" in key_lower:
        return "币别"
    elif "isdefault" in key_lower:
        return "默认"
    else:
        return "[需要翻译]"


def generate_english_from_key(key: str) -> str:
    """Generate English text from key name."""
    key_lower = key.lower()
    if "status" in key_lower:
        return "Status"
    elif "chanelid" in key_lower or "channelid" in key_lower:
        return "Channel ID"
    elif "chanelname" in key_lower or "channelname" in key_lower:
        return "Channel Name"
    elif "balance" in key_lower and "type" in key_lower:
        return "Currency Type"
    elif "isdefault" in key_lower:
        return "Default"
    else:
        return "[Needs Translation]"


def main():
    if len(sys.argv) < 2:
        print("Usage: python extract-i18n.py <source_file> [zh_json] [en_json]")
        print("\nExample:")
        print("  python extract-i18n.py views/account/agentpay_passage/index.html")
        print("  python extract-i18n.py views/account/agentpay_passage/index.html zh/translation.json en/translation.json")
        sys.exit(1)

    source_file = Path(sys.argv[1])

    # Default paths logic
    if len(sys.argv) >= 4:
        zh_json = Path(sys.argv[2])
        en_json = Path(sys.argv[3])
    else:
        # Auto-detect project base and module
        try:
            # Assuming script is in .agent/skills/dtg-ui/scripts/
            project_base = Path(__file__).parent.parent.parent.parent.parent
            source_abs = source_file.resolve()
            
            if "xxpay-manage" in str(source_abs):
                lang_dir = project_base / "xxpay-manage/src/main/resources/static/x_mgr/start/json/language"
            else:
                # Agent or Merchant - default to ezpay skin if not detectable
                skin = "ezpay"
                if "724pay" in str(source_abs): skin = "724pay"
                elif "lupay" in str(source_abs): skin = "lupay"
                
                lang_dir = project_base / f"xxpay-merchant/src/main/resources/static/{skin}/x_mch/start/json/language"
            
            zh_json = lang_dir / "zh/translation.json"
            en_json = lang_dir / "en/translation.json"
        except Exception:
            # Fallback to hardcoded default if detection fails
            base_dir = Path(__file__).parent.parent.parent.parent.parent
            zh_json = base_dir / "xxpay-merchant/src/main/resources/static/ezpay/x_mch/start/json/language/zh/translation.json"
            en_json = base_dir / "xxpay-merchant/src/main/resources/static/ezpay/x_mch/start/json/language/en/translation.json"

    if not source_file.exists():
        print(f"Error: Source file not found: {source_file}")
        sys.exit(1)

    if not zh_json.exists():
        print(f"Error: Chinese translation file not found: {zh_json}")
        sys.exit(1)

    if not en_json.exists():
        print(f"Error: English translation file not found: {en_json}")
        sys.exit(1)

    # Process
    result = process_file(source_file, zh_json, en_json)

    # Print results
    print("\n" + "="*60)
    print("i18n Key Extraction Results")
    print("="*60)
    print(f"\nSource File: {source_file}")
    print(f"Total keys extracted: {len(result['extracted_keys'])}")

    if result['missing_zh']:
        print(f"\nMissing Chinese translations: {len(result['missing_zh'])}")
        for key, text in result['missing_zh']:
            print(f"  - {key}: {text}")

    if result['missing_en']:
        print(f"\nMissing English translations: {len(result['missing_en'])}")
        for key, text in result['missing_en']:
            print(f"  - {key}: {text}")

    if not result['missing_zh'] and not result['missing_en']:
        print("\n✓ All translations are complete!")

    print("\n" + "="*60)
    print("Translation Summary Table")
    print("="*60)
    print(f"{'Key Path':<45} | {'Chinese':<20} | {'English':<25}")
    print("-"*95)

    for key, _ in result['extracted_keys']:
        lookup_key = key.replace(':', '.')
        zh_data = json.loads(zh_json.read_text(encoding='utf-8'))
        en_data = json.loads(en_json.read_text(encoding='utf-8'))
        zh_val = get_nested_value(zh_data, lookup_key) or "[missing]"
        en_val = get_nested_value(en_data, lookup_key) or "[missing]"
        print(f"{key:<45} | {zh_val:<20} | {en_val:<25}")


if __name__ == "__main__":
    main()
