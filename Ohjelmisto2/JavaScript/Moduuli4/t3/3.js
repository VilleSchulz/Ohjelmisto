//Develop the app even further. Print the following information for all
// series from the search result on the web page. (7p)
// required information: Name, link to details (url), medium image and summary
// show the name in <h2> element
// show the url in <a> element. Also add target="_blank" to the link.
// show the medium image with <img src="" alt="">. Add medium image to src
// attribute and name property to alt attribute.
// some TV-shows don't have images. This will cause an error. You can fix
// this by adding ? operator to image property. Example: tvShow.show.image?
// .medium;. This is called optional chaining.
// show summary in <div> element (not <p>). This is because the summary is
// already in <p> element, and the result will not be valid if <p> is inside
// another <p>.
// collect the elements to <article> elements and append <article> elements
// to the HTML document.
// make <div id="results"> element to the HTML document where you append
// the <article> elements.
// clear the old results with innerHTML = ''
// before you append the new results.


'use strict';


async function funktio (evt) {
evt.preventDefault();

const code = newQuery.value;
try {

    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${code}`);
    const  jsonData = await response.json();
    console.log( jsonData);
    const targetElem = document.body;
    const html_Result = document.createElement('div');
    html_Result.id = 'results';
    targetElem.appendChild(html_Result);
    const resultsContainer = document.getElementById('results');

        // Clear old results
        resultsContainer.innerHTML = '';

    for (let showData of  jsonData) {
        const newArticle = document.createElement('article');
        html_Result.appendChild(newArticle);
        const newLink = document.createElement('a');
        newLink.target = '_blank';
        newLink.href = showData.show.url;
        newLink.style.color = 'inherit';
        newArticle.appendChild(newLink);
        const newH2 = document.createElement('h2');
        newLink.appendChild(newH2)
        newH2.innerText = showData.show.name;
        const newImg = document.createElement('img');
        newArticle.appendChild(newImg);
        newImg.alt = showData.show.name;
        newImg.src = showData.show.image.medium;

        const newSummary = document.createElement('div');
        newSummary.id = 'summary'
        newArticle.appendChild(newSummary);
        newSummary.innerHTML = showData.show.summary;

    }

} catch (error) {
    console.log(error.message);
}

}


const newQuery = document.querySelector('#query');
const button = document.querySelector('input[type="submit"]');
button.addEventListener('click',funktio )


