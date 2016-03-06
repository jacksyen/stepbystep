# _*_ coding=utf-8 _*_
__author__ = 'patrick'

t = 123, "abc", ["name", "test"]
print type(t)
try:
    t[0] = 334
except TypeError, e:
    print e.message
    print e.args
print t

print len(t)
print t[2]

for k in t:
    print k

# like list/str
print(t[1][0])
print(t[2][1])

print list(t)
for element in list(t):
    print "element:"+str(element)

print tuple(t)
temp = tuple(t)
try:
    print dict(temp) # TypeError, can't convert tuple to dict
except TypeError, e:
    print e.message

# tuple where to use?
# tuple is quicker than list, used to iterate
# tuple used in as key in dict, but list can't,so tuple immutable??
# yes tuple is immutable, but tuple can include list which is mutable, it is not safe
# only tuple without list, safe to use as key if dictionary

d = {("abcd", 123): "test"}
try:
    d = {["abcd",123]:"test"}
except TypeError, e:
    print e

print type(d)

