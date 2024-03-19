function fibonacci(num) {
  //Started the fibonacci sequence
  let fiboArray = [0, 1, 1]
  
  /*it is adding the last 2 digits of the current sequence
  pushing that number to the array and repeating
  until the sequence reaches the Num'th number*/
  while (fiboArray.length < (num + 1)) {
    newNum = fiboArray[fiboArray.length-2] + fiboArray[fiboArray.length-1];
    fiboArray.push(newNum);
  }
  //returns the num'th number of the fiboArray
  return fiboArray[num];
}

module.exports = fibonacci;
