def FlattenList(lst):
    result = []
    for item in lst:
        if isinstance(item, int):
            result.append(item)
        elif isinstance(item, list):
            result.extend(FlattenList(item))
    return result


test_1 = [1, 2, [3], [4, 5]]
test_2 = [1, [2], [3, [4, 5, [6]]], 7]
print(FlattenList(test_1))
print(FlattenList(test_2))
