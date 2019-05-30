"""
[Hard]
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def largest_sum_non_adjacent(numbers):
    if not numbers:  #empty list
        return 0
    elif len(numbers) == 1:  #list only contains one integer
        return numbers[0]
    elif len(numbers) == 2:  #list contains two integers
        return max(numbers)
    else:  #list contains at least three integers
        sum_1 = numbers[0] + largest_sum_non_adjacent(numbers[2:])
        sum_2 = numbers[1] + largest_sum_non_adjacent(numbers[3:])
        return max(sum_1, sum_2)


test_data1 = [2, 4, 6, 2, 5]
assert largest_sum_non_adjacent(test_data1) == 13

test_data2 = [5, 1, 1, 5]
assert largest_sum_non_adjacent(test_data2) == 10



