import Main from './components/main';
import React from "react";
import './App.css';
import {BrowserRouter as Router} from "react-router-dom"

function App() {
  return (
    <div className="App">
      <Router>
        <main>
          <Main/>
        </main>
      </Router>
    </div>
  );
}

export default App;