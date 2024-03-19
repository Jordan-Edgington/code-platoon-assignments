// How can you make this more scalable and reusable later?

function findArmstrongNumbers(numbers) {
    //loop through the input list and determines how many digits are in each number
    let armstrongNums = []
    for (let num = 0; num < numbers.length; num++) {
        let digitCount = numbers[num].toString().length;
        let digitListProducts = [];
        //then we add each digit to digitListProducts raised to the exponent of its length
        const numString = numbers[num].toString();
        for (let digit = 0; digit < numString.length; digit ++) {
            digitListProducts.push(Number(numString[digit])**digitCount);
        }
        //add up all the products in digitListProducts to see if they = numbers[num]
        let armstrongTestNum = 0;
        for (let product = 0; product < digitListProducts.length; product ++) {
            armstrongTestNum += digitListProducts[product];
        }
        // if they do equal, add them tot he list we will return at the end of the function
        if (armstrongTestNum === numbers[num]) {
            armstrongNums.push(numbers[num]);
        }
    };
    return armstrongNums;
}

console.log(findArmstrongNumbers([1, 10, 371, 100]));

module.exports = {findArmstrongNumbers}