import { React, useState, useEffect } from "react";
import WebSocketService from './WebSocketService.tsx'

interface BoardProps {
    boardSize: number;
}

const EMPTY_COLOR = "white";
// players are 1-indexed so black color is for error detection
const PLAYER_COLORS = [ "black", "blue", "green", "yellow", "red" ];

const wss = new WebSocketService();

const Board: React.FC<BoardProps> = ({ boardSize }) => {
     const [cellColors, setCellColors] = useState<string[]>(
        Array(boardSize * boardSize).fill("white") // default color is white for each cell
      );

    useEffect(() => {
        wss.subscribe(stone_placed);
    }, []); // Empty dependency array ensures it runs only once

    const handleCellClick = (index: number) => {
        const row = Math.floor(index / boardSize);
        const col = index % boardSize;

        wss.place_stone(col, row)

        // Log the row and column where the click happened
        // console.log(`Clicked on cell at row: ${row}, column: ${col}`);
    };

    const stone_placed = (player, col, row)  => {
        const index = row * boardSize + col;

        setCellColors((prevColors) => {
            const newCellColors = [...prevColors]; // Copy the current state
            newCellColors[index] = PLAYER_COLORS[player];
            return newCellColors; // Return the updated state
        });

        console.log(`STONE PLACED ${player}@${col}x${row}`);
    }

    const stone_captured = (col, row)  => {
        const index = row * boardSize + col;

        setCellColors((prevColors) => {
            const newCellColors = [...prevColors]; // Copy the current state
            newCellColors[index] = EMPTY_COLOR;
            return newCellColors; // Return the updated state
        });

        console.log(`STONE CAPTURED ${col}x${row}`);
    }

    wss.subscribe(stone_placed);

    return (
        <div
        className="grid border border-gray-500"
        style={{
            gridTemplateColumns: `repeat(${boardSize}, 50px)`,
            gridTemplateRows: `repeat(${boardSize}, 50px)`,
        }}
        >
        {Array.from({ length: boardSize * boardSize }).map((_, index) => (
            <div
                key={index}
                style={{ backgroundColor: cellColors[index] }}
                className="w-12 h-12 border border-gray-500"
                onClick={() => handleCellClick(index)}
            />
        ))}
        </div>
    );

};

export default Board;
