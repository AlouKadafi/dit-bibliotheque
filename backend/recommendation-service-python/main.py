from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "service": "recommendation-service",
        "status": "running"
    }