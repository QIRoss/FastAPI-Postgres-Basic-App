from fastapi import FastAPI
from pydantic import BaseModel
from src.endpoints import router
import os

app = FastAPI()

app.include_router(router)

class HealthResponse(BaseModel):
    status: str

@app.get("/health", response_model=HealthResponse)
def health_check():
    print("DB_USER:", os.getenv("DB_USER"))
    print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
    return {"status": "ok"}

