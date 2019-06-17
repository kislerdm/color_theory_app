import React from 'react';
import { HuePicker } from 'react-color';

export default function Input({ color, onChange }) {
  return (
    <>
      <div className="color_sample" style={{ background: color }}></div>
      <div className="color_input">
        <p align="center">Pick a color on slider</p>
        <HuePicker
          color={color}
          onChangeComplete={ e => onChange(e.hex) }
        />
      </div>
    </>
  );
}
