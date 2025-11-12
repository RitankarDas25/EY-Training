import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.analyze_route import router as analyze_router
from routes.scrape_route import router as scrape_router


app = FastAPI(title="Client Sentiment Radar API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(analyze_router, prefix="/analyze", tags=["Analysis"])
app.include_router(scrape_router, prefix="/scrape", tags=["Scraping"])

@app.get("/")
def home():
    return {"message": "Client Sentiment Radar API is running "}
