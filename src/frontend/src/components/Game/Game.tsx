import { useState, useEffect } from 'react';
import { useAppSelector } from "../../store";
import Board from './Board'

interface GameProps {
    boardSize: number
    playerCount: number
}

const Game: React.FC<GameProps> = ({ boardSize, playerCount }) => {
    const [points, setPoints] = useState<number[]>([ 0, 0 ]);
    const [playerOnTurn, setPlayerOnTurn] = useState<number>(0);

    const wss = useAppSelector((state) => state.global.webSocketService);


    useEffect(() => {
            const updatePoints = (points: number[]) =>
                setPoints(points);

            const playerPass = (playerId: number) =>
                setPlayerOnTurn((playerId + 1) % playerCount)

        wss.subscribeUpdatePointsCallback(updatePoints);
        wss.subscribePlayerPassCallback(playerPass);
    }, [wss, points, playerCount]);

    return (
      <>
        <h3>{`Player on turn ${ playerOnTurn }`}</h3>
        <h3>{`Player_id: ${ wss.getPlayerId() }`}</h3>
        <h3>{`Player_count: ${ wss.getPlayerCount() }`}</h3>
        <h3>{`Game_id: ${ wss.getGameId() }`}</h3>
        <Board boardSize={boardSize} />

        <div
          style = {{
              display: "grid",
              gridTemplateColumns: `repeat(${playerCount}, minmax(0, 1fr))`,
              gridTemplateRows: `repeat(1), minmax(0, 1fr))`,
              background: "red",
          }}
          >
          { Array.from({ length: playerCount}).map((_, index) => (
            <p key={index}>player: {index} points: {points[index]}</p>
          ))}
        </div>
        <button onClick={ () => wss.playerPass() }>Player pass</button>
      </>
    );
}

export default Game;
