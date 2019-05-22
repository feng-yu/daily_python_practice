"""
This is a complicate thread example, using queue, threading, etc
"""
import threading
from queue import Queue
import time

"""
get a lock first
"""
print_lock = threading.Lock()
q = Queue()


def exampleJob(worker):
    time.sleep(0.5)

    with print_lock:
        print(threading.current_thread().getName(), worker)


def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()


for _ in range(10):
    t = threading.Thread(target=threader, daemon=True)
    t.start()

start = time.time()

for worker in range(20):
    q.put(worker)

q.join()
print('Entir job takes: ' + str(time.time() - start) + ' seconds')