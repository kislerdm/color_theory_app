import React, { useEffect, useState } from 'react';
import { hexCut } from '../common/utils';

export default function Type({ color }) {
  const [type, setType] = useState(null);

  useEffect(() => {
      const url = `${process.env.REACT_APP_URL_BACKEND_TYPE}?hexcode=${hexCut(color)}`;
      fetch(url)
        .then(response => response.json())
        .then(data => setType((data.data.is_warm===0) ? 'Cool':'Warm'));
  }, [color]);

  if (type) {
    return <div>
      <label htmlFor="output_type" id="output_label">Color Type:</label>
      <output name="color_type" id="output_type"> {type}</output>
    </div>
  } else {
    return null;
  }
};
