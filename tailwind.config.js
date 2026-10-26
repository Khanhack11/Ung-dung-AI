/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      spacing: {
        px: '1px',
        0: '0px',
        1: '4px',
        2: '5px',
        3: '6px',
        4: '10px',
        5: '13px',
        6: '20px',
        7: '40px',
        8: '32px',
        10: '40px', 
        12: '48px',
        16: '64px',
        32: '128px',
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        primary: ['Inter', 'sans-serif'],
      },
      fontSize: {
        base: ['14px', '16.8px'],
        xs: '12px',
        sm: '13px',
        md: '14px',
        lg: '17px',
      },
      colors: {
        surface: {
          base: '#0f172a',
          muted: '#ffffff',
          raised: '#f8fafc',
          subtle: '#f1f5f9',
        },
        text: {
          secondary: '#9a7b4f',
          inverse: '#ffffff',
        },
        border: {
          strong: 'rgba(15, 23, 42, 0.15)',
          light: '#e2e8f0',
        },
        primary: {
          50: '#faf8f5',
          100: '#f2ece1',
          200: '#e5d9c3',
          300: '#d4b996',
          400: '#c5a77c',
          500: '#b89768',
          600: '#9a7b4f', // Luxury Desert Titanium Gold
          700: '#7d623c',
          800: '#524025',
          900: '#26231f',
          DEFAULT: '#9a7b4f',
        },
        brand: {
          50: '#faf8f5',
          100: '#f2ece1',
          200: '#e5d9c3',
          300: '#d4b996',
          400: '#c5a77c',
          500: '#b89768',
          600: '#9a7b4f', // Luxury Desert Titanium Gold
          700: '#7d623c',
          800: '#524025',
          900: '#26231f',
          DEFAULT: '#9a7b4f',
        },
        titanium: {
          dark: '#1c1b18',
          charcoal: '#272521',
          gold: '#d4b996',
          sand: '#f5f3ef',
        }
      },
      transitionDuration: {
        instant: '100ms',
        fast: '200ms',
      }
    },
  },
  plugins: [],
}
