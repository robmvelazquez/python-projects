from threading import Thread
from multiprocessing import Process
import os
import time

# This function will allow us to view the Python thread running in Task Manager
def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

# Define multiple (10) threads
if __name__ == "__main__":
    threads = []
    num_threads = 10

# Create threads and define target (square_numbers)
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

# Start
for thread in threads:
    thread.start()

# Join = wait for threads to finish execution before printing 'End main'.
for thread in threads:
    thread.join()

print('End main')

"""
# Processes

processes = []
num_processes = os.cpu_count()

# Create processes
for i in range(num_threads):
    p = Process(target=square_numbers)
    processes.append(t)

# Start
for p in processes:
    p.start()

# Join processes
for p in processes:
    p.join()

print('End main')
"""