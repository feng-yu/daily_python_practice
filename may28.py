"""
[medium]
Implement a job scheduler which takes in a function f and an integer n,
and calls f after n milliseconds.
"""
import time
import threading


def f(name):
    print(f'Hello {name}')


def scheduler(target, args, delay):
    print(f'Sleep for {delay} milliseconds!')
    time.sleep(delay / 1000000)
    return target(args)


job = threading.Thread(target = scheduler,
                       daemon = True,
                       # args = (lambda: f('from new thread'), 1000))
                       args = (f, 'John', 1000))

print('Start')
job.start()
job.join()
print('End')


