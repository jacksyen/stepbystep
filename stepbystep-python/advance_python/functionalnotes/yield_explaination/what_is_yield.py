# _*_ coding=utf-8 _*_
__author__ = 'patrick'

my_list = [1, 2, 3]

"""
iterator:迭代器，每次读取一个元素，
一般都有has_next(),next(),remove()方法
理解迭代的内部机制：

迭代(iteration）就是对可迭代对象
（iterables，实现了__iter__()方法）
和迭代器（iterators，实现了__next__()方法）的一个操作过程。
可迭代对象是任何可返回一个迭代器的对象，
迭代器是应用在迭代对象中迭代的对象，
换一种方式说的话就是：iterable对象的__iter__()
方法可以返回iterator对象，
iterator通过调用next()方法获取其中的每一个值(译者注)，
读者可以结合Java API中的 Iterable接口和Iterator接口进行类比。
"""
for my in my_list:
    print my

"""
迭代器用起来很方便但是也不是全部都是好处，因为my_list的数据必须预先在内存中
"""
my_list = [x * x for x in range(4)]
for my in my_list:
    print my

"""
generator:生成器同样也可以迭代对象，但是你只能读取一次，因为所有值
没有都放在内存，而是动态生成的
"""
my_generator = (x * x for x in range(4))
for my in my_generator:
    print my

print "start execute second time"
for my in my_generator:
    print my

"""
yield 类似于return,返回一个生成器
"""


def create_generator():
    items = range(4)
    for my in items:
        yield my * my * 2


my_generator = create_generator()
print my_generator
for x in my_generator:
    print x

"""
中间过程不能传递，复用性差
"""


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1


print fab(5)


def fab_list(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L

print fab_list(5)

for n in fab(5):
    print n

for my in range(1000):print my
"""
少内存,iterator
"""
for my in xrange(1000):print my

