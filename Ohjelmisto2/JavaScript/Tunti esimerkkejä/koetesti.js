function laskin(array){

  let sum = 0;
  for (num of array){
    sum+= num
  }

  let average = sum/array.length;
  return average;
}


console.log(laskin[1,2,3,4])