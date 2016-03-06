# _*_ coding=utf-8 _*_
__author__ = 'patrick'


def dump(value):
    print value, "=>", dir(value)

import sys

dump(0)
dump(1.0)
dump(0.0j)
dump([])
dump({})
dump("string")
dump(len)
dump(sys)


class A():

    def __init__(self):
        pass

    def a(self):
        pass

    def b(self):
        pass


class B(A):
    def c(self):
        pass

    def d(self):
        pass


def get_members(klass, members=None):
        # get a list of all class members
        if members is None:
            members=[]
        for k in klass.__bases__:
            get_members(k,members)
        for m in dir(klass):
            if m not in members:
                members.append(m)
        return members

print get_members(A)
# include a members
print get_members(B)
print get_members(IOError)

# 每个变量当前值
print vars()
