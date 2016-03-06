# _*_ coding=utf-8 _*_
__author__ = 'patrick'

print ('adam')
print ('adam',)

t = ('adam')
print t
t = ('adam',)
print t

print type(t)
# mututable tuple
t = (1, 2, [3, 4])
print t
l = t[2]
l[0] = 6
l[1] = 7

print t

m = (1, 2, (3, 4))
try:
    m[0] = 23
except Exception:
    print Exception.message

print m