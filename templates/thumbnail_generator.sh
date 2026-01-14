#!/bin/bash

# 缩略图生成模板
# 从视频中提取关键帧生成缩略图

VIDEO_INPUT="$1"
OUTPUT_DIR="${2:-./thumbnails}"
THUMBNAIL_WIDTH="${3:-320}"
THUMBNAIL_HEIGHT="${4:-180}"

if [ -z "$VIDEO_INPUT" ]; then
    echo "用法: $0 <视频文件路径> [输出目录] [宽度] [高度]"
    echo "示例: $0 movie.mp4 ./thumbnails 320 180"
    exit 1
fi

if [ ! -f "$VIDEO_INPUT" ]; then
    echo "错误: 视频文件不存在: $VIDEO_INPUT"
    exit 1
fi

echo "生成视频缩略图..."
echo "输入: $VIDEO_INPUT"
echo "输出: $OUTPUT_DIR"
echo "缩略图尺寸: ${THUMBNAIL_WIDTH}x${THUMBNAIL_HEIGHT}"
echo "提取频率: 每10秒一帧"
echo "格式: JPG，质量: 80"

python extract_frames.py \
    --input "$VIDEO_INPUT" \
    --output "$OUTPUT_DIR" \
    --interval 10.0 \
    --format jpg \
    --quality 80 \
    --prefix "thumb" \
    --resize "${THUMBNAIL_WIDTH}x${THUMBNAIL_HEIGHT}"

echo "缩略图生成完成！"