#!/bin/bash
echo "🚀 一键上传所有成果到 GitHub..."
cd ~/my-ai-business/我的智能体课程

# 1. 添加所有文件（包括新文档、新脚本）
git add .

# 2. 创建统一提交信息（带日期）
git commit -m "第19轮统一成果上传: $(date +%Y%m%d_%H%M%S)"

# 3. 推送到 GitHub（自动连接已配置）
git push origin main

# 4. 显示结果
echo "✅ 上传完成！仓库地址："
echo "https://github.com/lw8707/gh-repo-create-autocode-video-gen---public"
