const factorial = require("./factorial.js");

describe("Tests factorial(0) and factorial (1) both equal 1.", () => {
    test("Tests factorial(0) equals 1", () => {
        expect(factorial(0)).toBe(1);
    })
    test("Tests factorial(1) equals 1", () => {
        expect(factorial(1)).toBe(1);
    })
})

describe("Tests other possible num values.", () => {
    test("Tests factorial(2) equals 2", () => {
        expect(factorial(2)).toBe(2);
    })
    test("Tests factorial(4) equals 24", () => {
        expect(factorial(4)).toBe(24);
    })
    test("Tests factorial(8) equals 40320", () => {
        expect(factorial(8)).toBe(40320);
    })
    test("Tests factorial(18) equals 6402373705728000", () => {
        expect(factorial(18)).toBe(6402373705728000);
    })
})
