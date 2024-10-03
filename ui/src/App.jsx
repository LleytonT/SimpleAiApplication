// src/App.js
import React from "react";
import Chatbox from "./components/Chatbox";

function App() {
  return (
    <div className="min-h-screen h-screen flex flex-col bg-grey">
      <h1 className="text-4xl text-center py-4">Simple HSC Tutor</h1>
      <div className="flex-grow flex items-center justify-center">
        <Chatbox />
      </div>
    </div>
  );
}

export default App;
