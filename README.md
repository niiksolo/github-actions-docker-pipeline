[![CI/CD](https://github.com/niiksolo/github-actions-docker-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/niiksolo/github-actions-docker-pipeline/actions)

# Booking Service 

Учебный проект. Микросервис на **FastAPI + PostgreSQL** с тестами и настроенным CI/CD на **GitHub Actions**.

---

## 🚀 Технологии
- Python 3.12, FastAPI  
- PostgreSQL 15  
- Pytest (unit, integration, e2e)  
- Docker / Docker Compose  
- GitHub Actions + GitHub Container Registry (GHCR)  

---

## ⚙️ CI/CD
- При пуше в `feature/*` → unit-тесты  
- При пуше в `develop` → unit + integration + smoke  
- При пуше в `main` → полный прогон тестов и публикация образа в **GHCR**  
- Заглушки для деплоя (staging/prod), можно подключить docker-compose или Kubernetes  

---

## 🐳 Запуск
```bash
docker compose up --build