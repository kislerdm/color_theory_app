import React from 'react';
import Hex from '../features/hex';
import Rgb from '../features/rgb';
import Name from '../features/name';

const fe_features = [
  Hex,
  Rgb,
  Name
];

export default function Output({ color }) {
  return  (
    <div className="color_output">
      {fe_features.map(
        (Component, index) => <Component key={index} color={color} />
      )}
    </div>
  );
}
