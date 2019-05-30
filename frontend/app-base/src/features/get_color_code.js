import React from 'react'
import ReactDOM from 'react-dom'
import "./jscolor.js"

// get button
var fire = document.getElementById("input_apply");

function get_rgb(css_style) {
  return css_style.replace(/^(rgb|rgba)\(/,'').
                   replace(/\)$/,'').
                   replace(/\s/g,'').
                   split(',').
                   toString();
}

if (fire) {
  fire.addEventListener("click", function() {
    // get hex color
    var hex = document.getElementById("color_value");

    const color_hex = (
      <div>
        <label htmlFor="code_hex" id="output_label">Color HEX Code:</label>
        <output name="code_hex" id="code_hex"> {hex.value} </output>
      </div>
    );
    
    ReactDOM.render(color_hex, document.getElementById("color_hex"));
    // get rgb color
    var rgb = document.getElementById("color_picker").style["background-color"];
    rgb = get_rgb(rgb);
    const color_rgb = (
      <div>
        <label htmlFor="code_rgb" id="output_label">Color RGB Code:</label>
        <output name="code_rgb" id="code_rgb"> {rgb} </output>
      </div>
    );

    ReactDOM.render(color_rgb, document.getElementById("color_rgb"));

  }, false);
};
