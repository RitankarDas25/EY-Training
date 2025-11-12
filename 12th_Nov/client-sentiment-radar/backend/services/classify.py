import pandas as pd
from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis")

def batch_classify(feedbacks):
    results = sentiment_model(feedbacks)
    df = pd.DataFrame({
        "feedback": feedbacks,
        "sentiment": [r["label"] for r in results],
        "confidence": [r["score"] for r in results],
    })
    return df
