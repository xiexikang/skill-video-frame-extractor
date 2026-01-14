#!/bin/bash

# 批量视频帧提取脚本
# 从指定目录中提取所有视频文件的帧

INPUT_DIR="${1:-./videos}"
OUTPUT_BASE_DIR="${2:-./extracted_frames}"
INTERVAL="${3:-1.0}"
FORMAT="${4:-jpg}"

if [ ! -d "$INPUT_DIR" ]; then
    echo "错误: 输入目录不存在: $INPUT_DIR"
    exit 1
fi

mkdir -p "$OUTPUT_BASE_DIR"

# 支持的视频格式
VIDEO_EXTENSIONS="mp4 avi mov mkv flv wmv webm"

extracted_count=0

for ext in $VIDEO_EXTENSIONS; do
    for video_file in "$INPUT_DIR"/*.$ext; do
        if [ -f "$video_file" ]; then
            filename=$(basename "$video_file" .$ext)
            output_dir="$OUTPUT_BASE_DIR/$filename"
            
            echo "正在处理: $video_file"
            echo "输出目录: $output_dir"
            
            python extract_frames.py \
                --input "$video_file" \
                --output "$output_dir" \
                --interval "$INTERVAL" \
                --format "$FORMAT"
            
            extracted_count=$((extracted_count + 1))
            echo "----------------------------------------"
        fi
    done
done

echo "批量提取完成！共处理 $extracted_count 个视频文件"
echo "输出目录: $OUTPUT_BASE_DIR"