# Booking Service

![CI](https://github.com/USERNAME/REPO/actions/workflows/ci.yml/badge.svg)
![CD](https://github.com/USERNAME/REPO/actions/workflows/cd.yml/badge.svg)

Учебный проект с CI/CD на GitHub Actions:
- **CI Pipeline**: build → unit tests → integration + smoke + e2e tests.
- **CD Pipeline**: build Docker image → deploy staging (develop) → deploy prod (main).
- Docker-образы публикуются в **GitHub Container Registry (GHCR)**.

## 🚀 Технологии
- Python 3.12, FastAPI  
- PostgreSQL 15  
- Pytest (unit, integration, e2e)  
- Docker / Docker Compose  
- GitHub Actions + GitHub Container Registry (GHCR)  

📌 Все отчёты по тестам доступны в логах GitHub Actions. При необходимости можно подключить сохранение HTML/JUnit-отчётов как artifacts.
