# _*_ coding=utf-8 _*_
__author__ = 'patrick'

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
s1 = set(['Adam', 'Paul'])
for x in s:
    print x[0],":",x[1]

L = ['Adam', 'Lisa', 'Bart', 'Paul']

for item in L:
    if item in s1:
        s1.remove(item)

print s1

