console.log("HELLO WHISKEY PLATOON!")
// Your function(s) should go here that will interact with the webpage or DOM
let goal = Math.floor(Math.random()*100);
guessesArr = [];

// need a guesser that saves the current guess and compares it to goal
// add current guess to guesses
// eventhandler to update ul in html with guesses


function createGuess() {
    let guess = Number(document.getElementById("guessInput").value);
    guessesArr.push(` ${guess}`)
    addResult(checkGuess(guess));
    document.getElementById("guessInput").value = "";
    console.log(guessesArr)
    pField = document.getElementById("guesses")
    pField.textContent = guessesArr.toString()

}


function addResult(result) {
    const resultField = document.getElementById("result");
    resultField.innerText = result
} 

function checkGuess(num) {
    if (num == goal) {
        return `Congratulations! ${num} is correct!`;
    } else if (num > goal) {
        return "Too high. Guess again.";
    } else {
        return "Too low. Guess Again.";
    }
}

function showAnswer() {
    if (document.getElementById("answer").style.display == "block") {
        document.getElementById("answer").style.display = "none";
    } else {
        document.getElementById("answer").style.display = "block";
    }
}
const redBtn = document.querySelector("#secret")
redBtn.addEventListener("click", () => {
    document.getElementById("answer").innerHTML = goal;
    showAnswer();
})
