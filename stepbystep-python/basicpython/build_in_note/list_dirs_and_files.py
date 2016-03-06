# _*_ coding=utf-8 _*_
import os

__author__ = 'patrick'

for root,dirs,files in os.walk('/Users/patrick/workspace'):
    open('myfile.txt','a').write('路径:%s\n -文件夹:%s\n -文  件:%s  \n\n' % (root,dirs,files))
    print root,dirs,files