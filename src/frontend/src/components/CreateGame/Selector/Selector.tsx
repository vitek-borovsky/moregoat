interface SelectorProps {
  options: number[];
  defaultValue: number;
  setter: React.Dispatch<React.SetStateAction<number>>;

}

const Selector: React.FC<SelectorProps> = ({ options, defaultValue, setter }) => {
  const handleClick = (option: number) => {
    setter(option);
  };

  return (
    <div style={{ display: "flex", justifyContent: "space-around" }}>
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
