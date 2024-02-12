//Write a program that rolls user defined number of dice and displays
// the sum of the results of the dice rolls.(2p)
// First, program asks the user for the number of dice rolls.
// Then the program throws a die as many times as the user defined.
// Print the sum of the results in the console or in the HTML document.

'use strict'

let dice_rolls = parseInt(prompt("Give dice amount"));
let sum = 0;
for ( let i = 0; i < dice_rolls; i++){
  let rollResult = Math.floor(Math.random() * 6 + 1);
  console.log("Dice roll" + (i+1)+": " + rollResult);
  sum +=rollResult;

}

console.log(`Roll sum: ${sum}`)



