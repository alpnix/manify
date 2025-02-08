import React, { useRef, useState, useEffect } from 'react';

const VideoSection = ({ video, transcript }) => {
  const videoRef = useRef(null);
  const [currentTime, setCurrentTime] = useState(0);
  const [hoveredTimestamp, setHoveredTimestamp] = useState(null);

  const timestampedTranscript = `0:00
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
And that's all there is to it! The Power Rule - simple, elegant, and incredibly useful. Thanks for watching!`;

  // Parse timestamps and create a structured array of transcript segments
  const segments = timestampedTranscript.split('\n\n').map(segment => {
    const [timestamp, ...textParts] = segment.split('\n');
    const [minutes, seconds] = timestamp.split(':').map(Number);
    return {
      timestamp,
      timeInSeconds: minutes * 60 + seconds,
      text: textParts.join(' ')
    };
  });

  // Find the current segment based on video time
  const getCurrentSegment = (timeInSeconds) => {
    for (let i = segments.length - 1; i >= 0; i--) {
      if (timeInSeconds >= segments[i].timeInSeconds) {
        return segments[i].timestamp;
      }
    }
    return null;
  };

  // Handle video time updates
  useEffect(() => {
    const video = videoRef.current;
    if (!video) return;

    const handleTimeUpdate = () => {
      setCurrentTime(video.currentTime);
    };

    video.addEventListener('timeupdate', handleTimeUpdate);
    return () => video.removeEventListener('timeupdate', handleTimeUpdate);
  }, []);

  const handleSegmentClick = (timestamp) => {
    if (videoRef.current) {
      const [minutes, seconds] = timestamp.split(':').map(Number);
      const timeInSeconds = minutes * 60 + seconds;
      videoRef.current.currentTime = timeInSeconds;
      videoRef.current.play();
    }
  };

  const renderTranscript = () => {
    const currentSegmentTimestamp = getCurrentSegment(currentTime);

    return segments.map((segment, index) => {
      const isCurrentSegment = segment.timestamp === currentSegmentTimestamp;
      const isHovered = segment.timestamp === hoveredTimestamp;

      return (
        <div 
          key={index} 
          className={`mb-4 transition-colors duration-200 ${
            isCurrentSegment || isHovered ? 'bg-blue-100 rounded-md p-2' : ''
          }`}
          onClick={() => handleSegmentClick(segment.timestamp)}
          onMouseEnter={() => setHoveredTimestamp(segment.timestamp)}
          onMouseLeave={() => setHoveredTimestamp(null)}
        >
          <span className="text-blue-500 cursor-pointer hover:underline">
            [{segment.timestamp}]
          </span>
          <span className={`ml-2 text-gray-700 cursor-pointer`}>
            {segment.text}
          </span>
        </div>
      );
    });
  };

  if (!video) return null;

  return (
    <div className="container mx-auto px-4 mt-6">
      <div className="flex gap-4 h-4/5">
        <div className="w-4/5">
          <div className="w-full aspect-video bg-black rounded-lg">
          <video 
            autoPlay={true}
            ref={videoRef} 
            controls 
            className="w-full h-full object-contain"
          >
          <source src={video} type="video/mp4" />
          Your browser does not support the video tag.
          </video>
          </div>
        </div>
        
        <div className="w-1/5 p-4 bg-gray-50 rounded-lg overflow-y-auto max-h-[calc(100vh-20rem)]">
          <h3 className="text-lg font-semibold mb-2 text-gray-900">Transcript</h3>
          <div className="space-y-2">
            {renderTranscript()}
          </div>
        </div>
      </div>
    </div>
  );
};

export default VideoSection;