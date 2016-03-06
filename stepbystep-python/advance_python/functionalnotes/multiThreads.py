# _*_ coding=utf-8 _*_
from Queue import Queue
from random import randint
from time import sleep

__author__ = 'patrick'

from myThread import MyThread

def writeQ(queue):
    print 'producting object for Q ...'
    queue.put('xxx','input')
    print "size now",queue.qsize()


def readQ(queue):
    val = queue.get(1)
    print 'consumed object from Q... size now', queue.qsize()

def write(queue,loops):
    for i in range(loops):
        write(queue)
        sleep(randint(1,3))

def reader(queue,loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2.5))

func =[write,reader]
nfuncs = range(len(func))

def main():
    nloops =randint(2,5)
    q = Queue(32)

    threads =[]

    for i in nfuncs:
        t = MyThread(func[i], (q,nloops),func[i].__name__)
        threads.append(t)
    for i in nfuncs:
        threads[i].start()
    for i in nfuncs:
        threads[i].start
    for i in nfuncs:
        threads[i].join()
    print("all done")

if __name__=='__main__':
    main()