import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import summarize_route, qa_route

app = FastAPI(title="Research Paper Summarizer + QA API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(summarize_route.router)
app.include_router(qa_route.router)

@app.get("/")
def root():
    return {"message": "Welcome to Research Paper Summarizer API"}
