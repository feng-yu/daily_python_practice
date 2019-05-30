"""
There are 3 types of queues:
1. FIFO (First In First out)
2. LIFO (Last in First Out)
3. Priority Queue
"""
import queue
import threading
import time

fifo_queue = queue.Queue()


def test_fifo(q):
    """Test the FIFO queue"""
    for i in range(5):
        q.put(i)

    while not q.empty():
        print(q.get())


def test_lifo():
    """Test the LIFO queue"""
    lifo_queue = queue.LifoQueue()

    for i in range(5):
        lifo_queue.put(i)

    while not lifo_queue.empty():
        print(lifo_queue.get())


def test_priority_queue():
    """Test the priority queue"""
    priority_queue = queue.PriorityQueue()
    priority_queue.put((4, 'Priority 4'))
    priority_queue.put((3, 'Priority 3'))
    priority_queue.put((5, 'Priority 5'))
    priority_queue.put((2, 'Priority 2'))
    priority_queue.put((1, 'Priority 1'))

    while not priority_queue.empty():
        print(priority_queue.get()[1])

def putting_thread(q):
    while True:
        print('Sleep 3 seconds and then put something into queue')
        time.sleep(3)
        q.put(5)
        print('Put "5" in the queue')


def test_putting_thread():
    t = threading.Thread(target=putting_thread, args=(fifo_queue, ), daemon=True)
    t.start()
    print('\nTrying to get something from queue')
    x = queue.get()
    print(f'\nGot {x} from queue')


test_priority_queue()
# test_lifo()
# test_fifo(fifo_queue)
# test_putting_thread()




