//Write a program that asks the user for numbers until he gives zero.
// The given numbers are printed in the console from the largest to the
// smallest. (2p)

'use strict';
const num_list = [];
let count = 0;
while (true) {
  const num = parseInt(prompt('Give number! Hit 0 to cancel'));
  num_list.push(num);
  count + 1;
  if (num === 0) {
    break;
  }
}
num_list.sort();
num_list.reverse();

for (let i = 0; count > i; i++) {
  console.log(num_list[i]);

}

