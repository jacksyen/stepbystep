# _*_ coding=utf-8 _*_
import random

__author__ = 'patrick'

i = 0
while i <4 :
    print "i***************"
    num = input("please input a number which in range 0-9")
    rnum = random.randint(0,9)
    x = 3-i

    if num==rnum:
        print "good luck man!"
    elif num>rnum:
        print "your are right man!"
    elif num<rnum:
        print "sorry , your are wrong man, try it again!"
    print "i***************"

    i+=1

count = 0
while count<5:
    print count ,"is leass than 5"
    count +=1
else :
    print count , "is not less than 5"

