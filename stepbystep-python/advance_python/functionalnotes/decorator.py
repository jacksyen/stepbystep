# _*_ coding=utf-8 _*_
__author__ = 'patrick'

def deco_functionNeedDoc(func):
    if func.__doc__ == None:
        print func,"has no __doc__,bad habit"
    else:
        print func,":",func.__doc__,'.'

    return func

@deco_functionNeedDoc
def f():
    print 'f() do something'

f()

@deco_functionNeedDoc
def g():
    '''I have a __doc__'''
    print 'g() do something'

g()
