import React from "react";

interface BoardProps {
    boardSize: number;
}

const Board: React.FC<BoardProps> = ({ boardSize }) => {
    const handleCellClick = (index: number) => {
        // Calculate the row and column based on the index
        const row = Math.floor(index / boardSize);
        const col = index % boardSize;

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
                className="w-12 h-12 border border-gray-500"
                onClick={() => handleCellClick(index)}
            />
        ))}
        </div>
    );

};

export default Board;
