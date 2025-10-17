#!/bin/bash
echo "🛡️ 量子修复启动，稍等5秒..."
# 先忽略子模块警告，再自动add所有文件，再提交
git config advice.addEmbeddedRepo false
git add -A
git commit -m "量子修颜色：$(date +%m%d-%H%M%S)"
echo "✅ 红/黄代码已合并成一次新提交，下次上传即消失！"
