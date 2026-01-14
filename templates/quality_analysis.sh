#!/bin/bash

# 视频质量分析模板
# 高质量提取帧用于视频分析

VIDEO_INPUT="$1"
OUTPUT_DIR="${2:-./analysis_frames}"

if [ -z "$VIDEO_INPUT" ]; then
    echo "用法: $0 <视频文件路径> [输出目录]"
    echo "示例: $0 footage.mp4 ./analysis_frames"
    exit 1
fi

if [ ! -f "$VIDEO_INPUT" ]; then
    echo "错误: 视频文件不存在: $VIDEO_INPUT"
    exit 1
fi

echo "视频质量分析..."
echo "输入: $VIDEO_INPUT"
echo "输出: $OUTPUT_DIR"
echo "提取频率: 每0.5秒一帧"
echo "格式: PNG（无损）"

python extract_frames.py \
    --input "$VIDEO_INPUT" \
    --output "$OUTPUT_DIR" \
    --interval 0.5 \
    --format png \
    --prefix "analysis"

echo "视频质量分析帧提取完成！"