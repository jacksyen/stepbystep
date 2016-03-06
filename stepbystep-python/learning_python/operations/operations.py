# _*_ coding=utf-8 _*_

from __future__ import division
__author__ = 'patrick'

a=4+2
b=4.0+2
# 自动处理整数溢出
x= 123456789870987654321122343445567678890098876*1233455667789990099876543332387665443345566999999999999

print a,b,x
print(type(a))
print(type(b))
print(type(x))


print a/b
print a/2
try:
    print a/2.0
    print x/0
except ZeroDivisionError as e:
    print e

print 5/2