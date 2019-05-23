"""
show the inner or nested function.
It's used in following scenario:
1. Encapsulate (hiding the function from public use)
2. Factory function to generate another function object
3. Calling some specific code
"""
import math


def num1(x):
    def num2(y):
        print('x: ', x)
        print('y: ', y)
        return x * y
    return num2


res = num1(5)
print(res(10))
print(num1(5)(10))


"""
Example of factory function. A factory function is a function that creates another object.
"""
def power_generator(num):

    # Create the inner function
    def power_n(power):
        return num ** power

    return power_n


power_two = power_generator(2)
power_three = power_generator(3)
print(power_two(8))  #256
print(power_three(4))  #381


"""
call some specific code example
"""
def counter():
    for x in range(1000):
        pass


def in_club(name, club):
    pass


def whats_running(function):

    def new_function():
        print(function.__name__, 'has started.')
        function()
        print(function.__name__, 'has ended')

    return new_function


def time_this(function):
    import time

    def wrapper(*args, **kargs):
        start = time.time()
        function(*args, **kargs)
        end = time.time()
        print(f'{function.__name__} takes {end - start} seconds to execute')

    wrapper.__name__ = function.__name__ + '_timed'
    return wrapper


counter = time_this(counter)
print(counter.__name__)
in_club = whats_running(in_club)

counter()
in_club('John', 'pass')


