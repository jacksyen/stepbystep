# _*_ coding=utf-8 _*_
__author__ = 'patrick'

# list and str different str is immutable
a= "this is test"
b =["this","is","test"]
print a
print b
print len(a)
print len(b)

print a[0]
print b[0]

# error
try:
    a.append("test again")
except AttributeError, error:
    print error.args


b.append("test again")

# 多维
matrix = [[1,2,3],[4,5,6]]
print matrix
print matrix[0]
print matrix[0][1]

# len is 2
print len(matrix)

# a= a.split(" ")
a= a.split()
print type(a)

print a

# join with ","
print ",".join(a)

