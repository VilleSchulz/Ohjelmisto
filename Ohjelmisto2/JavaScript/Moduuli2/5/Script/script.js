//Write a program that prompts the user for numbers. When the user enters
// one of the numbers he previously entered, the program will announce that
// the number has already been given and stops its operation and then prints
// all the given numbers to the console in ascending order. (2p)
'use strict';
const num_list = [];
let count = 0;
while (true) {
  const num = parseInt(prompt('Give number!'));
  if (num_list.includes(num)) {
    console.log('Numbers has already been given');
    num_list.pop();
    break;
  }
  num_list.push(num);
  count += 1;

}
num_list.sort((a, b) => a - b);

for (let i = 0; count-1 > i; i++) {
  console.log(num_list[i]);

}

