# Justin Rodriguez
# Project 1: Hash Table with chaining
# CS 5352: Advanced Operating systems
import random
import time
import psutil
import os
import pandas as pd
from tabulate import tabulate


# Function to get time it takes for function to complete its task
# Taken from: https://stackoverflow.com/questions/5478351/python-time-measure-function
def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('{:s} function took {:.3f} ms to complete'.format(f.__name__, (time2 - time1) * 1000.0))

        return ret

    return wrap


hash_list = [[] for _ in range(50000)]
print(hash_list)
len_hash = len(hash_list)


def hashFunc(item, size):
    return item % size

@timing
def insert(hashlist):
    for item in hashlist:
        idx = hashFunc(item, len_hash)
        hash_list[idx].append(item)


def displayHash(hashtable):
    for i in range(len(hashtable)):
        print("Bucket number: " + str(i), end=" ")

        for j in hashtable[i]:
            print("-->", end=" ")
            print(j, end=" ")
        print()


# System level information
pid1 = os.getpid()
p = psutil.Process(pid1)

def sysinfo1():
    memory = p.memory_info()
    print(memory)
    print("CPU Usage Percent: " + str(p.cpu_percent()) + "%")
    io = p.io_counters()
    print(io)

# Print initial system level info
print("~" * 300)
print("Initial System Level Information:")
sysinfo1()
print("~" * 300 + "\n")


@timing
def main():
    to_hash = random.sample(range(1, 10000000), 1000000)  # Generate list of 1000000 numbers to be stored in hashtable
    insert(to_hash)  # add list of number to our hashtable
    # displayHash(hash_list)
    # Print System level info after program completes tasks
    print("~" * 300)
    print("System Level Information After Program Completion")
    sysinfo1()
    print("~" * 300 + "\n")


main()
