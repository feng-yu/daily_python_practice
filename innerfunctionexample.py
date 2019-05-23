"""
show the inner or nested function
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


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

a = cons(2, 3)
print(a(math.pow))

