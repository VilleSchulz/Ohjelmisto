//Write a program that asks the user to enter a year and notifies the user
// whether the input year is a leap year. A year is a leap year if it is
// divisible by four. However, years divisible by 100 are leap years only if
// they are also divisible by 400. Print the result on the HTML document. (3p)

'use strict';

const year = parseInt(prompt('Anna vuosi: '));

let leap_year = null;

if ((year % 4 == 0) && (year % 100 != 0) || (year % 4 == 0) && (year % 100 == 0) && (year % 400 == 0)) {
  leap_year = `${year} on karkausvuosi`;
  document.querySelector('#target').innerHTML = leap_year;
} else {
  leap_year = `${year} ei ole karkausvuosi`;
}
