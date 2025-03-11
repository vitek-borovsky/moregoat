import { useState, useEffect } from 'react';
import { useAppSelector } from "../../store";
import Board from './Board'

interface GameProps {
    boardSize: number
    playerCount: number
}

const Game: React.FC<GameProps> = ({ boardSize, playerCount }) => {
    const wss = useAppSelector((state) => state.global.webSocketService);

    return (
      <>
        <h3>{`Player_id: ${ wss.getPlayerId() }`}</h3>
        <h3>{`Player_count: ${ wss.getPlayerCount() }`}</h3>
        <h3>{`Game_id: ${ wss.getGameId() }`}</h3>
        <Board boardSize={boardSize} />


        <div
          key={0}
          onClick={() => handleClick(option)}
          style={{
            padding: "10px",
            border: "1px solid #000",
            cursor: "pointer",
            backgroundColor: "red",
          }}
        >
          { Array.from({ length: playerCount}).map((_, index) => (
            <p key={index}>player: {index} points: #TODO</p>
          ))}
        </div>

      </>
    );
}

export default Game;
