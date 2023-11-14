//Write a program that prompts the user for five numbers and prints them in
// the reverse order they were entered. Print the result to the console.(2p)
// Save the numbers to an array, then use for-loop to iterate in reverse order.
// Do not use array.reverse() function.
const num_list = [];
for (i = 0; i < 5; i++) {
  let number = parseInt(prompt(`Give a number:${i+1}`));
  num_list.push(number);

}
for (i = 4; i >= 0; i--) {
  console.log(num_list[i]);
}
