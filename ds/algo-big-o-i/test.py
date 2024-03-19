import random
# this is insertion sort


def insertionSort(arr):
    steps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            steps += 1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print(steps)
    print(arr)


arr = []
for num in range(1, 1001):
    arr.append(random.random()*100:.2f)

insertionSort(arr)
