from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # TODO(you): allow_origins takes a list of strings — add the full
    # URL (scheme + host + port) of your Vite dev server here
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "hello everyone!"}

@app.get("/runs")
def list_runs():
    return [
        {"id": 1, "date": "2026-08-25", "distance_km": 5.0, "duration_min": 27.5},
        {"id": 2, "date": "2026-08-26", "distance_km": 6.0, "duration_min": 30}
    ]