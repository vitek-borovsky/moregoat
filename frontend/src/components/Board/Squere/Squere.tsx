interface SquereProps {
    color: string;
    onClick: (number) => void;
}

const Squere: React.FC<SquereProps> = ({ color, onClick }) => {
    return (
        <div
        className="grid border gorder-gray-500 w-[50px] h-[50px]"
        onClick={onClick}
        style={{
            backgroundColor: "yellow"
        }}>
        </div>
    );
}

export default Squere
