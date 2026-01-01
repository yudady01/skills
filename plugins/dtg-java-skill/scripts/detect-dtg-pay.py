#!/usr/bin/env python3
"""
dtg-pay 项目检测脚本 (Python 版本)

功能：检测当前目录是否为 dtg-pay 项目
输出：JSON 格式的检测结果
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Tuple


def detect_dtg_pay(project_path: str = None) -> Tuple[bool, str]:
    """
    检测指定目录是否为 dtg-pay 项目

    Args:
        project_path: 要检测的项目路径，默认为当前工作目录

    Returns:
        (检测结果, 检测原因)
    """
    if project_path is None:
        project_path = os.getcwd()

    project_path = os.path.abspath(project_path)
    dir_name = os.path.basename(project_path)

    # 1. 检查目录名称
    if "dtg-pay" in dir_name.lower() or "xxpay" in dir_name.lower():
        return True, f"目录名称匹配: {dir_name}"

    # 2. 检查 pom.xml 是否包含 Spring Boot 和 Dubbo
    pom_file = os.path.join(project_path, "pom.xml")
    if os.path.exists(pom_file):
        try:
            with open(pom_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if "spring-boot-starter-parent" in content and "dubbo-spring-boot-starter" in content:
                    return True, "检测到 Spring Boot + Dubbo 配置"
        except Exception:
            pass

    # 3. 检查父目录
    parent_dir = os.path.dirname(project_path)
    parent_name = os.path.basename(parent_dir)
    if "dtg-pay" in parent_name.lower() or "xxpay" in parent_name.lower():
        return True, f"父目录名称匹配: {parent_name}"

    # 4. 检查是否存在 dtg-pay 特征模块目录
    characteristic_modules = [
        "xxpay-pay",
        "xxpay-gateway",
        "xxpay-shop",
        "xxpay-common",
        "xxpay-service"
    ]

    for module in characteristic_modules:
        if os.path.exists(os.path.join(project_path, module)):
            return True, f"检测到 dtg-pay 特征模块目录: {module}"

    return False, "未检测到 dtg-pay 项目特征"


def main():
    """主程序"""
    if len(sys.argv) > 1 and sys.argv[1] in ["--help", "-h"]:
        print("用法: python3 detect-dtg-pay.py [项目目录路径]")
        print("")
        print("检测指定目录是否为 dtg-pay 项目")
        print("默认检测当前工作目录")
        print("")
        print("检测标准：")
        print("  1. 目录名称包含 'dtg-pay' 或 'xxpay'")
        print("  2. pom.xml 包含 Spring Boot 和 Dubbo 依赖")
        print("  3. 父目录名称匹配")
        print("  4. 包含 dtg-pay 特征模块目录")
        print("")
        print("返回值：")
        print("  0 - 检测到 dtg-pay 项目")
        print("  1 - 未检测到")
        sys.exit(0)

    project_path = sys.argv[1] if len(sys.argv) > 1 else None
    detected, reason = detect_dtg_pay(project_path)

    result = {
        "detected": detected,
        "project_path": os.path.abspath(project_path) if project_path else os.getcwd(),
        "reason": reason,
        "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if detected else 1)


if __name__ == "__main__":
    main()
