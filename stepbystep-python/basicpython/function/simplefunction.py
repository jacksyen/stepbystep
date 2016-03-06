# _*_ coding=utf-8 _*_
__author__ = 'patrick'

# todo python name convension
def add(a, b):
    c = int(a)+int(b)
    return c

print add(2, 3)
print add(2.0, 3)
print add(4, "s")

if __name__== "main":
    print add(5,10)