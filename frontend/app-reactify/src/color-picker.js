import React, { useState } from 'react';
import { Hex, Rgb, Name} from './features';

const components = [
  Hex,
  Rgb,
  Name
];

export default function ColorPickerApp() {
  const [color, setColor] = useState("#000");
  const [color2, setColor2] = useState(null);

  return <div className="container">
    <input value={color} onChange={(e) => setColor(e.target.value)} />
    <button onClick={() => setColor2(color)}>Search</button>
    {components.map(
      Component => <Component color={color2} />
    )}
  </div>
}
