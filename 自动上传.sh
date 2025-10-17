#!/bin/bash
echo "🚀 自动上传（Termux 版）..."
git add .
git commit -m "Termux 自动上传：$(date +%m%d-%H%M%S)"
git push origin main
echo "✅ 上传成功！GitHub 地址："
echo "https://github.com/lw8707/video-gen-suite"
