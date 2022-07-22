import React from 'react';
import { Link } from 'react-router-dom';
import './navbar.css'
function NavBar() {
  return (
    <nav className="navbar">
      <div className="navbar_logo">
        <i className="fa-regular fa-copy"></i>
        <Link className="link" to='/'> Python similarity measure</Link>
      </div>
      <ul className="navbar_menu">
        <li><Link className="link" to="/similar">유사도</Link></li>
        <li><Link className="link" to="/elegant">우아함</Link></li>
        <li><Link className="link" to="/question">문의</Link></li>
      </ul>
    </nav>
  )
}

export default NavBar
