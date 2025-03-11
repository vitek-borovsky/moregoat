interface SquareProps {
    color: number;
    onClick: () => void;
}

const Square: React.FC<SquareProps> = ({ color, onClick }) => {
    const getColor = (value: number) => {
        if  (value === -1) return "white";
        const colors = [ "blue", "green", "orange", "pink", "purple" ]
        return colors[value];
    }

    return (
        <div
        className="grid border border-gray-400 w-[100px] h-[100px] p-0 m-0 gap-0"
        onClick={onClick}
        style={{
            backgroundColor: getColor(color)
        }}>
        </div>
    );
}

export default Square
