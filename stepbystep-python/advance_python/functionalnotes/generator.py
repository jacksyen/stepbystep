# _*_ coding=utf-8 _*_
__author__ = 'patrick'

from random import randint

def rand_gen(a_list):
    while len(a_list)>0:
        yield a_list.pop(randint(0,len(a_list)))


def count(start=0):
    count=start
    while True:
        val = (yield count)
        if val is not None:
            count=val
        else:
            count +=1

for item in rand_gen(['rock','paper','scissors']):
    print item