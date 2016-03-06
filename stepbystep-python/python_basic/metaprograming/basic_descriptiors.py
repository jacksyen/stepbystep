__author__ = 'patrick'


class Foo(object):
    def my_function(self):
        pass

    @property
    def foo(self):
        return "hello pycon"

print(Foo.my_function)

print(Foo.__dict__['my_function'])
print(Foo.__dict__['my_function'].__get__(None, Foo))
print(Foo.__dict__['my_function'].__get__(Foo(), Foo))

print(Foo().my_function)

print(Foo().foo)
