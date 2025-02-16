const input = document.querySelector('#searchbar input');
const form = document.querySelector('form')

const pokeFrontImage = document.querySelector('.poke-front-image')
const pokeName = document.querySelector('.poke-name')
const pokeId = document.querySelector('.poke-number')
const pokeHeight = document.querySelector('.poke-height')
const pokeWeight = document.querySelector('.poke-weight')
const pokeBio = document.querySelector('.poke-bio')


form.addEventListener("submit", e => {
    e.preventDefault();

    let inputVal = input.value;

    fetch(`https://pokeapi.co/api/v2/pokemon/${inputVal}`)
    .then(res=> res.json())
    .then((data)=> {
        console.log(data);

        pokeName.textContent = data['name'];
        pokeId.textContent = data['id'];
        pokeHeight.textContent = data['height'];
        pokeWeight.textContent = data['weight'];
        pokeBio.textContent = data['base_experience']
        pokeFrontImage.src = data['sprites']['front_default'] || '';
    });
})
