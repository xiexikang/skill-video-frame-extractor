# 🎬 视频帧提取器 (Skill Video Frame Extractor)

一个功能强大的Python工具，用于从视频文件中提取帧并保存为高质量图片。支持多种视频格式、灵活的提取策略和丰富的配置选项，适用于视频分析、缩略图生成、关键帧提取等多种专业场景。

## 🌟 项目特色

- **🎯 多格式支持**: 支持MP4、AVI、MOV、MKV、FLV、WMV、WebM等主流视频格式
- **⚡ 高效处理**: 基于OpenCV优化算法，处理速度快，内存占用低
- **🔧 灵活配置**: 支持时间间隔、帧步长、时间范围等多种提取策略
- **🖼️ 质量保证**: 可调节输出图片质量和格式，支持JPG和PNG格式
- **📊 实时反馈**: 提供详细的进度显示和统计信息
- **📝 完整日志**: 自动生成提取日志，便于后续分析和追踪
- **🔄 批量处理**: 支持批量处理多个视频文件
- **📐 尺寸调整**: 支持输出图片尺寸调整，优化存储空间

## 🚀 快速开始

### 安装依赖

```bash
# 克隆项目
git clone https://github.com/your-username/skill-video-frame-extractor.git
cd skill-video-frame-extractor

# 安装依赖
pip install -r requirements.txt
```

### 基础使用

```bash
# 提取demo视频的帧（默认每秒一帧）
python extract_frames.py --input videos/demo.mp4 --output output/demo/
```

### 高级用法示例

```bash
# 每2秒提取一帧，输出高质量PNG图片
python extract_frames.py \
  --input videos/demo.mp4 \
  --output output/demo/ \
  --interval 2 \
  --format png

# 每10帧提取一次，调整图片尺寸为640x480
python extract_frames.py \
  --input videos/demo.mp4 \
  --output output/demo/ \
  --frame-step 10 \
  --resize 640x480

# 提取指定时间范围的高质量帧
python extract_frames.py \
  --input videos/demo.mp4 \
  --output output/demo/ \
  --start 30 \
  --end 60 \
  --interval 0.5 \
  --quality 95
```

## 📋 项目结构

```
skill-video-frame-extractor/
├── 📁 项目根目录
│   ├── extract_frames.py          # 主程序 - 核心帧提取功能
│   ├── requirements.txt          # Python依赖包列表
│   ├── README.md                 # 项目文档
│   ├── SKILL.md                  # 技能要求文档
│   ├── LICENSE                   # 开源许可证
│   ├── 📁 videos/                # 示例视频目录
│   │   └── demo.mp4              # 示例视频文件
│   ├── 📁 output/                # 默认输出目录
│   │   └── demo/                 # 示例输出结果
│   │       ├── frame_0000.00_0001.jpg
│   │       ├── frame_0001.00_0002.jpg
│   │       └── extraction_log.txt
│   ├── 📁 scripts/               # 实用脚本集合
│   │   ├── batch_extract.sh      # 批量处理脚本
│   │   └── extract_highlights.py # 精彩片段提取脚本
│   └── 📁 templates/             # 模板脚本集合
│       ├── dataset_preparation.sh    # 数据集准备模板
│       ├── quality_analysis.sh       # 质量分析模板
│       ├── thumbnail_generator.sh    # 缩略图生成模板
│       └── video_summary.sh         # 视频摘要模板
```

## ⚙️ 详细配置参数

### 核心参数

| 参数 | 说明 | 默认值 | 示例 |
|------|------|--------|------|
| `--input, -i` | 输入视频文件路径（必需） | - | `videos/movie.mp4` |
| `--output, -o` | 输出目录路径 | `./frames` | `output/extracted/` |
| `--interval` | 时间间隔（秒） | `1.0` | `0.5`, `2.0` |
| `--frame-step` | 帧步长（每N帧提取一次） | `None` | `10`, `30` |

### 质量控制参数

| 参数 | 说明 | 默认值 | 可选值 |
|------|------|--------|--------|
| `--format` | 输出图片格式 | `jpg` | `jpg`, `jpeg`, `png` |
| `--quality` | 图片质量（1-100） | `90` | `85-95`（推荐） |
| `--resize` | 调整输出尺寸 | `None` | `640x480`, `1280x720` |

### 范围控制参数

| 参数 | 说明 | 默认值 | 示例 |
|------|------|--------|------|
| `--start` | 开始时间（秒） | `0.0` | `30.0`, `120.5` |
| `--end` | 结束时间（秒） | `视频末尾` | `60.0`, `300.0` |
| `--prefix` | 输出文件名前缀 | `frame` | `img`, `shot` |

## 🎯 使用场景详解

### 1. 📹 视频分析与内容审查
```bash
# 每秒提取一帧用于AI内容分析
python extract_frames.py \
  --input review_video.mp4 \
  --output analysis_frames/ \
  --interval 1.0 \
  --format png \
  --quality 100
```

### 2. 🖼️ 缩略图和预览图生成
```bash
# 生成视频预览缩略图（每5秒一帧，低质量JPG）
python extract_frames.py \
  --input movie.mp4 \
  --output thumbnails/ \
  --interval 5.0 \
  --format jpg \
  --quality 75 \
  --resize 320x240
```

### 3. 🤖 机器学习数据集准备
```bash
# 为深度学习准备训练数据（高质量，固定尺寸）
python extract_frames.py \
  --input training_videos/*.mp4 \
  --output dataset/images/ \
  --frame-step 30 \
  --format png \
  --resize 224x224
```

### 4. 🔍 视频质量检测
```bash
# 提取关键帧进行质量分析（无损PNG）
python extract_frames.py \
  --input footage.mp4 \
  --output quality_check/ \
  --interval 0.1 \
  --format png \
  --start 10 \
  --end 20
```

### 5. 🎬 精彩片段提取
```bash
# 提取精彩片段（假设精彩部分在第2-3分钟）
python extract_frames.py \
  --input sports_game.mp4 \
  --output highlights/ \
  --start 120 \
  --end 180 \
  --interval 0.2 \
  --format jpg \
  --quality 90
```

## 🔄 批量处理工作流

### 使用批量处理脚本
```bash
# 批量处理videos目录下的所有视频文件
bash scripts/batch_extract.sh ./videos ./extracted_frames 2.0 jpg

# 自定义参数：每3秒提取一帧，输出PNG格式
bash scripts/batch_extract.sh ./videos ./batch_output 3.0 png
```

### 批量处理特性
- ✅ 自动扫描指定目录下的所有视频文件
- ✅ 支持多种视频格式（MP4, AVI, MOV, MKV, FLV, WMV, WebM）
- ✅ 为每个视频创建独立的输出目录
- ✅ 显示处理进度和统计信息
- ✅ 支持自定义提取参数

## 📊 输出文件命名规范

提取的图片文件遵循以下命名格式：
```
{prefix}_{timestamp}_{frame_number}.{format}
```

### 命名示例
- `frame_0000.00_0001.jpg` - 第1帧，时间戳0.00秒
- `frame_0002.50_0075.jpg` - 第75帧，时间戳2.50秒
- `frame_0120.00_3600.png` - 第3600帧，时间戳120.00秒

### 日志文件
每个提取任务都会生成详细的日志文件`extraction_log.txt`，包含：
- 📹 视频基本信息（分辨率、帧率、时长）
- ⚙️ 提取参数配置
- 📈 处理进度和统计
- ⏱️ 性能指标（处理速度、耗时）

## 🛠️ 安装部署指南

### 系统要求
- **操作系统**: Windows 10+, macOS 10.14+, Linux (Ubuntu 18.04+)
- **Python版本**: 3.8 或更高版本
- **内存要求**: 至少4GB RAM（推荐8GB+）
- **磁盘空间**: 根据视频大小和提取密度而定

### 详细安装步骤

#### 1. 环境准备
```bash
# 检查Python版本
python --version
# 或
python3 --version

# 建议创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

#### 2. 安装依赖
```bash
# 升级pip
pip install --upgrade pip

# 安装项目依赖
pip install -r requirements.txt

# 验证安装
python extract_frames.py --help
```

#### 3. 测试安装
```bash
# 运行示例提取
python extract_frames.py --input videos/demo.mp4 --output test_output/

# 检查输出
ls test_output/
```

### Docker部署（可选）
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

VOLUME ["/input", "/output"]

ENTRYPOINT ["python", "extract_frames.py"]
```

## 🔧 故障排除与优化

### 常见问题解决方案

#### 1. 🐌 提取速度过慢
**症状**: 处理大视频文件时速度很慢
**解决方案**:
```bash
# 增大时间间隔
python extract_frames.py --input large_video.mp4 --interval 5.0

# 使用帧步长代替时间间隔
python extract_frames.py --input large_video.mp4 --frame-step 60

# 减小输出图片尺寸
python extract_frames.py --input large_video.mp4 --resize 640x480
```

#### 2. 💾 内存不足错误
**症状**: 处理过程中出现内存溢出
**解决方案**:
```bash
# 分段处理长视频
python extract_frames.py --input long_video.mp4 --start 0 --end 300
python extract_frames.py --input long_video.mp4 --start 300 --end 600

# 降低提取密度
python extract_frames.py --input long_video.mp4 --interval 10.0
```

#### 3. 📁 输出文件过大
**症状**: 提取的图片占用过多磁盘空间
**解决方案**:
```bash
# 使用JPG格式并降低质量
python extract_frames.py --input video.mp4 --format jpg --quality 75

# 调整图片尺寸
python extract_frames.py --input video.mp4 --resize 1280x720

# 增大提取间隔
python extract_frames.py --input video.mp4 --interval 5.0
```

#### 4. 🎨 输出图片模糊
**症状**: 提取的图片质量不佳，细节模糊
**解决方案**:
```bash
# 提高图片质量
python extract_frames.py --input video.mp4 --quality 95

# 使用无损PNG格式
python extract_frames.py --input video.mp4 --format png

# 保持原始分辨率（不设置resize参数）
python extract_frames.py --input video.mp4
```

### 性能优化建议

#### 1. 硬件优化
- **CPU**: 多核处理器可显著提升处理速度
- **内存**: 8GB+ RAM推荐用于处理大视频文件
- **存储**: SSD存储可加快读写速度

#### 2. 软件优化
- **并行处理**: 使用多进程处理多个视频文件
- **缓存优化**: 合理设置OpenCV的缓存参数
- **格式选择**: 根据用途选择合适的输出格式

#### 3. 参数调优
- **提取间隔**: 根据分析需求选择合适的时间间隔
- **图片质量**: 平衡文件大小和图像质量
- **输出尺寸**: 根据后续用途调整输出图片尺寸

## 📚 API文档与扩展

### 核心类：`VideoFrameExtractor`

```python
from extract_frames import VideoFrameExtractor

# 创建提取器实例
extractor = VideoFrameExtractor(
    input_path="video.mp4",
    output_dir="output/"
)

# 提取帧
extracted_count = extractor.extract_frames(
    interval=1.0,           # 时间间隔（秒）
    frame_step=None,        # 帧步长（可选）
    start_time=0.0,         # 开始时间
    end_time=None,          # 结束时间
    output_format="jpg",    # 输出格式
    quality=90,            # 图片质量
    prefix="frame",        # 文件名前缀
    resize=None,            # 尺寸调整（可选）
    save_log=True           # 保存日志
)
```

### 扩展开发

#### 自定义提取策略
```python
class CustomExtractor(VideoFrameExtractor):
    def extract_frames(self, **kwargs):
        # 自定义提取逻辑
        # 添加特殊的帧选择算法
        # 实现智能关键帧检测等
        pass
```

#### 集成到工作流
```python
# 在数据处理管道中使用
import subprocess

def process_video_pipeline(video_path):
    # 步骤1: 提取帧
    subprocess.run([
        "python", "extract_frames.py",
        "--input", video_path,
        "--output", "temp/frames/",
        "--interval", "0.5"
    ])
    
    # 步骤2: 进行图像分析
    # ... 其他处理逻辑
```

## 🤝 贡献指南

### 开发环境搭建
1. Fork项目到个人仓库
2. 克隆本地开发环境
3. 创建功能分支
4. 安装开发依赖

### 代码规范
- **Python风格**: 遵循PEP 8编码规范
- **类型注解**: 使用类型提示提高代码可读性
- **文档字符串**: 为所有公共函数编写文档
- **错误处理**: 完善的异常处理和用户反馈

### 提交规范
- **Commit消息**: 使用清晰的提交信息格式
- **Pull Request**: 详细描述变更内容和测试情况
- **代码审查**: 积极参与代码审查和讨论

### 测试要求
- **单元测试**: 为核心功能编写测试用例
- **集成测试**: 验证完整的处理流程
- **性能测试**: 确保优化不会引入性能回退

## 📄 许可证

本项目采用MIT许可证 - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- **OpenCV社区**: 提供强大的计算机视觉库
- **Python生态系统**: 丰富的第三方库支持
- **开源贡献者**: 社区成员的积极参与和贡献

## 📞 支持与联系

- **问题反馈**: 请通过GitHub Issues提交问题
- **功能建议**: 欢迎提出新功能建议和改进意见
- **技术支持**: 查看文档和常见问题解答
- **社区讨论**: 参与项目讨论和经验分享

---

**⭐ 如果这个项目对你有帮助，请给颗星支持一下！**