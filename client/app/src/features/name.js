import React, { useEffect, useState } from 'react';
import { hexCut } from '../common/utils';

export default function Name({ color }) {
  const [name, setName] = useState(null);

  useEffect(() => {
      const url = `${process.env.REACT_APP_URL_BACKEND_NAME}?hexcode=${hexCut(color)}`;
      fetch(url)
        .then(response => response.json())
        .then(data => setName(data.data.name));
  }, [color]);

  if (name) {
    return <div>
      <label htmlFor="output_name" id="output_label">Color Name:</label>
      <output name="color_name" id="output_name"> {name}</output>
    </div>
  } else {
    return null;
  }
};
