__author__ = 'patrick'

@macro
def add(a,b):
    return a+b

@macro
def times(i):
    for __x in range(i):
        __body__

def doing_something():
    a=add(1,2)
    with times(10):
        print('iterating......')