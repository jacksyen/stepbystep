# _*_ coding=utf-8 _*_
__author__ = 'patrick'

s = "test"
print s.capitalize()
print s.isalpha()
print s.endswith("st")
print s.startswith("te")
print s.count("(S)")
print s.decode()
print s.encode()
print s.encode("base64")
print s.upper()
print s.isupper()
print s.capitalize()

# todo understand center
print s.center(10, chr(34))
print s.lower()
print s.islower()

print s.istitle()

# get character from string
temp = "  test string which used as list or array"
print temp[-1]
print temp[12]
for t in temp:
    print t

print temp[1:20]
print temp[:10]
print temp[1:]

print temp.lstrip()
print temp.rstrip()
print temp.strip()

print "write your name:"
name =raw_input()
print "your name is %s"%name
