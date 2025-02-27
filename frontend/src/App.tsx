import { useState, useEffect, useRef } from 'react';
import WebSocketService from './WebSocketService.tsx'
import Board from './components/Board/Board'
import CreateGame from './components/CreateGame/CreateGame'
import './App.css'

function App() {
    const wss = useRef(null);
    const [gameStarted, setGameStarted] = useState(false);
    useEffect(() => {
        wss.current = new WebSocketService()
    }, [])

    return (
      <>
        <div>
          <h1>Hello World</h1>
          <button onClick={wss.sendEcho}>Send Echo</button>
        </div>

        { gameStarted || <CreateGame /> }
        { gameStarted && <Board boardSize={5} /> }
        <button onClick={() => setGameStarted(true)}>Start Game</button>
      </>
    );
}

export default App
