import React, { useState, useEffect } from 'react';
import BlueLoadingScreen from './BlueLoadingScreen';

const Loading = () => {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Simulate data fetching or any async operation
    const timer = setTimeout(() => {
      setLoading(false);
    }, 3000);

    return () => clearTimeout(timer);
  }, []);

  return (
    <>
      {loading ? (
        <BlueLoadingScreen />
      ) : (
        <div>
          <h1>Your main application content goes here!</h1>
        </div>
      )}
    </>
  );
};

export default Loading;