import React from 'react'

export default function Hex( {color} ) {
  return <div>
    <label htmlFor="code_hex" id="output_label">Color HEX Code:</label>
    <output name="code_hex" id="code_hex"> {color} </output>
  </div>
};
