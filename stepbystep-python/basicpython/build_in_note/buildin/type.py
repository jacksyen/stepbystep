# _*_ coding=utf-8 _*_
__author__ = 'patrick'


def function(value):
    print value

function(1)
function(1.0)
function("one")


def dump(value):
    print type(value), value, dir(value)

dump(1)
dump(1.0)
dump('one')
dump("one")
dump([1,2,3,45])
dump({"a":1,"b":2})
dump(None)
dump("")

def load(file):
    print type(file)
    if isinstance(file,type("")):
        print type(file)
        file=open(file,"rb")
    return file.read()

print len(load("namespace.py")),"bytes"
print len(load(open("namespace.py","rb"))),"bytes"

#__callable__gi
from basicpython.build_in_note.buildin.namespace import *

def dump_1(function):
    if callable(function):
        print function,"is callable"
    else:
        print function,"is not callable"

a = A()
b = B()

dump_1(a)
dump_1(b)
dump_1(a.__dict__)
dump_1(b.b)



