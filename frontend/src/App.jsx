import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Main from "./pages/Main";
import About from "./pages/About";
import Documents from "./pages/Documents";

import CanvasBackground from "./components/Background";

import "./App.css";



function App() {
  return (
    <>
      <CanvasBackground />
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