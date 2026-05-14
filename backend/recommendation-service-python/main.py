from fastapi import FastAPI, HTTPException

app = FastAPI(title="Recommendation Service")

@app.get("/")
def root():
    return {
        "service": "recommendation-service",
        "status": "running"
    }

