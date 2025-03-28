import { useState } from 'react'
import Selector from './Selector'
import { useAppSelector } from "../../store";

// interface CreateGameProps { }

// const CreateGame: React.FC<CreateGameProps> = ({ }) => {
const CreateGame: React.FC<object> = () => {
    const [playerCount, setPlayerCount] = useState(2);
    const [boardSize, setBoardSize] = useState(5);
    const [gameId, setGameId] = useState("");

    const wss = useAppSelector((state) => state.global.webSocketService);



    return (
        <>
          <div>
            <div>
              <h2>Select Number of players</h2>
              <Selector
                  options = { [ 2, 3, 4, 5 ] }
                  defaultValue = { playerCount }
                  rows = { 1 }
                  setter = { setPlayerCount }
              />
            </div>
            <div>
              <h2>Select board size</h2>
              <Selector
                  options = { [ 5, 7, 9, 11, 13, 15, 17, 19 ] }
                  defaultValue = { boardSize }
                  rows = { 2 }
                  setter = { setBoardSize }
              />
              <button onClick = { () => wss.createGame(boardSize, playerCount) }>Start Game</button>
            </div>
          </div>

          <div>
            <input
              type="text"
              placeholder="Enter game code"
              value={gameId}
              onChange={(e) => setGameId(e.target.value)}
            />
            <button onClick={() => wss.joinGame(gameId)}>Join Game</button>
          </div>
      </>
    );
}

export default CreateGame
