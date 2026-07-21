# Backend API Documentation

## Overview

The backend server is implemented using FastAPI.

Its responsibilities include:

- Receiving bump reports
- Validating coordinates
- Managing stored data
- Serving mobile clients

---

# Architecture

Flutter

↓

HTTP

↓

FastAPI

↓

JSON Database

↓

Response

---

# Base URL

[text](http://localhost:8000)


---

# Endpoints

---

## GET /

Returns API status.

Example Response

```json
{
"status":"running"
}
```

## POST /report_bump

Stores a detected bump.

Request
```json 
{
"latitude":30.0443,
"longitude":31.2357,
"confidence":0.92
}

```

Response

```json 
{
"message":"Bump saved successfully"
}

```

## GET /get_bumps

Returns all bumps.

Response

```json 

[
{
"latitude":30.0443,
"longitude":31.2357
}
]
```

## DELETE /clear_bumps

Clears database.

Response

```json 

{
"message":"Database cleared"
}
```

## Validation

Coordinates are validated before storage.

Checks include:

- Latitude range
- Longitude range
- Duplicate detection

# Error Codes
| Code | Meaning            |
| ---- | ------------------ |
| 200  | Success            |
| 400  | Bad Request        |
| 404  | Endpoint Not Found |
| 422  | Validation Error   |
| 500  | Server Error       |


FastAPI automatically generates interactive API documentation.


[text](http://localhost:8000/docs)

# Advantages

- Automatic Documentation
- Type Validation
- High Performance
- Lightweight
- Easy Integration

---

# docs/responsibilities.md

```markdown
# Project Responsibilities

## Team Overview

The project was developed collaboratively by eight team members.

Each member contributed to a dedicated subsystem.

---

# Team Structure

| Member | Responsibility |
|---------|---------------|
| Mahmoud Kamal Abd Elkader | Team Lead & System Integration |
| Abd El-Rahman Adel Sayed | Software Architecture & Documentation |
| Omar Ahmed Zaki | Backend Development |
| Mahmoud Ahmed Mohamed | Mobile Development |
| Abd El-Rahman Ahmed Zaki | AI Model Training |
| Ali Mohamed Ali | Hardware Integration |
| Hossam Sayed Ahmed | Embedded Systems |
| El-Hussin Ahmed Abo El-Magd | GPS & Sensors |

---

# My Role

Software Architecture Engineer

Documentation Engineer

---

# Responsibilities

## Software Architecture

Designed the complete system architecture.

Defined interaction between modules.

Prepared workflow diagrams.

Designed software layers.

---

## Technical Documentation

Produced:

- Architecture documentation
- Engineering decisions
- API documentation
- Technical specifications

---

## Repository Organization

Created documentation structure.

Managed documentation standards.

Maintained engineering consistency.

---

## Integration Planning

Defined interaction between:

- AI
- Backend
- Mobile
- Embedded

---

## Technical Review

Reviewed:

- Documentation
- Interfaces
- Architecture

---

# Deliverables

- Architecture Documentation
- README
- API Documentation
- Engineering Decisions
- Project Structure
- Technical Specifications