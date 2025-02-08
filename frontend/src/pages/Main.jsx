import React, { useState } from 'react';
import Navbar from '../components/Navbar';          // Your existing Navbar component
import VideoSection from '../components/VideoTranscript'; // Your video/transcript component
import { Send, Trash2 } from 'lucide-react';

const MainPage = ({}) => {
  const [video, setVideo] = useState(null);
  const [transcript, setTranscript] = useState('');
  const [isHistoryOpen, setIsHistoryOpen] = useState(false);
  const [prompt, setPrompt] = useState('');
  const [pastPrompts, setPastPrompts] = useState(localStorage.getItem('pastPrompts') ? JSON.parse(localStorage.getItem('pastPrompts')) : []);

  const youtubeVideos = ["https://www.youtube.com/embed/LPZh9BOjkQs"];
  const youtubeTranscripts = ["good video"] 


  const onPromptSubmit = (prompt) => {
    const newPrompt = {
      id: Date.now(),
      prompt: prompt.length > 50 ? prompt.slice(0, 50) + "..." : prompt,
    };
    const newPrompts = [newPrompt, ...pastPrompts];
    localStorage.setItem('pastPrompts', JSON.stringify(newPrompts));
    const randomIndex = Math.floor(Math.random() * Math.min(youtubeVideos.length, youtubeTranscripts.length));
    setVideo(youtubeVideos[randomIndex]);
    setTranscript(youtubeTranscripts[randomIndex]);
    setPastPrompts(newPrompts);
  }

  const onPromptSelect = (prompt) => {
    setPrompt(prompt.prompt);
  } 
  
  const onPromptDelete = (id) => {
    const newPrompts = pastPrompts.filter((item) => item.id !== id);
    localStorage.setItem('pastPrompts', JSON.stringify(newPrompts));
    setPastPrompts(newPrompts); 
  }

  const handleSubmit = () => {
    if (prompt.trim()) {
      onPromptSubmit(prompt);
      setPrompt('');
    }
  };

  // Handle key press on the textarea to submit on Enter (unless Shift is pressed)
  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault(); // Prevents adding a newline
      handleSubmit();
    }
  };

  return (
    <div className="flex flex-col h-screen bg-dark text-white">
      {/* Navbar at the very top, wrapped in a full-width container */}
      <div className="w-full">
        <Navbar />
      </div>

      {/* Main Content Area */}
      <div className="flex flex-1 relative">
        {/* History Sidebar (overlay on left) */}
        {isHistoryOpen && (
          <div className="absolute left-0 top-0 h-full w-1/4 bg-gray-800 border-r border-gray-700 p-4 overflow-y-auto z-10">
            <h3 className="text-xl font-semibold mb-4">History</h3>
            {pastPrompts.length === 0 ? (
              <p className="text-gray-400 text-center">No history yet</p>
            ) : (
              <div className="space-y-2">
                {pastPrompts.map((item) => (
                  <div
                    key={item.id}
                    onClick={() => onPromptSelect(item)}
                    className="flex items-center justify-between p-3 border border-gray-700 rounded-md cursor-pointer hover:bg-gray-700"
                  >
                    <p className="text-sm">{item.prompt}</p>
                    <button
                      onClick={(e) => {
                        // Prevent triggering onPromptSelect when clicking the trash icon
                        e.stopPropagation();
                        e.target.parentElement.parentElement.style.display = "none";
                        // Call onPromptDelete (ensure this prop is passed from the parent)
                        onPromptDelete(item.id);
                      }}
                      className="text-gray-400 hover:text-gray-200"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}

        {/* Central Content: Video & Transcript */}
        <div className="flex flex-col flex-1 overflow-y-auto">
          <div className="px-4 py-6">
            {video ? (
              <VideoSection video={video} transcript={transcript} />
            ) : (
              <div className="flex flex-1 items-center justify-center">
                <p className="text-gray-400">Submit a prompt to generate a video.</p>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Prompt Input Area (fixed at bottom) */}
      <div className="border-t border-gray-700 px-4 py-4 bg-gray-800">
        <div className="flex items-center gap-4">
          {/* Hamburger Button for History placed at bottom-left */}
          <button
            onClick={() => setIsHistoryOpen(!isHistoryOpen)}
            className="flex flex-col gap-1.5 p-2 focus:outline-none"
          >
            <div className="w-6 h-0.5 bg-white"></div>
            <div className="w-6 h-0.5 bg-white"></div>
            <div className="w-6 h-0.5 bg-white"></div>
          </button>

          {/* Textarea for prompt input (allows wrapping) */}
          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Enter your prompt here..."
            rows={2}
            className="flex-1 p-3 border border-gray-600 rounded-md bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
          />

          {/* Submit Button */}
          <button
            onClick={handleSubmit}
            className="px-6 py-3 bg-primary text-white rounded-md hover:bg-opacity-90 flex items-center gap-2 focus:outline-none"
          >
            <Send className="w-4 h-4" />
            Generate
          </button>
        </div>
      </div>
    </div>
  );
};

export default MainPage;
