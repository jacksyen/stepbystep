# _*_ coding=utf-8 _*_
from __future__ import division
import math

print 5 / 2

print divmod(5, 2)
print divmod(10, 3)[0], divmod(10, 3)[1], divmod(10, 3)

print round(1.2345567, 2)
print round(1.23456677, 3)
print round(10.0 / 3, 4)

print math.pi
functions = dir(math)
print pow(4, 2)
for x in functions:
    print x
    print help(x)