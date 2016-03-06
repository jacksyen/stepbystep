# _*_ coding=utf-8 _*_
import math
import sys

__author__ = 'patrick'

print "%d %s" %(3,"a")
print "%4d %s" %(3,"a")
print "%.9f %s" %(3,"a")

print "PI = %10.3f" % math.pi

website = "www.baidu.com"
print "%.3s"%website
print "%.*s" % (3,website)
print "%7.*s" % (3,website)
print "%7.4s" % (website)


myinfo = {"site":"www.baidu.com", 'name':"patrick", "room":"704"}

print "patrick is in {0}, {1}".format(myinfo["name"],myinfo["room"])
# print "patrick is in %{room}d"%myinfo

# template
template = "My name is {name}. My website is {site}"
template = template.format(name = "patrick",site="baidu")
print template
# template matching
print "{number} is in {all}. {0} are my number.".format("seven",number=7,all=[1,2,3,4,5,6,7,8,9,0])

word = "python"
word_list = list(word)

template = "First ={0[0]},Third = {0[2]}"
template = template.format(word_list)
print template

# build in property
print 'PI is {0.pi}. My lptop runs {1.platform}'.format(math, sys)

