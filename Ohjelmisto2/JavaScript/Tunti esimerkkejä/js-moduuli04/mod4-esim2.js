/**
 * JS Mod 4 esim. osa 2
 */

async function getMultiply(num) {
  try {
    const response = await fetch('http://localhost:3000/multiply/' + num);
    const json = await response.json();
    console.log(json.msg, json.result);
    return json;
  } catch (error) {
    console.error('doMultiply fetch fail', error);
  }
}

// eventinkäsittelijä buttonille
async function doMultiply(event) {
  // testataan promptilla
  //const number = prompt('Anna numero:');
  // luetaan number-arvo sivun ainoast input-kentästä
  const number = document.querySelector('input').value;
  // asynkronista funktiota pitää kutsua await-sanalla, jos haluaa sen
  // palauttavan jotain muuta kuin Promise-olion
  const resultJson = await getMultiply(number);
  const outputElem = document.querySelector('#toka');
  if (resultJson.result) {
    outputElem.textContent = 'Tulos: ' + resultJson.result;
  } else {
    outputElem.textContent = `${resultJson.msg} (${resultJson.input_num}`;
  }
}
// Sido DOMin ainoaan button-elementtiin tapahtumankäsittelijä
document.querySelector('button').addEventListener('click', doMultiply);
