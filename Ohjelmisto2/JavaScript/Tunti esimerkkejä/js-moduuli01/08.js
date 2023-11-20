const targetElem = document.querySelector('#output');
const startYear = parseInt(prompt('Alkuvuosi?'));
const endYear = parseInt(prompt('Loppuvuosi?'));

const ulElem = document.createElement('ul');
targetElem.append(ulElem);

for (let i=startYear; i<=endYear; i++) {
  // console.log('years to be tested', i);
  // neljällä tai neljälläsadalla jaollinen, mutta ei sadalla
  if (i % 4 == 0 && i % 100 != 0 || i % 400 == 0) {
    console.log('leap year', i);
    const newLI = document.createElement('li');
    newLI.innerText = `${i} on karkausvuosi.`;
    ulElem.append(newLI);
  }
}

ulElem.style = 'list-style-type: none;';
// attribuuttien lisäys ja poisto (ei kuulu tehtävään)
ulElem.setAttribute('kukkuu', 'moro');
ulElem.removeAttribute('kukkuu');