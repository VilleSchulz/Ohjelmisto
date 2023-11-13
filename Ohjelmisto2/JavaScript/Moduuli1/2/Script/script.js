//Write a program that prompts for user's name and then greets the user.
// Print the result to the HTML document: Hello, Name! (2p)
'use strict';
console.log(fillName);
const name = prompt("Anna nimesi");
document.querySelector('#fillName').innerHTML = `Hello ${name}`;