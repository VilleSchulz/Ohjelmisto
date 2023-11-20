//Open t1 folder in your IDE/editor. Add HTML by using innerHTML property (2p)
// Add the following HTML code to the element with id="target"
// <li>First item</li>
// <li>Second item</li>
// <li>Third item</li>
// Add class my-list to the element with id="target"

'use strict';
const targetElement = document.getElementById('target');
const newElement = document.createElement('div');
newElement.className = 'my-list';
targetElement.append(newElement);
let newLI1 = document.createElement('li');
newLI1.innerHTML = 'First item';
newElement.append(newLI1);
let newLI2 = document.createElement('li');
newLI2.innerHTML = 'Second item';
newElement.append(newLI2);
let newLI3 = document.createElement('li');
newLI3.innerHTML = 'Third item';
newElement.append(newLI3);









