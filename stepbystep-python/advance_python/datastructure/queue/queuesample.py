# _*_ coding=utf-8 _*_
import Queue
import random
import threading
import time

__author__ = 'patrick'

WORKERS = 2


class Worker(threading.Thread):
    def __init__(self, queue):
        self._queue = queue
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            item = self._queue.get()
            if item is None:
                break
            time.sleep(random.randint(10, 100) / 100.0)
            print "task", item, "finished"


queue = Queue.Queue(2)

for i in range(WORKERS):
    Worker(queue).start()

for i in range(8):
    print "push", i
    queue.put(i)

for i in range(WORKERS):
    print "push", "NONE to", i
    queue.put(None)