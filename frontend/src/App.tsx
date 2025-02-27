import { useState, useEffect, useRef } from 'react';
import WebSocketService from './WebSocketService.tsx'
import Board from './components/Board/Board'
import CreateGame from './components/CreateGame/CreateGame'
import './App.css'

function App() {
    const wss = useRef(null);
    const [isConnected, setIsConnected] = useState(false);
    const [gameStarted, setGameStarted] = useState(false);
    useEffect(() => {
        wss.current = new WebSocketService()
        setIsConnected(true);
    }, [])

    return (
      <>
        <h1>Hello World</h1>
        { isConnected && <button onClick={ wss.current.sendEcho }>Send Echo</button> }
        { isConnected && (gameStarted || <CreateGame createGame = { wss.current.createGame }/>) }
        { isConnected && gameStarted && <Board boardSize={5} /> }

      </>
    );
}

export default App
