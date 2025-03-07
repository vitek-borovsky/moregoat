import { useState, useEffect } from 'react';
import Board from './components/Board/Board'
import CreateGame from './components/CreateGame/CreateGame'
import { useAppSelector } from "./store";
// @ts-ignore
import './App.css'

function App() {
    const [gameStarted, setGameStarted] = useState(false);

    // @ts-ignore NotImplemeted
    const [playerId, setPlayerId] = useState<number | null>(null);
    const [boardSize, setBoardSize] = useState<number | null>(null);

    const joinGame = (player_id: number, board_size: number) => {
        setPlayerId(player_id);
        setBoardSize(board_size);
        setGameStarted(true);
    }

    const wss = useAppSelector((state) => state.global.webSocketService);

    useEffect(() => {
        wss.subscribe_join_game_callback(joinGame);
    }, [])

    return (
      <>
        { gameStarted || <CreateGame /> }
        { gameStarted && <Board boardSize={ boardSize! } placeStone={ wss.placeStone } /> }
      </>
    );
}

export default App
