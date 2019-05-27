"""
thread and event simple example
event = threading.Event()
event.set()  #set flag
event.is_set()   #check the flag to be set
event.clear   #clear the flag
event.wait()   #wait for the flag to be set
"""
import threading
import time
import random

event = threading.Event()


def flag():
    print('In flag, sleep for 1 second')
    time.sleep(1)
    print('Event is set and sleep 5 seconds')
    event.set()
    time.sleep(5)
    print('Event is cleared')
    event.clear()


def operation():
    total_try_count = 0
    guess_right_count = 0
    print('In operation, wait for event to be set')
    event.wait()
    while event.is_set():
        print('Guess a number between 1 and 10. Is it 5?')
        total_try_count += 1
        if random.randint(1, 10) == 5:
            guess_right_count += 1
            print('Finally, got 5')
    print('Event was cleared, operation is done!')
    print(f'Out of {total_try_count} tries, {guess_right_count} times our guess is right. '
          f'Percentage is {guess_right_count / total_try_count * 100}%')


t1 = threading.Thread(target=flag)
t2 = threading.Thread(target=operation)

t1.start()
t2.start()

