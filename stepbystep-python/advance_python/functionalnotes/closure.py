# _*_ coding=utf-8 _*_
__author__ = 'patrick'

from time import time

# 闭包
def count(start_at=0):
    count = [start_at]

    def incr():
        count[0] += 1
        return count[0]

    return incr


def logged(when):
    def log(f, *args, **kwargs):
        print("called: \n" \
              "function: %s \n" \
              "args:%r kwargs:%s" %(f,args,kwargs))

    def pre_logged(f):
        def wrapped(*args,**kwargs):
            log(f,args,kwargs)
            return f(*args,**kwargs)
        return wrapped

    def post_logged(f):
        def wrapped(*args,**kwargs):
            now =time()
            try:
                return f(*args,**kwargs)
            finally:
                log(f,*args,**kwargs)
                print("time delta:%s" %(time()-now))
        return wrapped()

    try:
        return {"pre":pre_logged,"post":post_logged}[when]
    except KeyError as e:
        raise ValueError(e,'must be "pre" or "post"')

@logged("post")
def hello(name):
    print("hello ,",name)

hello("patrick")