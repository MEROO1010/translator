import React, { useState } from "react";

export default function GlossaryManager({ glossary, setGlossary }) {
  const [source, setSource] = useState("");
  const [target, setTarget] = useState("");

  const addTerm = () => {
    setGlossary({ ...glossary, [source]: target });
    setSource("");
    setTarget("");
  };

  return (
    <div>
      <input
        value={source}
        onChange={(e) => setSource(e.target.value)}
        placeholder="Source term"
      />
      <input
        value={target}
        onChange={(e) => setTarget(e.target.value)}
        placeholder="Target term"
      />
      <button onClick={addTerm}>Add Term</button>
      <ul>
        {Object.entries(glossary).map(([s, t]) => (
          <li key={s}>{s} → {t}</li>
        ))}
      </ul>
    </div>
  );
}