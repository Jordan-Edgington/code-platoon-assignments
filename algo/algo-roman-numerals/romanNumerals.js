function toRomanLazy(num) {
  let output = "";
  romanNumeralToArabic = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50 ,
    "X": 10,
    "V": 5,
    "I": 1
  }
  const romanNumeralPriorityOrder = [
    "M",
    "D",
    "C",
    "L",
    "X",
    "V",
    "I"
  ]
  for (let i = 0; i < romanNumeralPriorityOrder.length; i++) {
    //Divides num by the numerical value of the current roman numeral and gives the rounded down solution
    romanDividesTimes = Math.floor(num / romanNumeralToArabic[romanNumeralPriorityOrder[i]]);
    //Adds the number of that roman numeral to output
    numeralsToAdd = romanNumeralPriorityOrder[i].repeat(romanDividesTimes);
    output = output.concat(numeralsToAdd);
    //Subtracts that value from num
    num -= romanDividesTimes * romanNumeralToArabic[romanNumeralPriorityOrder[i]];
  }
  return output;
}
function toRoman(num) {
  let output = "";
  romanNumeralToArabic = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
  }
  const romanNumeralPriorityOrder = [
    "M",
    "CM",
    "D",
    "CD",
    "C",
    "XC",
    "L",
    "XL",
    "X",
    "IX",
    "V",
    "IV",
    "I"
  ]
  for (let i = 0; i < romanNumeralPriorityOrder.length; i++) {
    //Divides num by the numerical value of the current roman numeral and gives the rounded down solution
    romanDividesTimes = Math.floor(num / romanNumeralToArabic[romanNumeralPriorityOrder[i]]);
    //Adds the number of that roman numeral to output
    numeralsToAdd = romanNumeralPriorityOrder[i].repeat(romanDividesTimes);
    output = output.concat(numeralsToAdd);
    //Subtracts that value from num
    num -= romanDividesTimes * romanNumeralToArabic[romanNumeralPriorityOrder[i]];
  }
  return output;
}
module.exports = { toRoman, toRomanLazy };
