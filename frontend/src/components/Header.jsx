import React from 'react';
import { useNavigate } from 'react-router';

function Header() {
  const navigate = useNavigate();

  return (
    <>
      <h1>My Daily Sugar & BP Data</h1>
      <div className="header">
        <button type="button" onClick={() => navigate('/addbp')}>Add BP</button>
        <button type="submit" onClick={() => navigate('/addsugar')}>Add Sugar</button>
      </div>
    </>
  )
}

export default Header;