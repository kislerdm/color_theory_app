import React, { Fragment } from 'react';
import ColorProperties from './features-logic';

const app_name = 'Color Theory App';

const footer_obj = {
  web: 'https://www.dkisler.com',
  text: 'D. Kisler',
  prefix: new Date().getFullYear() + ' © '
};

const Header = ({ app_name }) => (
  <div className="header">
      {app_name}
  </div>
);

function Footer({ web, text, prefix, test }) {
  return <div className="footer">
      {prefix}
      <a href={web} target="_blank" rel="noopener noreferrer">
        {text}
      </a>
  </div>
}

const App = () => (
  <Fragment>
    <Header app_name={app_name} />
    <ColorProperties />
    <Footer {...footer_obj} />
  </Fragment>
);

export default App;
