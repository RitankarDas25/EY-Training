import React from "react";
import * as XLSX from "xlsx";

export default function FileUpload({ setReviews }) {
  const handleFile = async (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();

    reader.onload = (evt) => {
      const data = evt.target.result;
      const workbook = XLSX.read(data, { type: "binary" });
      const sheet = workbook.Sheets[workbook.SheetNames[0]];
      const rows = XLSX.utils.sheet_to_json(sheet, { header: 1 });
      const feedbacks = rows.flat().filter((f) => typeof f === "string");
      setReviews(feedbacks);
    };

    reader.readAsBinaryString(file);
  };

  return (
    <div className="input-card">
      <h3>Upload Review File</h3>
      <input type="file" accept=".csv, .xlsx, .txt" onChange={handleFile} />
    </div>
  );
}
