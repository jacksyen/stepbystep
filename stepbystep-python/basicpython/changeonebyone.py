# _*_ coding=utf-8 _*_

from random import randint
__author__ = 'patrick'

a=[randint(0,10) for i in range(10)]
print(a)

def moveOneStep(a):
    b= a.pop(0)
    a.append(b)
    return a


if __name__=="__main__":
   print moveOneStep(a)