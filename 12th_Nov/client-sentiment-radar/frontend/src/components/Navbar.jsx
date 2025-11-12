import React from "react";

export default function Navbar({ mode, setMode }) {
  return (
    <nav className="navbar">
      <div className="nav-logo">Client Sentiment Radar</div>

      <ul className="nav-links">
        <li>
          <button
            className={mode === "scrape" ? "active" : ""}
            onClick={() => setMode("scrape")}
          >
            Scrape
          </button>
        </li>
        <li>
          <button
            className={mode === "upload" ? "active" : ""}
            onClick={() => setMode("upload")}
          >
            Upload
          </button>
        </li>
        <li>
          <button
            className={mode === "about" ? "active" : ""}
            onClick={() => setMode("about")}
          >
            About
          </button>
        </li>
      </ul>
    </nav>
  );
}
