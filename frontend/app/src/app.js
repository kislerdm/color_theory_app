import React, { useState } from 'react';
import Input from './components/input';
import Output from './components/output';
import AppContainer from './components/app-container';

const app_name = 'Color Theory App';

const footer_obj = {
  web: 'https://www.dkisler.com',
  text: 'D. Kisler',
  prefix: new Date().getFullYear() + ' © '
};

function App() {
  const [color, setColor] = useState('#000000');

  return (
    <AppContainer app_name={app_name} footer_obj={footer_obj}>
      <Input color={color} onChange={setColor} />
      <Output color={color} />
    </AppContainer>
  );
}

export default App;
