'use strict';

const vastaus = confirm('Should i calculate square root');
let result = document.querySelector('.result');

if (vastaus) {
  const number = parseInt(prompt('Give number'));
  if (number >= 0) {
    let squareRoot = Math.sqrt(number);
    result.innerHTML = `The square root of ${number} is ${squareRoot}`;
  } else {
    result.innerHTML = ` The number you entered is negative number.`;
  }
} else {
  result.innerHTML = 'The square root is not calculated';

}



