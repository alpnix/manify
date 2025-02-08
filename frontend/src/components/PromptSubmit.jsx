import React, { useState } from 'react';
import { Send } from 'lucide-react';

const TopSection = ({ onPromptSubmit, pastPrompts, onPromptSelect }) => {
  const [isHistoryOpen, setIsHistoryOpen] = useState(false);
  const [prompt, setPrompt] = useState('');

  const handleSubmit = () => {
    if (prompt.trim()) {
      onPromptSubmit(prompt);
      setPrompt('');
    }
  };

  return (
    <div className="container mx-auto px-4 py-6">
      <div className="flex gap-4 items-center">
        {/* History Toggle Button */}
        <button 
          onClick={() => setIsHistoryOpen(!isHistoryOpen)}
          className="flex flex-col gap-1.5 p-2"
        >
          <div className="w-6 h-0.5 bg-white"></div>
          <div className="w-6 h-0.5 bg-white"></div>
          <div className="w-6 h-0.5 bg-white"></div>
        </button>

        {/* Prompt Input */}
        <input
          type="text"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your prompt here..."
          className="flex-1 p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />

        {/* Submit Button */}
        <button
          onClick={handleSubmit}
          className="px-6 py-3 bg-primary text-white rounded-md hover:bg-primary-800 flex items-center gap-2"
        >
          <Send className="w-4 h-4" />
          Generate
        </button>
      </div>

      {/* History Section */}
      {isHistoryOpen && (
        <div className="mt-4 border border-gray-200 rounded-md bg-white">
          <div className="max-h-60 overflow-y-auto p-4">
            {pastPrompts.length === 0 ? (
              <p className="text-gray-500 text-center">No history yet</p>
            ) : (
              <div className="space-y-2">
                {pastPrompts.map((item) => (
                  <div
                    key={item.id}
                    onClick={() => onPromptSelect(item)}
                    className="p-3 border border-gray-200 rounded-md cursor-pointer hover:bg-gray-50"
                  >
                    <p className="text-sm">{item.prompt}</p>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default TopSection;