import { useRef, useState } from 'react'
import Selector from './Selector'
interface CreateGameProps {
}

const CreateGame: React.FC<BoardProps> = ({ }) => {
    const [playerCount, setPlayerCount] = useState(2);
    const [boardSize, setBoardSize] = useState(5);

    const handleClick = () => {
        console.log(`${playerCount} ${boardSize}`);
    }

    return (
        <>
          <h3>This is CreateGame component</h3>
          <Selector options = { [ 2, 3, 4, 5 ] } defaultValue = { playerCount } setter = { setPlayerCount }/>
          <Selector options = { [ 5, 7, 9, 11, 13, 15, 17, 19 ] } defaultValue = { boardSize } setter = { setBoardSize } />
          <button onClick = { () => handleClick() }>Confirm</button>
        </>
    );
}

export default CreateGame
