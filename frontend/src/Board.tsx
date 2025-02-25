import { useEffect } from 'react';

interface BoardProps {
    boardSize: number;
}

const Board: React.FC<BoardProps> = ({ boardSize }) => {
  return (
    <>
        <p>This is board { boardSize }</p>
    </>
  );
}

export default Board

