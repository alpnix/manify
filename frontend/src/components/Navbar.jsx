import React from "react";

const Navbar = () => {
  return (
    <>
    <nav className="mx-auto grid grid-cols-3 items-center px-48 py-4 bg-dark shadow-md grid-flow-col grid-flow-row-dense">
      {/* Left Section: About */}
      <div className="flex justify-start">
        <a 
          href="/about"
          className="text-xl font-semibold text-primary hover:underline transition-colors duration-200"
        >
          About
        </a>
      </div>

      {/* Center Section: Logo (Home link) */}
      <div className="flex justify-center">
        <a href="/">
          <img 
            src="/manify_logo.png" 
            alt="Manify Logo" 
            className="h-12" 
          />
        </a>
      </div>

      {/* Right Section: Documents */}
      <div className="flex justify-end">
        <a 
          href="/documents" 
          className="text-xl font-semibold text-primary hover:underline transition-colors duration-200"
        >
          Documents
        </a>
      </div>
    </nav>
    <hr />
    </>
  );
};

export default Navbar;
