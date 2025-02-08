// App.js
import React, { useState, useEffect } from 'react';

// A reusable loading component with a transparent background and a blue spinner.
const BlueLoadingComponent = () => {
  // Container style: It will only fill its parent's area with a transparent background.
  const containerStyle = {
    backgroundColor: 'transparent', // No overlay color; background remains transparent.
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    // Optionally, you can set a minHeight or other dimensions if needed.
  };

  // Spinner style: a circular spinner with a blue rotating border.
  const spinnerStyle = {
    width: '400px',
    height: '400px',
    border: '4px solid rgba(52, 152, 219, 0.3)', // Semi-transparent blue for all borders.
    borderTop: '4px solid #3498db',                // Blue color for the top border.
    borderRadius: '50%',
    animation: 'spin 1s linear infinite',         // Spin animation.
  };

  return (
    <div style={containerStyle}>
      <div style={spinnerStyle}></div>
      {/* Define keyframes for the spinner animation */}
      <style>
        {`
          @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
          }
        `}
      </style>
    </div>
  );
};

export default BlueLoadingComponent; 