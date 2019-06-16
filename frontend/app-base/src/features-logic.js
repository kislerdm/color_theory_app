import React from 'react';
import { Hex, Rgb, Name } from './features';
import { HuePicker } from 'react-color';

const fe_features = [
  Hex,
  Rgb
];

function hexCut(color) {
  return (color.charAt(0)==="#") ? color.substring(1,7):color;
}

export default class ColorProperties extends React.Component {
  state = {
    background: '#000000',
    name: 'Black'
  };

  handleChangeComplete = (color) => {

    this.setState({ background: color.hex });

    const hex = hexCut(color.hex);

    const url_name = `${process.env.REACT_APP_URL_BACKEND_BASE}?hexcode=${hex}`;

    fetch(url_name)
      .then(response => response.json())
      .then(data => this.setState({ name: data.data.name }));

    };

  render() {
    return (
      <div className="container">

        <div className="color_sample" style={this.state}></div>
        <div className="color_input">
        <p align="center">Pick a color on slider</p>
          <HuePicker
            color={ this.state.background }
            onChangeComplete={ this.handleChangeComplete }
          />
        </div>
        <div className="color_output">
          {fe_features.map(
            Component => <Component color={this.state.background} />
          )}
          <Name name={this.state.name} />
        </div>
      </div>
    );
  }
};
