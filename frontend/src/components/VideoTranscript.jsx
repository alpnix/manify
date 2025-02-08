import React from 'react';

const VideoSection = ({ video, transcript }) => {
  if (!video) return null;

  return (
    <div className="container mx-auto px-4 mt-6">
      <div className="flex gap-4 h-4/5">
        {/* Video Container - 80% */}
        <div className="w-4/5">
          <div className="w-full aspect-video bg-black rounded-lg">
          <video controls className='w-full h-full object-contain'>
            <source src={"/videos/power rule.mp4"} type="video/mp4" />
            Your browser does not support the video tag.
          </video>
          </div>
        </div>

        {/* Transcript Container - 20% */}
        <div className="w-1/5 p-4 bg-gray-50 rounded-lg overflow-y-auto max-h-[calc(100vh-20rem)]">
          <h3 className="text-lg font-semibold mb-2 text-secondary">Transcript</h3>
          <p className="text-gray-700">{transcript}</p>
        </div>
      </div>
    </div>
  );
};

export default VideoSection;