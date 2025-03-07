import { useState, useEffect, useRef } from 'react';
import WebSocketService from './WebSocketService.tsx'
import Board from './components/Board/Board'
import CreateGame from './components/CreateGame/CreateGame'
import './App.css'
import { useAppSelector } from "./store";

function App() {
    const [gameStarted, setGameStarted] = useState(false);

    const [boardSize, setBoardSize] = useState<number | null>(null);

    const join_game = (player_id, board_size) => {
        setBoardSize(board_size);
        setGameStarted(true);
    }

    const wss = useAppSelector((state) => state.global.webSocketService);

    useEffect(() => {
        wss.subscribe_join_game_callback(join_game);
    }, [])

    return (
      <>
        { gameStarted || <CreateGame createGame = { wss.createGame }/> }
        { gameStarted && <Board boardSize={boardSize} placeStone={ wss.placeStone } /> }
      </>
    );
}

export default App
