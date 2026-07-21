# Engineering Decisions

## Overview

Engineering decisions determine the long-term quality, maintainability, scalability, and performance of any software system.

This document explains the most important architectural and technical decisions made during the development of the ADAS Smart Speed Bump Detection System, along with the rationale behind each decision.

---

# Design Philosophy

The project was designed around five engineering principles:

- Simplicity
- Reliability
- Scalability
- Modularity
- Maintainability

Every subsystem was developed independently while remaining fully integrated with the complete architecture.

---

# Decision 1
## Why Raspberry Pi 5?

### Alternatives Considered

- NVIDIA Jetson Nano
- Raspberry Pi 4
- Raspberry Pi 5

### Comparison

| Platform | Pros | Cons |
|----------|------|------|
| Raspberry Pi 4 | Affordable | Lower AI performance |
| Jetson Nano | GPU acceleration | Higher cost and power consumption |
| Raspberry Pi 5 | Excellent CPU performance, affordable, active community | No CUDA support |

### Final Decision

Raspberry Pi 5 was selected because it provides:

- Excellent CPU performance
- Low power consumption
- Strong community support
- Wide hardware compatibility
- Easy deployment

---

# Decision 2
## Why YOLO11?

### Alternatives

- SSD
- Faster R-CNN
- YOLOv8
- YOLO11

### Evaluation

| Model | Speed | Accuracy | Edge Deployment |
|--------|--------|----------|----------------|
| SSD | Medium | Medium | Good |
| Faster R-CNN | Slow | High | Poor |
| YOLOv8 | Excellent | High | Excellent |
| YOLO11 | Excellent | Higher | Excellent |

### Final Decision

YOLO11 was selected because it offers:

- Better feature extraction
- Improved small object detection
- Lower inference latency
- Better accuracy
- Optimized Ultralytics pipeline

---

# Decision 3
## Why FastAPI?

### Alternatives

- Flask
- Django
- Express.js
- FastAPI

### Comparison

| Framework | Performance | Async | API Docs |
|------------|------------|-------|----------|
| Flask | Medium | No | Manual |
| Django | Heavy | Partial | Manual |
| Express | High | Yes | External |
| FastAPI | Excellent | Native | Automatic |

### Final Decision

FastAPI provides:

- Automatic Swagger documentation
- Excellent performance
- Native asynchronous support
- Simple implementation
- Strong typing

---

# Decision 4
## Why Flutter?

### Alternatives

- Native Android
- React Native
- Flutter

Flutter was selected because it provides:

- Cross-platform support
- High rendering performance
- Excellent UI
- Strong Google support

---

# Decision 5
## Local JSON Database

During prototype development, JSON storage was intentionally selected.

### Advantages

- Zero configuration
- Lightweight
- Fast development
- Easy debugging

### Future Upgrade

The architecture supports migration to:

- PostgreSQL
- Firebase
- MongoDB
- Supabase

without modifying the mobile application.

---

# Decision 6
## REST API

REST architecture was chosen because:

- Lightweight
- Platform independent
- Easy Flutter integration
- Scalable

---

# Decision 7
## Modular Architecture

The project was divided into independent modules.

AI Module

↓

GPS Module

↓

Backend

↓

Mobile

Each module can be upgraded independently.

---

# Decision 8
## Edge AI

Inference runs directly on Raspberry Pi instead of cloud servers.

Benefits:

- Low latency
- Offline operation
- Better privacy
- Reduced bandwidth

---

# Decision 9
## GPS Localization

Instead of estimating location from maps,

actual GPS coordinates are recorded.

Advantages:

- Real-world accuracy
- Easy visualization
- Route sharing

---

# Decision 10
## Future Scalability

The architecture was intentionally designed to support:

- Cloud deployment
- Fleet management
- Crowdsourcing
- Smart cities
- Navigation systems

without redesigning the core software.

---

# Lessons Learned

The project demonstrated the importance of:

- Clean architecture
- Documentation
- Modular software
- Edge AI optimization
- Hardware-software integration