from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

logs = []

class LogIn(BaseModel):
    bmi: float
    glucose: float

@app.post("/api/logger")
def create_log(entry: LogIn):
    logs.append({
        "bmi": entry.bmi,
        "glucose": entry.glucose,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    return {"status": "ok"}

@app.get("/api/logger")
def read_logs():
    return logs
