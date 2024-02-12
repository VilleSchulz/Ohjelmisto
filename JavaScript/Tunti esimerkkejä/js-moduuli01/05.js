  'use strict';

  // Loogiset operaattori hieman erilaisia
  // and &&, or ||, not !

  const year = parseInt(prompt('Enter the year'));
  let result = document.querySelector('.result');
  console.log(result);

  if ((year % 4 == 0) && (year % 100 != 0) || (year % 400 == 0)) {
    result.innerHTML = `Year ${year} is a leapyear`;
  } else {
    result.innerHTML = `Year ${year} is NOT a leapyear`;
  }
