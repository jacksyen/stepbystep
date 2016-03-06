# _*_ coding=utf-8 _*_
__author__ = 'patrick'

s = "hello world"
a = []
print type(a)

a.append(s)

print(a)

a.append("patrick")
a.append("simon")
a[len(a):]=["Test"] # equivalent to
a[len(a):]="Test"  # the difference

print a

print a.pop() # the last element
print a


b = ["123",35,4567]
a.extend(b)

print a
print b

print a.count(35) # not existing ,raise error
print a.count("patrick")
print a.count("simon")
print a.index(35)
print a.index('simon')

print range(9)
print range(1,9)
print range(0,9,2)
print range(0,-9,-2)

a.sort(reverse=True)
print a


matrix = [[1,2,3],[4,5,6],[12,34,45]]
print matrix[0][1]

t = "hello world"
print t.split(" ")

print ",".join(a)