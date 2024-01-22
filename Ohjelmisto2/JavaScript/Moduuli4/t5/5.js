'use strict';

 async function joke (evt){
   evt.preventDefault();
   try{
     await fetch()}
catch (error){
     console.log(error.message)
}
 }

 const targetElement = document.body
const container = document.createElement('div');
targetElement.appendChild(container);
const button = document.createElement('button');
container.appendChild(button);
button.innerText= 'Get me a JOKE!';
button.style.scale='2'

button.addEventListener('click', joke);