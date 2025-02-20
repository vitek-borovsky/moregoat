import { React, useState } from "react";
import place_stone from './WebSocketService.tsx'

interface BoardProps {
    boardSize: number;
}

const Board: React.FC<BoardProps> = ({ boardSize }) => {
     const [cellColors, setCellColors] = useState<string[]>(
        Array(boardSize * boardSize).fill("white") // default color is white for each cell
      );

    const handleCellClick = (index: number) => {
        // TODO optimize this without copying the whole list
        const newCellColors = [...cellColors]; // copy the existing cell colors
        // Toggle the color between white and blue (you can choose any color logic)
        newCellColors[index] = newCellColors[index] === "white" ? "blue" : "white";
        setCellColors(newCellColors); // update state with the new colors

        // Calculate the row and column based on the index
        const row = Math.floor(index / boardSize);
        const col = index % boardSize;

        place_stone(col, row)

        // Log the row and column where the click happened
        console.log(`Clicked on cell at row: ${row}, column: ${col}`);
    };

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
