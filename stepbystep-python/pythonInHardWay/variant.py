__author__ = 'simon'
# _*_ coding:utf-8 _*_

from sys import argv

script,first,second,third=argv

print "this is parameters %s,%s,%s in script %s" % (first,second,third,script)

if __name__ == '__main__':
    print argv
