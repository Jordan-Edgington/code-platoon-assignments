// import { useState } from 'react'
import { Outlet } from 'react-router-dom'
import {useState} from 'react'
import NavbarComp from './components/NavbarComp'
import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css';



function App() {
  const [favorites, setFavorites] = useState([])
  const checkIfFavorite = (char) => {
    const idArr = favorites.map(char => char.id)
    console.log(idArr)
    if (idArr.includes(char.id)) {
      return true
    }
    return false
  }

  const removeFromFavorites = (character) => {
    const newFavorites = favorites.filter((char) => {
      if (char.id === character.id) {
        return false} else {return true}
      })
      setFavorites(newFavorites)
    }

  const addToFavorites = (char) => {
    console.log(favorites)
    setFavorites([...favorites, char])
  }
  

  return (
    <>
    <NavbarComp />
      <Outlet context={{checkIfFavorite, removeFromFavorites, addToFavorites, favorites}}/>
    </>
  )
}

export default App
