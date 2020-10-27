import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  /**
   * This is an example function in arrow notation and with typed JSDoc.
   * @param {number} a Summand 1.
   * @param {number} b Summand 2.
   */
  const exampleArrowFunctionWithJSDoc = (a, b) => {
    return a + b;
  };
  exampleArrowFunctionWithJSDoc();

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit
          <code>src/App.js</code>
          and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
