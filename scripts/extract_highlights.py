#!/usr/bin/env python3
"""
视频高光片段帧提取脚本
自动检测视频中的场景变化并提取关键帧
"""

import cv2
import numpy as np
import os
import sys
from pathlib import Path
import argparse


def detect_scenes(video_path, threshold=30.0):
    """
    检测视频中的场景变化
    
    Args:
        video_path: 视频文件路径
        threshold: 场景变化阈值
        
    Returns:
        场景变化的时间戳列表
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"无法打开视频文件: {video_path}")
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    scene_changes = []
    prev_frame = None
    
    print("正在检测场景变化...")
    
    for frame_idx in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            break
        
        # 转换为灰度图
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        if prev_frame is not None:
            # 计算帧间差异
            diff = cv2.absdiff(prev_frame, gray)
            diff_score = np.mean(diff)
            
            if diff_score > threshold:
                timestamp = frame_idx / fps
                scene_changes.append(timestamp)
                print(f"检测到场景变化: {timestamp:.2f}s (帧 {frame_idx})")
        
        prev_frame = gray
        
        # 显示进度
        if frame_idx % 100 == 0:
            progress = (frame_idx / total_frames) * 100
            print(f"\r进度: {progress:.1f}%", end="", flush=True)
    
    cap.release()
    print(f"\n检测到 {len(scene_changes)} 个场景变化")
    
    return scene_changes


def extract_highlight_frames(video_path, output_dir, scene_changes, format="jpg", quality=95):
    """
    从场景变化点提取帧
    
    Args:
        video_path: 视频文件路径
        output_dir: 输出目录
        scene_changes: 场景变化时间戳列表
        format: 输出格式
        quality: 图片质量
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"无法打开视频文件: {video_path}")
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    extracted_count = 0
    
    print("正在提取高光帧...")
    
    for i, timestamp in enumerate(scene_changes):
        # 计算帧位置
        frame_idx = int(timestamp * fps)
        
        # 设置帧位置
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        
        ret, frame = cap.read()
        if not ret:
            continue
        
        # 保存帧
        filename = f"highlight_{i+1:03d}_{timestamp:.2f}s.{format}"
        output_file = output_path / filename
        
        # 转换颜色空间并保存
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame_rgb)
        
        if format.lower() == "jpg" or format.lower() == "jpeg":
            pil_image.save(str(output_file), "JPEG", quality=quality, optimize=True)
        else:
            pil_image.save(str(output_file), "PNG", optimize=True)
        
        extracted_count += 1
        print(f"提取: {filename}")
    
    cap.release()
    
    return extracted_count


def main():
    parser = argparse.ArgumentParser(description="视频高光帧提取工具")
    parser.add_argument("--input", "-i", required=True, help="输入视频文件路径")
    parser.add_argument("--output", "-o", required=True, help="输出目录")
    parser.add_argument("--threshold", "-t", type=float, default=30.0, help="场景变化阈值 (默认: 30.0)")
    parser.add_argument("--format", choices=["jpg", "jpeg", "png"], default="jpg", help="输出格式 (默认: jpg)")
    parser.add_argument("--quality", type=int, default=95, help="图片质量 1-100 (默认: 95)")
    parser.add_argument("--min-interval", type=float, default=1.0, help="最小场景间隔（秒） (默认: 1.0)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"错误: 输入文件不存在: {args.input}")
        sys.exit(1)
    
    try:
        # 检测场景变化
        scene_changes = detect_scenes(args.input, args.threshold)
        
        # 过滤掉间隔太短的场景变化
        filtered_changes = []
        prev_time = -args.min_interval
        
        for timestamp in scene_changes:
            if timestamp - prev_time >= args.min_interval:
                filtered_changes.append(timestamp)
                prev_time = timestamp
        
        print(f"过滤后剩余 {len(filtered_changes)} 个场景变化")
        
        if len(filtered_changes) == 0:
            print("未检测到有效的场景变化")
            sys.exit(0)
        
        # 提取高光帧
        extracted_count = extract_highlight_frames(
            args.input, args.output, filtered_changes, args.format, args.quality
        )
        
        print(f"\n提取完成！共提取 {extracted_count} 个高光帧")
        print(f"输出目录: {args.output}")
        
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # 导入PIL（在脚本中导入以避免在函数定义时出错）
    from PIL import Image
    main()