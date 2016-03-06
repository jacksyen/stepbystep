# _*_ coding=utf-8 _*_
__author__ = 'patrick'


def square(x):
    """Squares x.
    >>> square(2)
    4
    >>> square(-2)
    4
    """
    return x * x


if __name__ == '__main__':
    import doctest
    doctest.testmod()