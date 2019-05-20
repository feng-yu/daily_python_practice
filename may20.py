"""
Given an array of integers, return a new array such that each element at index i of the new array is
the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def product_except_itself(li):
    product = 1
    result_list = []

    for number in li:
        product = product * number
    print(product)

    for number in li:
        result_list.append(product // number)

    return result_list


def product_exception_itself_no_division(li):
    result_list = []

    for index in range(len(li)):
        product = 1
        for number in li[:index]:
            product = product * number
        for number in li[index + 1: ]:
            product = product * number
        result_list.append(product)

    return result_list


test_data = [1, 2, 3, 4, 5]
expected_result = [120, 60, 40, 30, 24]
# result = product_except_itself(test_data)
result = product_exception_itself_no_division(test_data)
print(result)
assert result == expected_result



