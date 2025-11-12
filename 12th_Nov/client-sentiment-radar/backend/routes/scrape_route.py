from fastapi import APIRouter, Query
from services.scrape import auto_scrape

router = APIRouter()

@router.get("/")
def scrape_reviews(url: str = Query(..., description="Product review page URL"), pages: int = 2):
    reviews = auto_scrape(url, max_pages=pages)
    return {"reviews": reviews, "count": len(reviews)}
