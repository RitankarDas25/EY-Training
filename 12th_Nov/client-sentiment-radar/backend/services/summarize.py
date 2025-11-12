from services.llm import chat

def generate_summary(feedbacks):
    """
    Generates a summary of up to 50 feedback entries.
    """
    joined = "\n".join(feedbacks[:50])
    prompt = f"""
You are an AI sentiment analyst. Given these customer reviews, summarize key insights:
- Top praises
- Common complaints
- Churn risk overview

Reviews:
{joined}
"""
    return chat(prompt)
