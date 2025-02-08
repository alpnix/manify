import React from "react";

const Navbar = () => {
  return (
    <nav className="grid grid-cols-3 items-center px-6 py-4 bg-white shadow-md">
      {/* Left Section: About */}
      <div className="text-left">
        <a 
          href="/about" 
          className="text-xl text-gray-700 hover:text-gray-900 transition-colors duration-200"
        >
          About
        </a>
      </div>

      {/* Center Section: Logo (Home link) */}
      <div className="flex justify-center">
        <a href="/">
          <img 
            src="/manify-logo.png" 
            alt="Manify Logo" 
            className="h-12" 
          />
        </a>
      </div>

      {/* Right Section: Documents */}
      <div className="text-right">
        <a 
          href="/documents" 
          className="text-xl text-gray-700 hover:text-gray-900 transition-colors duration-200"
        >
          Documents
        </a>
      </div>
    </nav>
  );
};

export default Navbar;
