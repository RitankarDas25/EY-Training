from pydantic import BaseModel, Field
from typing import Optional

class AIRequest(BaseModel):
    """
    Schema for AI-based operations: math, date, reverse, etc.
    """
    action: str = Field(
        ...,
        description="The operation to perform. Options: 'math', 'date', 'reverse'."
    )
    payload: Optional[str] = Field(
        default="",
        description="Input text or expression (used for 'math' or 'reverse')."
    )
    model: str = Field(
        default="gpt-4omini",
        description="The OpenRouter model to use."
    )
    temperature: float = Field(
        default=0.7,
        description="Creativity level for AI response."
    )
    max_tokens: int = Field(
        default=150,
        description="Maximum number of tokens in AI output."
    )


class Feedback(BaseModel):
    """
    Schema for user feedback on AI responses.
    """
    action: str
    rating: int
    comment: Optional[str] = ""
