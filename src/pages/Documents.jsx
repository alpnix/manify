import React from 'react';
import "../App.css";

import Navbar from "../components/Navbar";

const Documents = () => {

    return (
        <div className="min-h-screen justify-center">
        <Navbar />
        <h1 className="text-4xl font-bold text-blue-500">
          Documents Page
        </h1>
        <p className="mt-4 text-gray-700">
          This is a basic template to get you started.
        </p>
      </div>
    );
}

export default Documents;