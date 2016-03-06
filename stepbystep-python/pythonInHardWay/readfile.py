__author__ = 'simon'
# _*_ coding:utf-8 _*_

from sys import argv

script,filename=argv

text =open(filename)

print "Here's your file %r" % filename

print text.read()

print "Type the filename again:"
file_another = raw_input("> ")
file_another = open(file_another)

print file_another.read()

if __name__ == '__main__':
    "do nothing"
