# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"] for stricter security
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/students")
def get_students():
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
        {"id": 4, "name": "Diana"},
        {"id": 5, "name": "Ethan"}
    ]
