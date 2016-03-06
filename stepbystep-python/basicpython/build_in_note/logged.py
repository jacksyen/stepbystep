# -*- coding:utf-8 -*-
from time import time
'''一个日志装饰器'''
def logged(when):
    def log(f,*args,**kargs):
        print '''@ called:
    function: %s()
    args :%r
    kargs :%r
        '''%(f.__name__,args,kargs)

    def pre_logged(f):
        def wrapper(*args,**kargs):
            print '@ in pre_logged'
            return f(*args,**kargs)
        return wrapper

    def post_logged(f):
        def wrapper(*args,**kargs):
            print('@ in post_logged *')
            now =time()
            try:
                return f(*args,**kargs)
            finally:
                log(f,*args,**kargs)
                print('@ time delta: %ss' % (time()-now))
                print('@ in post_logged')
        return wrapper
    try:
        return {"pre":pre_logged,"post":post_logged}[when]
    except KeyError as e:
        raise ValueError(e)('@must be "pre" or "post" ')

@logged('pre')
@logged('post')
@logged('pre')
def hello(*args,**kargs):
    for i in range(10000000):
        k = i
    print "hello world"

hello('test',test='test')
'''
控制台输出如下:

@ in pre_logged
@ in post_logged *
hello world
@ called:
    function: hello()
    args :('test',)
    kargs :{'test': 'test'}

@ time delta: 0.412999868393s
@ in post_logged

'''
