---
title: Resume Screening AI Service
emoji: "🤖"
colorFrom: blue
colorTo: green
sdk: docker
app_port: 8000
pinned: false
---

# Resume Screening AI Service

This Space runs the FastAPI-based AI service for resume parsing and matching.

## Runtime

- SDK: Docker
- Exposed Port: 8000
- Entrypoint: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

## Endpoints

- `GET /` Health message
- Resume/JD matching and embeddings endpoints under `/` via the FastAPI routers in `app/api/`

## Notes

This repository is configured as a Docker Space, so Hugging Face builds from the `Dockerfile` in this folder.
