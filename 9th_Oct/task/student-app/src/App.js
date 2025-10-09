// src/App.js

import React, { useEffect, useState } from 'react';
import './App.css'; // Import the CSS file

function App() {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:8000/students')
      .then((res) => res.json())
      .then((data) => {
        setStudents(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Error fetching students:', err);
        setLoading(false);
      });
  }, []);

  return (
    <div className="container">
      <h1 className="title"> Student List</h1>
      {loading ? (
        <p className="loading">Loading students...</p>
      ) : (
        <ul className="student-list">
          {students.map((student) => (
            <li key={student.id} className="student-item">
              {student.id}. {student.name}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
