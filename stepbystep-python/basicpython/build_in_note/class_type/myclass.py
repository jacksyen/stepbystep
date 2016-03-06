# _*_ coding=utf-8 _*_
__author__ = 'patrick'


class MyClass(object):
    common = 10

    def __init__(self):
        self.myvariable1 = 3

    def my_function(self, arg1, arg2):
        return self.myvariable1


class1= MyClass()
print class1.common
class2=MyClass()
print class2.common

print class1.my_function(1,2)
print class2.my_function(9,2)
