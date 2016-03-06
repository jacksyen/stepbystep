# _*_ coding=utf-8 _*_
import functools
import time

__author__ = 'patrick'

# 不改变函数，但是可以实现其他新的功能，使用高阶函数，接受函数，同时返回函数
# 有点AOP的概念


def f1(x):
    return x*2

def new_fn(f):
    def fn(x):
        print 'call'+f.__name__
        return f(x)
    return fn

f1 = new_fn(f1)
print f1(5)


## 装饰器
# @log
# @transaction
# @performance
# @post('/register')

# 无参数装饰器
def performance(f):
    def fn(*arg,**kw):
        t1 = time.time()
        r=f(*arg,**kw)
        t2=time.time()
        print 'call %s() in %fs' % (f.__name__,(t2-t1))
        return r
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y:x*y,range(1,n+1))

print factorial(10)

# 参数装饰
def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print '[%s] %s()...' % (prefix, f.__name__)
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log('DEBUG')
def test(name):
    print name
print test('patrick')
print test.__name__

# 装饰器不改变原来函数内容，包括名字，doc等等
# @functools.wraps(f)

# 偏函数

sorted_ignore_case = functools.partial(sorted,cmp=lambda s1,s2:cmp(s1.upper(),s2.upper()))

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])

