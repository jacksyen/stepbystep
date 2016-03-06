# _*_ coding=utf-8 _*_
__author__ = 'patrick'

a = []
print type(a)

print len(a)

a.append(12)

print len(a)

# 列表无限大
a.append("12")
a.append("test")

print len(a)

for o in a:
    print o

print a

print a[1]
a[len(a):] = [990]
print a

# append /extend
# append object to list
a.append(["abc", "deb"])
print a
print len(a)
# extend the list
a.extend(["a", "b"])
print a
print len(a)

# list.count(object)
la = [1,11,23,22,22,11,11,23]
print la.count(11)

# index of list
print la.index(11)
print la.index(11,5,10)

# try and except
try: 
    print la.index("abcd")
except ValueError, error:
    print error.args

# insert
a.insert(1, 567)
print a
print len(a)
# remove
a.remove(567)
print len(a)
print a
try:
    a. remove(4444)
except ValueError, error:
    print error.args
    print error

# pop
a.pop(0)
a.pop(len(a)-1)
print a
print a.pop() # last one of the list
print a

# iterator of list
print a.__iter__()
print dir(a)
a.sort()
print a

# range
print range(9)
print range(0,9,3)
print type(range(10))
print range(-10,1,1)

# sort for list
num = [1, 3,4,56,778,554,345,34,455,44]
num.sort()
print num
sorted(num, reverse=True) ## todo why not sorted as expected
print num
num.sort(reverse=True)
print num
