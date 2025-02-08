import React from 'react';
import "../App.css";

import Navbar from "../components/Navbar";

const About = () => {

    return (
        <div className="min-h-screen justify-center background-dark">
        <Navbar />
        <h1 className="text-4xl font-bold text-blue-500">
          About Page
        </h1>
        <p className="mt-4 text-gray-700">
          This is a basic template to get you started.
        </p>
      </div>
    );
}

export default About;