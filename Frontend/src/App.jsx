import { useState } from 'react'
import './App.css'

function App() {
  const [feeling, setFeeling] = useState('');

  const handleChange = (e) => {
    setFeeling(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
  };

  return (
    <>
    <form onSubmit={handleSubmit} >
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
        <button
          type="submit"        
        >
          Submit
        </button>
    </form>
    </>
  )
}

export default App
