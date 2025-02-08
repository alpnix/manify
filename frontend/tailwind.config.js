/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx}", // Ensure all files where you use Tailwind classes are included
  ],
  theme: {
    extend: {
      colors: {
        primary: "#74C0E2",   // Use as your primary color
        secondary: "#8C6137", // Use as your secondary color
        dark: "#000000",      // Use as your dark color
      },
    },
  },
  plugins: [],
};