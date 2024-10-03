import React, { useState } from "react";
import axios from "axios";

function Chatbox() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [response, setResponse] = useState("");
  const [contextMode, setContextMode] = useState(null); // null means mode not selected

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (input.trim()) {
      setMessages((prevMessages) => [
        ...prevMessages,
        { user: "User", text: input },
      ]);
      setInput("");
    }

    try {
      const res = await axios.post("http://localhost:8000/api/process_input/", {
        input,
        contextMode,
        messages,
      });
      setResponse(res.data.response);
      if (res.data.response.trim()) {
        setMessages((prevMessages) => [
          ...prevMessages,
          { user: "Bot", text: res.data.response },
        ]);
      }
    } catch (error) {
      console.error("Error occurred:", error);
      setResponse("Error processing input.");
    }
  };

  const handleModeSelection = (mode) => {
    setContextMode(mode);
  };

  const handleBack = () => {
    setContextMode(null);
    setMessages([]);
  };

  return (
    <div className="flex items-center justify-center">
      <div
        className={`${
          contextMode === null ? "w-full max-w-md" : "w-2/3 h-2/3"
        } mx-auto bg-white shadow-lg rounded-lg overflow-hidden flex flex-col`}
        style={{
          height: contextMode === null ? "auto" : "66vh",
          width: "66vw",
        }}
      >
        {contextMode === null ? (
          <div className="p-6 flex flex-col items-center space-y-4">
            <h1 className="text-2xl font-bold mb-4 text-center">
              Select Chat Mode
            </h1>
            <button
              onClick={() => handleModeSelection(true)}
              className="bg-blue-500 text-white p-2 rounded w-full"
            >
              Keep Context
            </button>
            <button
              onClick={() => handleModeSelection(false)}
              className="bg-gray-500 text-white p-2 rounded w-full"
            >
              Do Not Keep Context
            </button>
          </div>
        ) : (
          <>
            <div className="p-6 h-full overflow-y-auto relative flex-grow">
              <button
                onClick={handleBack}
                className="sticky top-0 left-0 mt-2 ml-2 bg-gray-500 text-white p-2 rounded"
              >
                Back
              </button>
              <div className="space-y-4 mt-10">
                {messages.map((message, index) => (
                  <div
                    key={index}
                    className={`flex ${
                      message.user === "User" ? "justify-end" : "justify-start"
                    }`}
                  >
                    <span
                      className={`${
                        message.user === "User"
                          ? "bg-blue-500 text-white"
                          : "bg-gray-300 text-black"
                      } rounded px-4 py-2`}
                    >
                      {message.text}
                    </span>
                  </div>
                ))}
              </div>
            </div>
            <form onSubmit={handleSubmit} className="border-t p-4">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                className="w-full p-2 border rounded focus:outline-none focus:ring focus:border-blue-300"
                placeholder="Type here..."
              />
            </form>
          </>
        )}
      </div>
    </div>
  );
}

export default Chatbox;
