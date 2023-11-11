console.log("MOikka ulkoisesta tiedostosta");
 console.log("moro maailma");
    //alert('Terve minun nimeni on alert')
    const nimi =  prompt('Anna nimesi:');
    //kommentti
    console.log(nimi);
    //string literal = merkkijono
    const merkkijono = 'Nimesi siis on : '+ nimi;
    console.log(merkkijono);
    const muotoilu = alert(`Kiva tavata ${nimi}`);
    console.log(muotoilu);

    // var, älä käytä jos ei ole pakko
  //älkää tehkö näin
  //var muuttujan voi määritellä useaan kertaan
  //hoisting eli käyttö enne määrittelyä mahdollista
  console.log(age)
  var age= 12;
  var age=13;
  console.log(age)


  //tämän takia strict ja const / let

  let teacher = 'Ulla';
  let surname;
  surname = 'kekeke'
  teacher = teacher +''+ surname;
  console.log(teacher);
  const teacher2 = 'Matti'
  const surname2 = 'Peltoniemi'
  //aiheuttaa virheen, const siis muuttumaton/constant
  //teacher2 = teacher2 + surname2;
   // console.log(teacher2)
  const multiplier = 4.1868;
  const k1 = prompt('Give the amount of energy  for lunch')
  const j1 = multiplier * k1
  console.log(`At breakfast you got ${j1}KJ`)

  const taulukko = [0,1,2,3,4,5];
  console.log(taulukko);
  //ei onnistu jos koittaa korvata taulukkon uudella, muokkaus onnistuu
  //const taulukko = [1,2,3,4,5,6];
  taulukko[0]=1;
  console.log(taulukko);
//let muuttujan tyyppiä voi vaihtaa lennossa
  let nameAgain = 'Ulla';
  console.log(typeof,nameAgain, nameAgain)
  nameAgain = 200
  console.log(typeof nameAgain,nameAgain);

  //käytetään toString metodia
  //sillä voidaan muuttaa esim int ->string
  const ageStr = 13;
  const age3= ageStr.toString();
  console.log(typeof age3, age3);
