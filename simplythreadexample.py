"""
show one way to use thread: create a class extend thread class
"""
import threading
import time

print_lock = threading.Lock()


class Messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            time.sleep(0.1)
            with print_lock:
                print(threading.current_thread().getName(), time.time())


sender = Messenger(name='sender')
receiver = Messenger(name='receiver')

sender.start()
receiver.start()
print('send.is_aline()', sender.is_alive())
print('receiver.is_aline()', receiver.is_alive())
sender.join()
receiver.join()
print('after join() method is called')
print('send.is_aline()', sender.is_alive())
print('receiver.is_aline()', receiver.is_alive())
