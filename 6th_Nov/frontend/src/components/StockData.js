import React from 'react';

function StockData({ data }) {
  return (
    <div>
      <h3>Stock Data</h3>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default StockData;
