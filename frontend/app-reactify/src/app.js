import React, { Fragment } from 'react';
import ColorPickerApp from './color-picker';

const app_name = 'Color Theory App';

const footer_obj = {
  web: 'https://www.dkisler.com',
  text: 'D. Kisler',
  prefix: new Date().getFullYear() + ' © '
};

const Header = ({ app_name }) => (
  <div class="header">
      {app_name}
  </div>
);

function Footer({ web, text, prefix }) {
  return <div class="footer">
      {prefix}
      <a href={web} target="_blank">
        {text}
      </a>
  </div>
}

const App = () => (
  <Fragment>
    <Header app_name={app_name} />
    <ColorPickerApp />
    <Footer {...footer_obj} />
  </Fragment>
);

export default App;
