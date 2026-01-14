# Skill Video Frame Extractor

## 概述
从视频文件中提取帧并保存为图片的工具。支持按时间间隔控制提取频率，适用于视频分析、缩略图生成、关键帧提取等场景。

## 功能特性
- 支持多种视频格式（MP4, AVI, MOV, MKV等）
- 可控制提取间隔（每N秒或每N帧）
- 支持自定义输出格式（JPG, PNG）
- 可设置输出图片质量
- 显示提取进度和统计信息

## 使用方法  (根据文件名，自动创建目录output/文件名/)

### 基础用法
```bash
python extract_frames.py --input videos/demo.mp4 --output output/demo/
```

### 高级选项
```bash
# 每2秒提取一帧
python extract_frames.py --input videos/demo.mp4 --output output/demo/ --interval 2

# 每10帧提取一次
python extract_frames.py --input videos/demo.mp4 --output output/demo/ --frame-step 10

# 指定输出格式和质量
python extract_frames.py --input videos/demo.mp4 --output output/demo/ --format png --quality 95

# 提取指定时间范围
python extract_frames.py --input videos/demo.mp4 --output output/demo/ --start 1 --end 5
```

## 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--input` | 输入视频文件路径 | 必需 |
| `--output` | 输出目录 | `./output/文件名/` |
| `--interval` | 提取间隔（秒） | 1.0 |
| `--frame-step` | 每N帧提取一次 | None |
| `--format` | 输出格式（jpg/png） | jpg |
| `--quality` | 图片质量（1-100） | 90 |
| `--start` | 开始时间（秒） | 0 |
| `--end` | 结束时间（秒） | 视频末尾 |
| `--prefix` | 输出文件名前缀 | frame |
| `--resize` | 调整大小（宽x高） | None |

## 依赖要求

```bash
pip install opencv-python pillow numpy
```

## 输出格式

提取的图片将按以下格式命名：
```
{prefix}_{timestamp}_{frame_number}.{format}
```

例如：
- `frame_0000.00_0001.jpg`
- `frame_0002.50_0075.jpg`

## 使用场景

1. **视频分析**: 提取关键帧进行内容分析
2. **缩略图生成**: 快速生成视频预览图
3. **数据集准备**: 为机器学习准备训练数据
4. **质量检查**: 检查视频编码质量
5. **动画制作**: 提取帧用于二次创作

## 注意事项

- 确保有足够的磁盘空间存储提取的图片
- 高分辨率视频会生成较大的图片文件
- 建议使用 `--resize` 参数减小输出文件大小
- PNG格式文件更大但无损，JPG格式更小但有压缩

## 示例

### 场景1：每秒提取一帧用于视频摘要
```bash
python extract_frames.py \
  --input movie.mp4 \
  --output summary_frames/ \
  --interval 1 \
  --format jpg \
  --quality 85
```

### 场景2：高质量提取用于分析
```bash
python extract_frames.py \
  --input footage.mp4 \
  --output analysis/ \
  --interval 0.5 \
  --format png
```

### 场景3：提取特定时间段
```bash
python extract_frames.py \
  --input video.mp4 \
  --output highlight/ \
  --start 120 \
  --end 180 \
  --interval 0.1
```

## 故障排除

### 问题：提取速度很慢
- 解决：增大 `--interval` 值或使用 `--frame-step`
- 解决：使用 `--resize` 减小输出尺寸

### 问题：内存不足
- 解决：处理较短的视频片段
- 解决：使用 `--start` 和 `--end` 分段处理

### 问题：输出图片模糊
- 解决：提高 `--quality` 参数
- 解决：使用 PNG 格式而非 JPG