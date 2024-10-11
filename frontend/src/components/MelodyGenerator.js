
import React, { useState } from 'react';
import axios from 'axios';
import ReactAudioPlayer from 'react-audio-player';
import PromptGenerator from './PromptGenerator';
import './MelodyGenerator.css';

function MelodyGenerator() {
  const [settings, setSettings] = useState({
    tempo: 120,
    temperature: 1.0,
    total_bars: 4,
    prompt: '',
  });
  const [audioSrc, setAudioSrc] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setSettings({ ...settings, [e.target.name]: e.target.value });
  };

  const setPrompt = (prompt) => {
    setSettings({ ...settings, prompt });
  };

  const generateMelody = () => {
    setLoading(true);
    axios.post('/music/generate_melody', settings)
      .then(response => {
        setAudioSrc(response.data.audio_file);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error generating melody:', error);
        setLoading(false);
      });
  };

  return (
    <div className="generator">
      <h2>Melody Generator</h2>
      <PromptGenerator setPrompt={setPrompt} />
      <div className="controls">
        <label>
          Tempo (BPM):
          <input type="number" name="tempo" value={settings.tempo} onChange={handleChange} min="60" max="200" />
        </label>
        <label>
          Temperature:
          <input type="number" name="temperature" value={settings.temperature} onChange={handleChange} min="0.1" max="2.0" step="0.1" />
        </label>
        <label>
          Total Bars:
          <input type="number" name="total_bars" value={settings.total_bars} onChange={handleChange} min="1" max="16" />
        </label>
        <button onClick={generateMelody} disabled={loading}>
          {loading ? 'Generating...' : 'Generate Melody'}
        </button>
      </div>
      {audioSrc && (
        <div className="audio-player">
          <ReactAudioPlayer src={audioSrc} controls />
        </div>
      )}
    </div>
  );
}

export default MelodyGenerator;
