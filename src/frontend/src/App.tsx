import { useState, useEffect, useRef } from 'react';
import WebSocketService from './WebSocketService.tsx'
import Board from './components/Board/Board'
import CreateGame from './components/CreateGame/CreateGame'
import './App.css'
import { useAppSelector, useAppDispatch, setValue } from "./store";

function App() {
    const [gameStarted, setGameStarted] = useState(false);

    const [boardSize, setBoardSize] = useState<number | null>(null);
    const [playerCount, setPlayerCount] = useState<number | null>(null);

    const dispatch = useAppDispatch();

    const join_game = (player_id, board_size, player_count) => {
        setBoardSize(board_size);
        setPlayerCount(player_count);
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
