from abc import ABCMeta
from collections import Iterator
from setuptools.compat import unicode

__author__ = 'patrick'


# “if it's not a penguin it must be a duck”
# abstract bases for improved duck typing

class MyIter(object):
    def __iter__(self):
        return self

    def __next__(self):
        return 42


print(isinstance(MyIter(), Iterator))  # true


# Custom Duck

class Markedup(object):
    __metaclass__ = ABCMeta

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Markedup:
            if hasattr(C, "__html__"):
                return True
        return NotImplemented


class Markup(unicode):
    def __html__(self):
        return self


print(isinstance(Markup('test'), Markedup))  # False
