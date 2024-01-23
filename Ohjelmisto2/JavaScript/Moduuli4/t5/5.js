'use strict';

async function joke(evt) {
  evt.preventDefault();
jokeTxt.innerText.replace('')
  try {
    const response = await fetch('https://api.chucknorris.io/jokes/random');

    const jsonData = await response.json();
    console.log('Joke', jsonData.value);

    jokeTxt.innerText = jsonData.value;
  } catch {
    (error);
    {
      console.log(error.message);
    }
  }
}

const targetElement = document.body;
const container = document.createElement('div');
container.classList.add('container');
targetElement.appendChild(container);
const button = document.createElement('button');
container.appendChild(button);
button.innerText = 'Get me a JOKE!';
button.style.scale = '2';
const txtContainer = document.createElement('div');
txtContainer.classList.add('txtcontainer');

targetElement.appendChild(txtContainer)
const jokeTxt = document.createElement('p');
txtContainer.appendChild(jokeTxt);


button.addEventListener('click', joke);