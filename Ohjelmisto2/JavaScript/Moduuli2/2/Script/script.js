//Write a program that asks the user for the number of participants.
// After this, the program asks for the names of all participants. Finally,
// the program prints the names of the participants on the web page in an
// ordered list (<ol>) in alphabetical order. (2p)

const part_amount = parseInt(prompt('Give number of participants'));
for(i=part_amount;i<=0;i--) {
  part_name = prompt(`Give name number ${i + 1}`)
}
