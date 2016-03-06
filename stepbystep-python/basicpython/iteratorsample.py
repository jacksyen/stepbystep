# _*_ coding=utf-8 _*_
__author__ = 'patrick'

s = "hello world"
for element in s:
    print element

print(len(s))

test=[]
for n in range(0,1000):
    if(n%3)==0:
        test.append(n)

print test

t = [n for n in range(100) if n%2==0]
print t

mybag = ['glass','apple','green leaf']
mybag = [one.strip() for one in mybag]
print mybag

print list(enumerate(mybag))

for(index,element) in enumerate(mybag):
    print(str(index)+"is"+element)

#
print dir(dict)