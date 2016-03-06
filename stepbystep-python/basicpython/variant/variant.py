# _*_ coding=utf-8 _*_
__author__ = 'patrick'

a = 0
b = "s"

print(b)
print a
print str(a)+b


# 对象类型	举例
# int/float	123, 3.14
# str	'qiwsir.github.io'
# list	[1, [2, 'three'], 4]
# dict	{'name':"qiwsir","lang":"python"}
# tuple	(1, 2, "three")
# set	set("qi"), {"q", "i"}

a_set ={"abcd"}
print a_set
a_set.add("123")
print len(a_set)
print a_set

# 变量无类型，对象有类型

x=2
y=2
print x==y
print x is y

x=200000
y=200000
print x==y
print x is y