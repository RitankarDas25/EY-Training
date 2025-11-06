import React, { useState } from "react";
import axios from "./axios";  // Axios instance for API requests
import StockData from "./components/StockData";  // Component to display stock data
import FinancialInsights from "./components/FinancialInsights";  // Component to display financial insights

function App() {
  const [ticker, setTicker] = useState(""); // Stock ticker input
  const [data, setData] = useState(null); // State to store stock data
  const [insights, setInsights] = useState(null); // State to store generated insights
  const [loading, setLoading] = useState(false); // State to manage loading state

  // Function to fetch stock data from the backend
  const fetchStockData = async () => {
    setLoading(true);
    try {
      const response = await axios.post("/get-stock-data/", {
        ticker: ticker,
        period: "1y",
      });
      setData(response.data.data);
    } catch (error) {
      console.error("Error fetching stock data:", error);
    } finally {
      setLoading(false);
    }
  };

  // Function to fetch financial insights using OpenRouter models
  const fetchFinancialInsights = async () => {
    setLoading(true);
    try {
      const response = await axios.post("/financial-insights/", {
         ticker: ticker,
         period: "1y",  // ✅ Added period (default: 1 year)
         model: "gpt-4o-mini",  // Use GPT-4O-mini model
         temperature: 0.7,
         max_tokens: 150,
         prompt: "Analyze the recent stock trends and predict next week's movement.", // Optional but good to include
     });
      setInsights(response.data.insights);
    } catch (error) {
      console.error("Error fetching insights:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>AI-Driven Financial Analytics Dashboard</h1>

      {/* Input for stock ticker */}
      <input
        type="text"
        placeholder="Enter Stock Ticker (e.g., AAPL)"
        value={ticker}
        onChange={(e) => setTicker(e.target.value)}
      />
      <button onClick={fetchStockData} disabled={loading}>
        Get Stock Data
      </button>
      <button onClick={fetchFinancialInsights} disabled={loading}>
        Get Financial Insights
      </button>

      {/* Show loading spinner if data or insights are being fetched */}
      {loading && <p>Loading...</p>}

      {/* Display stock data if available */}
      {data && <StockData data={data} />}

      {/* Display financial insights if available */}
      {insights && <FinancialInsights insights={insights} />}
    </div>
  );
}

export default App;
