"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time,
you could climb any number from a set of positive integers X? For example,
if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""


import functools
@functools.lru_cache(maxsize=1000)
def find_ways(n, steps):
    """
    Uing cache to speed up
    :param n: total steps
    :param steps:  a tuple that contains the allowed steps
    :return: how many ways
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        ways = 0
        for step in steps:
            ways += find_ways(n-step, steps)
        return ways

def main():
    n = 6
    steps = (1,3,5)
    ways = find_ways(n, steps)
    print(ways)

main()