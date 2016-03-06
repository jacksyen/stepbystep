# _*_ coding=utf-8 _*_
__author__ = 'patrick'

lam = lambda x:x+3
n=[]
for i in range(10):
    n.append(lam(i))

print n

def add(i):
    i+3

print map(add(i),range(10))
print map(lam,range(20))

print reduce(lambda x,y:x+y,range(20))

print filter(lambda  x: x>5,range(10))