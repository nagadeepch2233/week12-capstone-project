# Architecture Overview

This portfolio project is a **full-stack Python + React application** with a modern infrastructure setup.

## Components

### Backend
- **Language & Framework:** Python 3.11 + FastAPI
- **Architecture:** Service layer, models, async support
- **Database:** PostgreSQL (or SQLite for dev)
- **Testing:** pytest + pytest-asyncio

### Frontend
- **Framework:** React + TypeScript
- **Structure:** Components, Pages, Services, Store
- **State Management:** Custom hooks
- **Styling:** CSS (optional Tailwind)

### Infrastructure
- **Docker:** Backend + frontend containers
- **Docker Compose:** Local dev orchestration
- **Kubernetes:** Deployment manifests for scalable cloud deployment
- **Terraform:** IaC for cloud resources (EC2 + S3)
