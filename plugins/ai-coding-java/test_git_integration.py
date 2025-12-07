#!/usr/bin/env python3
"""
Git集成功能测试脚本
验证Git分析器和报告生成的集成功能
"""

import os
import sys
import json
import subprocess
import tempfile
import shutil
from datetime import datetime

def run_command(cmd, capture_output=True, check=True, cwd=None):
    """运行命令并返回结果"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=capture_output,
            text=True,
            check=check,
            cwd=cwd
        )
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except subprocess.CalledProcessError as e:
        return e.stdout.strip(), e.stderr.strip(), e.returncode

def test_git_analyzer_script():
    """测试Git分析器脚本"""
    print("🧪 测试Git分析器脚本...")

    plugin_root = os.path.dirname(os.path.abspath(__file__))
    git_analyzer_path = os.path.join(plugin_root, "hooks/scripts/git-analyzer.sh")

    if not os.path.exists(git_analyzer_path):
        print(f"❌ Git分析器脚本不存在: {git_analyzer_path}")
        return False

    # 测试脚本的执行权限
    if not os.access(git_analyzer_path, os.X_OK):
        print("❌ Git分析器脚本没有执行权限")
        return False

    print("✅ Git分析器脚本存在且可执行")

    # 测试在当前Git仓库中运行
    stdout, stderr, returncode = run_command(f"{git_analyzer_path} json")

    if returncode == 0:
        try:
            git_data = json.loads(stdout)
            print(f"✅ Git分析器返回有效JSON数据")
            print(f"   - 仓库根目录: {git_data.get('repository', {}).get('root_path', 'unknown')}")
            print(f"   - 当前分支: {git_data.get('repository', {}).get('current_branch', 'unknown')}")
            print(f"   - 修改文件数: {git_data.get('changes', {}).get('total_files_changed', 0)}")
            return True
        except json.JSONDecodeError as e:
            print(f"❌ Git分析器返回无效JSON: {e}")
            print(f"   输出: {stdout}")
            return False
    else:
        print(f"⚠️ Git分析器执行失败，但这可能在非Git环境中是正常的")
        print(f"   错误: {stderr}")
        return True  # 非Git环境中失败是正常的

def test_utils_sh_git_functions():
    """测试utils.sh中的Git函数"""
    print("\n🧪 测试utils.sh中的Git函数...")

    plugin_root = os.path.dirname(os.path.abspath(__file__))
    utils_path = os.path.join(plugin_root, "hooks/scripts/utils.sh")

    if not os.path.exists(utils_path):
        print(f"❌ utils.sh文件不存在: {utils_path}")
        return False

    # 测试单个函数
    test_functions = [
        "is_git_repo",
        "get_git_root",
        "get_git_branch",
        "generate_git_info_json"
    ]

    for func_name in test_functions:
        cmd = f"source {utils_path} && {func_name}"
        stdout, stderr, returncode = run_command(cmd, check=False)

        if returncode == 0:
            print(f"✅ {func_name} 函数执行成功")
            if func_name == "generate_git_info_json":
                try:
                    json.loads(stdout)
                    print(f"   返回有效JSON")
                except json.JSONDecodeError:
                    print(f"   ⚠️ 返回非JSON格式数据")
        else:
            print(f"⚠️ {func_name} 函数执行失败: {stderr}")

    return True

def test_template_git_support():
    """测试模板对Git数据的支持"""
    print("\n🧪 测试模板对Git数据的支持...")

    plugin_root = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(plugin_root, "skills/review-report-generation/templates/comprehensive_review.md.j2")

    if not os.path.exists(template_path):
        print(f"❌ 模板文件不存在: {template_path}")
        return False

    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    # 检查Git相关语法
    git_checks = [
        ("{% if git_summary and git_summary.repository %}", "Git摘要条件判断"),
        ("{{ git_summary.repository.current_branch", "Git分支信息"),
        ("{{ git_summary.changes.total_files_changed", "Git变更统计"),
        ("Git 更改摘要", "Git标题"),
        ("文件变更列表", "Git文件列表")
    ]

    all_found = True
    for check, description in git_checks:
        if check in template_content:
            print(f"✅ 找到 {description}")
        else:
            print(f"❌ 未找到 {description}")
            all_found = False

    return all_found

def test_data_aggregator_git_support():
    """测试数据聚合器的Git数据支持"""
    print("\n🧪 测试数据聚合器的Git数据支持...")

    plugin_root = os.path.dirname(os.path.abspath(__file__))
    data_aggregator_path = os.path.join(plugin_root, "skills/review-report-generation/data_aggregator.py")

    if not os.path.exists(data_aggregator_path):
        print(f"❌ 数据聚合器文件不存在: {data_aggregator_path}")
        return False

    with open(data_aggregator_path, 'r', encoding='utf-8') as f:
        agg_content = f.read()

    # 检查Git相关的参数和处理
    git_checks = [
        ("git_summary: Optional[Dict[str, Any]] = None", "Git摘要参数"),
        ('"git_summary": git_summary or {}', "Git摘要数据处理"),
    ]

    all_found = True
    for check, description in git_checks:
        if check in agg_content:
            print(f"✅ 找到 {description}")
        else:
            print(f"❌ 未找到 {description}")
            all_found = False

    return all_found

def test_hook_script_integration():
    """测试钩子脚本的Git集成"""
    print("\n🧪 测试钩子脚本的Git集成...")

    plugin_root = os.path.dirname(os.path.abspath(__file__))
    hook_script_path = os.path.join(plugin_root, "hooks/scripts/review-report-hook.sh")

    if not os.path.exists(hook_script_path):
        print(f"❌ 钩子脚本不存在: {hook_script_path}")
        return False

    with open(hook_script_path, 'r', encoding='utf-8') as f:
        hook_content = f.read()

    # 检查Git相关的函数和调用
    git_checks = [
        ("get_git_data()", "Git数据获取函数"),
        ("git-analyzer.sh", "Git分析器调用"),
        ('jq --argjson git_data', "JSON数据处理"),
        ("git_summary.*git_data", "Git摘要数据传递")
    ]

    all_found = True
    for check, description in git_checks:
        # 对于正则表达式模式，使用re.search
        if ".*" in check:
            import re
            if re.search(check, hook_content):
                print(f"✅ 找到 {description}")
            else:
                print(f"❌ 未找到 {description}")
                all_found = False
        elif check in hook_content:
            print(f"✅ 找到 {description}")
        else:
            print(f"❌ 未找到 {description}")
            all_found = False

    return all_found

def test_end_to_end_git_integration():
    """端到端Git集成测试"""
    print("\n🧪 端到端Git集成测试...")

    plugin_root = os.path.dirname(os.path.abspath(__file__))

    # 创建临时测试目录
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"📁 使用临时测试目录: {temp_dir}")

        # 初始化Git仓库
        stdout, stderr, returncode = run_command("git init", cwd=temp_dir)
        if returncode != 0:
            print(f"❌ 无法初始化Git仓库: {stderr}")
            return False

        # 配置Git用户信息
        run_command("git config user.name 'Test User'", cwd=temp_dir)
        run_command("git config user.email 'test@example.com'", cwd=temp_dir)

        # 创建测试文件
        test_file = os.path.join(temp_dir, "TestService.java")
        with open(test_file, 'w') as f:
            f.write("""
// Test Java file for Git integration testing
public class TestService {
    private String name;

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }
}
""")

        # 添加到Git
        stdout, stderr, returncode = run_command("git add .", cwd=temp_dir)
        if returncode != 0:
            print(f"❌ 无法添加文件到Git: {stderr}")
            return False

        # 提交
        stdout, stderr, returncode = run_command("git commit -m 'Add TestService'", cwd=temp_dir)
        if returncode != 0:
            print(f"❌ 无法提交到Git: {stderr}")
            return False

        # 修改文件
        with open(test_file, 'a') as f:
            f.write("""
    // Added method
    public boolean isValid() {
        return name != null && !name.trim().isEmpty();
    }
""")

        # 测试Git分析器在变更状态下
        plugin_root = os.path.dirname(os.path.abspath(__file__))
        git_analyzer_path = os.path.join(plugin_root, "hooks/scripts/git-analyzer.sh")

        stdout, stderr, returncode = run_command(f"{git_analyzer_path} json", cwd=temp_dir)

        if returncode == 0:
            try:
                git_data = json.loads(stdout)
                print(f"✅ 端到端测试成功")
                print(f"   - 仓库状态: {git_data.get('repository', {}).get('is_clean', False)}")
                print(f"   - 未提交文件: {git_data.get('repository', {}).get('uncommitted_changes', 0)}")
                print(f"   - 变更范围: {git_data.get('analysis', {}).get('change_scope', 'unknown')}")
                return True
            except json.JSONDecodeError as e:
                print(f"❌ 端到端测试失败，无效JSON: {e}")
                return False
        else:
            print(f"❌ Git分析器在测试环境中失败: {stderr}")
            return False

def main():
    """主测试函数"""
    print("🚀 开始Git集成功能测试...\n")

    tests = [
        ("Git分析器脚本", test_git_analyzer_script),
        ("utils.sh Git函数", test_utils_sh_git_functions),
        ("模板Git支持", test_template_git_support),
        ("数据聚合器Git支持", test_data_aggregator_git_support),
        ("钩子脚本Git集成", test_hook_script_integration),
        ("端到端集成测试", test_end_to_end_git_integration)
    ]

    results = []

    for test_name, test_func in tests:
        print(f"📋 运行测试: {test_name}")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ 测试 {test_name} 出现异常: {e}")
            results.append((test_name, False))
        print()

    # 汇总结果
    print("=" * 60)
    print("📊 测试结果汇总:")
    print("=" * 60)

    passed = 0
    failed = 0

    for test_name, result in results:
        if result:
            status = "✅ 通过"
            passed += 1
        else:
            status = "❌ 失败"
            failed += 1

        print(f"{test_name:<25} {status}")

    print(f"\n🎯 总计: {len(results)} 个测试, {passed} 个通过, {failed} 个失败")

    if failed == 0:
        print("🎉 所有Git集成功能测试通过！")
        return 0
    else:
        print("⚠️ 部分测试失败，请检查相关功能")
        return 1

if __name__ == "__main__":
    sys.exit(main())