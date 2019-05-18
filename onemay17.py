"""
From:  https://dev.to/cwetanow/daily-coding-problem-1-23e0

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
import numbers
import sys


def twoenumbersequals(n, X):
    for x in X:
        if (n-x) in X:
            return True
    return False


re_enter = True

while re_enter:
    try:
        n = float(input('Please enter a number: '))
        re_enter = not isinstance(n, numbers.Number)
    except ValueError as ve:
        print('The input has to be a number!')

re_enter = True

while re_enter:
    X = []
    not_number = False
    # try:
    number_list_str = input('Please enter a number list as [1, 2, 4]: ')
    number_list = number_list_str.strip().strip('[').strip(']').split(',')
    try:
        for number_str in number_list:
            number = float(number_str.strip())
            if not isinstance(number, numbers.Number):
                not_number = True
            else:
                X.append(number)
        if not not_number:
            re_enter = False
    except ValueError as ve:
        print('Input has to be a number list!')

print(n)
print(X)
print(twoenumbersequals(n, X))