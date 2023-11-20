// JS funktiot
// (3 eri tapaa määritellä, harkoissa keskitytään ensimmäiseen)

function doSomething(name) {
  console.log('moi ' + name);
}
const doSomething2 = function(name) {
  console.log('moi täältäkin', name);
};
const doSomething3 = (name) => {
  console.log('ja moi vielä täältäkin', name);
};
doSomething('Iines');
doSomething2('Don');
doSomething3('John');

// Lottorivin arvonta ja palautusarvo
// arvotaan n numeron lottorivi, pallot 1-maxValue
// palautetaan rivi taulukkona (esim. [3, 6, 23, 34, 35, 38, 40])
function generateLotteryRow(numberCount, maxValue) {
  const lotteryRow = [];
  while (lotteryRow.length < numberCount) {
    const number = Math.floor(Math.random() * maxValue + 1);
    if (!lotteryRow.includes(number)) {
      lotteryRow.push(number);
    }
    //console.log('arvotun pallon arvo: ' + number);
  }
  return lotteryRow.sort((num1, num2) => num1-num2);
}

const myRow = generateLotteryRow(7, 40);
console.log('myRow', myRow);
console.log(generateLotteryRow(9, 100));

// Luodaa lottokuponki, jossa n määrä rivejä
function createLotteryTicket(rowCount) {
  const ticket = [];
  for (let i=0; i<rowCount; i++) {
    const row = generateLotteryRow(7, 40);
    ticket.push(row);
  }
  return ticket;
}

const myTicket = createLotteryTicket(5);
console.log('koko lottolappu', myTicket);
// tulostetaan 2. kupongin 3. numero
console.log('tulostetaan 2. kupongin 3. numero', myTicket[1][2]);

// value scope / näkyvyysalue
// muuttuja2 on globaali, koska esitelty pääohjelmassa
let muuttuja2 = 2;
{
  const muuttuja = 0;
  muuttuja2 = 'uusi arvo';
  {
    const muuttuja = 'a';
    let muuttuja2 = 'vielä uudempi arvo';
    console.log(muuttuja2);
  }
  {
    console.log(muuttuja);
  }
}
console.log(muuttuja2);

// Taulukko muuttujan parametrina
// uusi muuttua numbers viittaa samaa taulukkoon kuin pääohjelman numbers
function arrayTest(numbers) {
  numbers.push(9);
  return numbers;
}
const numbers = [1, 2, 3];
const numbers2 = numbers; // kopioidaan viittaus uuteen muuttujaan
let numbers3 = []; // uuden taulukon luominen ja olemassaolevan taulukon arvojen liittäminen siihen
numbers3 = numbers3.concat(numbers);
// toinen tapa kopioida arvot uuteen taulukkoon (spread-operaattori)
const numbers4 = [...numbers]; // ...[1, 2, 3] => 1, 2, 3
console.log('funktion paluuarvo', arrayTest(numbers));
console.log('alkuperäinen taulukko', numbers);
console.log('"kopioitu" taulukko', numbers2);
console.log('"kopioidut" taulukon arvot', numbers3);

console.log('numbers4', numbers4);

