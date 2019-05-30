"""
Demo the usage for threading.Lock to lock an object
There are two ways to use it:
1. using: 'with' statement
2. using lock.acquire() and lock.release()
"""
import threading

x = 0
count = 100000
try_count = 30
not_zero_count = 0
lock = threading.Lock()


def adding_two():
    global x
    for _ in range(count):
        with lock:
            x += 2


def adding_three():
    global x
    for _ in range(count):
        with lock:
            x += 3


def subtracting_one():
    global x
    for _ in range(count):
        lock.acquire()
        x -= 1
        lock.release()


def subtracting_four():
    global x
    for _ in range(count):
        lock.acquire()
        x -= 4
        lock.release()


for _ in range(try_count):
    t1 = threading.Thread(target=adding_two)
    t2 = threading.Thread(target=adding_three)
    t3 = threading.Thread(target=subtracting_four())
    t4 = threading.Thread(target=subtracting_one())

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print(x)
    if x != 0:
        not_zero_count += 1

print(f'Out of {try_count} try, there are {not_zero_count} times the result is not zero' )


