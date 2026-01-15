# ⚽ Football Analysis with YOLO

> A cutting-edge computer vision project leveraging YOLOv11 and advanced ML techniques to detect, track, and analyze football players in real-time videos.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![YOLO](https://img.shields.io/badge/YOLO-v11-brightgreen?style=flat-square)
![OpenCV](https://img.shields.io/badge/OpenCV-Enabled-purple?style=flat-square)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [🔑 Key Features](#-key-features)
- [🛠️ Requirements](#-requirements)
- [📦 Installation](#-installation)
- [🚀 Getting Started](#-getting-started)
- [📚 What I'm Learning](#-what-im-learning)
- [🔧 Project Implementation Steps](#-project-implementation-steps)
- [📁 Project Structure](#-project-structure)
- [🤖 Models & Datasets](#-models--datasets)
- [📊 Technologies Used](#-technologies-used)
- [🎓 Advanced Concepts](#-advanced-concepts)
- [📝 Contributing](#-contributing)

---

## 🎯 Project Overview

This comprehensive football analysis system uses state-of-the-art **YOLOv11 (You Only Look Once)** for real-time object detection combined with advanced computer vision techniques to provide deep insights into football match analysis.

### The Vision
Transform raw football video footage into actionable intelligence by:
- 🎬 **Detecting & Tracking** players, referees, and balls with high precision
- 🏃 **Analyzing Movement** using optical flow to understand camera motion
- 👕 **Team Assignment** using K-means clustering on t-shirt colors
- 📏 **Perspective Transformation** to convert pixel measurements to real-world meters
- 📈 **Performance Metrics** including speed, distance covered, and ball possession

### Real-World Applications
- Match analytics and performance evaluation
- Player movement analysis and coaching insights
- Automated highlight generation
- Sports statistics computation
- Training and development insights

---

## 🔑 Key Features

### ✨ Core Capabilities
- **Real-time Object Detection**: Detect players, referees, and footballs in video streams
- **Multi-Object Tracking**: Track individual players across frames
- **Team Color Detection**: Automatically assign players to teams using K-means clustering
- **Ball Possession Analysis**: Calculate ball acquisition percentage per team
- **Movement Tracking**: Measure player movements using optical flow
- **Perspective Mapping**: Convert pixel coordinates to real-world metrics
- **Performance Metrics**: Calculate player speed and distance covered

### 🎨 Advanced Features
- Custom trained models on football-specific datasets
- Optimized inference with YOLOv11 (smaller, faster model)
- Support for multiple video formats
- Batch processing capabilities
- Visualization of detection and tracking results

---

## 🛠️ Requirements

### System Requirements
- **Python**: 3.8 or higher
- **RAM**: 8GB minimum (16GB recommended for batch processing)
- **GPU**: Optional but recommended for faster inference (CUDA 11.0+)
- **Storage**: ~500MB for models and dependencies

### Python Dependencies

```
ultralytics>=8.0.0          # YOLOv11 framework
opencv-python>=4.5.0        # Computer vision library
numpy>=1.19.0              # Numerical computing
matplotlib>=3.3.0          # Visualization
pandas>=1.1.0              # Data analysis
supervision>=0.1.0         # Detection utilities
scikit-learn>=0.24.0       # K-means clustering
scipy>=1.5.0               # Scientific computing
```

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Keshtech2002/Football_Analysis_with_YOLO.git
cd Football_Analysis_with_YOLO
```

### 2. Create Virtual Environment (Recommended)
```bash
# Using venv
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n football-analysis python=3.10
conda activate football-analysis
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install ultralytics opencv-python numpy matplotlib pandas supervision scikit-learn scipy
```

### 4. Download Pre-trained Models
The project includes pre-trained YOLOv11 models:
- `models/best.pt` - Custom trained model (186MB) - Best performance
- `models/last.pt` - Last checkpoint (186MB)
- `yolo11s.pt` - YOLOv11 Small baseline model

---

## 🚀 Getting Started

### Quick Start Example

```python
from ultralytics import YOLO

# Load the custom-trained model
model = YOLO('models/best.pt')

# Run inference on a video
results = model.predict('input_videos/your_video.mp4', save=True)

# Print detection details
for result in results:
    print(f"Detected {len(result.boxes)} objects")
    for box in result.boxes:
        print(f"Confidence: {box.conf[0]:.2f}, Class: {box.cls}")
```

### Running the Main Script
```bash
python main.py
```

### Running Inference
```bash
python yolo_inference.py
```

---

## 📚 What I'm Learning

This project is a comprehensive learning experience covering multiple domains:

### 🤖 **Machine Learning & Deep Learning**
- Understanding YOLO architecture and real-time object detection
- Training custom models on domain-specific datasets
- Transfer learning and fine-tuning pre-trained models
- Model optimization and inference acceleration
- Handling imbalanced datasets and class weights

### 👁️ **Computer Vision**
- Object detection and localization
- Multi-object tracking (MOT) across frames
- Optical flow computation for motion estimation
- Perspective transformation and homography
- Color space manipulation (RGB, HSV)
- Image segmentation techniques

### 📊 **Advanced Image Processing**
- K-means clustering for color-based segmentation
- Feature extraction and descriptor matching
- Morphological operations
- Image pyramid and multi-scale processing
- Video frame extraction and manipulation

### 🔬 **Data Science & Analytics**
- Statistical analysis of player movements
- Time-series analysis for trajectory tracking
- Clustering and classification techniques
- Data visualization and reporting
- Performance metric calculations

### 💻 **Software Engineering**
- Working with large datasets and video files
- Code organization and modular design
- Performance optimization techniques
- Version control (Git)
- Documentation and project management

### 📈 **Domain Knowledge**
- Football/soccer field understanding
- Player positioning and movement patterns
- Team dynamics and formation analysis
- Sports analytics fundamentals

---

## 🔧 Project Implementation Steps

### ✅ **Phase 1: Foundation & Setup** (Completed)
- [x] Project initialization and structure setup
- [x] Git repository creation and configuration
- [x] Environment setup and dependency management
- [x] YOLOv11 and supporting libraries installation
- [x] Basic project scaffolding

**Timeline**: Early January 2026

### ✅ **Phase 2: Data Preparation & Training** (Completed - Jan 2)
- [x] Sourced football-players-detection dataset (Roboflow)
- [x] Dataset structure: 
  - Training set: Custom-labeled football player images
  - Validation set: Independent validation examples
  - Test set: Holdout test examples
- [x] Created YOLOv5 training notebooks for Google Colab and local training
- [x] **Trained custom model on football-specific dataset**
- [x] Generated trained models:
  - `best.pt` (186MB) - Best performing checkpoint
  - `last.pt` (186MB) - Final checkpoint
- [x] Created training pipeline with `football_training_yolo_v5.ipynb`

**Key Dates**: Jan 2, 2026
**Training Status**: ✅ Complete

### ✅ **Phase 3: Inference & Detection** (In Progress - Jan 2-3)
- [x] Implemented basic YOLO inference with `yolo_inference.py`
- [x] Set up video input pipeline
- [x] Integrated detection box extraction
- [x] Created inference script that processes video files
- [x] Generated prediction outputs in `runs/detect/predict*` directories
- [x] Started main script structure with `main.py`

**Current Status**: Basic inference working ✅

### 🔄 **Phase 4: Advanced Tracking & Analysis** (Next Steps)
- [ ] Implement multi-object tracking (MOT)
- [ ] Integrate optical flow for camera motion detection
- [ ] Develop team color detection using K-means clustering
- [ ] Build player-to-team assignment logic
- [ ] Implement perspective transformation
- [ ] Calculate speed and distance metrics
- [ ] Create visualization utilities

### 📊 **Phase 5: Analytics & Insights** (Planned)
- [ ] Ball possession percentage calculation
- [ ] Player movement heatmaps
- [ ] Speed and acceleration analysis
- [ ] Formation detection and analysis
- [ ] Automated report generation

### 🎬 **Phase 6: Output & Visualization** (Planned)
- [ ] Video annotation and rendering
- [ ] Interactive dashboard creation
- [ ] Performance statistics export
- [ ] High-quality result visualization

---

## 📁 Project Structure

```
Football_Analysis_with_YOLO/
├── 📄 main.py                          # Main application entry point
├── 🔍 yolo_inference.py               # Inference script for YOLO
├── 📋 README.md                       # This file
│
├── 📁 models/                         # Pre-trained models directory
│   ├── 🤖 best.pt                    # Best custom-trained model (186MB)
│   ├── 🤖 last.pt                    # Last checkpoint (186MB)
│   └── 📄 README                      # Models documentation
│
├── 📁 training/                       # Training notebooks and datasets
│   ├── 📓 football_training_yolo_v5.ipynb              # Local training
│   ├── 📓 football_training_yolo_v5_googlecolab.ipynb  # Colab training
│   └── 📁 football-players-detection-1/               # Training dataset
│       ├── 📁 train/                  # Training images and labels
│       ├── 📁 valid/                  # Validation set
│       ├── 📁 test/                   # Test set
│       ├── 📄 data.yaml              # Dataset configuration
│       └── 📄 README files            # Dataset documentation
│
├── 📁 input_videos/                   # Input video files for processing
│   └── 📄 README                      # Input instructions
│
├── 📁 runs/                           # Output directory for detection results
│   └── 📁 detect/
│       ├── 📁 predict/                # First prediction run results
│       ├── 📁 predict2/               # Second prediction run results
│       └── 📁 predict3/               # Third prediction run results
│
├── 📁 utils/                          # Utility functions and helpers
│   └── 🐍 video_utils.py             # Video processing utilities
│
├── 🤖 yolo11s.pt                     # YOLOv11 Small baseline model
├── .env                              # Environment variables
├── .gitignore                        # Git ignore rules
└── .git/                             # Git repository
```

---

## 🤖 Models & Datasets

### Pre-trained Models

| Model | Size | Date | Status | Purpose |
|-------|------|------|--------|---------|
| `best.pt` | 186MB | Jan 2, 2026 | ✅ Ready | Custom-trained for football detection |
| `last.pt` | 186MB | Jan 2, 2026 | ✅ Ready | Final checkpoint from training |
| `yolo11s.pt` | - | - | ✅ Available | YOLOv11 Small baseline |

### Dataset Information

**Football Players Detection Dataset** (Roboflow)
- **Training Set**: Diverse football player images
- **Validation Set**: Independent validation examples
- **Test Set**: Holdout test examples
- **Format**: YOLO v5 format with bounding box annotations
- **Classes Detected**: Players, Referees, Ball
- **Location**: `training/football-players-detection-1/`

### Training Details

- **Framework**: YOLOv5
- **Epochs**: Trained to convergence
- **Batch Size**: Optimized for available GPU memory
- **Augmentation**: Enabled for robustness
- **Performance**: Best model weights saved as `best.pt`

---

## 📊 Technologies Used

### Core Technologies

<table>
  <tr>
    <td align="center"><b>YOLOv11</b><br/>Object Detection</td>
    <td align="center"><b>OpenCV</b><br/>Computer Vision</td>
    <td align="center"><b>NumPy</b><br/>Numerical Computing</td>
  </tr>
  <tr>
    <td align="center"><b>Scikit-learn</b><br/>K-means Clustering</td>
    <td align="center"><b>Pandas</b><br/>Data Analysis</td>
    <td align="center"><b>Matplotlib</b><br/>Visualization</td>
  </tr>
</table>

### Key Libraries

- **ultralytics**: YOLOv11 implementation and training
- **opencv-python**: Video processing and image manipulation
- **numpy**: Array operations and numerical computation
- **scikit-learn**: K-means clustering for team detection
- **scipy**: Scientific computing and optical flow
- **supervision**: Detection utilities and visualization
- **matplotlib**: Data visualization and plotting

### Optional GPU Support
- **CUDA**: For GPU acceleration (NVIDIA GPUs)
- **cuDNN**: For optimized deep learning operations
- **PyTorch/TensorFlow**: Backend support through ultralytics

---

## 🎓 Advanced Concepts

### 1. **YOLO Architecture**
Real-time object detection using a single neural network that predicts bounding boxes and class probabilities directly from full images.

```
Input Image → CNN Feature Extraction → Grid Division → 
Bounding Box Prediction → Class Probability → Output Detections
```

### 2. **K-means Clustering**
Unsupervised learning algorithm used to cluster t-shirt colors and assign players to teams based on dominant color.

### 3. **Optical Flow**
Technique to estimate motion between consecutive frames, crucial for measuring camera movement and player motion independently.

### 4. **Perspective Transformation**
Homography matrix calculation to map pixels to real-world coordinates, enabling accurate distance measurements in meters.

### 5. **Multi-Object Tracking (MOT)**
Associating detections across frames to maintain consistent player IDs throughout the video sequence.

---

## 🎬 Sample Usage

### Basic Detection
```python
from ultralytics import YOLO

# Load model
model = YOLO('models/best.pt')

# Run detection
results = model.predict('input_videos/match.mp4', save=True, imgsz=640)
```

### Accessing Detection Results
```python
for result in results:
    # Get bounding boxes
    boxes = result.boxes
    
    # Iterate through detections
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        confidence = box.conf[0]
        class_id = box.cls[0]
        
        print(f"Box: ({x1}, {y1}, {x2}, {y2})")
        print(f"Confidence: {confidence:.2f}")
```

---

## 📈 Project Progress

```
Foundation       ████████████░░░░░░░░░░░░░░░░░░ 30%
Training         ██████████████████░░░░░░░░░░░░░ 60%
Inference        ██████████████████░░░░░░░░░░░░░ 60%
Analysis         ███░░░░░░░░░░░░░░░░░░░░░░░░░░░  10%
Visualization    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  0%
Overall          ████████████░░░░░░░░░░░░░░░░░░░ 25%
```

---

## 🚀 Next Steps

- [ ] Implement robust multi-object tracking
- [ ] Add optical flow computation
- [ ] Build team color detection pipeline
- [ ] Create perspective transformation module
- [ ] Develop analytics dashboard
- [ ] Generate comprehensive visualizations
- [ ] Add unit tests and documentation
- [ ] Deploy as web service (optional)

---

## 📚 Resources & References

### Official Documentation
- [Ultralytics YOLOv11 Docs](https://docs.ultralytics.com/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Scikit-learn Documentation](https://scikit-learn.org/)

### Useful Articles & Papers
- YOLOv3: An Incremental Improvement
- YOLOv4: Optimal Speed and Accuracy of Object Detection
- You Only Look Once: Unified, Real-Time Object Detection

### Related Datasets
- [Football Players Detection](https://universe.roboflow.com/)
- [Sports Video Datasets](https://www.activision.com/research)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs and issues
- 💡 Suggest improvements and enhancements
- 🔧 Submit pull requests with new features
- 📖 Improve documentation

---

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 👤 About

**Project Owner**: [Keshtech2002](https://github.com/Keshtech2002)

**Created**: January 2026

**Status**: 🔄 In Active Development

---

## ⭐ Support

If you find this project helpful, please consider:
- ⭐ Giving it a star on GitHub
- 🔗 Sharing it with others
- 💬 Providing feedback and suggestions
- 🐛 Reporting issues

---

**Last Updated**: January 3, 2026 | **Version**: 0.2.0 (Alpha)

