import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Main from "./pages/Main";
import About from "./pages/About";
import Documents from "./pages/Documents";
import CanvasBackground from "./components/Background";
import CloudflareChallenge from "./components/CloudflareChallenge.jsx"; // Import the challenge component

import "./App.css";

function App() {
  return (
    <>
      {/* Load Cloudflare challenge script */}
      <CloudflareChallenge />
      
      {/* Your background component */}
      <CanvasBackground />
      
      {/* React Router setup */}
      <Router>
        <Routes>
          <Route path="/about" element={<About />} />
          <Route path="/" element={<Main />} />
          <Route path="/documents" element={<Documents />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
