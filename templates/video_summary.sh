#!/bin/bash

# 视频摘要生成模板
# 从视频中每秒提取一帧，用于生成视频摘要

VIDEO_INPUT="$1"
OUTPUT_DIR="${2:-./video_summary}"

if [ -z "$VIDEO_INPUT" ]; then
    echo "用法: $0 <视频文件路径> [输出目录]"
    echo "示例: $0 movie.mp4 ./summary_frames"
    exit 1
fi

if [ ! -f "$VIDEO_INPUT" ]; then
    echo "错误: 视频文件不存在: $VIDEO_INPUT"
    exit 1
fi

echo "生成视频摘要..."
echo "输入: $VIDEO_INPUT"
echo "输出: $OUTPUT_DIR"
echo "提取频率: 每秒一帧"
echo "格式: JPG，质量: 85"

python extract_frames.py \
    --input "$VIDEO_INPUT" \
    --output "$OUTPUT_DIR" \
    --interval 1.0 \
    --format jpg \
    --quality 85 \
    --prefix "summary"

echo "视频摘要生成完成！"