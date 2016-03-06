from _collections_abc import Callable

__author__ = 'patrick'


def test():
    print("hello world")


print(isinstance(test,Callable))
print(isinstance(test(),Callable))
