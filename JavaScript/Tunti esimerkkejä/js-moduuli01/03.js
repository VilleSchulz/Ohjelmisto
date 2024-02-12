  'use strict';
    const sum = document.querySelector('.sum');
    const product = document.querySelector('.product');
    const average = document.querySelector('.average');
    // Write a program that prompts for three integers. The program prints the sum,
    // product and average of the numbers to the HTML document.

    const num1 = parseInt(prompt('Please give number 1:'));
    console.log(typeof num1);
    const num2 = parseInt(prompt('Please give number 2:'));
    const num3 = parseInt(prompt('Please give number 3:'));

    let totalSum = num1 + num2 + num3;
    let totalProduct = num1 * num2 * num3;
    let totalAveraage = totalProduct / 3;

    sum.innerHTML = `Sum: ${totalSum}`;
    product.innerHTML = `Product: ${totalProduct}`;
    average.innerHTML = `Average: ${totalAveraage}`;