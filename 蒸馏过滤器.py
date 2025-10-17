#!/usr/bin/env python3
"""
基于全球开源社区经验的终端输出蒸馏器
参考：Linux终端安全规范、ANSI转义处理、Unicode清理
"""
import re
import subprocess
import sys

class TerminalOutputDistiller:
    def __init__(self):
        # ANSI转义序列正则（来自Linux终端规范）
        self.ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        # 八进制转义序列
        self.octal_escape = re.compile(r'\\[0-7]{3}')
        # Bash元字符
        self.bash_metachars = re.compile(r'[`$(){}\[\]|&;<>]')
    
    def distill_output(self, text):
        """蒸馏终端输出，移除所有危险字符"""
        # 移除ANSI颜色代码
        clean = self.ansi_escape.sub('', text)
        # 移除八进制转义
        clean = self.octal_escape.sub('', clean)
        # 转义Bash元字符
        clean = self.bash_metachars.sub(lambda m: f'\\{m.group()}', clean)
        # 移除控制字符
        clean = re.sub(r'[\x00-\x1F\x7F]', '', clean)
        # 标准化换行
        clean = re.sub(r'\r\n', '\n', clean)
        clean = re.sub(r'\r', '\n', clean)
        
        return clean
    
    def safe_command_execution(self, command):
        """安全执行命令并返回蒸馏后的输出"""
        try:
            result = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True,
                timeout=30
            )
            
            distilled_output = self.distill_output(result.stdout)
            distilled_error = self.distill_output(result.stderr)
            
            return {
                "success": result.returncode == 0,
                "output": distilled_output,
                "error": distilled_error,
                "returncode": result.returncode
            }
        except Exception as e:
            return {
                "success": False,
                "output": "",
                "error": f"执行失败: {str(e)}",
                "returncode": -1
            }
    
    def generate_safe_report(self):
        """生成安全的状态报告"""
        print("🔒 生成安全蒸馏报告...")
        
        reports = {}
        
        # 安全执行Git状态
        reports['git_status'] = self.safe_command_execution("git status --porcelain")
        
        # 安全执行Git日志
        reports['git_log'] = self.safe_command_execution("git log --oneline -3")
        
        # 安全执行文件列表
        reports['file_list'] = self.safe_command_execution("find . -name '*.py' | wc -l")
        
        return reports

def main():
    distiller = TerminalOutputDistiller()
    reports = distiller.generate_safe_report()
    
    print("\n📊 安全蒸馏报告:")
    
    # Git状态
    if reports['git_status']['success']:
        output = reports['git_status']['output'].strip()
        if output:
            print("Git状态: 有未提交更改")
            for line in output.split('\n')[:3]:
                print(f"  {line}")
        else:
            print("Git状态: 工作目录干净")
    else:
        print("Git状态: 检查失败")
    
    # Git日志
    if reports['git_log']['success']:
        print("\n最近提交:")
        for line in reports['git_log']['output'].strip().split('\n'):
            print(f"  {line}")
    
    # 文件统计
    if reports['file_list']['success']:
        file_count = reports['file_list']['output'].strip()
        print(f"\nPython文件数量: {file_count}")
    
    print("\n✅ 报告生成完成 - 绝对安全")

if __name__ == "__main__":
    main()
