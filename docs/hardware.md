# Hardware Documentation

---

# Overview

The hardware subsystem forms the foundation of the ADAS Smart Speed Bump Detection & Localization System. It provides the sensing, processing, localization, and driver notification capabilities required for real-time operation.

The system was intentionally designed using affordable and commercially available hardware while maintaining sufficient computational performance for edge AI inference.

The hardware architecture consists of:

- Embedded Processing Unit
- Vision Sensor
- Localization Module
- Motion Sensor
- Alert System
- Storage
- Power Management

---

# Hardware Architecture

```

Power Supply

↓

Raspberry Pi 5

├─────────────┬─────────────┬──────────────┐

│             │             │

Camera      GPS          MPU6050

│             │             │

└─────────────┴─────────────┘

↓

YOLO11 Detection

↓

FastAPI

↓

Mobile Application

↓

Driver Notification

```

---

# Raspberry Pi 5

## Description

The Raspberry Pi 5 serves as the central embedded computing platform responsible for executing all software components of the system.

Unlike microcontrollers, Raspberry Pi supports Linux, making it suitable for AI inference, REST APIs, and real-time image processing.

---

## Specifications

| Feature | Value |
|------------|----------------|
| CPU | Quad-Core Cortex-A76 |
| Frequency | 2.4 GHz |
| RAM | 8 GB LPDDR4X |
| GPU | VideoCore VII |
| Storage | MicroSD |
| Operating System | Raspberry Pi OS 64-bit |
| USB | USB 3.0 + USB 2.0 |
| Camera Interface | CSI |

---

## Responsibilities

- Operating System
- Camera Control
- AI Inference
- GPS Reading
- IMU Communication
- Backend Communication
- Local Storage
- Mobile Synchronization

---

## Why Raspberry Pi 5?

Several embedded platforms were evaluated before selecting Raspberry Pi 5.

| Platform | Advantages | Limitations |
|------------|-------------------------|-----------------------|
| Raspberry Pi 5 | High performance, Linux support, CSI Camera | No dedicated AI accelerator |
| Jetson Nano | GPU acceleration | Higher cost |
| ESP32 | Very low cost | Cannot run YOLO |
| Arduino | Easy hardware control | No AI support |

Raspberry Pi 5 provided the best balance between cost, computational power, and compatibility with AI frameworks.

---

# Raspberry Pi Camera Module V2

## Description

The Raspberry Pi Camera Module V2 continuously captures road images during vehicle movement.

Captured images are streamed directly into the YOLO11 detection pipeline.

---

## Specifications

| Feature | Value |
|------------|----------------|
| Sensor | Sony IMX219 |
| Resolution | 8 MP |
| Interface | CSI |
| Video | 1080p |
| Frame Rate | Up to 60 FPS |

---

## Responsibilities

- Image Acquisition
- Continuous Streaming
- Road Monitoring
- AI Input

---

## Why Camera Module V2?

Reasons for selection include:

- Native Raspberry Pi support
- Low latency
- High image quality
- Stable Linux drivers
- Excellent OpenCV compatibility

---

# GPS Module (u-blox NEO-6M)

## Description

The GPS subsystem provides geographic coordinates whenever a speed bump is confirmed by the AI model.

---

## Specifications

| Feature | Value |
|------------|----------------|
| Model | NEO-6M |
| Accuracy | 2.5–5 meters |
| Communication | UART / USB |
| Update Rate | 1 Hz |
| Antenna | Ceramic Patch |

---

## Responsibilities

- Latitude
- Longitude
- GPS Fix
- Timestamp
- Position Validation

---

## Why NEO-6M?

The NEO-6M was selected because it provides:

- Low cost
- Good outdoor accuracy
- Wide community support
- Easy Raspberry Pi integration

Future versions may adopt NEO-M8N for improved accuracy.

---

# MPU6050 IMU

## Description

The MPU6050 combines a 3-axis accelerometer and a 3-axis gyroscope.

Although currently optional, it provides valuable motion information that can improve bump confirmation.

---

## Specifications

| Feature | Value |
|------------|----------------|
| Accelerometer | 3-axis |
| Gyroscope | 3-axis |
| Communication | I2C |
| Voltage | 3.3V |

---

## Responsibilities

- Vehicle Acceleration
- Vehicle Orientation
- Motion Detection
- Sensor Fusion

---

## Future Usage

Future releases will combine IMU data with YOLO detections using Sensor Fusion algorithms to reduce false positives.

---

# OLED Display

## Description

The OLED display provides real-time local system information.

Displayed information includes:

- GPS Status
- Camera Status
- Detection Count
- System Temperature

---

# Buzzer

The buzzer provides immediate audio feedback after bump detection.

Alert types include:

- Successful Detection
- GPS Failure
- System Warning

---

# MicroSD Card

The SD card stores:

- Raspberry Pi OS
- AI Models
- Project Source Code
- Local Database
- Logs

Recommended capacity:

64 GB Class 10

---

# Power Supply

## Requirements

The Raspberry Pi 5 requires a stable 5V / 5A power source for reliable AI inference.

---

## Laboratory Power

Official Raspberry Pi USB-C Adapter

---

## Vehicle Deployment

Future deployment will use:

12V Car Battery

↓

Buck Converter

↓

5V / 5A USB-C

↓

Raspberry Pi

---

# Hardware Connections

| Device | Interface |
|-------------|-------------|
| Camera | CSI |
| GPS | USB |
| MPU6050 | I2C |
| OLED | I2C |
| Buzzer | GPIO |

---

# Wiring Diagram

```

Camera

↓

CSI Port

↓

Raspberry Pi

↓

USB

↓

GPS

↓

I2C

↓

MPU6050

↓

GPIO

↓

Buzzer

```

---

# Power Consumption

| Component | Power |
|----------------|-----------|
| Raspberry Pi 5 | ~8–12 W |
| Camera | ~1 W |
| GPS | ~0.2 W |
| IMU | <0.1 W |
| OLED | <0.1 W |

Estimated total:

≈13 W

---

# Cooling System

During prolonged AI inference, CPU temperature may approach the thermal throttling threshold.

The current prototype uses:

- Passive Heatsink

Future deployment will include:

- Official Raspberry Pi Active Cooler

Benefits:

- Lower CPU temperature
- Stable inference speed
- Reduced thermal throttling

---

# Hardware Assembly Procedure

1. Install Raspberry Pi OS.
2. Connect Camera Module.
3. Attach GPS Module.
4. Connect MPU6050.
5. Connect OLED Display.
6. Connect Buzzer.
7. Insert SD Card.
8. Connect Power Supply.
9. Boot Raspberry Pi.
10. Verify hardware status.

---

# Hardware Validation

Each component was individually tested before full system integration.

| Component | Test | Status |
|------------|------------------------|---------|
| Raspberry Pi | Boot Test | Passed |
| Camera | Live Preview | Passed |
| GPS | Satellite Fix | Passed |
| IMU | Motion Reading | Passed |
| OLED | Display Output | Passed |
| Buzzer | Audio Test | Passed |

---

# Future Hardware Improvements

Several hardware upgrades are planned for future versions:

- Raspberry Pi AI HAT+
- Dual Camera System
- NEO-M8N GPS
- CAN Bus Interface
- 4G/LTE Connectivity
- Battery Backup Module
- Weatherproof Enclosure
- Automotive-grade Power Supply

---

# Hardware Summary

The selected hardware provides a cost-effective yet powerful platform for implementing an AI-based Advanced Driver Assistance System.

By combining Raspberry Pi 5, Camera Module V2, GPS, IMU, and peripheral devices, the system achieves reliable real-time speed bump detection while maintaining modularity, affordability, and scalability for future intelligent transportation applications.