import os
from threading import Thread
import time
import Project1
import Project1Chaining
import psutil


# Function to get time it takes for function to complete its task
# Taken from: https://stackoverflow.com/questions/5478351/python-time-measure-function
def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2 - time1) * 1000.0))

        return ret

    return wrap


def func1():
    print("Starting Project1.py")
    Project1.main()


def func2():
    print("Starting Project1Chaining.py\n")
    Project1Chaining.main()


# System level information
pid3 = os.getpid()
p = psutil.Process(pid3)


def sysinfo2():
    memory = p.memory_info()
    print(memory)
    print("CPU Usage Percent: " + str(p.cpu_percent()) + "%")
    io = p.io_counters()
    print(io)


print("~" * 300)
print("Initial System Level Information For Concurrent.py:")
sysinfo2()
print("~" * 300 + "\n")


@timing
def main():
    print("Starting threads:\n")
    t1 = Thread(target=func1)
    t2 = Thread(target=func2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Threads are now complete!\n")
    # Print System level info after program completes tasks
    print("~" * 300)
    print("System Level Information After Program Completion For Concurrent.py")
    sysinfo2()
    print("~" * 300 + "\n")

main()
