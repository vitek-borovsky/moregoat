import { useEffect } from 'react';
import Squere from './Squere.tsx';

interface BoardProps {
    boardSize: number;
}

const Board: React.FC<BoardProps> = ({ boardSize }) => {
  return (
    <>
        <p>This is board { boardSize }</p>
        <div
            style = {{
                display: "grid",
                gridTemplateColumns: `repeat(${boardSize}, minmax(0, 1fr))`,
                gridTemplateRows: `repeat(${boardSize}, minmax(0, 1fr))`,
            }}
        >
            { Array.from({ length: boardSize * boardSize}).map((_, index) => (
                <Squere />
            ))}
        </div>
    </>
  );
}

export default Board;
