# _*_ coding=utf-8 _*_
__author__ = 'patrick'

lists=[]
print type(lists)
#false
print bool(lists)

lists=[1,2,'www.github.com']
print bool(lists)

print lists

# slice
url ='www.github.com'
print url[2]

print url[:4]
print url[4:10]
print url[:-8]
print url[:-3]
print url[-1:]

alst=[1,2,3,4,55,665]
print alst[::2]
print alst[::-1]
print alst[::-2]
print len(alst)
lst=[3,324,1234]
print alst+lst
print len(alst+lst)

# append list
alst.append(5567)
alst[len(alst):]=[9000]
print alst
# 合并list
alst.extend(lst)
print alst