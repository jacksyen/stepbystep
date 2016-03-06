# _*_ coding=utf-8 _*_
import os
import time

__author__ = 'patrick'

f = open("filesample.txt","a")
f.write("test")

f = open("filesample.txt","r")
for line in f:
    print line

# 模式	描述
# r	以读方式打开文件，可读取文件信息。
# w	以写方式打开文件，可向文件写入信息。如文件存在，则清空该文件，再写入新内容
# a	以追加模式打开文件（即一打开文件，文件指针自动移到文件末尾），如果文件不存在则创建
# r+	以读写方式打开文件，可对文件进行读和写操作。
# w+	消除文件内容，然后以读写方式打开文件。
# a+	以读写方式打开文件，并把文件指针移到文件尾。
# b	以二进制模式打开文件，而不是以文本模式。该模式只对Windows或Dos有效，类Unix的文件是用二进制模式进行操作的。

f.close()

f = open("filesample.txt","w+")
f.write("this is test \n")
f.write("this is test \n")
f.write("this is test \n")
f.write("this is test \n")
f.write("this is test \n")

f.close()

# file status
file_stat = os.stat("filesample.txt")
print file_stat
print file_stat.st_atime
print time.localtime(file_stat.st_birthtime)

# file function
f = open("filesample.txt","r")
# print f.read()
# contant =f.read()

# print type(contant)

# start read all the lines in file
for line in f.readlines():
    print line,

f.close()