import { useState, useEffect } from 'react';
import Squere from './Squere';

interface BoardProps {
    boardSize: number;
}


const Board: React.FC<BoardProps> = ({ boardSize }) => {
    const [board, setBoard] = useState(Array(boardSize * boardSize).fill(-1));

    const handleClick = (index) => {
        const col = index % boardSize;
        const row = Math.floor(index / boardSize);
        setBoard((prevBoard) => {
          const newBoard = [...prevBoard];
            newBoard[index] += 1;
            return newBoard;
        });
        console.log(`clicked on (${col}, ${row}), new value=${board[index]}`);
    }



    return (
      <div
          style = {{
              display: "grid",
              gridTemplateColumns: `repeat(${boardSize}, minmax(0, 1fr))`,
              gridTemplateRows: `repeat(${boardSize}, minmax(0, 1fr))`,
          }}
      >
          { Array.from({ length: boardSize * boardSize}).map((_, index) => (
              <Squere key={index} color = { board[index] } onClick={ () => handleClick(index) } />
          ))}
      </div>
    );
}

export default Board;
