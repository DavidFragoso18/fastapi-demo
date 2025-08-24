# FastAPI Demo

Small demo API built with [FastAPI](https://fastapi.tiangolo.com/).

---

## 🚀 Run locally (without Docker)

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

➡️ App available at [http://localhost:8000](http://localhost:8000)  
Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Run with Docker

Build the image:
```bash
docker build -t fastapi-demo:latest .
```

Run the container (map host port 8000 → container port 80):
```bash
docker run --rm -p 8000:80 fastapi-demo:latest
```

➡️ Open [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧩 Run with Docker Compose (optional)

If you have a `docker-compose.yml`:
```bash
docker compose up --build
```

---

## ☁️ Deploy to AWS (overview)

**1. Push image to ECR**
```bash
docker tag fastapi-demo:latest <account-id>.dkr.ecr.<region>.amazonaws.com/fastapi-demo:latest
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/fastapi-demo:latest
```

**2. Deploy with App Runner**
- Go to **App Runner → Create service**
- Source: *ECR* → select `fastapi-demo:latest`
- Set **Port** = `80`, Health check path = `/docs`
- App Runner gives you a public HTTPS URL

**3. (Optional) CI/CD**
- Add a GitHub Actions workflow to:
  - Build & push the image on each commit to `main`
  - Trigger App Runner to deploy the new version

---

## 🔧 Notes

- Inside Docker/AWS, the app runs on **port 80**:  
  ```dockerfile
  CMD ["python","-m","uvicorn","main:app","--host","0.0.0.0","--port","80"]
  ```
- Locally we map it to **8000** → access at [http://localhost:8000](http://localhost:8000)  
- Swagger docs always available at `/docs`
