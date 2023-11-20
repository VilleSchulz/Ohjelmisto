'use strict';

// haettu html elementti
const fillName= document.querySelector('#fillName');
console.log(fillName);

// pyydetään nimi
const name = prompt('Please give your name: ');
console.log(name);

// printataan h2 elementtiin
fillName.innerHTML = `Hello ${name}!`;

// document.querySelector('#fillName').innerHTML = `Hello ${name}!`;

// Write a program that prompts for user's name and
// then greets the user. Print the result to the HTML document
// Hello, Name!