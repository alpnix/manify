import React, { useState } from 'react';
import Navbar from '../components/Navbar';
import VideoSection from '../components/VideoTranscript';
import { Send, Trash2 } from 'lucide-react';

const MainPage = () => {
  const [video, setVideo] = useState(null);
  const [transcript, setTranscript] = useState('');
  const [isHistoryOpen, setIsHistoryOpen] = useState(false);
  const [prompt, setPrompt] = useState('');
  const [pastPrompts, setPastPrompts] = useState(
    localStorage.getItem('pastPrompts') ? JSON.parse(localStorage.getItem('pastPrompts')) : []
  );

  const youtubeVideos = ["/videos/power_rule.mp4"];
  const youtubeTranscripts = [`0:00
Welcome! Today we're going to learn about one of the most fundamental concepts in calculus: the Power Rule for derivatives. This rule helps us find the derivatives of functions with variables raised to powers.

0:10
The Power Rule states that if we have a function f(x) = xⁿ, where n is any number, the derivative will be f'(x) = n · xⁿ⁻¹. In other words, we multiply by the power and reduce the exponent by 1.

0:25
This rule is incredibly powerful because it works for any exponent - whether it's positive, negative, or even a fraction. It's one of the first rules you'll learn in calculus, and you'll use it constantly.

0:35
The beauty of the Power Rule lies in its simplicity. There are just two steps: bring down the power as a multiplier, and subtract 1 from the original power.

0:45
Let's look at an example to see how this works. Say we have the function f(x) = x³.

0:52
Following the Power Rule, first we look at our exponent, which is 3. This becomes our multiplier.

1:00
Then we subtract 1 from the original exponent. So x³ becomes x².

1:08
Putting it all together, we get f'(x) = 3x². That's our derivative!

1:15
We can verify this works for any cubic function. If we had 2x³, the derivative would be 6x². If we had 5x³, the derivative would be 15x².

1:25
Remember, whenever you see a variable raised to a power, the Power Rule is your go-to method for finding the derivative. Just multiply by the power and subtract 1 from the exponent.

1:30
And that's all there is to it! The Power Rule - simple, elegant, and incredibly useful. Thanks for watching!`];

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
  };

  const onPromptSelect = (prompt) => {
    setPrompt(prompt.prompt);
  };

  const onPromptDelete = (id) => {
    const newPrompts = pastPrompts.filter((item) => item.id !== id);
    localStorage.setItem('pastPrompts', JSON.stringify(newPrompts));
    setPastPrompts(newPrompts);
  };

  const handleSubmit = () => {
    if (prompt.trim()) {
      onPromptSubmit(prompt);
      setPrompt('');
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  return (
    <div className="flex flex-col h-screen bg-dark text-white">
      <div className="w-full">
        <Navbar />
      </div>

      <div className="flex flex-1 relative">
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
                        e.stopPropagation();
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

      <div className="border-t border-gray-700 px-4 py-4 bg-gray-800">
        <div className="flex items-center gap-4">
          <button
            onClick={() => setIsHistoryOpen(!isHistoryOpen)}
            className="flex flex-col gap-1.5 p-2 focus:outline-none"
          >
            <div className="w-6 h-0.5 bg-white"></div>
            <div className="w-6 h-0.5 bg-white"></div>
            <div className="w-6 h-0.5 bg-white"></div>
          </button>

          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Enter your prompt here... (e.g. Derivative - Power Rule)"
            rows={2}
            className="flex-1 p-3 border border-gray-600 rounded-md bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
          />

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