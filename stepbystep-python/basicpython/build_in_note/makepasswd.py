# _*_ coding=utf-8 _*_
from random import choice
import string

__author__ = 'patrick'

def GenPasswd(length = 8, chars = string.letters + string.digits):
	return ''.join([ choice(chars) for i in range(length) ])

# 测试生成12位的随机密码
print GenPasswd(12)
print "simon".center(20,'+')