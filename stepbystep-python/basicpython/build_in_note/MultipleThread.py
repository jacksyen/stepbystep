# -*- coding:utf-8 -*-

'''使用thread模块的例子'''
import thread
def worker1():
    '''thread worker function'''
    print 'Worker'
thread.start_new_thread(worker1)


'''使用threading模块的例子'''
import threading
def worker2():
    """thread worker function"""
    print 'Worker'
t = threading.Thread(target=worker2)
t.start()

'''或者Java Style'''
class worker3(threading.Thread):
    def __init__(self):
        pass
    def run(self):
        """thread worker function"""
        print 'Worker'
t = worker3()
t.start()
