import React, { useState } from "react";
import Navbar from "./components/Navbar.jsx";
import ScrapeInput from "./components/ScrapeInput.jsx";
import FileUpload from "./components/FileUpload.jsx";
import AnalysisDashboard from "./components/AnalysisDashboard.jsx";
import About from "./components/About.jsx";
import Footer from "./components/Footer.jsx";
import axios from "axios";
import "./App.css";

const API_URL = "http://127.0.0.1:8000";

export default function App() {
  const [mode, setMode] = useState("scrape"); // "scrape" | "upload" | "about"
  const [reviews, setReviews] = useState([]);
  const [results, setResults] = useState(null);
  const [status, setStatus] = useState(""); // <-- new: to show user messages

  const handleAnalyze = async () => {
    if (!reviews.length) {
      alert("No reviews to analyze!");
      return;
    }

    try {
      setStatus("Analyzing reviews... please wait ⏳");
      const res = await axios.post(`${API_URL}/analyze/`, { feedbacks: reviews });
      setResults(res.data);
      setStatus("✅ Analysis complete!");
      setTimeout(() => setStatus(""), 3000); // clear after few seconds
    } catch (err) {
      console.error(err);
      setStatus("❌ Error analyzing reviews. Please try again.");
    }
  };

  const handleModeChange = (newMode) => {
    setMode(newMode);
    setStatus(""); // clear status on mode switch

    // Clear results and reviews when switching to About
    if (newMode === "about") {
      setReviews([]);
      setResults(null);
    }
  };

  return (
    <>
      <Navbar mode={mode} setMode={handleModeChange} />

      <div className="container">
        <h1>Client Sentiment Radar</h1>

        {/* Status message display */}
        {status && <p className="status-message">{status}</p>}

        {/* Conditional rendering based on mode */}
        {mode === "scrape" && (
          <ScrapeInput
            setReviews={(data) => {
              setReviews(data);
              setStatus("Fetched reviews successfully ✅");
              setTimeout(() => setStatus(""), 3000);
            }}
          />
        )}
        {mode === "upload" && (
          <FileUpload
            setReviews={(data) => {
              setReviews(data);
              setStatus("File uploaded successfully ✅");
              setTimeout(() => setStatus(""), 3000);
            }}
          />
        )}
        {mode === "about" && <About />}

        {/* Analyze button and results only shown in scrape/upload mode */}
        {mode !== "about" && reviews.length > 0 && (
          <button className="analyze-btn" onClick={handleAnalyze}>
            Analyze Reviews
          </button>
        )}

        {mode !== "about" && results && <AnalysisDashboard data={results} />}
      </div>

      <Footer />
    </>
  );
}
