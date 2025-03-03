import { useState, useEffect, useRef } from 'react';
import WebSocketService from './WebSocketService.tsx'
import Board from './components/Board/Board'
import CreateGame from './components/CreateGame/CreateGame'
import './App.css'

function App() {
    const wss = useRef(null);
    const [isConnected, setIsConnected] = useState(false);
    const [gameStarted, setGameStarted] = useState(false);

    const [boardSize, setBoardSize] = useState<number | null>(null);
    const [playerCount, setPlayerCount] = useState<number | null>(null);

    const join_game = (game_id, player_id, board_size, player_count) => {
        setBoardSize(board_size);
        setPlayerCount(player_count);
        setGameStarted(true);
    }

    useEffect(() => {
        wss.current = new WebSocketService()
        setIsConnected(true);
        wss.current.subscribe_join_game_callback(join_game);
    }, [])


    return (
      <>
        <h1>Hello World</h1>
        { isConnected && <button onClick={ wss.current.sendEcho }>Send Echo</button> }
        { isConnected && (gameStarted || <CreateGame createGame = { wss.current.createGame }/>) }
        { isConnected && gameStarted && <Board boardSize={boardSize} placeStone={ wss.current.placeStone } /> }
      </>
    );
}

export default App
