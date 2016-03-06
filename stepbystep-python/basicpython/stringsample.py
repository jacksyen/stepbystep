# _*_ coding=utf-8 _*_
__author__ = 'patrick'


print "this is \"this is \""

a = 5
print type(a)

b = "hello world"

print type(b)
print len(b)
print b.upper()
print b.lower()
print b.capitalize()
print b.istitle()
print b.title().istitle()

print "one is %d" %a
print "%s%s" %(a,b)

s = "hello world"
print s[1]
print s[-3]
print len(s)

for n in s:
    print n
