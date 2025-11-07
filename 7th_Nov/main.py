from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import requests
import os
import json

# Load environment variables
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

if not OPENROUTER_API_KEY:
    raise RuntimeError("Missing OPENROUTER_API_KEY in .env")

app = FastAPI()

# Allow frontend requests from your local HTML page
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data model for incoming JSON
class Prompt(BaseModel):
    query: str

@app.post("/generate")
async def generate_response(prompt: Prompt):
    """Generate a response using an OpenRouter model"""
    if not prompt.query.strip():
        raise HTTPException(status_code=400, detail="Empty input not allowed.")

    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "mistralai/mixtral-8x7b-instruct",  # <-- corrected model ID
            "messages": [
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt.query},
            ],
        }

        # Send request to OpenRouter
        response = requests.post(f"{OPENROUTER_BASE_URL}/chat/completions",
                                 headers=headers, json=payload)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code,
                                detail=f"OpenRouter error: {response.text}")

        data = response.json()
        answer = data["choices"][0]["message"]["content"]

        # Save Q&A history to local JSON file
        history_entry = {"query": prompt.query, "response": answer}
        with open("qa_history.json", "a", encoding="utf-8") as f:
            f.write(json.dumps(history_entry, ensure_ascii=False) + "\n")

        return {"response": answer}

    except Exception as e:
        print(" Backend Error:", e)
        raise HTTPException(status_code=500, detail=str(e))
