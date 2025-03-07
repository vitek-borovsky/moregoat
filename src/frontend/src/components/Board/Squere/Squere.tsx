interface SquereProps {
    color: number;
    onClick: (number) => void;
}

const Squere: React.FC<SquereProps> = ({ color, onClick }) => {

    const getColor = (value) => {
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

export default Squere
