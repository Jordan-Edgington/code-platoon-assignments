# Linear Search


def linear_search_unsorted(arr, target):
    steps = 0
    # enumerates through the list to be able to return the index easily in our return statement
    for idx, num in enumerate(arr):
        # increments the step counter
        steps += 1
        # checks to see if the current number matches our target
        if num == target:
            # returns the index the item was found and how many steps it took
            return f"Scenario 1 (Linear Search): Target {target} found at index {idx} in {steps} steps."
    # returns how many steps occurred before it determined the target was not in the array
    return f"Scenario 1 (Linear Search): Target {target} not found after {steps} steps."

# Binary Search


def binary_search_unsorted(arr, target):
    # first turns the unsorted list into a sorted list
    sorted_list = sorted(arr)
    left = 0
    right = len(arr) - 1
    steps = 0
    while left <= right:
        # dynamically sets the middle equal to the current result of performing floor division on the sum of left and right
        middle = (left + right)//2
        # incrememnts the step counter
        steps += 1
        # if the item at index middle is less than the target
        if sorted_list[middle] < target:
            # move the left of our search area to the right of the middle
            left = middle + 1
        # if the item at index middle is greater than the target
        elif sorted_list[middle] > target:
            # move the right of our search area to the left of the middle
            right = middle - 1
        # if the item at the middle of our search is equal to the target
        elif sorted_list[middle] == target:
            # return a string with the number of steps it took to find and the index of our target
            return f"Scenario 1 (Binary Search): Target {target} found at index {middle} in {steps} steps."
    # if not in list, returns a string with the number of steps it took to determine that the target was not in the list
    return f"Scenario 1 (Binary Search): Target {target} not found after {steps} steps."


def linear_search_sorted(arr, target):
    steps = 0
    # enumerates through the list to be able to return the index easily in our return statement
    for idx, num in enumerate(arr):
        # increments the step counter
        steps += 1
        # checks to see if the current number matches our target
        if num == target:
            # returns the index the item was found and how many steps it took
            return f"Scenario 1 (Linear Search): Target {target} found at index {idx} in {steps} steps."
    # returns how many steps occurred before it determined the target was not in the array
    return f"Scenario 1 (Linear Search): Target {target} not found after {steps} steps."


def binary_search_sorted(arr, target):
    # first turns the unsorted list into a sorted list
    left = 0
    right = len(arr) - 1
    steps = 0
    while left <= right:
        # dynamically sets the middle equal to the current result of performing floor division on the sum of left and right
        middle = (left + right)//2
        # incrememnts the step counter
        steps += 1
        # if the item at index middle is less than the target
        if arr[middle] < target:
            # move the left of our search area to the right of the middle
            left = middle + 1
        # if the item at index middle is greater than the target
        elif arr[middle] > target:
            # move the right of our search area to the left of the middle
            right = middle - 1
        # if the item at the middle of our search is equal to the target
        elif arr[middle] == target:
            # return a string with the number of steps it took to find and the index of our target
            return f"Scenario 1 (Binary Search): Target {target} found at index {middle} in {steps} steps."
    # if not in list, returns a string with the number of steps it took to determine that the target was not in the list
    return f"Scenario 1 (Binary Search): Target {target} not found after {steps} steps."


# # Scenario 1 Test
unsorted_list = [42, 15, 7, 30, 22, 10, 18]
target_1 = 30

# Scenario 2 Test
sorted_word_list = ['apple', 'banana',
                    'cherry', 'grape', 'orange', 'strawberry']
target_2 = 'orange'

# Scenario 3 Test
occurrence_list = [5, 10, 15, 20, 10, 25, 30, 35, 10, 40]
target_3 = 10


print(linear_search_unsorted(unsorted_list, target_1))
print(binary_search_unsorted(unsorted_list, target_1))
print(linear_search_sorted(sorted_word_list, target_2))
print(binary_search_sorted(sorted_word_list, target_2))
print(linear_search_unsorted(occurrence_list, target_3))
print(binary_search_unsorted(occurrence_list, target_3))
