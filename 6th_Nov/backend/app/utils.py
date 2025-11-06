import requests
import yfinance as yf
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Fetch OpenRouter credentials from the environment variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")

# Function to fetch stock data using yfinance
def get_stock_data(ticker: str, period: str = "1y"):
    stock = yf.Ticker(ticker)
    stock_data = stock.history(period=period)
    return stock_data

# Function to call OpenRouter API for generating insights
def call_openrouter_model(prompt: str, model: str, temperature: float, max_tokens: int):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": model,
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    url = f"{OPENROUTER_BASE_URL}/v1/engines/{model}/completions"
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to generate response", "status_code": response.status_code}
