class Roman:
    numbers = []

    def __init__(self, roman_num, arabic):
        self.roman_num = roman_num
        self.arabic = arabic
        Roman.numbers.append(self)


# Creates all the objects we will be working with (roman numeral values up to M)
M = Roman("M", 1000)
CM = Roman("CM", 900)
D = Roman("D", 500)
CD = Roman("CD", 400)
C = Roman("C", 100)
XC = Roman("XC", 90)
L = Roman("L", 50)
XL = Roman("XL", 40)
X = Roman("X", 10)
IX = Roman("IX", 9)
V = Roman("V", 5)
IV = Roman("IV", 4)
I = Roman("I", 1)


def to_roman(num):

    final_num = ""

    # establish a for loop of the items Roman.numbers, and determine how many times each one fits into num
    for item in Roman.numbers:
        divided_num = num // item.arabic
        if divided_num > 0:
            temp_str = item.roman_num * divided_num
            final_num += temp_str
            num -= item.arabic*divided_num
    return final_num


print(to_roman(4))
print(to_roman(11))
print(to_roman(14))
print(to_roman(16))
print(to_roman(1437))
# TEST CASES
