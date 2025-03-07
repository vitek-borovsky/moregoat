import { useRef, useState } from 'react'
import Selector from './Selector'
interface CreateGameProps {
    createGame: (boardSize: number, playerCount: number) => void;
}

const CreateGame: React.FC<CreateGameProps> = ({ createGame }) => {
    const [playerCount, setPlayerCount] = useState(2);
    const [boardSize, setBoardSize] = useState(5);

    return (
        <>
          <Selector options = { [ 2, 3, 4, 5 ] } defaultValue = { playerCount } setter = { setPlayerCount }/>
          <Selector options = { [ 5, 7, 9, 11, 13, 15, 17, 19 ] } defaultValue = { boardSize } setter = { setBoardSize } />
          <button onClick = { () => createGame(boardSize, playerCount) }>Start Game</button>
        </>
    );
}

export default CreateGame
