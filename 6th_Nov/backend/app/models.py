from pydantic import BaseModel

# Updated StockRequest model with the necessary fields
class StockRequest(BaseModel):
    ticker: str
    period: str = '1y'  # Default to 1 year
    prompt: str  # Add this field
    model: str = 'gpt-4o-mini'  # Default model if not provided
    temperature: float = 0.7  # Default temperature
    max_tokens: int = 150  # Default max tokens
