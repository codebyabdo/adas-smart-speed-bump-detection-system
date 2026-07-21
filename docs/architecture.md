# System Architecture

---

# Overview

The ADAS Smart Speed Bump Detection & Localization System follows a modular layered architecture designed to separate hardware, artificial intelligence, backend services, and mobile applications into independent components. This modular design improves maintainability, scalability, testing, and future extensibility.

Unlike monolithic embedded systems, every subsystem communicates through well-defined interfaces, allowing individual modules to be upgraded without affecting the entire platform.

The architecture consists of five primary layers:

- Perception Layer
- AI Processing Layer
- Localization Layer
- Backend Layer
- Application Layer

---

# High-Level Architecture

```

Camera Module V2

↓

YOLO11 Detection Engine

↓

Detection Verification

↓

GPS + IMU Localization

↓

FastAPI REST API

↓

Database

↓

Flutter Mobile Application

↓

Driver Notification

```

---

# Layer 1 — Perception Layer

## Purpose

Acquire road images continuously while the vehicle is moving.

## Components

- Raspberry Pi Camera Module V2
- Picamera2 Library
- OpenCV

## Responsibilities

- Capture live frames
- Adjust image resolution
- Frame buffering
- Image normalization
- Pass frames to AI engine

---

# Image Acquisition Pipeline

```

Road

↓

Camera Sensor

↓

CSI Interface

↓

Picamera2

↓

OpenCV Frame

↓

YOLO11

```

---

# Why Camera Module V2?

The Raspberry Pi Camera Module V2 was selected because it offers:

- Native CSI interface
- Low latency
- Stable frame rate
- Good image quality
- Full Raspberry Pi compatibility

---

# Layer 2 — AI Processing Layer

The AI layer performs real-time speed bump detection using a custom-trained YOLO11 model.

---

## Responsibilities

- Object Detection
- Bounding Box Prediction
- Confidence Calculation
- Filtering
- Detection Validation

---

## Detection Workflow

```

Input Image

↓

Resize

↓

Normalization

↓

CNN Backbone

↓

Feature Extraction

↓

Prediction Head

↓

Bounding Boxes

↓

Confidence Score

↓

Final Detection

```

---

## Confidence Threshold

Only detections above the configured confidence threshold are accepted.

Example:

Confidence ≥ 0.50

↓

Valid Detection

Otherwise

↓

Ignored

This reduces false positive detections.

---

# Layer 3 — Localization Layer

Once a bump has been detected, the localization subsystem records its exact geographic location.

---

## Components

- NEO-6M GPS
- GPSD
- IMU MPU6050

---

## Responsibilities

- Latitude
- Longitude
- Timestamp
- Motion confirmation
- Coordinate validation

---

## Localization Workflow

```

Detection

↓

GPS Fix

↓

Coordinate Validation

↓

Timestamp

↓

JSON Object

↓

API

```

---

# GPS Validation

Coordinates are accepted only when:

- GPS Fix Available
- Latitude Valid
- Longitude Valid
- Coordinates inside expected range

Invalid readings are discarded automatically.

---

# IMU Integration

The IMU measures:

- X acceleration
- Y acceleration
- Z acceleration

Future versions will combine IMU data with computer vision using Sensor Fusion.

---

# Layer 4 — Backend Layer

The backend provides communication between embedded hardware and mobile applications.

---

## Technology

FastAPI

---

## Responsibilities

- Receive detections
- Validate requests
- Store records
- Serve APIs
- Synchronize data

---

## Backend Workflow

```

Detection

↓

POST Request

↓

Validation

↓

Database

↓

GET Request

↓

Flutter

```

---

# Database Layer

The current implementation uses a lightweight JSON database.

Example record:

```json
{
    "latitude":30.044315,
    "longitude":31.235729,
    "confidence":0.91,
    "timestamp":"2026-06-10T12:30:15"
}
```

Future versions will migrate to PostgreSQL.

---

# REST API

## POST /report_bump

Stores newly detected bumps.

---

## GET /get_bumps

Returns all recorded bumps.

---

## DELETE /clear_bumps

Resets the database during testing.

---

# Layer 5 — Mobile Layer

The Flutter application provides the user interface.

---

## Features

- Live Map
- Driver Alerts
- Search
- History
- Route Analysis

---

# Mobile Workflow

```

Open App

↓

Get GPS

↓

Request Backend

↓

Receive JSON

↓

Render Markers

↓

Alert Driver

```

---

# End-to-End System Workflow

```

Vehicle Moving

↓

Camera

↓

YOLO11

↓

Detection

↓

Confidence Check

↓

GPS

↓

Backend

↓

Database

↓

Flutter

↓

Driver Notification

```

---

# Data Flow

```

Image

↓

Detection

↓

Coordinates

↓

REST API

↓

Database

↓

Mobile

↓

Alert

```

---

# Design Principles

The system architecture follows several software engineering principles:

## Modularity

Each subsystem operates independently.

---

## Scalability

New sensors or AI models can be integrated without redesigning the entire system.

---

## Maintainability

Each module can be updated independently.

---

## Portability

The software can run on different Raspberry Pi models and Linux distributions.

---

## Reliability

Validation is performed before storing any road information.

---

# Advantages of the Architecture

- Lightweight
- Modular
- Edge AI Ready
- Cloud Ready
- Mobile Ready
- Low Cost
- Easy Deployment
- High Maintainability

---

# Current Limitations

The current prototype has several limitations:

- Local JSON database
- Single Raspberry Pi deployment
- No cloud synchronization
- Limited GPU resources
- Limited detection classes

---

# Future Architecture

```

Vehicle

↓

Camera

↓

YOLO11

↓

Sensor Fusion

↓

Cloud API

↓

PostgreSQL

↓

Analytics Dashboard

↓

Flutter

↓

Navigation System

↓

Smart City Platform

```

---

# Architecture Summary

The proposed architecture successfully combines Embedded Systems, Artificial Intelligence, GPS Localization, REST APIs, and Mobile Applications into a complete Advanced Driver Assistance System capable of detecting and localizing road speed bumps in real time.

Its modular design enables future expansion toward cloud computing, smart transportation, fleet management, and autonomous driving applications.
