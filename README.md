# 📦 Booking Service

![CI](https://github.com/niiksolo/github-actions-docker-pipeline/actions/workflows/ci.yml/badge.svg)  
![CD](https://github.com/niiksolo/github-actions-docker-pipeline/actions/workflows/cd.yml/badge.svg)  

Training project with full CI/CD setup on GitHub Actions.  
Booking Service built with FastAPI and PostgreSQL database.  

---

## 🔧 Features
- **CI Pipeline:** build → unit tests → integration → smoke → e2e  
- **CD Pipeline:** build Docker image → deploy to staging (develop) → deploy to production (main)  
- **Automatic publishing of Docker images** to GitHub Container Registry (GHCR)  

---

## 🐳 Docker Images
You can view and download project images here: [GitHub Container Registry](https://github.com/niiksolo/github-actions-docker-pipeline/pkgs/container/github-actions-docker-pipeline)  

---

## 🚀 Technologies
- Python 3.12 + FastAPI  
- PostgreSQL 15  
- Pytest (unit, integration, smoke, e2e)  
- Docker / Docker Compose  
- GitHub Actions + GitHub Container Registry  

---

## ⚡ Local Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run using Docker Compose
docker-compose up --build

# Run tests
pytest tests/unit tests/integration tests/smoke tests/e2e