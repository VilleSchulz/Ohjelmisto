'use strict';

const start_year = parseInt(prompt('Give start year'));
const end_year = parseInt(prompt('Give end year'));

const targetElem = document.body; // You need to specify the targetElem, assuming it's the body element for now
const ulElement = document.createElement('ul');
targetElem.append(ulElement);

if (start_year < end_year) {
  for (let i = 0; start_year + i <= end_year; i++) {
    const currentYear = start_year + i;
    if ((currentYear % 4 === 0) && (currentYear % 100 !== 0) || (currentYear % 400 === 0)) {
      const newLi = document.createElement('li'); // Move this line here
      newLi.innerText = `${currentYear}`; // Use currentYear instead of start_year + i
      ulElement.append(newLi);
    }
  }
} else if (end_year < start_year) {
  for (let i = 0; end_year + i <= start_year; i++) {
    const currentYear = end_year + i;
    if ((currentYear % 4 === 0) && (currentYear % 100 !== 0) || (currentYear % 400 === 0)) {
      const newLi = document.createElement('li'); // Move this line here
      newLi.innerText = `${currentYear}`; // Use currentYear instead of end_year + i
      ulElement.append(newLi);
    }
  }
}