import { useState } from 'react';
import './App.css';

function App() {
  const [feeling, setFeeling] = useState('');
  const [recommendation, setRecommendation] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFeeling(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setRecommendation('');

    try {
      const response = await fetch('http://localhost:5000/recommend_movie', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ feeling }),
      });

      const data = await response.json();

      if (response.ok) {
        setRecommendation(data.recommendation);
      } else {
        setRecommendation('Error: ' + data.error);
      }
    } catch (error) {
      setRecommendation('Request failed: ' + error.message);
    }

    setLoading(false);
  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        <label>
          How are you feeling today?
        </label>
        <input
          id="feeling"
          type="text"
          value={feeling}
          onChange={handleChange}
          placeholder="Type your feeling..."
        />
        <button type="submit">
          Submit
        </button>
      </form>

      {loading && <p>Loading...</p>}
      {recommendation && <p>{recommendation}</p>}
    </>
  );
}

export default App;
