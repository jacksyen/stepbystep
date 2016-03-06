# /usr/bin python
# _*_ coding=utf-8 _*_
from __future__ import division
import random
__author__ = 'patrick'

a=[random.randint(0,100) for i in range(40)]
print(len(a))
print(a)

a.sort(reverse=True)
sorted(a,reverse=True)
print(a)

def get_average_num(a):
  average_num = sum(a)/len(a)  # todo to understand why here is using float
  print(average_num)
  return [i for i in a if i > average_num]

if __name__=="__main__":
    print(get_average_num(a))
