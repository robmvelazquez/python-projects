from threading import Thread, Lock
import time
# This program demonstrates the usage of threads and locks in Python.

database_value = 0  # Define global variable to simulate a stored value in a database.


def increase(lock):  # Defines target function for the threads with 'lock' argument
    global database_value

    with lock:  # Ensures thread safety
        local_copy = database_value  # Creates local copy of the database_value variable
        local_copy += 1
        time.sleep(0.1)  # Simulates processing
        database_value = local_copy


if __name__ == "__main__":

    main_lock = Lock()  # Initializes lock object
    print('Start value =', database_value)

    thread1 = Thread(target=increase, args=(main_lock,))
    thread2 = Thread(target=increase, args=(main_lock,))
    thread3 = Thread(target=increase, args=(main_lock,))

    # Start initiates thread execution
    thread1.start()
    thread2.start()
    thread3.start()

    # Join blocks the main thread until each thread has completed its execution.
    thread1.join()
    thread2.join()
    thread3.join()

    print('End value =', database_value)
