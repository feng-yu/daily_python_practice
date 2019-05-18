"""
Given a list of numbers and a number k, return how many ways that any numbers from the list add up to k.
For example, given [10, 15, 2, 7] and k of 17, return 2 since 10 + 7 is 17 and 15 + 2 is 17.
"""
import functools
import math


# @functools.lru_cache(maxsize=1000)
def findways(n, X):
    ways_list = []

    sorted_numbers = sorted(X)
    # Only need to go through half of data
    middle_point = math.ceil(len(sorted_numbers) / 2)
    for number in sorted_numbers[0:middle_point]:
        if number > n:
            break
        else:
            remainder = n - number
            sorted_numbers.remove(number)
            if remainder in sorted_numbers:
                ways_list.append([number, remainder])
            else:
                if len(sorted_numbers) > 1:
                    remainder_ways_list = findways(remainder, sorted_numbers)
                    if len(remainder_ways_list) != 0:
                        for remainder_way in remainder_ways_list:
                            remainder_way.insert(0, number)
                            ways_list.append(remainder_way)
                else:
                    break

    return ways_list


n = 17
X = [12, 4, 7, 5, 6, 1, 10, 2]
#X = [ 4, 6, 7]
# X = [12, 4, 7, 5, 6, 10]

result = findways(n, X)
print(result)
