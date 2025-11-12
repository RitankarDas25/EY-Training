import React, { useState } from "react";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default function ScrapeInput({ setReviews }) {
  const [url, setUrl] = useState("");
  const [pages, setPages] = useState(2);

  const handleScrape = async () => {
    const res = await axios.get(`${API_URL}/scrape`, {
      params: { url, pages },
    });
    setReviews(res.data.reviews || []);
  };

  return (
    <div className="input-card">
      <h3>Scrape Product Reviews</h3>
      <input
        type="text"
        placeholder="Enter product URL..."
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />
      <input
        type="number"
        min="1"
        max="5"
        value={pages}
        onChange={(e) => setPages(e.target.value)}
      />
      <button onClick={handleScrape}>Fetch Reviews</button>
    </div>
  );
}
