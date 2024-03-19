
const randomPokemonGen = (numOfPokemon) => {
    let randomID = Math.floor(Math.random()*numOfPokemon);
    return randomID;
}



const getPokemon = async () => {
    let response = await fetch(`https://pokeapi.co/api/v2/pokemon/${randomPokemonGen(1025)}`);
    let responseData = await response.json();
    let pokemonTypeLink = responseData.types[0].type.url;
    //creates the p tag containing the type of pokemon team
    let typeText = document.createElement("p");
    typeText.innerHTML = `Pokemon Type: ${responseData.types[0].type.name.toUpperCase()}`;
    typeText.id = "type"
    document.body.insertBefore(typeText, document.getElementById("imgs"));
    //creates the image from our original random pokemon
    newImg = document.createElement("img");
    newImg.src = responseData.sprites.front_default;
    document.getElementById("imgs").appendChild(newImg);

    let typeResponse = await fetch(pokemonTypeLink);
    let typeResponseData = await typeResponse.json();
    let numOfType = typeResponseData.pokemon.length;
    for (let i = 1; i <= 5; i++) {
        pokemonID = randomPokemonGen(numOfType);
        const newPokemonLink = typeResponseData.pokemon[pokemonID].pokemon.url;
        let newPokemon = await fetch(newPokemonLink);
        let newPokemonData = await newPokemon.json();
        newImg = document.createElement('img');
        newImg.src = newPokemonData.sprites.front_default;
        document.getElementById('imgs').appendChild(newImg);
    }
}

const reset = () => {
    imgs = document.getElementById("imgs");
    imgs.parentNode.removeChild(imgs);
    p = document.getElementById("type");
    p.parentNode.removeChild(p);
    newDiv = document.createElement("div");
    newDiv.id = "imgs";
    resetButton = document.getElementById("reset");
    document.body.insertBefore(newDiv, resetButton);

}
