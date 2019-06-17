import React from 'react';

function Header({ app_name }) {
  return (
    <div className="header">
        {app_name}
    </div>
  );
}

function Footer({ web, text, prefix, test }) {
  return <div className="footer">
      {prefix}
      <a href={web} target="_blank" rel="noopener noreferrer">
        {text}
      </a>
  </div>
}

export default function AppContainer({ children, app_name, footer_obj }) {
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
