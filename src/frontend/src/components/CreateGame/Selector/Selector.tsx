interface SelectorProps {
  options: number[];
  defaultValue: number;
  rows: number
  setter: React.Dispatch<React.SetStateAction<number>>;
}

const Selector: React.FC<SelectorProps> = ({ options, defaultValue, rows, setter }) => {
  const handleClick = (option: number) => {
    setter(option);
  };
  const element_count = options.length;
  const column_count = Math.floor(element_count / rows);

  return (
    <div
    style={{
        display: "grid",
        gridTemplateColumns: `repeat(${column_count}, minmax(0, 1fr))`,
        gridTemplateRows: `repeat(${rows}, minmax(0, 1fr))`,
        justifyContent: "space-around"
    }}>
      {options.map((option, index) => (
        <div
          key={index}
          onClick={() => handleClick(option)}
          style={{
            padding: "10px",
            border: "1px solid #000",
            cursor: "pointer",
            backgroundColor: defaultValue === option ? "red" : "white",
          }}
        >
          {option}
        </div>
      ))}
    </div>
  );
};

export default Selector;
