module.exports = {
  purge: ["./src/**/*.{js,jsx,ts,tsx}", "./public/index.html"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        customBackground: "#f0f4f8", // Replace with your desired color
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
