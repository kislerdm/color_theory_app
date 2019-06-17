import React, { useEffect, useState } from 'react';
import { hexCut } from '../common/utils';

export default function Name({ color }) {
  const [name, setName] = useState('Black');

  useEffect(() => {
      const url = `${process.env.REACT_APP_URL_BACKEND_BASE}?hexcode=${hexCut(color)}`;
      fetch(url)
        .then(response => response.json())
        .then(data => setName(data.data.name));
  }, [color]);

  return <div>
    <label htmlFor="output_name" id="output_label">Color Name:</label>
    <output name="color_name" id="output_name"> {name}</output>
  </div>
};
