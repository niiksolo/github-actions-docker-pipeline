# 📦 Booking Service

![CI](https://github.com/niiksolo/github-actions-docker-pipeline/actions/workflows/ci.yml/badge.svg)
![CD](https://github.com/niiksolo/github-actions-docker-pipeline/actions/workflows/cd.yml/badge.svg)

Учебный проект с полноценным **CI/CD на GitHub Actions**.  
Автоматизирует сборку, тестирование и публикацию Docker-образов в **GitHub Container Registry (GHCR)**.

---

## 🔧 Возможности
- **CI Pipeline**: build → unit tests → integration → smoke → e2e  
- **CD Pipeline**: build Docker image → deploy staging (develop) → deploy production (main)  
- Автоматическая публикация Docker-образов в GHCR  

---

## 🚀 Технологии
- Python 3.12 + FastAPI  
- PostgreSQL 15  
- Pytest (unit, integration, smoke, e2e)  
- Docker / Docker Compose  
- GitHub Actions + GitHub Container Registry  