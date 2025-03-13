import { useState, useEffect } from 'react';
import Square from './Square';
import { useAppSelector } from "../../../store";

const SQUARE_EMPTY = -1

interface BoardProps {
    boardSize: number;
}

const Board: React.FC<BoardProps> = ({ boardSize }) => {
    const [board, setBoard] = useState(Array(boardSize * boardSize).fill(SQUARE_EMPTY));

    const wss = useAppSelector((state) => state.global.webSocketService);

    useEffect(() => {
        const stonePlaced = (col: number, row: number, player_id: number) => {
            const index = boardSize * row + col;
            setBoard((prevBoard) => {
                const newBoard = [...prevBoard];
                newBoard[index] = player_id;
                return newBoard;
            });
        }

        const stoneCaptured = (stones: number[][]) => {
            setBoard((prevBoard) => {
                const newBoard = [...prevBoard];
                stones.forEach(([col, row]) => {
                    const index = boardSize * row + col;
                    newBoard[index] = SQUARE_EMPTY;
                });
                return newBoard;
            });
        }

        wss.subscribeStonePlacedCallback(stonePlaced);
        wss.subscribeStoneCapturedCallback(stoneCaptured);
    }, [wss, boardSize, board, setBoard]);

    const handleClick = (index: number) => {
        const col = index % boardSize;
        const row = Math.floor(index / boardSize);
        console.log(`clicked on (${col}, ${row})`);
        wss.placeStone(col, row);
    }

    return (
      <>
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
