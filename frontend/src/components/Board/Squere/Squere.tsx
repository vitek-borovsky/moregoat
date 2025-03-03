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
        className="grid border gorder-gray-500 w-[50px] h-[50px]"
        onClick={onClick}
        style={{
            backgroundColor: getColor(color)
        }}>
        </div>
    );
}

export default Squere
