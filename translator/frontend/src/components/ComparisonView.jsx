import React from "react";

export default function ComparisonView({ results }) {
  return (
    <div style={{ display: "flex" }}>
      {Object.entries(results).map(([engine, result]) => (
        <div key={engine} style={{ flex: 1, padding: "10px" }}>
          <h3>{engine}</h3>
          <p>{result.translated_text}</p>
        </div>
      ))}
    </div>
  );
}