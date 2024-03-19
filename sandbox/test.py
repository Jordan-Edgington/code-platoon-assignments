def multiply(n):
    tempArr = []
    nString = str(n)
    for char in nString:
        if char.isnumeric():
            tempArr.append(char)
    numLen = len(tempArr)
    print(n*(5**numLen))


multiply(3)
multiply(10)
multiply(200)
multiply(0)
multiply(-3)
