# _*_ coding=utf-8 _*_
__author__ = 'patrick'

s1 = set("testset")
print(type(s1))
print s1

s2 = set([123,"google","face"])
print s2

s3={"book",123}
print(type(s3))
s3.add("name")
print s3
print type(s3)
s3.pop() # remove not mutable
print s3

# set {}
# list []
# dic ()
a_set ={}
#a_set.add("name")
print(type(a_set))
print a_set

f_set = set("testing")  # no duplicated
f_set.add("python")
print  f_set

# equal, set subset
b_set=set("se")
print b_set.issubset(f_set)

print "中国"
