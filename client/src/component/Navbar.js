import React from 'react';
import "../reset.css"
import "./Navbar.css"
import { Link } from "react-router-dom";

const Navbar= () =>{
  return (
		<header class="header">
		<div class="left">
			<a href="http://localhost:3000/">Home</a>
		</div>
  <div class="mid">
		<ul class="navbar">
			 <li>
      <Link to="/"></Link>
    </li>
    <li>
      <Link to="/produtosproteinas">Proteínas</Link>
    </li>
    <li>
      <Link to="/produtoscarboidratos">Carboidratos</Link>
    </li>
    <li>
      <Link to="/produtosgorduras">Gorduras</Link>
    </li>
		</ul>
   
  </div>
    </header>
  );
}
export default Navbar;