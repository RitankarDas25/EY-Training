import React from 'react';

function FinancialInsights({ insights }) {
  return (
    <div>
      <h3>Financial Insights</h3>
      <pre>{insights}</pre>
    </div>
  );
}

export default FinancialInsights;
