//js functiot

//esimmäistä funktioo voi kutsusa mistä vain
function doSomething(name) {
  console.log('moi ' + name);
}

const doSomething2 = function(name) {
  console.log('moi täälläkin', name);
};

const doSomething3 = (name) => {
  console.log('moi täälläkin', name);
};

doSomething('ville');
doSomething2('ville');
doSomething3('ville');

function generateLotteryRow(numberCount, maxValue) {
  const lotteryRow = [];
  while (lotteryRow.length < numberCount) {
    const number = Math.floor(Math.random() * maxValue + 1);
    if (!lotteryRow.includes(number)) {
      lotteryRow.push(number);
    }
    console.log('. pallon arvo: ' + number);
  }

  return lotteryRow.sort((num1, num2) => num1 - num2);
}

const myRow = generateLotteryRow(8, 70);
console.log('myROw', myRow);

//luodaan lottokuponki, jossa n määrä rivejä

function createLotteryTicket(rowcount) {
  const ticket = [];
  for (let i = 0; i < rowcount; i++) {
    const row = generateLotteryRow(7, 40);
    ticket.push(row);

  }
  return ticket;
}

console.log(createLotteryTicket(5));