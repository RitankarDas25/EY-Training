import React from "react";


export default function Footer() {
  return (
    <footer className="footer">
      <div className="footer-content">
        <h3>Client Sentiment Radar</h3>
        <p>
          Powered by AI-driven insights. Analyze customer sentiment, identify trends,
          and predict churn with confidence.
        </p>

        <div className="footer-contact">
          <p>📧 Email: ritankar25@gmail.com</p>
          <p>📞 Phone: +91-xxxxxxxxx</p>
          <p>🌐 Website: www.clientsentimentradar.ai</p>
        </div>

        <p className="footer-copy">
          © {new Date().getFullYear()} Client Sentiment Radar. All rights reserved.
        </p>
      </div>
    </footer>
  );
}
