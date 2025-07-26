# file-sync

Simple file uploader with periodic polling to check upload status.  
No real-time magic — just reliable, steady updates.

---

## About

This project implements a lightweight file upload service where clients can upload files and periodically poll the server to check the upload and processing status.

Ideal for environments where real-time connections like WebSocket are not feasible or desired.

---

## Features

- Upload files via REST API
- Poll for upload status through a dedicated endpoint
- Basic metadata persistence with PostgreSQL
- Modular design to support future extensions (e.g., message queues, cloud storage)
- Designed for reliability and simplicity

---

## Tech Stack

- Python 3.13+
- FastAPI
- PostgreSQL (via Docker for local development)
- SQLAlchemy with asyncpg driver
- Uvicorn for local development server

---

## Architecture Overview

This project follows a modular, clean architecture approach:

- **Domain layer** handles core business logic like file upload states and processing rules
- **Application layer** manages use cases and orchestrates workflows
- **Adapters layer** contains implementations for external services such as the REST API and the database
- This separation allows components to be decoupled and easily swapped (e.g., switching databases or integrating message queues) without major rewrites
- The messaging/polling mechanism is implemented in a modular way to allow future replacements (like RabbitMQ, AWS SQS/SNS)
