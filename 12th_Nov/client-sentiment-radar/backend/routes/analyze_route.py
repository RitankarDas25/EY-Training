from fastapi import APIRouter
from pydantic import BaseModel
from services.classify import batch_classify
from services.churn import add_churn_scores, aggregate_by_client
from services.topics import extract_topics
from services.summarize import generate_summary

router = APIRouter()

class FeedbackRequest(BaseModel):
    feedbacks: list[str]

@router.post("/")
def analyze_feedback(req: FeedbackRequest):
    df = batch_classify(req.feedbacks)
    df = add_churn_scores(df)
    topics = extract_topics(df)
    summary = generate_summary(req.feedbacks)
    stats = aggregate_by_client(df)

    return {
        "summary": summary,
        "topics": topics,
        "stats": stats,
        "data": df.to_dict(orient="records")
    }
