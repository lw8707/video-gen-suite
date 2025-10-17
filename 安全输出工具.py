#!/usr/bin/env python3
"""
安全输出工具 - 过滤特殊字符，避免终端和模型问题
"""
import re
import subprocess

def safe_git_status():
    """安全的Git状态检查"""
    result = subprocess.run(['git', 'status', '--porcelain'], 
                          capture_output=True, text=True)
    lines = result.stdout.strip().split('\n') if result.stdout else []
    
    # 过滤和清理输出
    clean_lines = []
    for line in lines:
        # 移除特殊字符和八进制转义
        clean_line = re.sub(r'\\[0-7]{3}', '', line)
        clean_line = clean_line.encode('utf-8', 'ignore').decode('utf-8')
        clean_lines.append(clean_line)
    
    return clean_lines

def safe_git_log(count=3):
    """安全的Git日志检查"""
    result = subprocess.run(['git', 'log', f'--oneline', f'-{count}'], 
                          capture_output=True, text=True)
    lines = result.stdout.strip().split('\n') if result.stdout else []
    
    clean_lines = []
    for line in lines:
        # 确保输出安全
        clean_line = line.encode('utf-8', 'ignore').decode('utf-8')
        clean_lines.append(clean_line)
    
    return clean_lines

def main():
    print("🔒 安全系统状态检查")
    
    print("\n📊 Git状态:")
    status_lines = safe_git_status()
    if status_lines:
        for line in status_lines[:5]:  # 只显示前5行
            print(f"  {line}")
    else:
        print("  ✅ 工作目录干净")
    
    print("\n📜 最近提交:")
    log_lines = safe_git_log(3)
    for line in log_lines:
        print(f"  {line}")
    
    print(f"\n🎯 系统状态: {'正常' if not status_lines else '有未提交更改'}")

if __name__ == "__main__":
    main()
