console.log(window);
// BOM browser object model
//window.alert('moro');
//alert('moro');

/**
// confirm returns boolean value (true/false)
if (confirm('Ookko tosissas?')) {
  console.log('Käyttäjä klikkasi OK');
} else {
  console.log('Käyttäjä painoi "Peruuta"');
}

// prompt palauttaa käyttäjän syöttämän merkkijonon, jos painetaan ok
// palauttaa null, jos painetaan cancel
const userInput = prompt('Sano jotain!');
console.log('user input', userInput);
*/

// DOM - Document Object Model
console.log(document);

//const targetElements = document.getElementsByTagName('p');
const targetElements = document.querySelectorAll('p');
console.log(targetElements);

// id aina yksilöllinen
const targetElement = document.querySelector('#toka');
console.log(targetElement);

targetElement.textContent = 'Tässä JS:n kautta muokattu sisältö';

// HTML-elementtien luominen ja lisääminen DOMiin
const newParagraph =  document.createElement('p');
//newParagraph.innerText = "Tässa jotain <b>uutta</b> juttua.";
newParagraph.innerHTML = "Tässa jotain <b>uutta</b> juttua.";
document.querySelector('article').append(newParagraph);
//newParagraph.style = 'color: blue';
newParagraph.classList.add('blue');

// viittaus kaikkiin p-elementteihin löytyy targetElements-muuttujasta
// käsitellään ensimmäistä niistä
targetElements[0].classList.add("bold", "red");
//targetElements[0].classList.remove("red");

// tapahtumankäsittely (event-olio sisältää tietoa tapahtumasta)
function clickHandler(event) {
  console.log('p clicked', event);
  targetElements[0].classList.remove("red");
}
// klikkien käsittely
targetElements[0].addEventListener('click', clickHandler);

// kakkosklikin (context menu) käsittely koko dokumentille (nimetön funktiota)
document.addEventListener('contextmenu', function(event){
  console.log('context menu', event);
  event.preventDefault();
});

// key loggeri
const keyPressHistory = [];
document.addEventListener('keyup', function(event){
  console.log('näppäin ylös', event.key);
  keyPressHistory.push(event.key);
  console.log('näppäinpainallushistoria', keyPressHistory.toString());
});

// hiirenseuranta
document.addEventListener('mousemove', function(event) {
  console.log('mouse position', event.clientX, event.clientY);
});
