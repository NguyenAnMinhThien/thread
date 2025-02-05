import os
import psutil
import threading
import time
from concurrent.futures import thread, process

def print_info(value):
    time.sleep(1)
    print(
        f"THREAD: {threading.get_ident()}",
        f"PROCESS: {os.getpid()}",
        f"VALUE: {value}",
    )

def multithreading_logic(values):
    with thread.ThreadPoolExecutor() as multithreading_executor:
        multithreading_executor.map(
            print_info,
            values,
        )

def multiprocessing_executor():
    hehe = time.time()
    with process.ProcessPoolExecutor() as multiprocessing_executor:
        multiprocessing_executor.map( multithreading_logic, (range(1000 * x, 1000 * (x + 1)) for x in range(os.cpu_count())))
    haha = time.time()
    print(haha - hehe)
if __name__ == '__main__':
    multiprocessing_executor()