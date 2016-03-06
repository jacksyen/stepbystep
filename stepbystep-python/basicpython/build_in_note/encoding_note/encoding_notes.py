# _*_ coding=utf-8 _*_
import sys

__author__ = 'patrick'

s = "测试"
print s

d = unicode(s,"utf-8")
print d.encode('utf-8')
print s.decode('utf-8')

print sys.getdefaultencoding()
print sys.getfilesystemencoding()


