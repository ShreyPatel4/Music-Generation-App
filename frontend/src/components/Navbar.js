
import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
  return (
    <nav className="navbar">
      <h2>MusicGenApp</h2>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/drums">Drum Generator</Link></li>
        <li><Link to="/melody">Melody Generator</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;
