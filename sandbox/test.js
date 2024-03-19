async function getWords() {
	const url = 'https://random-word-api.herokuapp.com/word';
  
  try {
	  const response = await fetch(url);
	  const result = await response.json();
	  word = result[0];
	  return word
  } catch (error) {
	  console.error(error);
  }
  }
  
let word = getWords()
console.log(word)