#!/usr/bin/env python3
"""
Video Frame Extractor
从视频文件中提取帧并保存为图片的工具
"""

import argparse
import os
import sys
import cv2
import numpy as np
from PIL import Image
from pathlib import Path
from typing import Optional, Tuple
import time


class VideoFrameExtractor:
    def __init__(self, input_path: str, output_dir: str = "./frames"):
        self.input_path = input_path
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # 初始化视频捕获
        self.cap = cv2.VideoCapture(input_path)
        if not self.cap.isOpened():
            raise ValueError(f"无法打开视频文件: {input_path}")
        
        # 获取视频信息
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.duration = self.total_frames / self.fps if self.fps > 0 else 0
        
    def __del__(self):
        if hasattr(self, 'cap'):
            self.cap.release()
    
    def extract_frames(self, 
                      interval: float = 1.0,
                      frame_step: Optional[int] = None,
                      start_time: float = 0.0,
                      end_time: Optional[float] = None,
                      output_format: str = "jpg",
                      quality: int = 90,
                      prefix: str = "frame",
                      resize: Optional[Tuple[int, int]] = None,
                      save_log: bool = True) -> int:
        """
        提取视频帧
        
        Args:
            interval: 时间间隔（秒）
            frame_step: 帧步长（每N帧提取一次）
            start_time: 开始时间（秒）
            end_time: 结束时间（秒）
            output_format: 输出格式（jpg/png）
            quality: 图片质量（1-100）
            prefix: 文件名前缀
            resize: 调整大小 (宽, 高)
            
        Returns:
            提取的帧数量
        """
        
        # 设置结束时间
        if end_time is None:
            end_time = self.duration
        elif end_time > self.duration:
            end_time = self.duration
        
        # 计算开始和结束帧
        start_frame = int(start_time * self.fps)
        end_frame = int(end_time * self.fps)
        
        # 设置帧读取位置
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        
        frame_count = 0
        extracted_count = 0
        
        # 准备日志内容
        log_content = []
        log_content.append("视频信息:")
        log_content.append(f"  分辨率: {self.width}x{self.height}")
        log_content.append(f"  总帧数: {self.total_frames}")
        log_content.append(f"  FPS: {self.fps:.2f}")
        log_content.append(f"  时长: {self.duration:.2f}秒")
        log_content.append(f"  提取范围: {start_time:.2f}s - {end_time:.2f}s")
        log_content.append(f"  输出目录: {self.output_dir}")
        log_content.append("-" * 50)
        
        # 打印到控制台
        for line in log_content:
            print(line)
        
        # 确定提取策略
        if frame_step is not None:
            # 按帧步长提取
            extract_strategy = "frame_step"
            step_value = frame_step
            strategy_info = f"按帧步长提取: 每{frame_step}帧提取一次"
            log_content.append(strategy_info)
        else:
            # 按时间间隔提取
            extract_strategy = "time_interval"
            step_value = interval
            frames_per_interval = int(interval * self.fps)
            strategy_info = f"按时间间隔提取: 每{interval}秒提取一次"
            log_content.append(strategy_info)
        
        start_time_extract = time.time()
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
                
            current_frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
            current_time = current_frame / self.fps
            
            # 检查是否到达结束时间
            if current_time > end_time:
                break
            
            # 检查是否应该提取此帧
            should_extract = False
            
            if extract_strategy == "frame_step":
                should_extract = (frame_count % frame_step == 0)
            else:
                should_extract = (frame_count % frames_per_interval == 0)
            
            if should_extract:
                # 处理帧
                processed_frame = self._process_frame(frame, resize)
                
                # 保存帧
                timestamp = current_time
                output_filename = f"{prefix}_{timestamp:07.2f}_{current_frame:06d}.{output_format}"
                output_path = self.output_dir / output_filename
                
                self._save_frame(processed_frame, str(output_path), output_format, quality)
                
                extracted_count += 1
                
                # 显示进度
                progress = (current_frame - start_frame) / (end_frame - start_frame) * 100
                print(f"\r进度: {progress:.1f}% | 已提取: {extracted_count}帧 | "
                      f"当前时间: {current_time:.2f}s", end="", flush=True)
            
            frame_count += 1
        
        extract_time = time.time() - start_time_extract
        
        # 完成信息
        completion_info = []
        completion_info.append("\n提取完成！")
        completion_info.append(f"  总提取帧数: {extracted_count}")
        completion_info.append(f"  提取用时: {extract_time:.2f}秒")
        completion_info.append(f"  平均速度: {extracted_count/extract_time:.2f}帧/秒")
        completion_info.append(f"\n提取参数:")
        completion_info.append(f"  输入文件: {self.input_path}")
        completion_info.append(f"  输出格式: {output_format}")
        completion_info.append(f"  图片质量: {quality}")
        completion_info.append(f"  文件名前缀: {prefix}")
        if resize is not None:
            completion_info.append(f"  调整大小: {resize[0]}x{resize[1]}")
        if frame_step is not None:
            completion_info.append(f"  帧步长: {frame_step}")
        else:
            completion_info.append(f"  时间间隔: {interval}秒")
        
        # 打印到控制台
        for line in completion_info:
            print(line)
        
        # 添加到日志内容
        log_content.extend(completion_info)
        
        # 保存日志文件
        if save_log:
            log_file = self.output_dir / "extraction_log.txt"
            try:
                with open(log_file, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(log_content))
                print(f"\n提取日志已保存到: {log_file}")
            except Exception as e:
                print(f"\n警告: 无法保存日志文件: {e}")
        
        return extracted_count
    
    def _process_frame(self, frame: np.ndarray, resize: Optional[Tuple[int, int]]) -> np.ndarray:
        """处理帧：调整大小等"""
        if resize is not None:
            target_width, target_height = resize
            frame = cv2.resize(frame, (target_width, target_height), interpolation=cv2.INTER_LINEAR)
        
        # 转换颜色空间（OpenCV使用BGR，PIL使用RGB）
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame_rgb
    
    def _save_frame(self, frame: np.ndarray, output_path: str, format: str, quality: int):
        """保存帧为图片"""
        pil_image = Image.fromarray(frame)
        
        if format.lower() == "jpg" or format.lower() == "jpeg":
            pil_image.save(output_path, "JPEG", quality=quality, optimize=True)
        elif format.lower() == "png":
            # PNG质量参数不同，使用optimize
            pil_image.save(output_path, "PNG", optimize=True)
        else:
            raise ValueError(f"不支持的格式: {format}")


def main():
    parser = argparse.ArgumentParser(description="视频帧提取工具")
    
    # 必需参数
    parser.add_argument("--input", "-i", required=True, help="输入视频文件路径")
    
    # 可选参数
    parser.add_argument("--output", "-o", default="./frames", help="输出目录 (默认: ./frames)")
    parser.add_argument("--interval", type=float, default=1.0, help="提取间隔（秒） (默认: 1.0)")
    parser.add_argument("--frame-step", type=int, help="每N帧提取一次")
    parser.add_argument("--format", choices=["jpg", "jpeg", "png"], default="jpg", help="输出格式 (默认: jpg)")
    parser.add_argument("--quality", type=int, default=90, help="图片质量 1-100 (默认: 90)")
    parser.add_argument("--start", type=float, default=0.0, help="开始时间（秒） (默认: 0)")
    parser.add_argument("--end", type=float, help="结束时间（秒） (默认: 视频末尾)")
    parser.add_argument("--prefix", default="frame", help="输出文件名前缀 (默认: frame)")
    parser.add_argument("--resize", help="调整大小，格式: 宽x高 (例如: 640x480)")
    
    args = parser.parse_args()
    
    # 验证参数
    if not os.path.exists(args.input):
        print(f"错误: 输入文件不存在: {args.input}")
        sys.exit(1)
    
    if args.quality < 1 or args.quality > 100:
        print("错误: 图片质量必须在1-100之间")
        sys.exit(1)
    
    if args.interval <= 0 and args.frame_step is None:
        print("错误: 时间间隔必须大于0")
        sys.exit(1)
    
    if args.frame_step is not None and args.frame_step <= 0:
        print("错误: 帧步长必须大于0")
        sys.exit(1)
    
    # 解析resize参数
    resize = None
    if args.resize:
        try:
            width, height = map(int, args.resize.split('x'))
            resize = (width, height)
        except ValueError:
            print("错误: resize格式错误，请使用 宽x高 格式 (例如: 640x480)")
            sys.exit(1)
    
    try:
        # 创建提取器
        extractor = VideoFrameExtractor(args.input, args.output)
        
        # 提取帧
        extracted_count = extractor.extract_frames(
            interval=args.interval,
            frame_step=args.frame_step,
            start_time=args.start,
            end_time=args.end,
            output_format=args.format,
            quality=args.quality,
            prefix=args.prefix,
            resize=resize,
            save_log=True
        )
        
        print(f"\n成功提取 {extracted_count} 帧到 {args.output}")
        
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()