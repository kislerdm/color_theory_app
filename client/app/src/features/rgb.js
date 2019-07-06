import React from 'react'

function hexToRGB( color ){
  const hex = (color.charAt(0)==="#") ? color.substring(1,7):color;
  const R = parseInt(hex.substring(0,2),16);
  const G = parseInt(hex.substring(2,4),16);
  const B = parseInt(hex.substring(4,6),16);

  return `${R},${G},${B}`

};

export default function Rgb( {color} ) {
  const rgb = hexToRGB(color);

  return <div>
    <label htmlFor="code_rgb" id="output_label">Color RGB Code:</label>
    <output name="code_rgb" id="code_rgb"> {rgb} </output>
  </div>
};
