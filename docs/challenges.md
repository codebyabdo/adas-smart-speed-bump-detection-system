# Engineering Challenges

## Overview

Developing an embedded AI-based driver assistance system presented several engineering challenges spanning hardware, software, artificial intelligence, and system integration.

---

# Challenge 1
## Dataset Collection

The biggest challenge was obtaining a high-quality speed bump dataset.

Problems included:

- Different bump shapes
- Different lighting
- Shadows
- Camera angles
- Road quality

Solution

- Combined multiple datasets
- Added custom collected images
- Added augmentation

---

# Challenge 2
## Small Object Detection

Speed bumps occupy a very small portion of each image.

Solution

YOLO11 architecture with higher feature extraction capability improved small-object detection.

---

# Challenge 3
## Raspberry Pi Performance

Running AI inference continuously on an embedded computer is computationally expensive.

Solution

- Reduced image resolution
- Optimized inference
- NCNN deployment
- Frame skipping

---

# Challenge 4
## Camera Compatibility

OpenCV camera capture was unreliable under Raspberry Pi OS Trixie.

Solution

Migrated to Picamera2.

---

# Challenge 5
## GPS Accuracy

GPS coordinates fluctuate.

Solution

Coordinate validation.

Signal filtering.

Duplicate rejection.

---

# Challenge 6
## False Positives

Objects such as road markings occasionally resembled speed bumps.

Solution

Additional training data.

Confidence threshold.

Validation pipeline.

---

# Challenge 7
## Integration

Synchronizing AI, GPS, Backend, and Mobile.

Solution

REST APIs.

Modular architecture.

Independent testing.

---

# Challenge 8
## Thermal Management

Continuous AI inference increases CPU temperature.

Solution

Official Raspberry Pi Active Cooler.

---

# Challenge 9
## Documentation

Maintaining documentation while software evolved.

Solution

Version-controlled documentation inside GitHub.

---

# Outcome

Every engineering challenge improved the final architecture and produced a more maintainable and scalable system.