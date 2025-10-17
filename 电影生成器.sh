#!/bin/bash
echo "🎬 电影生成器（Termux 真出片版）..."
echo "1) 科幻 2) 爱情 3) 悬疑 4) 全都要（连放 3 段）"
read -p "请输入 1-4：" choice

# 如果选 4→循环 3 次
for i in $(seq 1 $([ "$choice" == "4" ] && echo 3 || echo 1)); do
  genre=$([ "$choice" == "4" ] && echo $i || echo $choice)
  python3 -c "
import json,datetime,os
g={'1':'sci-fi','2':'romance','3':'mystery'}
gname=g[str($genre)]
script={
  'title':f'小白{gname}电影_{datetime.datetime.now().strftime(\"%m%d\")}_$i',
  'genre':gname,
  'scenes':['开场','冲突','高潮','结尾'],
  'world':{'主角':'AI','地点':'未来城','时间':'2088'}
}
with open(f'world_model_$i.json','w',encoding='utf-8') as f:
  json.dump(script,f,ensure_ascii=False,indent=2)
print(f'✅ 剧本_$i 已保存')
"

  # 真生成 10 秒 mp4（手机算力）
  ffmpeg -f lavfi -i testsrc=duration=10:size=720x1280:rate=30 \
         -vf "drawtext=text='小白${genre}电影_$i':fontsize=48:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2" \
         -c:v libx264 -pix_fmt yuv420p output_$i.mp4 -y 2>/dev/null &&
  echo "✅ 真·视频 output_$i.mp4 已生成" ||
  echo "⚠️ 视频引擎未装好，请先执行：pkg install ffmpeg -y"
done

echo "================ 电影交付报告 ================"
ls -lh output_*.mp4 2>/dev/null || echo "❌ 本次无视频，请装 ffmpeg 后重试"
echo "📲 文件路径：~/my-ai-business/我的智能体课程/output_*.mp4"
echo "=============================================="
