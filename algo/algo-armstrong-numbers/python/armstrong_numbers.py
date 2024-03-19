# must find digit count
# must then compare sum of digits^digit_count to num


def find_armstrong_numbers(numbers):
    # this determines the number of digits in each number
    armstrong_nums = []
    for num in numbers:
        digit_count = len(str(num))
        # then we add each digit to digit_list_products raised to the exponent of its length
        digit_list_products = []
        for digit in str(num):
            digit_list_products.append(int(digit)**digit_count)
        # add up all the products in digit_list_products to see if they = the original num
        armstrong_test_num = 0
        for product in digit_list_products:
            armstrong_test_num += product
        # if they do equal, add them to the list we will return at the end of the function
        if armstrong_test_num == num:
            armstrong_nums.append(num)

    # need to raise each digit to digit_coun

    return armstrong_nums


print(find_armstrong_numbers([1, 10, 371, 100]))
