def linear_search(value_to_find, array_to_search_through):
    # for loop for the array to searrch through looking for valuetofind
    counter = 0
    for item in array_to_search_through:
        if value_to_find == item:
            return counter
        counter += 1
    return "Not Found"


def linear_search_global(value_to_find, array_to_search_through):
    # Put empty list
    index_list = []
    counter = 0
    for item in array_to_search_through:
        if value_to_find == item:
            index_list.append(counter)
        counter += 1
    if (len(index_list) == 0):
        return "Item Not Found"
    # your code here
    return index_list


# TEST CASES

print(linear_search('a', 'banana'))
print(linear_search('a', 'zzzzzzz'))
print(linear_search_global('a', 'banana'))
print(linear_search_global('n', 'banana'))
