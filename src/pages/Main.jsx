import React, { useState } from 'react';
import "../App.css";
import Navbar from "../components/Navbar";
import TopSection from "../components/PromptSubmit";
import VideoSection from "../components/VideoTranscript";

const Main = () => {
  const [pastPrompts, setPastPrompts] = useState([]);
  const [selectedPrompt, setSelectedPrompt] = useState(null);

  const handlePromptSubmit = async (prompt) => {
    // Here you would typically make an API call to generate the video
    // For now, we'll simulate it with a new prompt object
    const newPrompt = {
      id: Date.now(),
      prompt: prompt,
      video: `/api/videos/${Date.now()}`, // This would be your actual video URL
      transcript: `Transcript for: ${prompt}` // This would be your actual transcript
    };
    
    setPastPrompts([newPrompt, ...pastPrompts]);
    setSelectedPrompt(newPrompt);
  };

  return (
    <div className="min-h-screen bg-dark">
      <Navbar />
      
      <TopSection 
        onPromptSubmit={handlePromptSubmit}
        pastPrompts={pastPrompts}
        onPromptSelect={setSelectedPrompt}
      />
      
      <VideoSection 
        video={selectedPrompt?.video}
        transcript={selectedPrompt?.transcript}
      />
    </div>
  );
};

export default Main;