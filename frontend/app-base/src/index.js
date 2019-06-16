import React, { Fragment } from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import * as serviceWorker from './serviceWorker';
import App from './app';

require('dotenv').config();

serviceWorker.unregister();

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
