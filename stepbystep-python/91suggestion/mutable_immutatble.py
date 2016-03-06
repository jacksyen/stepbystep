# _*_ coding=utf-8 _*_
__author__ = 'patrick'

my_list =[1,2,3,4]
my_list[0]=5
print my_list

x = 6
x = x +1
print x

# bad example :
nums =""
for n in range(20):
    nums =nums+str(n)

mu =[]
for my in range(20):
    mu.append(str(my))

print "".join(mu)


foo = 'foo'
bar = 'bar'
foobar = foo + bar # This is good
foo += 'ooo' # This is bad, instead you should do: foo = ''.join([foo, 'ooo'])
print foo

foo = 'foo'
bar = 'bar'
foobar = '%s%s' % (foo, bar) # It is OK
foobar = '{0}{1}'.format(foo, bar) # It is better
foobar = '{foo}{bar}'.format(foo=foo, bar=bar) # It is best
print foobar