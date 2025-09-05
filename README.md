# Booking Service

![CI](https://github.com/niiksolo/github-actions-docker-pipeline/actions/workflows/ci.yml/badge.svg)
![CD](https://github.com/niiksolo/github-actions-docker-pipeline/actions/workflows/cd.yml/badge.svg)

Учебный проект с полноценным **CI/CD на GitHub Actions**.  
Показывает, как можно автоматизировать сборку, тестирование и публикацию Docker-образов в **GitHub Container Registry (GHCR)**.

## 🔧 Возможности
- **CI Pipeline**: build → unit tests → integration + smoke + e2e tests  
- **CD Pipeline**: build Docker image → deploy staging (develop) → deploy prod (main)  
- Docker-образы автоматически пушатся в GHCR  

## 🚀 Технологии
- Python 3.12 + FastAPI  
- PostgreSQL 15  
- Pytest (unit, integration, smoke, e2e)  
- Docker / Docker Compose  
- GitHub Actions + GitHub Container Registry  

## ▶️ Запуск локально
```bash
git clone https://github.com/niiksolo/github-actions-docker-pipeline.git
cd github-actions-docker-pipeline
docker-compose up --build

📌 CI/CD
Все тестовые отчёты и логи деплоя доступны во вкладке Actions
Возможен ручной запуск staging-деплоя через workflow_dispatch