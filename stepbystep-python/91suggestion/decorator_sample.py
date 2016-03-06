# _*_ coding=utf-8 _*_
__author__ = 'patrick'


def foo():
    print "foo"


def decorator(func):
    print "decorator"
    return func


@decorator
def bar():
    foo()

bar
bar()