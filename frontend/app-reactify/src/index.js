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

const go_button = (
  <button type="button" id="input_apply">Search</button>
);

const elements = [
  header,
  footer,
  input,
  go_button
];

ReactDOM.render(
  elements,
  document.getElementById('root')
);
