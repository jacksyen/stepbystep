# _*_ coding=utf-8 _*_
from functools import partial
from operator import mul

__author__ = 'patrick'

def create_mulipliers():
  return [lambda x : i * x for i in range(5)]

for n in create_mulipliers():
    print n(2)

# explain why
def create_multipliers_another():
    muls=[]
    for i in range(5):
        def multuplier(x):
            return i*x
        muls.append(multuplier)
    return muls

for n in create_multipliers_another():
    print n(2)

def create_multipliers():
    return [lambda x,i=i:i*x for i in range(5)]

for n in create_multipliers():
    print n(4)

def functools_create():
    return [partial(mul,i) for i in range(5)]

for t in functools_create():
    print t(3)