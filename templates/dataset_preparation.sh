#!/bin/bash

# 数据集准备模板
# 为机器学习准备训练数据

VIDEO_INPUT="$1"
OUTPUT_DIR="${2:-./dataset}"
FRAME_STEP="${3:-30}"

if [ -z "$VIDEO_INPUT" ]; then
    echo "用法: $0 <视频文件路径> [输出目录] [帧步长]"
    echo "示例: $0 training_video.mp4 ./dataset 30"
    echo "说明: 帧步长30表示每30帧提取一张图片（约每秒1-2张，取决于视频FPS）"
    exit 1
fi

if [ ! -f "$VIDEO_INPUT" ]; then
    echo "错误: 视频文件不存在: $VIDEO_INPUT"
    exit 1
fi

echo "准备机器学习数据集..."
echo "输入: $VIDEO_INPUT"
echo "输出: $OUTPUT_DIR"
echo "提取策略: 每${FRAME_STEP}帧提取一张"
echo "格式: JPG，质量: 90"

python extract_frames.py \
    --input "$VIDEO_INPUT" \
    --output "$OUTPUT_DIR" \
    --frame-step "$FRAME_STEP" \
    --format jpg \
    --quality 90 \
    --prefix "data"

echo "数据集准备完成！"
echo ""
echo "后续建议："
echo "1. 检查提取的图片质量"
echo "2. 根据需要调整帧步长参数"
echo "3. 对图片进行标注或分类"
echo "4. 将数据集划分为训练集和验证集"