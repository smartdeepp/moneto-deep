/** @type {import('tailwindcss').Config} */
const primary = {
  100: '#D3BFF8',
  DEFAULT: '#6C33D9',
};
const success = {
  DEFAULT: '#4BF1C5',
};
const warning = {
  DEFAULT: '#EB3B4D',
};
const light = {
  100: '#D9D9D9',
  200: '#E4E4E4',
  300: '#F2F2F2',
  400: '#F5F5F5',
  450: '#FBFBFB',
  DEFAULT: '#FFFFFF',
};
const dark = {
  300: '#181818',
  400: '#0E0E0E',
  DEFAULT: '#000000',
  450: '#030303',
};
const grey = {
  100: '#BEBEBE',
  150: '#949494',
  200: '#ABABAB',
  250: '#B2B2B2',
  300: '#A8A5AD',
  350: '#A8A8A8',
  400: '#747474',
  420: '#868686',
  450: '#5D5D5D',
  DEFAULT: '#181818',
  600: '#666666',
  700: '#585858',
  750: '#3E3E3E',
  800: '#414141',
  850: '#525252',
};
const nyon = {
  DEFAULT: '#A6FF88',
};
module.exports = {
  content: [
    './templates/**/*.html',
    './static/**/*.js',
    './apps/**/templates/**/*.html',
    './**/templates/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        nyon,
        grey,
        dark,
        light,
        warning,
        success,
        primary,
      },
    },
  },
  plugins: [],
};
