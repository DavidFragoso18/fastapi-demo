from fastapi import FastAPI

app = FastAPI(title="FastAPI Demo")

@app.get("/")
def root():
    return {"message": "Hello, world!"}

@app.get("/status")
def status():
    return {"status": "ok"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": f"User {user_id}"}
