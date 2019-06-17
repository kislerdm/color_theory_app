import React, { useState } from 'react';
import { Input, Outputs } from './features-logic';

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


function AppContainer({ children }) {
  return (
    <>
      <Header app_name={app_name} />
      <div className="container">
        {children}
      </div>
      <Footer {...footer_obj} />
    </>
  );
}


function App() {
  const [color, setColor] = useState('#000000');

  return (
    <AppContainer>
      <Input color={color} onChange={setColor} />
      <Outputs color={color} />
    </AppContainer>
  );
}

export default App;
