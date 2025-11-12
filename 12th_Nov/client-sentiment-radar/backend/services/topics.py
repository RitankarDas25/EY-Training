from services.llm import chat
import json
import re

def extract_topics(df, top_n=5):
    """
    Uses LLM (chat from llm.py) to extract the top topics semantically.
    Ensures robust JSON parsing even if model adds text around JSON.
    """
    all_feedback = "\n".join(df["feedback"].astype(str).tolist())

    prompt = f"""
    Analyze the following customer reviews and extract the top {top_n} key discussion topics.
    Group similar feedback under one label (e.g., "battery backup" and "battery life" → "battery").
    For each topic, estimate roughly how many reviews discuss it.

    Return **only** valid JSON in this format:
    [
      {{"topic": "delivery time", "count": 12}},
      {{"topic": "customer support", "count": 9}},
      {{"topic": "app performance", "count": 6}}
    ]

    Do not include explanations, text, or markdown — only pure JSON.

    Reviews:
    {all_feedback}
    """

    try:
        response = chat(prompt, system="You are an expert data analyst extracting semantic topics from customer feedback.")
        response = response.strip()

        # Extract JSON portion only if LLM added extra text
        json_match = re.search(r"\[.*\]", response, re.DOTALL)
        if json_match:
            response = json_match.group(0)

        topics = json.loads(response)
        if isinstance(topics, list):
            return topics
        else:
            raise ValueError("Invalid LLM output structure")

    except Exception as e:
        print(f" Error extracting topics via LLM: {e}")
        print(f"Raw LLM response:\n{response}")
        # fallback topic output
        return [{"topic": "General Feedback", "count": len(df)}]
