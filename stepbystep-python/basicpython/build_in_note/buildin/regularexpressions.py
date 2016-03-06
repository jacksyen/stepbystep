# _*_ coding=utf-8 _*_
__author__ = 'patrick'

import re

text = "this is simple example"

m = re.match(".*", text)
print m.group(0)
print repr(m.groups())

m = re.match("(\w+) (\w+) (\w+)", text)
if m!= None:
   print repr(m.group(0,1,2,3))
   print repr(m.groups())

m = re.match("\d+", text)
if m!= None:
    print repr(m.group(0))
