import React, {useEffect, useState} from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [tweets, setTweets] = useState([])
  useEffect(() => {
    setTweets()
    
    return () => {
      cleanup
    }
  }, [])

  return (
    <div className="App">
      <header className="App-header">
      </header>
    </div>
  );
}

export default App;
