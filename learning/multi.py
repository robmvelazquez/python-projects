from threading import Thread
from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

threads = []
num_threads = os.cpu_count()

# Create processes
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

# Start
for t in threads:
    t.start()

# Join processes
for t in threads:
    t.join()

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