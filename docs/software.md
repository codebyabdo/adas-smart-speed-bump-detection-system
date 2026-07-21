# Software Architecture

---

# Overview

The software architecture of the ADAS Smart Speed Bump Detection & Localization System was designed using a modular and layered approach to ensure scalability, maintainability, and flexibility.

Each subsystem is responsible for a specific functionality and communicates with other modules through clearly defined interfaces. This separation of concerns allows independent development, testing, deployment, and future expansion without affecting the entire system.

The software is divided into five primary layers:

- Embedded Layer
- AI Processing Layer
- Backend Layer
- Data Layer
- Mobile Application Layer

---

# Software Architecture Diagram

```text
                    Flutter Mobile App
                            │
                     HTTP REST API
                            │
                     FastAPI Backend
                            │
        ┌───────────────────┴───────────────────┐
        │                                       │
 JSON Database                        Detection Engine
                                                │
                                        YOLO11 Model
                                                │
                                        OpenCV Pipeline
                                                │
                                Raspberry Pi Camera Module
                                                │
                                  Raspberry Pi 5 Hardware
```

---

# Layered Architecture

The project follows a five-layer architecture.

## Layer 1 – Embedded Layer

Responsible for interacting directly with hardware devices.

### Components

- Raspberry Pi OS
- Camera Driver
- GPS Driver
- IMU Driver
- GPIO Interface

### Responsibilities

- Capture camera frames
- Read GPS coordinates
- Access IMU data
- Handle GPIO devices
- Execute AI inference

---

## Layer 2 – AI Processing Layer

Processes captured images using Computer Vision and Deep Learning.

### Main Libraries

- Ultralytics YOLO11
- OpenCV
- NumPy
- PyTorch

### Responsibilities

- Image preprocessing
- Model inference
- Confidence filtering
- Bounding box generation
- Detection validation

---

## Layer 3 – Backend Layer

Acts as the communication hub between embedded hardware and the mobile application.

### Framework

FastAPI

### Responsibilities

- API endpoints
- Request validation
- Data storage
- Data retrieval
- Health monitoring
- Synchronization

---

## Layer 4 – Data Layer

Stores detected speed bump information.

Current implementation:

- JSON File Database

Future implementation:

- PostgreSQL
- Firebase
- MongoDB

Stored Information

- Latitude
- Longitude
- Confidence
- Timestamp
- Device ID

---

## Layer 5 – Mobile Layer

Provides the graphical user interface.

### Framework

Flutter

### Features

- Google Maps
- Live markers
- Alerts
- Search
- Route analysis

---

# Software Components

The software consists of several independent modules.

```text
Software

├── Detection Module
├── GPS Module
├── IMU Module
├── Backend Module
├── Database Module
├── Mobile Module
└── Utilities
```

---

# Detection Module

The detection module continuously receives images from the Raspberry Pi Camera Module.

Workflow

```text
Camera

↓

Frame Capture

↓

Image Resize

↓

YOLO11

↓

Bounding Boxes

↓

Confidence

↓

Detection Result
```

Responsibilities

- Camera control
- Image preprocessing
- AI inference
- Detection filtering

---

# GPS Module

The GPS module continuously monitors satellite information.

Responsibilities

- GPS initialization
- Coordinate acquisition
- Timestamp generation
- Coordinate validation

Example Output

```json
{
  "latitude":30.044315,
  "longitude":31.235729
}
```

---

# IMU Module

The IMU module provides motion information.

Collected values

- Acceleration X
- Acceleration Y
- Acceleration Z

Future versions will use Sensor Fusion.

---

# Backend Module

The backend is implemented using FastAPI.

Responsibilities

- Receive bump reports
- Validate data
- Update database
- Provide REST APIs
- Return JSON responses

---

# Database Module

The current implementation stores all detections inside:

```text
bumps_data.json
```

Each record contains

```json
{
  "latitude":30.044315,
  "longitude":31.235729,
  "confidence":0.91,
  "timestamp":"2026-06-10T13:45:22"
}
```

Advantages

- Lightweight
- Easy debugging
- Portable
- No installation required

Limitations

- Single-device storage
- No concurrent access
- No cloud synchronization

---

# Mobile Module

Developed using Flutter.

Responsibilities

- Display nearby bumps
- Visualize maps
- Alert drivers
- Search locations
- Display history

---

# Folder Structure

```text
Production/

api_server.py

run_raspberry_pi.py

requirements.txt

best.pt

start.sh

bumps_data.json

sounds/

README.md
```

---

# Application Flow

```text
Start System

↓

Initialize Camera

↓

Initialize GPS

↓

Load YOLO11

↓

Capture Frame

↓

Run Detection

↓

Detection Found?

↓

No → Continue

↓

Yes

↓

Read GPS

↓

Send REST Request

↓

Save Database

↓

Flutter Retrieves Data

↓

Driver Alert
```

---

# API Communication Flow

```text
YOLO11

↓

FastAPI

↓

JSON Database

↓

Flutter

↓

Google Maps
```

---

# Sequence Diagram

```text
Camera

↓

YOLO11

↓

GPS

↓

FastAPI

↓

Database

↓

Flutter

↓

Driver
```

---

# State Management

The system follows an event-driven architecture.

States

Idle

↓

Capturing

↓

Processing

↓

Detection

↓

Localization

↓

Database Update

↓

Notification

↓

Idle

---

# Error Handling

Several validation mechanisms are implemented.

Camera

- Camera disconnected
- Invalid frame
- Timeout

GPS

- No fix
- Invalid coordinates
- Weak signal

Backend

- Invalid request
- Duplicate bump
- Missing fields

Mobile

- Network unavailable
- Empty response
- Invalid JSON

---

# Logging

The application logs:

- System startup
- Camera status
- GPS status
- Detection events
- API requests
- Errors

Benefits

- Easier debugging
- Performance analysis
- Maintenance

---

# Configuration

The project keeps configurable parameters separate from the application logic.

Examples

```python
CONFIDENCE_THRESHOLD = 0.5

PROCESS_EVERY_N_FRAMES = 2

GPS_TIMEOUT = 10

API_URL = "http://localhost:8000"
```

---

# Software Design Principles

The architecture follows several software engineering principles.

## Separation of Concerns

Each module performs a single responsibility.

---

## Modularity

Modules can be replaced independently.

---

## Scalability

Supports adding:

- New sensors
- Cloud services
- Additional AI models

---

## Maintainability

Small independent modules simplify updates.

---

## Reusability

Modules can be reused in future ADAS projects.

---

# Security Considerations

The prototype includes basic protection mechanisms.

Current

- Request validation
- GPS validation
- Duplicate filtering

Future

- Authentication
- HTTPS
- JWT
- Cloud authorization

---

# Performance Optimization

Several optimizations were implemented.

- NCNN deployment
- Frame skipping
- Confidence filtering
- Lightweight JSON storage
- Headless Raspberry Pi mode
- Efficient OpenCV pipeline

---

# Future Software Improvements

Future releases may include:

- PostgreSQL database
- Cloud synchronization
- Docker deployment
- CI/CD pipeline
- Web dashboard
- MQTT communication
- AI model auto-update
- OTA updates

---

# Software Summary

The software architecture successfully integrates embedded computing, computer vision, backend services, and mobile technologies into a complete modular ADAS platform.

Its layered architecture provides high maintainability, easy extensibility, and a strong foundation for future intelligent transportation systems and smart city applications.