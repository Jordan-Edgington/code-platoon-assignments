/* eslint-disable no-empty */
import { useState, useEffect } from "react"

// eslint-disable-next-line react/prop-types
function Game ({ loseLife, lives, winGame, wordAPI }) {
    const [currentGuess, setCurrentGuess] = useState("")
    const [allGuesses, setAllGuesses] = useState([])
    const [answerArray, setAnswerArray] = useState([])


    const renderLetters = (allGuesses) => {
        let tempanswerArr = []
        console.log(wordAPI)
        //iterate through the answer word
        // eslint-disable-next-line react/prop-types
        for (let i = 0; i <= wordAPI.length - 1; i++) {
            //if letter has been guessed, use that letter when printing the word
            if (allGuesses.includes(wordAPI[i])) {
                tempanswerArr.push(wordAPI[i])
                //if not, use an "_" instead
            } else {
                tempanswerArr.push("_")
            }
        }

        // if there are no underscores, then you have succesfully guessed all letters, and sets the winGame state to true
        if (tempanswerArr.includes("_")) {
        } else if (tempanswerArr.length===0) {
        } else {winGame()}
        setAnswerArray(tempanswerArr)
    }
    
    const submitGuess = (e) => {
        e.preventDefault()
        let guessesList = [...allGuesses]
        
        //if your guess hasn't already been guessed
        if (allGuesses.includes(currentGuess) === false) {
            //update the guessesList var 
            guessesList = [...allGuesses, currentGuess]
            //set the allGuesses state to the guessesList
            setAllGuesses(guessesList)
            //look to see if the currentGuess was a correct guess or not
            if (wordAPI.includes(currentGuess)) {
                //if so, do nothing
            } else {
                //if not, you lose a life
                loseLife()
            }
        }
        renderLetters(guessesList)
        e.target.reset()
    }

    useEffect(() => {
        renderLetters(allGuesses)
    },[wordAPI])

    return (
        <div className='text-xl md:text-2xl flex flex-col justify-center items-center'>
            {answerArray.length > 0 ? (<p>{answerArray.join(" ")}</p>):<p>Loading your word...</p>}
            <form onSubmit={submitGuess} className='flex flex-col md:flex-row justify-center items-center'>
                <input className='border-2 border-black mr-2' type="text" placeholder="Guess a Letter" maxLength="1" onChange={(e)=>{setCurrentGuess(e.target.value)}}/>
                <input className='border-2 border-black bg-slate-200' type="submit" placeholder="Submit Guess"/>
            </form>
            <p> Guessed letters: {allGuesses} </p>
            <p> Guesses remaining: {lives} </p>
        </div>
    )
}
export default Game


//use same array for setAllGuesses