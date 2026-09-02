from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "hello everyone!"}

@app.get("/runs")
def list_runs():
    return [
        {"id": 1, "date": "2026-08-25", "distance_km": 5.0, "duration_min": 27.5},
        {"id": 2, "date": "2026-08-26", "distance_km": 6.0, "duration_min": 30}
    ]