/**console.log(window);
 //palauttaa boolean-arvon
 if (confirm('ootko tosissas')){
 console.log('Käyttäjä klikkasi OK');

 } else {
 console.log('Käyttäjä painoin peruuta');
 }



 //prompt palauttaa käyttäjän syöttämän merkkijonon tai
 const userInput = prompt('sano jotain')

 console.log(userInput)
 */

console.log();

//const targetElements = document.getElementsByTagName('p')
const targetElement = document.querySelector('p');
console.log(targetElement);
//tai sitte kaikki
const targetElements = document.querySelectorAll('p');
console.log(targetElements);

//id aina yksilöllinen
const targetElement1 = document.querySelector('#eka');
console.log(targetElement1);

targetElement.textContent = 'tässä on js:n kautta luotu sisältö';

//html-elementtien luominen ja lisääminen DOMiin
const newP = document.createElement('p');
newP.textContent = 'tässä jotai uutta';
document.querySelector('article').append(newP);
newP.style = 'color:blue';

