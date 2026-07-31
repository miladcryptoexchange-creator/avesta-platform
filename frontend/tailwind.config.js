/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        avesta: {
          dark: '#080808',
          purple: '#8B2BE2',
          blue: '#4169E1',
          gold: '#FFD700',
          neon: '#00FFFF'
        }
      }
    },
  },
  plugins: [],
}
