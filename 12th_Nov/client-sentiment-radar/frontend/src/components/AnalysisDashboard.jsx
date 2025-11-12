import React, { useEffect, useRef } from "react";
import Chart from "chart.js/auto";
import ReactMarkdown from "react-markdown";

export default function AnalysisDashboard({ data }) {
  const barChartRef = useRef(null);
  const pieChartRef = useRef(null);
  const barChartInstanceRef = useRef(null);
  const pieChartInstanceRef = useRef(null);

  useEffect(() => {
    if (!data?.stats) return;

    const labels = Object.keys(data.stats);
    const values = Object.values(data.stats);
    const colors = ["#4CAF50", "#FF9800", "#F44336"];

    // Destroy old charts before creating new ones
    if (barChartInstanceRef.current) barChartInstanceRef.current.destroy();
    if (pieChartInstanceRef.current) pieChartInstanceRef.current.destroy();

    // Bar Chart
    const barCtx = barChartRef.current.getContext("2d");
    barChartInstanceRef.current = new Chart(barCtx, {
      type: "bar",
      data: {
        labels,
        datasets: [
          {
            label: "Sentiment Breakdown",
            data: values,
            backgroundColor: colors,
            borderRadius: 8,
          },
        ],
      },
      options: {
        responsive: true,
        plugins: {
          legend: { labels: { color: "#e0e6ff" } },
        },
        scales: {
          x: {
            ticks: { color: "#b3c7ff" },
            grid: { color: "#1a2b55" },
          },
          y: {
            ticks: { color: "#b3c7ff" },
            grid: { color: "#1a2b55" },
          },
        },
      },
    });

    // Pie Chart
    const pieCtx = pieChartRef.current.getContext("2d");
    pieChartInstanceRef.current = new Chart(pieCtx, {
      type: "pie",
      data: {
        labels,
        datasets: [
          {
            label: "Sentiment Share",
            data: values,
            backgroundColor: colors,
            hoverOffset: 8,
          },
        ],
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: "bottom",
            labels: { color: "#e0e6ff" },
          },
        },
      },
    });

    return () => {
      barChartInstanceRef.current?.destroy();
      pieChartInstanceRef.current?.destroy();
    };
  }, [data]);

  return (
    <div className="results">
      <h2> Sentiment Analysis Dashboard</h2>

      <div className="dashboard-grid">
        {/* ===== Bar Chart Section ===== */}
        <div className="chart-section">
          <h3>Sentiment Overview (Bar)</h3>
          <canvas ref={barChartRef} style={{ maxHeight: "320px" }}></canvas>
        </div>

        {/* ===== Pie Chart Section ===== */}
        <div className="chart-section">
          <h3>Sentiment Share (Pie)</h3>
          <canvas ref={pieChartRef} style={{ maxHeight: "320px" }}></canvas>
        </div>
      </div>

      {/* ===== Trending Topics ===== */}
      <div className="topics-section">
        <h3 style={{ marginTop: "2rem" }}> Trending Topics</h3>
        {Array.isArray(data.topics) && data.topics.length > 0 ? (
          <ul>
            {data.topics.map((t, i) => (
              <li key={i}>
                {t.topic}: {t.count}
              </li>
            ))}
          </ul>
        ) : (
          <p>No topics found.</p>
        )}
      </div>

      {/* ===== AI Summary ===== */}
      <div className="summary-section" style={{ marginTop: "2rem" }}>
        <h3> AI Summary</h3>
        <div className="summary-markdown">
          <ReactMarkdown>{data.summary || "No summary available."}</ReactMarkdown>
        </div>
      </div>
    </div>
  );
}
