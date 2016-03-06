# _*_ coding=utf-8 _*_
__author__ = 'patrick'

# python type: int/str/bool/list/dict/tuple
# set
s1 = set("hello world")
print s1

s2 = {"test.com", 123}
print s2

# sorted
s3 = set([123, "google.com", "baidu.com", "163.com"])
print s3

# can't init set with list
try:
    s4 = {"google.com", [1, 234], 123}
except TypeError, e:
    print e.message

print list(s1)[0]
print dir(set)

#'add', 'clear', 'copy', 'difference', 'difference_update', 'discard'
# , 'intersection', 'intersection_update', 'isdisjoint', 'issubset',
# 'issuperset', 'pop',
# 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

a_set = {"acd","ppo"}
print type (a_set)
print a_set.add("test")
print a_set.add('[1,2,3,4,5,6]')
print type('[1,2,3,4,5,6,7]')
print a_set

# frozen set
f_set = frozenset("hello world")
print f_set
try:
    f_set.add("1234R")               #br AttributeError
except AttributeError, error:
    print error


u_set ={"123","testert","[123,334,556]"}
print "123" in u_set
a_set = {"github"}
b_set ={"github"}
print a_set==b_set
b_set.add("hello")
print a_set==b_set
print a_set in b_set
print a_set.issubset(b_set)
print b_set.issuperset(a_set)
print a_set.union(b_set)
print a_set.intersection(b_set)
print a_set and b_set
print a_set.difference(b_set)
print b_set.difference(a_set)
