# _*_ coding=utf-8 _*_
import os
from shutil import rmtree
import shutil

__author__ = 'patrick'


def read_file(path):
    fi = open(path)
    lines = []
    for line in fi.readlines():
        if line != "\n":
            lines.append(line)
    return lines


def remove_temp_file(file_name):
    temp = os.path.abspath(file_name)+".tmp"
    try:
        os.open(temp,1)
        os.remove(temp)
    except OSError:
        print OSError.message

print read_file("hello.py")
print remove_temp_file("hello.py")
print os.getcwd()
print os.pardir
os.chdir(os.pardir)
print os.getcwd()
os.chdir("buildin")
print os.getcwd()
print os.path.splitext(os.getcwd())[0]
print os.path.splitext(os.getcwd())[1]

#for fi in os.listdir(os.getcwd()):
#    print fi

try:
    os.mkdir("temp")
    os.chdir("temp")
    fi = open("temp1.py","w")
    fi.close()
except OSError:
    print OSError.message

print os.getcwd()
print os.path.exists("temp") # todo understand why it is false
try:
    shutil.rmtree("temp")
except OSError:
    print OSError.__dict__


#stat
file_name ="hello.py"
print os.stat(file_name)
