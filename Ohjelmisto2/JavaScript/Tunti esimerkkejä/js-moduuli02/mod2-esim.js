// Taulukot (array)
// alkioiden tietotyypit voi olla mitä vaan (kuin muuttujissakin)
const items = ['eka', 2, 3.3, [1, 2, 3], true];
console.log(items);

// alkion arvo saadaan alkion indeksiin viittaamalla
console.log(items[3]);

// alkion arvo voidaan lisätä tai muuttaa alkion indeksiin viittaamalla
items[3] = 99;
console.log(items[3]);
items[9] = '10. alkion esimerkkiarvo';
console.log(items);
// määrittämätön arvo (undefined, vähän kuin None/null)
console.log(items[6]);
// arrayn koko .length
console.log(items.length);

console.log('Tulostetaan kaikkien alkioiden arvor for:lla');
for (let i=0; i<items.length; i++) {
  console.log(i+1 + '. alkion arvo on ' + items[i]);
}

// sama for-of:lla, ei tulosteta tyhjiä alkioita
for (const item of items) {
  if (item != undefined) { // tai vain (item) ehdoksi, koska undefined on epätotuudellinen (falsy) arvo
    console.log(item);
  }
}

// Taulukoiden metodeita
const names = ['Frank', 'Scott', 'Jasmine', 'Don'];
const ages = [13, 8, 102, 46];
console.log(names);
// järjestä aakkosjärjestykseen
names.sort();
console.log(names);
// järjestä numerojärjestykseen
ages.sort((a,b) => a-b)
console.log(ages);
// käännä järj. ympäri
ages.reverse();
console.log(ages);
// lisää uusi nimi taulukon loppuun
names.push('Iines');
// lisää usi nimi taulukon alkuun
names.unshift('Hessu');
console.log(names);
// poista ja palauta viimeinen alkio
const lastNameInArr = names.pop();
console.log('taulukosta poistettiin', lastNameInArr);
console.log(names);
// onko taulukossa ko. arvo, palauttaa true/false boolean
console.log(names.includes('Iines'));
console.log(names.includes('Don'));

// JS objektit/oliot
// olioliteraali on tietorakenteena kuin Pythonin sanakirja (dict)
const person = {name: "Iines", age: 34}
console.log('person-olio', person);
// ominaisuuksien arvojen muuttaminen (kuin sijoits)
person['age'] = 36;
person.name = 'Iines Ankka';
// ominaisuuksien (property) lisääminen
person.profession = 'student';
console.log('person päivitetty', person);
// tiettyyn ominaisuuden arvon hakeminen
console.log(person.name + ' on ' + person.age + '-vuotias.');

// metodin luominen olioon nimettömänä funktiona
const person2 = {
  name: "Iines",
  age: 34,
  getInfo: function() {
    return this.name + ' on ' + this.age + '-vuotias.';
  },
};
console.log(person2.getInfo());

