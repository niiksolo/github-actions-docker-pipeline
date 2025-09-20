# 📦 Booking Service

![CI](https://github.com/niiksolo/github-actions-docker-pipeline/actions/workflows/ci.yml/badge.svg)
![CD](https://github.com/niiksolo/github-actions-docker-pipeline/actions/workflows/cd.yml/badge.svg)

Учебный проект с полноценным CI/CD на GitHub Actions.  
Сервис бронирования на FastAPI с базой PostgreSQL.  

## 🔧 Возможности
- CI Pipeline: build → unit tests → integration → smoke → e2e
- CD Pipeline: build Docker image → deploy staging (develop) → deploy production (main)
- Автоматическая публикация Docker-образов в GitHub Container Registry (GHCR)

## 🐳 Docker образы
Образы проекта можно посмотреть и скачать здесь: [GitHub Container Registry](https://github.com/niiksolo/github-actions-docker-pipeline/pkgs/container/github-actions-docker-pipeline)

## 🚀 Технологии
- Python 3.12 + FastAPI
- PostgreSQL 15
- Pytest (unit, integration, smoke, e2e)
- Docker / Docker Compose
- GitHub Actions + GitHub Container Registry

## ⚡ Локальный запуск
```bash
# Установить зависимости
pip install -r requirements.txt

# Запуск через Docker Compose
docker-compose up --build

# Прогон тестов
pytest tests/unit tests/integration tests/smoke tests/e2e