//In the Harry Potter children's books, the sorting hat assigns a new student
// at Hogwarts School of Witchcraft and Wizardry to one of the four classes,
// which are Gryffindor, Slytherin, Hufflepuff, and Ravenclaw. Write an
// electronic sorting hat that asks for a student's name and draws a room for
// him. If you enter Anna as the name, for example, the program prints to the
// HTML document "Anna, you are Ravenclaw." (3p)
//Use math.random() to draw a value (1, 2, 3 or 4)
//Once the number is drawn, you need to use a multiple choice structure
// (if, else if, ..., else or switch).
'use strict';
const name = prompt("Give your name! We will sort your class");
const number = Math.floor(Math.random() * 4);
//toinen tapa tehdä: function getRandomInt(min, max) {
//min = Math.ceil(min);
//max = Math.floor(max);
//return Math.floor(Math.random() * (max - min) + min);
//The maximum is exclusive and the minimum is inclusive
//}


//Tai switch case

//let class;
//switch (classes){
//  case 0;
//  classes = 'Gryffindor'
//    case 1;
//  classes = 'Slytherin'
//case 2;
 // classes = 'Hufflepuff'
 //   case 3;
//  classes = 'Ravenclaw'
//}
const classes = ["Gryffindor","Slytherin", "Hufflepuff","Ravenclaw"]
print = name +" Your class is " + classes[number];
document.querySelector('#target').innerHTML= print


