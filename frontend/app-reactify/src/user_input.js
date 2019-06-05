import React from 'react';
import './features/jscolor.js';

const default_color = '000';
const picker_text = "Pick a color";

// color picker
export const input = (
  <div class="input">
    <input name="color" type="hidden" id="color_value" value={default_color}/>
    <button class="jscolor {valueElement: 'color_value', closable:true, closeText:'Close'}" id="color_picker">{picker_text}</button>
  </div>
);
