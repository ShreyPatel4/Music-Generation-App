
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import DrumGenerator from './components/DrumGenerator';
import MelodyGenerator from './components/MelodyGenerator';
import './App.css';

function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path="/drums" component={DrumGenerator} />
        <Route path="/melody" component={MelodyGenerator} />
        <Route path="/" exact component={Home} />
      </Switch>
    </Router>
  );
}

const Home = () => (
  <div className="home">
    <h1>Welcome to the Music Generation App</h1>
    <p>Select an option from the menu to get started.</p>
  </div>
);

export default App;
