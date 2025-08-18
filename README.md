# FastAPI Demo

Small demo API with FastAPI.

## Run locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload

## Run with Docker
```bash
docker build -t fastapi-demo:latest .
docker run --rm -p 8000:8000 fastapi-demo:latest
# or
docker compose up --build
