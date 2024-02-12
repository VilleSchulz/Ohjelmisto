'use strict'

const targetElement = document.body;

function clickhandler(event){
  console.log(event)
  alert('Button Clicked');
}

targetElement.addEventListener('click', clickhandler);
