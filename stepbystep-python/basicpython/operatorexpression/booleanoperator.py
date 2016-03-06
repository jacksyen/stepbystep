# _*_ coding=utf-8 _*_
__author__ = 'patrick'

t = True
f= False
a =0
b= 1
c = -1
d = 12

print a and b
print t and f
print a and c
print (d and c)
if d and c:
    print True

if b and c:
    print True

if a and c:
    print True
else:
    print False

if a or c:
    print True

if not(a or c):
    print False
else:
    print True