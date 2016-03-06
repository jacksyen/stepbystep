# _*_ coding=utf-8 _*_
import random
__author__ = 'patrick'

print dir(random)

print random.randint(0,99)
print random.randrange(0,100,2)
print random.uniform(1,10)
print random.choice("test")

items = [1,2,3,4,5]
random.shuffle(items)
print(items)