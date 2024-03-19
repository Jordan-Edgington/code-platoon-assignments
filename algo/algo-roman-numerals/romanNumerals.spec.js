const { toRomanLazy, toRoman } = require("./romanNumerals.js");

describe("Tests toRomanLazy", () => {
    test("Tests toRomanLazy(4) equals IIII", () => {
        expect(toRomanLazy(4)).toBe("IIII")
    })
    test("Tests toRomanLazy(150) equals CL", () => {
        expect(toRomanLazy(150)).toBe("CL")
    })
    test("Tests toRomanLazy(944) equals DCCCCXXXXIIII", () => {
        expect(toRomanLazy(944)).toBe("DCCCCXXXXIIII")
    })
})

describe("Tests toRoman", () => {
    test("Tests toRoman(4) equals IV", () => {
        expect(toRoman(4)).toBe("IV")
    })
    test("Tests toRoman(150) equals IV", () => {
        expect(toRoman(150)).toBe("CL")
    })
    test("Tests toRoman(944) equals CMXLIV", () => {
        expect(toRoman(944)).toBe("CMXLIV")
    })
})