# _*_ coding=utf-8 _*_
__author__ = 'patrick'

"""
# Reduce
reduce/filter,从名字角度不是那么容易理解，它主要是通过一个supplied的函数来
减少一个列表的值。可以这样理解，就是通过某个过滤的条件，来过滤一个集合，
迭代器。

filter: 通过是针对单个元素的条件来过滤 （The filter filters out items based on a test function which is a filter）
reduce：通过一对元素的条件来执行函数（apply functions to pairs of item and running result which is reduce.）

map,reduce，filter都是python 函数式(functional programming)编程
"""


def learn_filter_range():
    print list(filter(lambda x: x < 0, range(-5, 5)))


def learn_filter_how_it_work():
    result = []
    for x in range(-5, 5):
        if x < 0:
            result.append(x)
    print(result)


def learn_reduce():
    print reduce(lambda x,y:x*y,range(1,5))

def learn_reduce_how_it_work():
    l=[12,2,3,4,5]
    result=0
    for x in l:
        result=result+x

    print result

def learn_reduce_how_it_works(fnc,seq):

    totally=seq[0]
    for next in seq[1:]:
        totally=fnc(totally,next)

    return totally

if __name__ == '__main__':
    learn_filter_range()
    learn_filter_how_it_work()
    learn_reduce()
    learn_reduce_how_it_work()
    print learn_reduce_how_it_works(lambda x,y:x*y,[1,4,5,6,7,8])