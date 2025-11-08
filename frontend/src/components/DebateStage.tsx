import React, { useState } from "react";
import "./DebateStage.css";

export default function DebateStage() {
  const [topic, setTopic] = useState("");
  const [started, setStarted] = useState(false);

  // Mock conversation
  const conversation = [
    {
      speaker: "AI1",
      text: "I believe technology improves our lives in countless ways.",
    },
    {
      speaker: "AI2",
      text: "But it also creates dependency and reduces human connection.",
    },
    {
      speaker: "AI1",
      text: "That’s true, but innovation drives progress and efficiency.",
    },
    {
      speaker: "AI2",
      text: "We must balance progress with empathy and responsibility.",
    },
  ];

  return (
    <div className="debate-stage">
      <h1>AI Debate</h1>

      {!started ? (
        <div className="setup">
          <input
            type="text"
            placeholder="Enter a debate topic..."
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
          />
          <button disabled={!topic} onClick={() => setStarted(true)}>
            Start Debate
          </button>
        </div>
      ) : (
        <div className="debate-area">
          <h2>Topic: {topic}</h2>
          <div className="chat">
            {conversation.map((msg, i) => (
              <div key={i} className={`message ${msg.speaker}`}>
                <div className="avatar">
                  {msg.speaker === "AI1" ? "🤖" : "🧠"}
                </div>
                <div className="bubble">
                  <strong>{msg.speaker}:</strong> {msg.text}
                </div>
              </div>
            ))}
          </div>
          <button onClick={() => setStarted(false)}>Reset</button>
        </div>
      )}
    </div>
  );
}
