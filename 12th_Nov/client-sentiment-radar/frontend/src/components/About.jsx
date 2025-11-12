import React from "react";

export default function About() {
  return (
    <div className="about-page">
      <h2>About Client Sentiment Radar</h2>
      <p>
        Client Sentiment Radar helps businesses quickly understand customer
        feedback through AI-powered sentiment analysis. Upload or scrape reviews
        and instantly visualize sentiment breakdown, trending topics, and churn risk.
      </p>
      <p>
        Built with React for the frontend and FastAPI for the backend. It uses AI models
        to summarize feedback and provide actionable insights.
      </p>
    </div>
  );
}
