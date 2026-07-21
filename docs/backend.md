# Backend Architecture

The backend provides communication between the embedded AI system and the Flutter mobile application.

---

# Technology Stack

- Python
- FastAPI
- Uvicorn
- JSON Storage

---

# Responsibilities

The backend is responsible for:

- Receiving bump detections
- Storing GPS coordinates
- Returning bump history
- Providing REST APIs
- Synchronizing mobile application data

---

# Architecture

```
YOLO Detection

↓

GPS Coordinates

↓

FastAPI

↓

JSON Database

↓

Flutter
```

---

# API Endpoints

## POST /detect

Runs object detection.

---

## POST /report_bump

Stores detected bump.

---

## GET /get_bumps

Returns all recorded bumps.

---

## GET /gps_status

Returns GPS information.

---

# Request Flow

Camera

↓

YOLO

↓

Backend

↓

Database

↓

Mobile

---

# JSON Storage

Current implementation stores

- Latitude
- Longitude
- Timestamp
- Confidence

inside

```
bumps_data.json
```

---

# Validation

The backend validates

- GPS values
- Confidence score
- Duplicate entries
- Request format

---

# Error Handling

Possible errors

400

Bad Request

404

Not Found

500

Internal Server Error

---

# Performance

FastAPI provides

- Low latency
- Async support
- Lightweight deployment
- Easy scalability

---

# Security

Future improvements

- Authentication
- HTTPS
- JWT
- API Keys

---

# Future Database

The backend can easily migrate to

- PostgreSQL
- Firebase
- MongoDB
- SQLite

without changing Flutter APIs.