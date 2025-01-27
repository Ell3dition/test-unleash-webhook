from fastapi import FastAPI
from app.routers import unleash

app = FastAPI()
app.include_router(unleash.router)


@app.get("/health")
def read_root():
    return {"status": "ok"}
