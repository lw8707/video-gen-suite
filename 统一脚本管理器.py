#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一脚本管理器 - 小白友好，对话可续，永不重复
运行这个脚本，就能知道前面做了什么，下一步该做什么
"""

import os
import subprocess
import time

# 统一脚本清单（只增不删）
SCRIPTS = {
    "1": ("全面诊断.sh", "一键检查项目健康状态"),
    "2": ("自动上传.sh", "一键推送GitHub"),
    "3": ("云盘同步检查.sh", "检查手机云盘备份"),
    "4": ("红色代码预防器.sh", "自动修复Git红色代码"),
    "5": ("项目结构优化.sh", "创建标准目录结构"),
    "6": ("技术雷达升级.sh", "集成全球最新技术"),
    "7": ("安全备份系统.sh", "三重备份"),
    "8": ("系统完整性验证.sh", "检查核心文件"),
    "9": ("第19轮紧急修复.sh", "重建核心系统"),
}

def print_banner():
    print("\n" + "="*50)
    print("🎯 统一脚本管理器 - 小白友好，对话可续")
    print("="*50)
    print("📖 先看文档: 统一项目历史文档.md")
    print("🧑‍💻 小白一句话: 先运行1，再运行2，其他的都不用管")
    print("="*50)

def list_scripts():
    print("\n📋 可用脚本清单（输入数字即可运行）:")
    for key, (name, desc) in SCRIPTS.items():
        print(f"  {key}. {name} - {desc}")

def run_script(choice):
    script_name, desc = SCRIPTS.get(choice, (None, None))
    if not script_name:
        print("❌ 输入错误，请重新输入数字")
        return

    print(f"\n🚀 正在运行: {script_name} - {desc}")
    if os.path.exists(script_name):
        subprocess.run(["bash", script_name])
    else:
        print(f"❌ 脚本不存在: {script_name}，请先修复项目结构")

def main():
    print_banner()
    list_scripts()

    while True:
        choice = input("\n请输入要运行的脚本编号（输入q退出）: ").strip()
        if choice.lower() == 'q':
            print("✅ 退出统一脚本管理器，再见！")
            break
        run_script(choice)
        time.sleep(1)
        print("\n" + "-"*50)
        list_scripts()

if __name__ == "__main__":
    main()
