'use strict';
const targetElement = document.body
targetElement.style.display = 'flex';
targetElement.style.alignItems = 'center';
targetElement.style.justifyContent = 'center';
targetElement.style.flexDirection = 'column'
const container = document.createElement('div');
container.style.height= '10%';
targetElement.appendChild(container);
const button = document.createElement('button');
container.appendChild(button);
button.innerText= 'Get me a JOKE!';
button.style.scale='2';
