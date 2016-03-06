# _*_ coding=utf-8 _*_
__author__ = 'patrick'

# 高阶函数
# 能接受函数作为参数

f = abs

print f(-2)


def add(x, y, f):
    return f(x) + f(y)


print add(-5, 9, abs)

# map, 对列表里面的每一个元素进行操作

def format_name(s):
    return s[0].upper() + s[1:].lower()


print map(format_name, ['adam', 'lisa', 'barT'])

# reduce： 前后两个元素进行操作

def prod(x, y):
    return x * y


def prod_3(x, y):
    return x + y;


print reduce(prod, [2, 3, 4, 5, 6])

# filter 对每个条件进行过滤

def is_odd(x):
    return x % 2 == 1


print filter(is_odd, [1, 2, 3, 4, 5, 6, 8])

# sort

# 返回函数
def calc_prod(lst):
    def prod():
        def f(x, y):
            return x * y

        return reduce(f, lst, 1)

    return prod


f = calc_prod([1, 2, 3, 4, 5, 6])
print f()

# closure
def count():
    fs = []
    for i in range(1, 5):
        def f(j):
            def g():
                return j*j
            return g
        r=f(i)
        fs.append(r)
    return fs
l= count()
print l## all function reference
f1,f2,f3,f4= count()
print f1(),f2(),f3(),f4()

## 匿名函数

print filter(lambda s:s and len(s.strip())>0,
             ['test', None, '', 'str', '  ', 'END'])

