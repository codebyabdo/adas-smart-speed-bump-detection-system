# Deployment Guide

This document explains how the ADAS system is deployed from development to production.

---

# Deployment Overview

The project is divided into four deployment layers.

- Embedded Layer
- AI Layer
- Backend Layer
- Mobile Layer

---

# Embedded Device

Hardware:

- Raspberry Pi 5
- Raspberry Pi Camera Module V2
- NEO-6M GPS
- Power Supply

Operating System

Raspberry Pi OS

---

# AI Deployment

The YOLO11 model is exported after training.

Model format:

best.pt

Inference is performed directly on Raspberry Pi.

---

# Backend Deployment

Backend Framework

FastAPI

Launch command

```bash
uvicorn api_server:app --host 0.0.0.0 --port 8000
```

---

# Local Storage

Current implementation uses

```
bumps_data.json
```

Future versions may migrate to

- PostgreSQL
- Firebase
- MongoDB

---

# Mobile Deployment

Flutter application connects to FastAPI using HTTP requests.

Current deployment

Local WiFi

Future deployment

Cloud Server

---

# Deployment Workflow

Camera

↓

YOLO11

↓

Detection

↓

GPS

↓

Backend

↓

JSON Storage

↓

Flutter

↓

Driver Alert

---

# Production Deployment

Future architecture

Raspberry Pi

↓

Cloud API

↓

Database

↓

Flutter

↓

Dashboard

---

# Docker (Future)

```dockerfile
FROM python:3.11

COPY .

RUN pip install -r requirements.txt

CMD ["uvicorn","api_server:app"]
```

---

# CI/CD

Future deployment pipeline

GitHub

↓

GitHub Actions

↓

Testing

↓

Docker

↓

Cloud Deployment

---

# Security Considerations

- API validation
- Input sanitization
- HTTPS
- Authentication
- Rate limiting

---

# Future Deployment Targets

- Raspberry Pi
- Render
- Railway
- Azure
- AWS
- Google Cloud