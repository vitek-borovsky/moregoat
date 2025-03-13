import { useState, useEffect } from 'react';
import Game from './components/Game/Game'
import CreateGame from './components/CreateGame/CreateGame'
import { useAppSelector } from "./store";
import './App.css'

function App() {
    const [gameStarted, setGameStarted] = useState(false);

    const [boardSize, setBoardSize] = useState<number | null>(null);

    const joinGame = (board_size: number) => {
        setBoardSize(board_size);
        setGameStarted(true);
    }

    const wss = useAppSelector((state) => state.global.webSocketService);
    useEffect(() => {
        wss.subscribeJoinGameCallback(joinGame);
    }, [wss])

    return (
      <>
        { gameStarted || <CreateGame /> }
        { gameStarted && <Game boardSize={ boardSize!} playerCount={2} /> }
      </>
    );
}

export default App
