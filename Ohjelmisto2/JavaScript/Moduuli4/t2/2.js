//Develop the app further.
// Add JavaScript that gets the value entered to the form and sends a request
// with fetch to https://api.tvmaze.com/search/shows?q=${value_from_input}.
// Print the search result to the console. (3p)
'use strict';
async function fetch_data() {
  let query = newQuery.value;
  try {
    const response = await fetch(
        `https://api.tvmaze.com/search/shows?q=${query}`);

    console.log('Result', response);
  } catch (error) {
    console.error('errori', error);
  }
}
const newQuery = document.querySelector('#query');
const newForm = document.querySelector('#form');
newForm.addEventListener('submit',fetch_data);




