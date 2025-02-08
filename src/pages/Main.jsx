import React from 'react';
import "../App.css";

import Navbar from "../components/Navbar";

const Main = () => {

    return (
        <div className="min-h-screen justify-center bg-dark">
        <Navbar />
        <h1 className="text-4xl font-bold text-primary">
          Main Page
        </h1>
        <p className="mt-4 text-gray-700 text-secondary">
          This is a basic template to get you started.
        </p>
      </div>
    );
}

export default Main;