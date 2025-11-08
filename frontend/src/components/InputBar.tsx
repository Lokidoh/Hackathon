import { ChangeEvent } from "react";
import React, { useState } from "react";

function InputBar() {
  // State to hold the current value of the input
  const [inputValue, setInputValue] = useState("");

  // Event handler for when the input value changes
  const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
    setInputValue(event.target.value);
  };

  return (
    <div>
      <input
        type="text"
        value={inputValue} // Bind the input's value to the state
        onChange={handleChange} // Update the state when the input changes
        placeholder="Type something..."
      />
      <p>Current value: {inputValue}</p>
    </div>
  );
}

export default InputBar;
