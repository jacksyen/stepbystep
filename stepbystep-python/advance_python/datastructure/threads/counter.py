# _*_ coding=utf-8 _*_
import random
import threading
import time

__author__ = 'patrick'


class Counter():
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def increament(self):
        """
        :type self: object
        """
        self.lock.acquire()
        self.value += 1
        self.lock.release()
        return self.value


counter = Counter()


class Worker(threading.Thread):
    def run(self):
        for i in range(10):
            value = counter.increament()
            time.sleep(random.randint(10, 100) / 100)
            print self.getName(),value

for i in range(10):
    Worker().start()