# _*_ coding=utf-8 _*_
__author__ = 'patrick'

s = '3'
s1 = "test"
print type(s)
print type(s1)

# operator of String
print s + s1


def join(o, s, seperator):
    return str(o) + seperator + str(s)

print join(4,"45",",")

print "我好高兴"

print "%s %s" % (s, s1)
print len(s)


