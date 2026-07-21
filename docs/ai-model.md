# AI Model

This document explains the Artificial Intelligence model used for speed bump detection.

---

# Overview

The project uses YOLO11 for real-time object detection.

The model identifies speed bumps from live camera images captured by Raspberry Pi.

---

# Why YOLO11?

YOLO11 was selected because it provides

- High accuracy
- Fast inference
- Lightweight deployment
- Edge AI compatibility
- Excellent real-time performance

---

# Dataset

Dataset sources included

- Custom road images
- Manual image collection
- Various road conditions

---

# Annotation

Bounding boxes were created using

- LabelImg
- Roboflow

Each speed bump was manually labeled.

---

# Dataset Split

Training

80%

Validation

20%

---

# Data Augmentation

Applied augmentations include

- Horizontal Flip
- Brightness
- Contrast
- Blur
- Rotation

---

# Training

Training performed using

Ultralytics YOLO11

Loss functions

- Box Loss
- Classification Loss
- DFL Loss

---

# Hyperparameters

Typical settings

Epochs

100+

Image Size

640

Batch Size

16

Optimizer

SGD / Adam

Learning Rate

0.01

---

# Validation

Evaluation metrics

- Precision
- Recall
- F1 Score
- mAP@50
- mAP@50-95

---

# Inference Pipeline

Camera

↓

Preprocessing

↓

YOLO11

↓

Bounding Boxes

↓

Confidence

↓

GPS Trigger

---

# Model Output

Each detection contains

- Bounding Box
- Confidence
- Class ID

---

# Performance

The model is optimized for

- Raspberry Pi deployment
- Low latency
- Real-time detection
- Reliable localization

---

# Future Improvements

Potential future enhancements

- Larger dataset
- More road anomaly classes
- TensorRT optimization
- ONNX deployment
- Quantization
- Better night detection
- Weather robustness