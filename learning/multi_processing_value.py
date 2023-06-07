from multiprocessing import Process, Value, Array, Lock
import os
import time


def add_100(number, lock):
    for i in range(100):
        lock.acquire()
        number.value += 1
        time.sleep(0.01)
        lock.release()


def square_numbers():
    for i in range(100):
        i * i


# Define multiple (10) threads
if __name__ == "__main__":

    lock = Lock()
    shared_number = Value('i', 0)
    print('Number at beggining is', shared_number.value)

    p1 = Process(target=add_100, args=(shared_number, lock))
    p2 = Process(target=add_100, args=(shared_number, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Number at end is', shared_number.value)