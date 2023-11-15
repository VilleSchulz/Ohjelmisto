//Write a program that asks for the names of six dogs. The program prints
// dog names to unordered list <ul> in reverse alphabetical order. (2p)
// Check assignment

const name_list = [];
const targetElem = document.body;
const olElement = document.createElement('ol');
targetElem.append(olElement);

for (i = 0; i < 6; i++) {
  let dog_name = prompt(`Give name of the dog number ${i + 1}`);
  name_list.push(dog_name);
}




name_list.sort();
name_list.reverse();
for (i = 0; i < 6; i++) {
  const newLI = document.createElement('li');
  newLI.innerText = `${name_list[i]}`;
  olElement.append(newLI);
}