import React, {useState, useEffect} from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from './component/Navbar'
import './reset.css'
import './App.css'

function App(){

  //Used useState to get the states
  const [prodprot, setProdProt] = useState([{}])
  const [prodcarb, setProdCarb] = useState([{}])
  const [prodgord, setProdGord] = useState([{}])

  //GET requests with fetch, including the URL of the endpoint we want to make our request
  useEffect(()=>{
    fetch("/produtosproteinas").then(
      res => res.json()
    ).then(
      prodprot=>{
        setProdProt(prodprot)
        console.log(prodprot)
      }
    );
    fetch("/produtoscarboidratos").then(
      res => res.json()
    ).then(
      prodcarb=>{
        setProdCarb(prodcarb)
        console.log(prodcarb)
      }
    );
    fetch("/produtosgorduras").then(
      res => res.json()
    ).then(
      prodgord=>{
        setProdGord(prodgord)
        console.log(prodgord)
      }
    );
  }, [])

  return ( 
   <div class="content">
      <BrowserRouter>
      <Navbar />
    <div class="description">Bem-vindo ao <i>Sapo Alimentício</i>, aqui você irá encontrar informações nutricionais dos principais alimentos do mercado.</div>
    <div class="results">  
      <Routes>
          <Route path='/' exact  />
          <Route path='/produtosproteinas' element={prodprot.produtos}/>
          <Route path='/produtoscarboidratos' element={prodcarb.produtos} />
          <Route path='/produtosgorduras' element={prodgord.produtos} />
      </Routes>
    </div>
    </BrowserRouter>
    </div>
  );
}
export default App;