
import React, { useState } from 'react';
import axios from 'axios';
import './PromptGenerator.css';

function PromptGenerator({ setPrompt }) {
  const [inputText, setInputText] = useState('');
  const [generatedPrompt, setGeneratedPrompt] = useState('');
  const [loading, setLoading] = useState(false);

  const generatePrompt = () => {
    setLoading(true);
    axios.post('/prompt/generate_prompt', { input_text: inputText })
      .then(response => {
        setGeneratedPrompt(response.data.prompt);
        setPrompt(response.data.prompt);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error generating prompt:', error);
        setLoading(false);
      });
  };

  return (
    <div className="prompt-generator">
      <h3>Prompt Generator</h3>
      <textarea
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Enter a seed text for the prompt..."
      />
      <button onClick={generatePrompt} disabled={loading}>
        {loading ? 'Generating...' : 'Generate Prompt'}
      </button>
      {generatedPrompt && (
        <div>
          <h4>Generated Prompt:</h4>
          <p>{generatedPrompt}</p>
        </div>
      )}
    </div>
  );
}

export default PromptGenerator;
