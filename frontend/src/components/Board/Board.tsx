import { useEffect } from 'react';
import Squere from './Squere';

interface BoardProps {
    boardSize: number;
}

const Board: React.FC<BoardProps> = ({ boardSize }) => {
    const handleClick = (index) => {
        const col = index % boardSize;
        const row = Math.floor(index / boardSize);
        console.log(`clicked on (${col}, ${row})`);
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
              <Squere key={index} color = { "yellow" } onClick={ () => handleClick(index) } />
          ))}
      </div>
    );
}

export default Board;
