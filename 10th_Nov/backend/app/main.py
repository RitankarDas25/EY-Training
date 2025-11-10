from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models import AIRequest
from .utils import ai_math, ai_date, ai_reverse
from .middleware import LoggingMiddleware

app = FastAPI(title="AI Backend with OpenRouter + LangChain")

app.add_middleware(LoggingMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ai-action/")
async def ai_action(req: AIRequest):
    if req.action == "math":
        result = ai_math(req.payload)
        return {"action": "math", "input": req.payload, "result": result}
    elif req.action == "date":
        result = ai_date()
        return {"action": "date", "result": result}
    elif req.action == "reverse":
        result = ai_reverse(req.payload)
        return {"action": "reverse", "input": req.payload, "result": result}
    else:
        return {"error": "Unknown action"}
