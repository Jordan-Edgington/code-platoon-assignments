def fibonacci(n):
    # create a list containing the first 3 values of the fibonacci sequence
    fib = [0, 1, 1,]
    # while length of list is less than n
    # take the last 2 values of the list, add them together, and append this value to the end of the list
    while len(fib) < n + 1:
        lastNum = fib[len(fib) - 1]
        secondLastNum = fib[len(fib)-2]
        fib.append(lastNum + secondLastNum)
    return fib[n]


print(fibonacci(3))
print(fibonacci(7))
