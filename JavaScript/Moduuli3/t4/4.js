//Add HTML by using createElement()
// and appenChild mehtods. (2p)
// Add the following HTML code to the element with id="target". Add the values
// from 'students' array to the <option> elements in a for-loop.

'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const targetElement = document.getElementById('target')
for( let i= 0; i<=2;i++){
  const newOpt = document.createElement('option');
  newOpt.innerText= students[i].name;
  newOpt.value = students[i].id;
  targetElement.appendChild(newOpt);

}