# _*_ coding=utf-8 _*_
__author__ = 'patrick'


def some_function():
    try:
        10 / 0
    except ZeroDivisionError:
        print "Oops, invalid"
    else:
        pass
    finally:
        print "We're done with that."

some_function()
