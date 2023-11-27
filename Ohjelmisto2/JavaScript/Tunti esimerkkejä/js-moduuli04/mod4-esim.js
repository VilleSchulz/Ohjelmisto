/**
 * Mod 4 + geolocation esimerkkejä
 */
let coordinates;
// navigator.geolocation - selaimen tarjoama paikannusrajapinta
// takaisinkutsu (callback) -funktiot
function positionSuccess(position) {
  console.log('paikannus onnistui!', position)
  coordinates = position.coords;
  console.log('sijaintikoordinaatit', coordinates.latitude, coordinates.longitude);
  // Tee tässä koordinaateille, mitä tarttee
}
function positionError(error) {
  console.log('paikannus epäonnistui', error.message);
  // Kerro käyttäjälle tässä, että homma meni pieleen
}
// Starts the location search
navigator.geolocation.getCurrentPosition(
  positionSuccess,
  positionError,
  {enableHighAccuracy: true}
);
// Huom asynkronisuus, koordinaatit eivät ole käytössä ennen kuin paikannettu
console.log('tulostuu geolocation-kutsun jälkeen', coordinates);

// Avoimet rajapinnat - Fetch ja AJAX

// oldschool tapa promisen käsittellyyn:
fetch('https://api.chucknorris.io/jokes/random').then(
  function (response) {
    console.log('oldschool fetch response', response);
    response.json().then(
      function(json) {
        console.log('oldschool vitsi', json.value);
      }
    ).catch(
      function (error) {
        console.error('fetch error', error);
      }
    );
  }).catch(
    function(error) {
      console.log('fetch error', error);
    });

// moderni tapa, async - await
async function fetchJoke() {
  let jokeContent;
  try {
    const response = await fetch('https://api.chucknorris.io/jokes/random');
    const joke = await response.json();
    console.log('moderni async vitsi', joke);
    jokeContent = joke.value;
  } catch (error) {
    console.log('fetch error', error);
    jokeContent = 'Ei vitsiä saatavilla';
  }
  document.querySelector('#toka').textContent = jokeContent;
}
fetchJoke();

console.log('viimeinen tuloste')
