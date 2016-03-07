"""
1. Constructor Calls
2. __new__() vs __init__()
3. static field
"""


class Foo(object):
    x = "a"
    count = 0

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(self.name,  'deleted')
        Foo.count -= 1
        if Foo.count == 0:
            print('last counter object deleted')
        else:
            print(Foo.count, 'counter objects remaining')

    # def __repr__(self):
    #     if self.name is None:
    #         self.name = 'None'
    #     self.name


# print(Foo.x)
# print(Foo('name').x)
# a = Foo('name')
# a.x = 'd'
# print(a.x)  # instance level x
# Foo.x = 'd'  # class level x
# print(a.x)
# print(Foo.x)

foo = Foo('name')
del foo

"""
1. __del__ invoked when program ending
2. __del__ invoked when del is called
"""
