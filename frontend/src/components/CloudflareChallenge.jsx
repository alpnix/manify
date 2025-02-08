// CloudflareChallenge.jsx
import React, { useEffect } from "react";

const CloudflareChallenge = () => {
  useEffect(() => {
    // Replace the URL below with the actual Cloudflare challenge script URL if you have one.
    const script = document.createElement("script");
    script.src = "https://example.com/path/to/cloudflare-challenge.js"; // <-- Update this URL
    script.async = true;
    document.body.appendChild(script);
    
    // Clean up the script when the component unmounts
    return () => {
      document.body.removeChild(script);
    };
  }, []);

  return null;
};

export default CloudflareChallenge;
