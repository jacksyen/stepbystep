# _*_ coding=utf-8 _*_
__author__ = 'patrick'

number = 3


def myfunc():
    print number


def anotherfunc():
    global number
    print number
    number=1


def yetanotherfunc():
    global number
    number=4