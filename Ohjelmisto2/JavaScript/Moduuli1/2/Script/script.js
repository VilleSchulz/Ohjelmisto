//Write a program that prompts for user's name and then greets the user.
// Print the result to the HTML document: Hello, Name! (2p)

const kysely =prompt("Anna nimesi!");
console.log(kysely);

const nimi = `Hello, ${kysely}!`;
document.write("<p>" + nimi + "</p>");