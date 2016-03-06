# _*_ coding=utf-8 _*_
from functools import wraps
import random
import time

__author__ = 'patrick'

def fn_timer(function):

    @wraps(function)
    def function_timer(*args,**kwargs):
        t0=time.time()
        result=function(*args,**kwargs)
        t1=time.time()
        print "total time used %s:%s seconds"%(function.func_name
                                               ,str(t1-t0))
        return result

    return function_timer

@fn_timer
def random_sort(n):
    return sorted([random.random() for i in range(n)])

random_sort(20000)

if __name__ == '__main__':
    random_sort(10000)