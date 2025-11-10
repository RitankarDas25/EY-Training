import os
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Initialize the OpenAI-compatible client
client = OpenAI(
    base_url=os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def call_openrouter(prompt: str, model="mistralai/mistral-7b-instruct", temperature=0.7, max_tokens=150):
    """Call OpenRouter (via OpenAI-compatible API)."""
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content.strip()

def ai_math(expr: str, model="mistralai/mistral-7b-instruct"):
    """Perform math using AI (with fallback safe eval)."""
    try:
        prompt = f"You are a math assistant. Solve this expression and return only the result: {expr}"
        return call_openrouter(prompt, model)
    except Exception:
        return safe_eval(expr)

def ai_date(model="mistralai/mistral-7b-instruct"):
    """Return current date/time using AI."""
    try:
        prompt = "Give the current date and time in format YYYY-MM-DD HH:MM:SS (local time)."
        return call_openrouter(prompt, model)
    except Exception:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def ai_reverse(text: str, model="mistralai/mistral-7b-instruct"):
    """Reverse given text using AI."""
    try:
        prompt = f"Reverse the following text: {text}"
        return call_openrouter(prompt, model)
    except Exception:
        return text[::-1]

def safe_eval(expr: str):
    """Safe fallback for math evaluation."""
    allowed = "0123456789+-*/(). "
    if not all(c in allowed for c in expr):
        raise ValueError("Unsafe expression.")
    return eval(expr, {"__builtins__": {}})
