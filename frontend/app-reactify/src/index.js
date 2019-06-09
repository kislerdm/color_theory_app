import React from 'react';
import ReactDOM from 'react-dom';
import { input } from './user_input.js';
import './index.css';
import * as serviceWorker from './serviceWorker';

serviceWorker.unregister();

const app_name = 'Color Theory App';

const footer_obj = {
  web: 'https://www.dkisler.com',
  text: 'D. Kisler',
  prefix: new Date().getFullYear() + ' © '
};

const header = (
  <div class="header">
      {app_name}
  </div>
);

const footer = (
  <div class="footer">
      {footer_obj.prefix}
      <a href={footer_obj.web} target="_blank">
        {footer_obj.text}
      </a>
  </div>
);

class Toggle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {isToggleOn: true};

    // This binding is necessary to make `this` work in the callback
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState(state => ({
      isToggleOn: !state.isToggleOn
    }));
  }

  render() {
    return (
      <button onClick={this.handleClick}>
        {this.state.isToggleOn ? 'ON' : 'OFF'}
      </button>
    );
  }
}

const elements = [
  header,
  footer
];

ReactDOM.render(
  elements,
  document.getElementById('root')
);

ReactDOM.render(
  input,
  document.getElementById('input')
);

ReactDOM.render(
  <Toggle/>,
  document.getElementById('input_apply')
);
