import { useState } from 'react';
import Square from './Square';
import { useAppSelector } from "../../store";

interface BoardProps {
    boardSize: number;
    placeStone: (col: number, row: number) => void;
}


const Board: React.FC<BoardProps> = ({ boardSize, placeStone }) => {
    const [board, setBoard] = useState(Array(boardSize * boardSize).fill(-1));

    const handleClick = (index: number) => {
        const col = index % boardSize;
        const row = Math.floor(index / boardSize);
        console.log(`clicked on (${col}, ${row}), new value=${board[index] + 1}`);
        setBoard((prevBoard) => {
          const newBoard = [...prevBoard];
            newBoard[index] += 1;
            return newBoard;
        });

        placeStone(col, row);
    }

    const wss = useAppSelector((state) => state.global.webSocketService);

    return (
      <>
        <h3>{`Player_id: ${ wss.getPlayerId() }`}</h3>
        <h3>{`Player_count: ${ wss.getPlayerCount() }`}</h3>
        <h3>{`Game_id: ${ wss.getGameId() }`}</h3>
        <div
              style = {{
                  display: "grid",
                  gridTemplateColumns: `repeat(${boardSize}, minmax(0, 1fr))`,
                  gridTemplateRows: `repeat(${boardSize}, minmax(0, 1fr))`,
              }}
          >
              { Array.from({ length: boardSize * boardSize}).map((_, index) => (
                  <Square key={index} color = { board[index] } onClick={ () => handleClick(index) } />
              ))}
        </div>
      </>
    );
}

export default Board;
