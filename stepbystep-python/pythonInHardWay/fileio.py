__author__ = 'simon'
# _*_ coding:utf-8 _*_
from os.path import exists
from sys import argv

script,sourcefile,tofile =argv

print "copying from %s to %s " % (sourcefile,tofile)

in_file = open(sourcefile)
in_data = in_file.read()
print len(in_data)
print exists(tofile)

out_file =open(tofile,"w")
out_file.write(in_data)

in_file.close()
out_file.close()

file_name = "ex1_print.py"

text=open(file_name)
for line in text.readlines():  # read file
    print line



file_name_w="io.txt"
text=open(file_name_w,"r")
for line in text.readlines():  # read file
    print line

#target =open(file_name_w,"w") # write to file
#target.write("test\n")
#target.write("test\n")
# target.write("test\n")

target = open(file_name_w,"a+") # open for append
target.write("append \n")
target.write("append \n")
target.write("append \n")

for line in target.readlines():
    print(line)

target.close()