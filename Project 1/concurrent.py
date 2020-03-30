from threading import Thread

import Project1 as p1
import Project1Chaining as p2


def main():
    t1 = Thread(target=p1)
    t2 = Thread(target=p2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


main()
