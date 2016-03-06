# _*_ coding=utf-8 _*_
__author__ = 'patrick'

"""
# Map,Reduce and Filter
## Map
## Reduce
## Filter
"""


def learn_map_for():
    """
    使用for的形式
    """
    items = [1, 2, 3, 4, 78, 9, 0]
    squared = []
    for x in items:
        squared.append(x * x)

    return squared


def learn_map_function():
    items = [1, 2, 3, 4, 78, 9, 0]

    def sqr(x): return x * x

    return map(sqr, items)


def learn_map_lambda():
    items = [1, 2, 3, 4, 78, 9, 0]
    return map(lambda x: x ** 2, items)


def learn_map_function_tuple():
    def square(x):
        return (x ** 2)

    def cube(x):
        return (x ** 3)

    funcs = [square, cube]
    for r in range(5):
        value = map(lambda x: x(r), funcs)
        print value


def learn_map_mock(aFunc, aSeq):
    result = []
    for x in aSeq: result.append(aFunc(x))
    return result

def learn_map_multiple_seqs():
    print list(map(pow,[2, 3, 4], [10, 11, 12]))

def learn_map_for_tuple():
    m =[1,2,3]
    n=[2,4,6]
    return map(None,m,n)

if __name__ == '__main__':
    print learn_map_for()
    print learn_map_function()
    print learn_map_lambda()
    learn_map_function_tuple()
    items = [1, 2, 3, 4, 78, 9, 0]
    learn_map_mock(lambda x: x * 2, items)
    learn_map_multiple_seqs()
    print learn_map_for_tuple()