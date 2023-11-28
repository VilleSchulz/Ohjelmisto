//Develop the app further.
// Add JavaScript that gets the value entered to the form and sends a request
// with fetch to https://api.tvmaze.com/search/shows?q=${value_from_input}.
// Print the search result to the console. (3p)
'use strict';
async function funktio (evt) {
    evt.preventDefault();
    const code = newQuery.value;
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${code}`)
        console.log(response);
    } catch (error) {
        console.log(error.message);
    }
}
const newQuery = document.querySelector('#query');
const button = document.querySelector('input[type="submit"]');
button.addEventListener('click',funktio )
