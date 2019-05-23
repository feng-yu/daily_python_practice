"""
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
import time


def findN(arr):
    for x in range(1,len(arr)+2):
        try:
            arr.remove(x)
        except ValueError as err:
            return x


arr = [3, 4, -1, 1]   #answer is 2
n = findN(arr)
print(n)
assert n == 2

arr = [1, 2, 0]  #answer is 3
n = findN(arr)
print(n)
assert n == 3

arr = [1, 2, 3]  #answer is 3
n = findN(arr)
print(n)
assert n == 4

arr = []
for x in range(100000):
    arr.append(x)
start = time.time()
n = findN(arr)
print(n)
print('It takes %f seconds to find N' % (time.time()-start))
assert n == 100000