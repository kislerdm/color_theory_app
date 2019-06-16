import React from 'react'

export function DemoSquare( {color} ) {
  return <div className="color_sample" style="background-color:{color};">
  </div>
};

export function Hex( {color} ) {
  return <div>
    <label htmlFor="code_hex" id="output_label">Color HEX Code:</label>
    <output name="code_hex" id="code_hex"> {color} </output>
  </div>
};

function hexToRGB( color ){
  const hex = (color.charAt(0)==="#") ? color.substring(1,7):color;
  const R = parseInt(hex.substring(0,2),16);
  const G = parseInt(hex.substring(2,4),16);
  const B = parseInt(hex.substring(4,6),16);

  return `${R},${G},${B}`

};

export function Rgb( {color} ) {
  const rgb = hexToRGB(color);

  return <div>
    <label htmlFor="code_rgb" id="output_label">Color RGB Code:</label>
    <output name="code_rgb" id="code_rgb"> {rgb} </output>
  </div>
};

export function Name( {name} ) {
  return <div>
    <label htmlFor="output_name" id="output_label">Color Name:</label>
    <output name="color_name" id="output_name"> {name} </output>
  </div>
};

export function Type( {type} ) {
  return <div>
    <label htmlFor="output" id="output_label">Color Type:</label>
    <output name="color_type" id="output"> {type} </output>
  </div>
};
