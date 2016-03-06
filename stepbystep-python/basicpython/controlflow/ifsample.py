# _*_ coding=utf-8 _*_
import random

__author__ = 'patrick'

numbers = [random.randint(100,1000) for i in range(20)]
print numbers

odd = [o for o in numbers if o%2!=0]
even = [o for o in numbers if o%2==0]

print odd
print even

name ="patrick" if "p" else "patric"
print name

# it look like (expression)?true:false
name ="patrick" if "" else "patric"
print name



