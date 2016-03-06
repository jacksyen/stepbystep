# _*_ coding=utf-8 _*_
__author__ = 'patrick'

# 单行注释
"""
    多行注释
"""

######################################
# 1. 基本数据类型和操作符
######################################

# 数字
print 3  # => 3

# 数学运算
print 1 + 1
print 8 - 1
print 10 * 2
print 35 / 5
"""
 取自动向下取小于结果的最大整数
"""
print 11 / 4
print 2.0
print 5.0 / 2.0
# 使用括号提高优先级
print (1 + 3) * 2

# boolean
print True
print False
print not True
print not False

# 相等比较==,!=,<,>,<=,>=
print 1 == 1
print 2 == 1
print 2 != 1
print 1 < 10
print 1 > 10
print 2 <= 10
print 2 >= 10
# 比较操作可以串接
print 1 < 2 < 3  # True
print 2 < 3 < 2  # False

# 可以使用”或“创建字符串
print "This is a String"
print "hello" + "world"
print "This is String"[0]

# None是个对象
print None

##########################
## 2. 变量与数据容器
##########################

# print
print "I am Python.Nice to meet you"

# 赋值之前不需要声明变量
some_var = 5
print some_var

# 访问之前未赋值的变量会产生异常
try:
    some_other_var
except NameError:
    print "Raises a name error"

# 赋值时可以使用条件表达式
a = 1
b = 23
some_var = a if a > b else b
print some_var

# 列表用于存储数据序列
li = []
other_li = [4, 5, 6]
li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.append(5)
print li
print other_li
# pop 从列表末尾删除数据
li.pop()
print li
print li[0]
print li[-1]

try:
    li[4]
except IndexError:
    print "Raises an IndexError"

# 可以通过分片(slice)语法查看列表摸个区间的数据
# 这是个闭合/开放区间
print li[1:3]
print li[1:]
print li[:3]

# 删除任意元素
del li[2]
print li

li = li + other_li
print li
li.extend(other_li)
print li
print 1 in li
print len(li)

# 元组类似列表 但是不可变
tup = (1, 2, 3)
print tup[0]
try:
    tup[0] = 3
except TypeError:
    print "Tuples cannot mutated"

# 可以在元组上使用和列表一样的操作
len(tup)
print tup + (4, 5, 6)
print tup[:2]
print 2 in tup

# 可以将元组分解包到变量
a, b, c = (1, 2, 3)
print a, b, c
a, b = b, a
print a, b

# dict
empty_dict = {}
filled_dict = {"one": 1, "two": 2, "three": 3}
print filled_dict
print filled_dict["one"]

print filled_dict.keys()
print "one" in filled_dict
print "1" in filled_dict
print filled_dict.get("one")
print filled_dict.get("test", 4)
filled_dict.setdefault("four", 4)
filled_dict.setdefault("five", 5)
print filled_dict

# 集合 set
empty_set = {}
filled_set = set([1, 2, 3, 4, 5, 6])

# & 集合交集
other_set = set([1, 7, 8, 9])
print filled_set & other_set
# | 集合合并
print filled_set | other_set

# -  执行集合差操作
print filled_set - other_set

# in
print 2 in filled_set
print 10 in other_set

#####################################
## 3. control flow
#####################################
some_var = 5
if some_var > 10:
    print "some_var is totally bigger than 10"
elif some_var < 10:
    print "some_var is smaller than 10"
else:
    print "some_var is indeed 10"

for animal in ["dog", "cat", "mouse"]:
    # % 格式化
    print "%s is a mammal" % animal

x = 0
while x < 4:
    print x
    x += 1

# try/catch
try:
    raise IndexError("This is an index error")
except IndexError as e:
    pass

try:
    raise IndexError("this is an index error")
except IndexError, e:
    pass

###########################
## 4.Function
###########################
# create function
def add(x, y):
    print "x is %s and y is %y"
    return x + y

# call function
print add(4, 19)
print add(x=10, y=11)

# 可变数量参数
def varargs(*args):
    return args


print varargs(1, 2, 3)
x, y, z = varargs(1, 2, 3)
print x, y, z


# 也可以接受可变数量关键字参数的函数
def keyword_args(**kwargs):
    return kwargs


print keyword_args(big="foot", loch="ness")


def all_the_args(*args, **kwargs):
    print args
    print "\n"
    print kwargs


arg1 = (1, 2)
key_args1 = {"a": 3, "b": 4}
all_the_args(arg1, key_args1)


# python 一等函数
def create_adder(x):
    print x

    def adder(y):
        print y
        return x + y

    return adder


add_10 = create_adder(10)
print add_10(3)



