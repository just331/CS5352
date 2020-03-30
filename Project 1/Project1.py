# Justin Rodriguez
# Project 1
# CS 5352: Advanced Operating systems
import random
import time
import psutil
import os

pid = os.getpid()
p = psutil.Process(pid)


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


class Hashtable:
    def __init__(self):
        self.size = 50000  # int(input("Enter the size of the hash table: "))
        self.table = list(0 for i in range(self.size))
        self.count = 0
        self.comp = 0

    def isFull(self):
        if self.count == self.size:
            return True
        else:
            return False

    def hashFunc(self, element):
        return element % self.size

    def collisionRes(self, element, position):
        found = False
        limit = 50
        i = 1
        while i < limit:
            newPos = position + (i ** 2)
            newPos = newPos % self.size
            if self.table[newPos] == 0:
                found = True
                break
            else:
                i += 1
        return found, newPos

    def add(self, element):
        if self.isFull():
            return False
        stored = False
        position = self.hashFunc(element)

        if self.table[position] == 0:
            self.table[position] = element
            stored = True
            self.count += 1

        else:
            # print("Collision has occured for element " + str(element) + " at position " + str(
            #    position) + " finding new position.")
            stored, position = self.collisionRes(element, position)
            if stored:
                self.table[position] = element
                self.count += 1
        return stored

    def display(self):
        print("\n")
        for i in range(self.size):
            print(str(i) + " = " + str(self.table[i]))
        print("Number of elements in table are: " + str(self.count))


@timing
def testHash1(inputlist):
    table = Hashtable()
    for item in inputlist:
        table.add(item)
    # table.display()
    # print()


def sysinfo():
    memory = p.memory_info()
    print(memory)
    print("CPU Usage Percent: " + str(p.cpu_percent()) + "%")
    io = p.io_counters()
    print(io)


print("~" * 300)
print("Initial System Level Information:")
sysinfo()
print("~" * 300 + "\n")


@timing
def main():
    toHash = random.sample(range(1, 10000000), 1000000)
    testHash1(toHash)
    print("~" * 300)
    print("System Level Information After Program Completion:")
    sysinfo()
    print("~" * 300 + "\n")


main()
