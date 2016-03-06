__author__ = 'simon'
# _*_ coding:utf-8 _*_

def print_two(*args):
    for arg in args:
        print "arg: %r" % arg


def print_nothing():
    print "I am doing nothing,enjoy it "

print_two("Test","Test2")
print_nothing()


def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
   print line_count,f.readline()

current_file = open("../io.txt")

print_all(current_file)
rewind(current_file)

print_a_line(1,current_file)
print_a_line(8,current_file)

rewind(current_file)
print_a_line(9,current_file)

## seek negative value

current_file.seek(60) # position
print current_file.readline()


def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multipy(a,b):
    return a*b

def divide(a,b):
    return a/b

def isEqual(a,b):
    return True

print add(12,23)
print multipy(12,34)
print divide(12,4)
print subtract(12,90)
print isEqual(12,34)

def secret(started):
    a1 = started*10
    a2= started*12
    a3 = started *14
    return a1,a2,a3

print "%s,%s,%s" % secret(12)
print "%s,%s,%s" % secret("test")
