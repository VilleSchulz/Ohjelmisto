//Open t1 folder in your IDE/editor. Add HTML by using innerHTML property (2p)
// Add the following HTML code to the element with id="target"
// <li>First item</li>
// <li>Second item</li>
// <li>Third item</li>
// Add class my-list to the element with id="target"


'use strict';

let items = '<li>First item</li><li>Second item</li><li>Third item</li>'

document.getElementById('target').innerHTML = items;
const element = document.getElementById('target');
element.classList.add('my-list');








