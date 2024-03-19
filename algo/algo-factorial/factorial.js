function factorial(num) {
  if (num === 0 || num === 1) {
    return 1;
  } else {
    newNum = num 
    for (let i = num; i > 1; i--) {
      newNum *= (i - 1)
    }
    return newNum
  }
}


module.exports = factorial;