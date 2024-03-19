import { useState, useEffect } from 'react'
import Game from "./components/game.jsx"
import Display from "./components/display.jsx"
// import words from "./assets/words.json"
import axios from "axios"
import './App.css'


// let randomIndex = Math.floor(Math.random()*words.length) + 1;
// let word = words[randomIndex];
// console.log(`Real word is: ${word}`)



function App() {
  const [lives, setLives] = useState(6)
  const [win, setWin] = useState(false)
  const [answer, setAnswer] = useState([])
  
  

  useEffect(() => {
    const getWordAPI = async () => {
      const response = await axios.get("https://random-word-api.herokuapp.com/word")
      setAnswer(response.data[0])
      console.log(`Answer from API is ${response.data[0]}`)
    }
    getWordAPI()
  },[]);

  console.log(answer)
  const loseLife = () => {
    setLives(lives - 1)
  }

  const winGame = () => {
    setWin(true)
  }
  
  
    

  return (
    <div className='p-4 grid gap-4 md:grid-cols-2'>
      <div className='h-full flex justify-center md:justify-end items-center'>
        <div className='border-4 border-black rounded-xl pl-2 pr-3 bg-white bg-opacity-50 h-full flex flex-col justify-center items-center'>
        <h1 className="text-xl md:text-6xl">Hangman</h1>
        <Game wordAPI={answer} loseLife={loseLife} lives={lives} winGame={winGame}/>
        </div>
      </div>
      <div className='flex justify-center md:justify-start items-center'>
        <Display lives={lives} win={win}/>
      </div>
      
    </div>
    
  )
}

export default App
