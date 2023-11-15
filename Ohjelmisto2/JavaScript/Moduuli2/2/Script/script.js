//Write a program that asks the user for the number of participants.
// After this, the program asks for the names of all participants. Finally,
// the program prints the names of the participants on the web page in an
// ordered list (<ol>) in alphabetical order. (2p)
'use strict'
const part_amount = parseInt(prompt('Give number of participants'));
const name_list = [];
const targetElem = document.body;
const olElement = document.createElement('ol');
targetElem.append(olElement);

for (i = 0; i < part_amount; i++) {
  let part_name = prompt(`Give name number ${i + 1}`);
  name_list.push(part_name);
}
name_list.sort();
for (i = 0; i < part_amount; i++) {
  const newLI = document.createElement('li');
  newLI.innerText = `${name_list[i]}`;
  olElement.append(newLI);
}