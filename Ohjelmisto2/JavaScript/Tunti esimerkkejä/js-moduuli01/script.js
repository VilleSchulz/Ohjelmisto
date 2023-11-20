console.log('Moikka ulkoisesta tiedostosta!');

// switch - case
/**
const cabinClass = prompt('Enter the cabin class (A/B/C).');
cabinClass.toUpperCase(); //a -> A, mutta uutta arvoa ei sijoiteta muuttujaan
console.log('user choice', cabinClass);
switch (cabinClass.toUpperCase()) {
  case 'A':
//case 'a': // monta ehtoa voi "pinota" samaan kohtaan
    console.log('Top deck cabin with window.');
    break;
  case 'B':
    console.log('Top deck cabin without window.');
    break;
  case 'C':
    console.log('Windowless cabin under the car deck.');
  default:
    console.log('Invalid cabin class.');
}
// suoritus jatkuu täältä break; lausekkeen jälkeen
*/

// Silmukat = Loopit = toistorakenteet
// While, toimii kuin Pythonissa
let counter = 0;
while (counter < 5) {
  console.log('ehto oli tosi ',  counter);
  counter++; //sama kuin counter = counter + 1 tai counter += 1
}

// heitetään noppaa niin kauan, että saadaan 6
let gameOver = false;
while (!gameOver) {
  //Math.random() // returns 0-0.99999999999999999999999999999999999
  // arvotaa silmäluku 1-6
  const number = Math.floor(Math.random() * 6 + 1);
  console.log('number', number)
  if (number === 6) {
    gameOver = true;
  }
}

// for silmukka
for (let i=100; i>0; i -= 3) {
  console.log('for-silmukan i:n arvo', i);
}

// arvotaan 7 numeron lottorivi, pallot 1-40
for (let i=0; i<7; i++) {
  const number = Math.floor(Math.random() * 40 + 1);
  console.log(i + 1 + '. pallon arvo: ' + number);
}

// while-silmukan korvaaminen for-silmukalla (RUMA TAPA!)
for (;;) {
  //Math.random() // returns 0-0.99999999999999999999999999999999999
  // arvotaa silmäluku 1-6
  const number = Math.floor(Math.random() * 6 + 1);
  console.log('number', number)
  if (number === 6) {
    break;
  }
}

