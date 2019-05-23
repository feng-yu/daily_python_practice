"""
[Medium]
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr
"""


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def f(a, b):
    return [a, b]


def car(con):
    return con(f)[0]


def cdr(con):
    return con(f)[-1]


test_data = cons(3, 4)

assert car(test_data) == 3
assert cdr(test_data) == 4