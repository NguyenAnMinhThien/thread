# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import numpy as np
#
# def increase_by_one(array):
#     array += 1
#
# data = np.ones((100,1))
# increase_by_one(data)
# import threading
# from threading import Thread
# print(data[0])
# # the array is muttable, so, it can be changed and no need to return value, that value later is used continued in another Thread
# t = Thread(target=increase_by_one, args=(data,))
# t.start()
# t.join()
# print(data[0])
# from time import sleep
#
# def print_numbers(number, delay=1):
#     for i in range(number):
#         print(i)
#         sleep(delay)
#
# from threading import Thread
# t = Thread(target=print_numbers, args=(10,), kwargs={'delay': .2})
# t.start()
# # this command is excuted in main thread, so it not effected by the delay of print_number function
# print('Thread started')
# # after join(), only one thread remain , mean, when the interpreter catch in this statement, it will wait for t thread finished and join with main thread .
# t.join()
# print('Thread finished')
# in this case, it is CPU bound, so, the using thread is not efficently , but if it is IO bound, the CPU have the time to sleep so the switch will be efficently.
#
from threading import Thread
import numpy as np
#
#
# def increase_by_one(array):
#     for i in range(30000):
#         array += 1
#
#
# def square(array):
#     for i in range(30000):
#         array /= 1.1
#
#
# data = np.ones((100, 1))
#
# t = Thread(target=increase_by_one, args=(data,))
# t2 = Thread(target=square, args=(data,))
# t.start()
# t2.start()
# t.join()
# t2.join()
# print(data[0])
# print(np.mean(data))
# prove the order of operation is not corrected:
def increase_by_one(array):
    with lock:
        for i in range(len(array)):
            array[i] += 1

def divide(array):
    with lock:
        for i in range(len(array)):
            array[i] /= 1.1


# t = Thread(target=increase_by_one, args=(data,))
# t2 = Thread(target=divide, args=(data,))
# t.start()
# t2.start()
# t.join()
# t2.join()
# print(np.max(data))
#lock.acquire()
from threading import Lock

lock = Lock()
# In this case, the Threads are excuted in synchronized , but the first Threads is excuted is decided by OS, why
# lock.acquire()
# data = np.ones((100000,1))
# t = Thread(target=increase_by_one, args=(data,))
# t2 = Thread(target=divide, args=(data,))
# t2.start()
# t.start()
# print('Threads are still not running')
# data += 10
# increase_by_one(data)
# lock.release()
# t.join()
# t2.join()
lock.acquire()
data = np.ones((100000,1))
t = Thread(target=increase_by_one, args=(data,))
t2 = Thread(target=divide, args=(data,))
t2.start()
t.start()
increase_by_one(data)
lock.release()
print(np.max(data))
print(np.min(data))
