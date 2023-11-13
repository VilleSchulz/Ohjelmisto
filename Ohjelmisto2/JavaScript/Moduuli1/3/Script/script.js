//Write a program that prompts for three integers. The program prints the sum,
// product and average of the numbers to the HTML document. (3p)
//remember to convert strings to numbers when adding

'use strict';
const num1 = parseInt(prompt("Anna numero 1"));

console.log(num1);

const num2= parseInt(prompt("Anna numero 2"));

console.log(num2);

const num3= parseInt(prompt("Anna numero 3"));

console.log(num3);

const sum = num1+num2+num3;
const product = num1*num2*num3;
const average = sum /3;
const sum_print = `Summa on ${sum}`;
const product_print = `Tulo on ${product}`;
const average_print = `Keskiarvo on ${average}`;

document.querySelector('#target1').innerHTML = sum_print;
document.querySelector('#target2').innerHTML = product_print;
document.querySelector('#target3').innerHTML = average_print;
