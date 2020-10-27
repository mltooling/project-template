module.exports = {
  root: true,
  globals: {
    define: false,
    window: true,
    console: true,
    document: true,
  },
  extends: [
    'airbnb',
    'airbnb/hooks',
    'plugin:prettier/recommended',
    'prettier/react',
  ],
  rules: {
    'no-case-declarations': 'warn',
  },
  parser: 'babel-eslint',
  parserOptions: {
    ecmaVersion: 2020,
  },
  env: {
    jest: true,
  },
};
