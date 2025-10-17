#!/bin/bash
echo "🚀 小白专用：恢复原样自动上传（用回公钥）..."

# 1. 把远程地址改回 ssh 格式（公钥自动认证）
git remote set-url origin git@github.com:lw8707/video-gen-suite.git

# 2. 立即测试上传（不用密码）
git add .
git commit -m "恢复原样上传: $(date +%m%d_%H%M%S)"
git push origin main

# 3. 结果提示
if [ $? -eq 0 ]; then
    echo "✅ 原样上传成功！又可以用回老脚本了"
else
    echo "⚠️  公钥好像有问题，我帮你再生成一次"
    # 重新生成公钥（一路回车即可）
    ssh-keygen -t ed25519 -C "lw8707@github.com" -f ~/.ssh/id_ed25519 -N ""
    # 把新公钥显示出来，复制到 GitHub 即可
    echo "📋 下面这段就是新公钥，全选复制："
    cat ~/.ssh/id_ed25519.pub
    echo ""
    echo "👉 打开 https://github.com/settings/ssh/new"
    echo "👉 把上面内容粘贴进去，保存即可"
    echo "👉 保存完再运行一次本脚本就彻底恢复"
fi
