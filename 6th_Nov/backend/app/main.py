from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models import StockRequest
from .utils import get_stock_data, call_openrouter_model

app = FastAPI()

# Add CORS middleware to allow requests from your React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (adjust as needed for production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


@app.post("/get-stock-data/")
def get_stock(request: StockRequest):
    # Fetch stock data using Yahoo Finance or another data source
    stock_data = get_stock_data(request.ticker, request.period)

    if stock_data is None:
        raise HTTPException(status_code=404, detail="Stock data not found or symbol might be delisted.")

    return {"data": stock_data.to_dict()}


@app.post("/financial-insights/")
def financial_insights(request: StockRequest):
    # Fetch stock data using the ticker and period
    stock_data = get_stock_data(request.ticker, request.period)

    if stock_data is None:
        raise HTTPException(status_code=404, detail="Stock data not found or symbol might be delisted.")

    # Convert stock data to a string format to pass to the model
    data_str = stock_data.to_string()

    # Generate a default prompt if no prompt is provided in the request
    prompt = f"Given the following stock data, provide insights on the trend and predict the next week: {data_str}"

    # Override prompt if the user has provided one
    if request.prompt:
        prompt = request.prompt

    try:
        # Call the OpenRouter model API to generate financial insights
        result = call_openrouter_model(
            prompt=prompt,
            model=request.model,  # Using the model specified in the request
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )

        # Get the insights from the result returned by the model
        insights = result.get("choices", [{}])[0].get("text", "No insights generated.")

    except Exception as e:
        # Handle errors that may occur during the OpenRouter API call
        raise HTTPException(status_code=500, detail=f"Error fetching insights from model: {str(e)}")

    return {"insights": insights}
