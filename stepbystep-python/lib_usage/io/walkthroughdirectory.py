# _*_ coding=utf-8 _*_
import codecs

__author__ = 'patrick'

import os
#
# for root, dirs, files in os.walk("/users/patrick/workspace"):
#     print root
#     print dirs
#     print files

for root,dirs, files in os.walk("/users/patrick/workspace/blog/books"):
    print root,dirs,files
    open('temp.txt','a').write("%s %s %s \n" %(root,dirs,files))

# not top to down
for root,dirs, files in os.walk("/users/patrick/workspace/blog/books", False):
    print root,dirs,files


# print tree for folder
# root
#   |__ [D]subfolder
#   ........
#   |__ [F]file
#   ........
# todo to finish a function which print folder structure
print dir()
# print help()

# with codes.open

codecs.open("temp.txt","a").write("test")

unicode_str= unicode("中文", encoding='utf-8')
print unicode_str




