from _collections_abc import Iterator

__author__ = 'patrick'


class Foo(object):
    def __iter__(self):
        return self

    def next(self):
        return 42


foo = Foo()
print(isinstance(foo, Iterator))
print(foo.next())
print(foo.next())
