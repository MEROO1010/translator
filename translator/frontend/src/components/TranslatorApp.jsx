import React, { useState } from "react";
import ComparisonView from "./ComparisonView";
import GlossaryManager from "./GlossaryManager";

export default function TranslatorApp() {
  const [text, setText] = useState("");
  const [results, setResults] = useState(null);
  const [context, setContext] = useState("technical");
  const [glossary, setGlossary] = useState({});

  const handleTranslate = async () => {
    const response = await fetch("/translate", {
      method: "POST",
      body: JSON.stringify({ text, context, glossary }),
    });
    const data = await response.json();
    setResults(data.results);
  };

  return (
    <div>
      <textarea value={text} onChange={(e) => setText(e.target.value)} />
      <select value={context} onChange={(e) => setContext(e.target.value)}>
        <option value="technical">Technical</option>
        <option value="legal">Legal</option>
      </select>
      <GlossaryManager glossary={glossary} setGlossary={setGlossary} />
      <button onClick={handleTranslate}>Translate</button>
      {results && <ComparisonView results={results} />}
    </div>
  );
}