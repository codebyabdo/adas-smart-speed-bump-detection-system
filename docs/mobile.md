# Mobile Application

## Overview

The mobile application is the user-facing component of the ADAS Smart Speed Bump Detection System.

It allows drivers to visualize detected speed bumps, receive notifications, browse previously recorded locations, and communicate with the backend through REST APIs.

The application was developed using Flutter to ensure cross-platform compatibility and high performance.

---

# Objectives

The application aims to:

- Improve driver awareness
- Display nearby speed bumps
- Synchronize with backend services
- Visualize bump locations on maps
- Provide an intuitive driving assistant

---

# Technology Stack

| Technology | Purpose |
|------------|---------|
| Flutter | Cross-platform framework |
| Dart | Programming language |
| Google Maps | Interactive maps |
| HTTP Package | API communication |
| JSON | Data exchange |

---

# Application Architecture

```text
Flutter UI

↓

State Management

↓

API Service

↓

FastAPI Backend

↓

JSON Database

↓

GPS Records
```

---

# Main Screens

## Splash Screen

Displayed during application startup.

Responsibilities:

- Initialize resources
- Check API availability
- Load saved preferences

---

## Home Screen

Contains:

- Project overview
- Quick actions
- Navigation

---

## Live Map Screen

Displays:

- Current user location
- Speed bump markers
- Nearby hazards

Google Maps API renders markers using latitude and longitude received from the backend.

---

## Search Screen

Allows users to:

- Search by location
- Search by coordinates
- Center map

---

## Alert Screen

When approaching a bump:

- Visual warning
- Distance information
- Navigation guidance

---

## History Screen

Displays:

- Previously detected bumps
- Date
- Confidence
- Coordinates

---

# API Integration

The application communicates using REST APIs.

GET

/get_bumps

↓

Retrieve bumps

POST

/report_bump

↓

Save bump

---

# Google Maps Integration

Google Maps provides:

- Live navigation
- Marker rendering
- User positioning
- Zoom controls

---

# Notifications

Future versions will include:

- Push Notifications
- Voice Alerts
- Background Monitoring

---

# Performance

Flutter offers:

- High FPS
- Smooth animations
- Native performance
- Cross-platform support

---

# Error Handling

The application handles:

- Internet loss
- GPS unavailable
- Server offline
- Invalid responses

---

# Future Improvements

- Dark Mode
- Voice Navigation
- Offline Maps
- Cloud Synchronization
- Route Recommendation
- Driver Analytics