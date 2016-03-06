# _*_ coding=utf-8 _*_
import itertools

__author__ = 'patrick'

horses=[1,2,3,4]
races =itertools.permutations(horses)
print (list(races))