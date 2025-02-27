import React, { useState } from "react";

interface SelectorProps {
  options: number[];
  defaultValue: number;
}

const Selector: React.FC<SelectorProps> = ({ options, defaultValue }) => {
  const [selectedOption, setSelectedOption] = useState<number | null>(defaultValue);

  const handleClick = (option: string) => {
    setSelectedOption(option);
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
            backgroundColor: selectedOption === option ? "red" : "white",
          }}
        >
          {option}
        </div>
      ))}
    </div>
  );
};

export default Selector;
