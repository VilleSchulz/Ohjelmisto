//Open t2 folder in your IDE/editor. Add HTML by using createElement()
// and appenChild mehtods. (2p)
// Add the following HTML code to the element with id="target"
//<li>First item</li>
// <li>Second item</li>
// <li>Third item</li>
'use strict'

const targetElement= document.getElementById('target')
const newLI1 = document.createElement('li');
const newLI2 = document.createElement('li');
const newLI3 = document.createElement('li');
targetElement.appendChild(newLI1);
newLI1.innerText = 'First item';
targetElement.appendChild(newLI2);
newLI2.classList.add('my-list');
newLI2.innerText = 'Second item';
targetElement.appendChild(newLI3);
newLI3.innerText = 'Third item';


