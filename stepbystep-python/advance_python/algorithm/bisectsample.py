# _*_ coding=utf-8 _*_
import bisect
__author__ = 'patrick'

a = range(100)
a = sorted(a,reverse=True)
print(a)
def bisect_search(a,value):
    i = bisect.bisect_left(a,value)
    if i!=len(a) and a[i]==value:
        return i
    raise ValueError

print(bisect_search(a,30))
print(a[30])
